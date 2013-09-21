"""
/***************************************************************************
         Value Tool       - A QGIS plugin to get values at the mouse pointer
                             -------------------
    begin                : 2008-08-26
    copyright            : (C) 2008 by G. Picard
    email                : 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

import logging
# change the level back to logging.WARNING(the default) before releasing
logging.basicConfig(level=logging.DEBUG)

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from ui_valuewidgetbase import Ui_ValueWidgetBase as Ui_Widget

hasqwt=True
try:
    from PyQt4.Qwt5 import QwtPlot,QwtPlotCurve,QwtScaleDiv,QwtSymbol
except:
    hasqwt=False

#test if matplotlib >= 1.0
hasmpl=True
try:
    import matplotlib
    import matplotlib.pyplot as plt 
    import matplotlib.ticker as ticker
    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
except:
    hasmpl=False
if hasmpl:
    if int(matplotlib.__version__[0]) < 1:
        hasmpl = False

class ValueWidget(QWidget, Ui_Widget):

    def __init__(self, iface):

        self.hasqwt=hasqwt
        self.hasmpl=hasmpl
        self.layerMap=dict()
        self.statsChecked=False
        self.ymin=0
        self.ymax=250

        # Statistics (>=1.9)
        self.statsSampleSize = 2500000
        self.stats = {} # stats per layer

        self.iface=iface
        self.canvas=self.iface.mapCanvas()
        self.legend=self.iface.legendInterface()
        self.logger = logging.getLogger('.'.join((__name__, 
                                        self.__class__.__name__)))

        QWidget.__init__(self)
        self.setupUi(self)
        self.setupUi_extra()

        QObject.connect(self.cbxActive,SIGNAL("stateChanged(int)"),self.changeActive)
        QObject.connect(self.cbxGraph,SIGNAL("stateChanged(int)"),self.changePage)
        QObject.connect(self.canvas, SIGNAL( "keyPressed( QKeyEvent * )" ), self.pauseDisplay )
        QObject.connect(self.plotSelector, SIGNAL( "currentIndexChanged ( int )" ), self.changePlot )

    def setupUi_extra(self):

        # checkboxes
        #self.changeActive(Qt.Checked)
        #set inactive by default - should save last state in user config
        self.cbxActive.setCheckState(Qt.Unchecked)

        # plot
        self.plotSelector.setVisible( False )
        self.cbxStats.setVisible( False )
        if QGis.QGIS_VERSION_INT >= 10900:
          # stats by default because estimated are fast
          self.cbxStats.setChecked( True )
        self.graphControls.setVisible( False )
        if self.hasqwt:
            self.plotSelector.addItem( 'Qwt' )
        if self.hasmpl:
            self.plotSelector.addItem( 'mpl' )
        self.plotSelector.setCurrentIndex( 0 );
        if (not self.hasqwt or not self.hasmpl):
            #self.plotSelector.setVisible(False)
            self.plotSelector.setEnabled(False)

        # Page 2 - qwt
        if self.hasqwt:
            self.qwtPlot = QwtPlot(self.stackedWidget)
            self.qwtPlot.setAutoFillBackground(False)
            self.qwtPlot.setObjectName("qwtPlot")
            self.curve = QwtPlotCurve()
            self.curve.setSymbol(
                QwtSymbol(QwtSymbol.Ellipse,
                          QBrush(Qt.white),
                          QPen(Qt.red, 2),
                          QSize(9, 9)))
            self.curve.attach(self.qwtPlot)
            self.qwtPlot.setVisible(False)
        else:
            self.qwtPlot = QtGui.QLabel("Need Qwt >= 5.0 or matplotlib >= 1.0 !")

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qwtPlot.sizePolicy().hasHeightForWidth())
        self.qwtPlot.setSizePolicy(sizePolicy)
        self.qwtPlot.setObjectName("qwtPlot")
        self.qwtPlot.updateGeometry()
        self.stackedWidget.addWidget(self.qwtPlot)

        #Page 3 - matplotlib
        self.mplLine = None #make sure to invalidate when layers change
        if self.hasmpl:
            # mpl stuff
            # should make figure light gray
            self.mplBackground = None #http://www.scipy.org/Cookbook/Matplotlib/Animations
            self.mplFig = plt.Figure(facecolor='w', edgecolor='w')
            self.mplFig.subplots_adjust(left=0.1, right=0.975, bottom=0.13, top=0.95)
            self.mplPlt = self.mplFig.add_subplot(111)   
            self.mplPlt.tick_params(axis='both', which='major', labelsize=12)
            self.mplPlt.tick_params(axis='both', which='minor', labelsize=10)                           
            # qt stuff
            self.pltCanvas = FigureCanvasQTAgg(self.mplFig)
            self.pltCanvas.setParent(self.stackedWidget)
            self.pltCanvas.setAutoFillBackground(False)
            self.pltCanvas.setObjectName("mplPlot")
            self.mplPlot = self.pltCanvas
            self.mplPlot.setVisible(False)
        else:
            self.mplPlot = QtGui.QLabel("Need Qwt >= 5.0 or matplotlib >= 1.0 !")

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplPlot.sizePolicy().hasHeightForWidth())
        self.mplPlot.setSizePolicy(sizePolicy)
        self.qwtPlot.setObjectName("qwtPlot")
        self.mplPlot.updateGeometry()
        self.stackedWidget.addWidget(self.mplPlot)

        self.stackedWidget.setCurrentIndex(0)

    def disconnect(self):
        self.changeActive(False)
        QObject.disconnect(self.canvas, SIGNAL( "keyPressed( QKeyEvent * )" ), self.pauseDisplay )
    
    def pauseDisplay(self,e):
      if ( e.modifiers() == Qt.ShiftModifier or e.modifiers() == Qt.MetaModifier ) and e.key() == Qt.Key_A:

        self.cbxActive.toggle()
        return True
      return False


    def keyPressEvent( self, e ):
      if ( e.modifiers() == Qt.ControlModifier or e.modifiers() == Qt.MetaModifier ) and e.key() == Qt.Key_C:
        items = ''
        for rec in range( self.tableWidget.rowCount() ):
          items += '"' + self.tableWidget.item( rec, 0 ).text() + '",' + self.tableWidget.item( rec, 1 ).text() + "\n"
        if not items == '':
          clipboard = QApplication.clipboard()
          clipboard.setText( items )
      elif (self.pauseDisplay(e)):
        pass
      else:
        QWidget.keyPressEvent( self, e )


    def changePage(self,state):
        if (state==Qt.Checked):
            self.plotSelector.setVisible( True )
            self.cbxStats.setVisible( True )
            self.graphControls.setVisible( True )
            if (self.plotSelector.currentText()=='mpl'):
                self.stackedWidget.setCurrentIndex(2)
            else:
                self.stackedWidget.setCurrentIndex(1)
        else:
            self.plotSelector.setVisible( False )
            if QGis.QGIS_VERSION_INT < 10900:
              self.cbxStats.setVisible( False )
            self.graphControls.setVisible( False )
            self.stackedWidget.setCurrentIndex(0)

    def changePlot(self):
        self.changePage(self.cbxActive.checkState())

    def changeActive(self,state):
        if (state==Qt.Checked):
            #QObject.connect(self.legend, SIGNAL( "itemAdded ( QModelIndex )" ), self.statsNeedChecked )
            #QObject.connect(self.legend, SIGNAL( "itemRemoved ()" ), self.invalidatePlot )
            QObject.connect(self.canvas, SIGNAL( "layersChanged ()" ), self.invalidatePlot )
            if QGis.QGIS_VERSION_INT >= 10300: # for QGIS >= 1.3
                QObject.connect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint &)"), self.printValue)
            else:
                QObject.connect(self.canvas, SIGNAL("xyCoordinates(QgsPoint &)"), self.printValue)
        else:
            QObject.disconnect(self.canvas, SIGNAL( "layersChanged ()" ), self.invalidatePlot )
            if QGis.QGIS_VERSION_INT >= 10300: # for QGIS >= 1.3
                QObject.disconnect(self.canvas, SIGNAL("xyCoordinates(const QgsPoint &)"), self.printValue)
            else:
                QObject.disconnect(self.canvas, SIGNAL("xyCoordinates(QgsPoint &)"), self.printValue)


    def printValue(self,position):

        if self.canvas.layerCount() == 0:
            self.values=[]         
            self.showValues()
            return
        
        needextremum = self.cbxGraph.isChecked() # if plot is checked

        # count the number of requires rows and remember the raster layers
        nrow=0
        rasterlayers=[]
        layersWOStatistics=[]

        for i in range(self.canvas.layerCount()):
            layer = self.canvas.layer(i)
            if (layer!=None and layer.isValid() and layer.type()==QgsMapLayer.RasterLayer):
              if QGis.QGIS_VERSION_INT >= 10900: # for QGIS >= 1.9
                if not layer.dataProvider():
                  continue

                if not layer.dataProvider().capabilities() & QgsRasterDataProvider.IdentifyValue:
                  continue

                nrow+=layer.bandCount()
                rasterlayers.append(layer)

              else: # < 1.9
                if layer.providerKey()=="wms":
                  continue

                if layer.providerKey()=="grassraster":
                  nrow+=1
                  rasterlayers.append(layer)
                else: # normal raster layer
                  nrow+=layer.bandCount()
                  rasterlayers.append(layer)
                
              # check statistics for each band
              if needextremum:
                for i in range( 1,layer.bandCount()+1 ):
                  if QGis.QGIS_VERSION_INT >= 10900: # for QGIS >= 1.9
                    has_stats = self.getStats ( layer, i ) is not None
                  else:
                    has_stats=layer.hasStatistics(i)
                  if not layer.id() in self.layerMap and not has_stats\
                          and not layer in layersWOStatistics:
                    layersWOStatistics.append(layer)

        if layersWOStatistics and not self.statsChecked:
          self.calculateStatistics(layersWOStatistics)
                  
        # create the row if necessary
        self.tableWidget.setRowCount(nrow)

        irow=0
        self.values=[]
        self.ymin=1e38
        self.ymax=-1e38

        if QGis.QGIS_VERSION_INT >= 10900:
            mapCanvasSrs = self.iface.mapCanvas().mapRenderer().destinationCrs()
        else:
            mapCanvasSrs = self.iface.mapCanvas().mapRenderer().destinationSrs()

        # TODO - calculate the min/max values only once, instead of every time!!!
        # keep them in a dict() with key=layer.id()
                
        for layer in rasterlayers:
            layername=unicode(layer.name())
            if QGis.QGIS_VERSION_INT >= 10900:
                layerSrs = layer.crs()
            else:
                layerSrs = layer.srs()

            pos = position         

            # if given no position, get dummy values
            if position is None:
                pos = QgsPoint(0,0)
            # transform points if needed
            elif not mapCanvasSrs == layerSrs and self.iface.mapCanvas().hasCrsTransformEnabled():
              srsTransform = QgsCoordinateTransform(mapCanvasSrs, layerSrs)
              try:
                pos = srsTransform.transform(position)
              except QgsCsException, err:
                # ignore transformation errors
                continue

            if QGis.QGIS_VERSION_INT >= 10900: # for QGIS >= 1.9
              if not layer.dataProvider():
                continue

              ident = None
              if position is not None:
                canvas = self.iface.mapCanvas()

                # first test if point is within map layer extent 
                # maintain same behaviour as in 1.8 and print out of extent
                if not layer.dataProvider().extent().contains( pos ):
                  ident = dict()
                  for iband in range(1,layer.bandCount()+1):
                    ident[iband] = str(self.tr('out of extent'))
                # we can only use context if layer is not projected
                elif canvas.hasCrsTransformEnabled() and layer.dataProvider().crs() != canvas.mapRenderer().destinationCrs():
                  ident = layer.dataProvider().identify(pos, QgsRaster.IdentifyFormatValue ).results()
                else:
                  extent = canvas.extent()
                  width = round(extent.width() / canvas.mapUnitsPerPixel());
                  height = round(extent.height() / canvas.mapUnitsPerPixel());

                  extent = canvas.mapRenderer().mapToLayerCoordinates( layer, extent );

                  ident = layer.dataProvider().identify(pos, QgsRaster.IdentifyFormatValue, canvas.extent(), width, height ).results()
                if not len( ident ) > 0:
                    continue

              # if given no position, set values to 0
              if position is None and ident is not None and ident.iterkeys() is not None:
                  for key in ident.iterkeys():
                      ident[key] = layer.dataProvider().noDataValue(key)

              for iband in range(1,layer.bandCount()+1): # loop over the bands
                layernamewithband=layername
                if ident is not None and len(ident)>1:
                    layernamewithband+=' '+layer.bandName(iband)

                if not ident or not ident.has_key( iband ): # should not happen
                  bandvalue = "?"
                else:
                  bandvalue = ident[iband]
                  if bandvalue is None:
                      bandvalue = "no data"

                self.values.append((layernamewithband,str(bandvalue)))

                if needextremum:
                  # estimated statistics
                  stats = self.getStats ( layer, iband )
                  if stats:
                    self.ymin=min(self.ymin,stats.minimumValue)
                    self.ymax=max(self.ymax,stats.maximumValue)

            else: # QGIS < 1.9
              isok,ident = layer.identify(pos)
              if not isok:
                  continue

              # if given no position, set values to 0
              if position is None:
                  for key in ident.iterkeys():
                      ident[key] = 0

              if layer.providerKey()=="grassraster":
                if not ident.has_key("value"):
                  continue
                value = ident["value"]
                if value is None:
                  continue
                if isinstance(value, str):
                  # if this is not a double, it is probably a (GRASS string like
                  # 'out of extent' or 'null (no data)'. Let's just show that:
                  self.values.append((layername, value))
                  continue
                self.values.append((layername,value))
                if needextremum:
                  self.ymin = min(self.ymin,value)
                  self.ymax = max(self.ymax,value)

              else:
                for iband in range(1,layer.bandCount()+1): # loop over the bands
                  bandvalue=ident[layer.bandName(iband)]
                  layernamewithband=layername
                  if len(ident)>1:
                      layernamewithband+=' '+layer.bandName(iband)

                  self.values.append((layernamewithband,bandvalue))

                  if needextremum:
                      has_stats=layer.hasStatistics(i)
                      if has_stats:
                          cstr=layer.bandStatistics(iband)
                      if has_stats:
                          self.ymin=min(self.ymin,cstr.minimumValue)
                          self.ymax=max(self.ymax,cstr.maximumValue)
                      else:
                          self.ymin=min(self.ymin,layer.minimumValue(i))
                          self.ymax=max(self.ymax,layer.maximumValue(i))

        self.showValues()

    def showValues(self):
        if self.cbxGraph.isChecked():
            #TODO don't plot if there is no data to plot...
            self.plot()
        else:
            self.printInTable()

    def calculateStatistics(self,layersWOStatistics):
        
        self.invalidatePlot(False)

        self.statsChecked = True

        layerNames = []
        for layer in layersWOStatistics:
            if not layer.id() in self.layerMap:
                layerNames.append(layer.name())

        if ( len(layerNames) != 0 ):
#            res = QMessageBox.warning( self, self.tr( 'Warning' ),
#                                       self.tr( 'There are no statistics in the following rasters:\n%1\n\nCalculate?' ).arg(layerNames.join('\n')),
#                                       QMessageBox.Yes | QMessageBox.No )
#            if res != QMessageBox.Yes:
            if not self.cbxStats.isChecked():
                #self.cbxActive.setCheckState(Qt.Unchecked)  
                for layer in layersWOStatistics:
                    self.layerMap[layer.id()] = True
                return
        else:
            print('ERROR, no layers to get stats for')
        
        save_state=self.cbxActive.isChecked()
        self.changeActive(Qt.Unchecked) # deactivate

        # calculate statistics
        for layer in layersWOStatistics:
            if not layer.id() in self.layerMap:
                self.layerMap[layer.id()] = True
                for i in range( 1,layer.bandCount()+1 ):
                    if QGis.QGIS_VERSION_INT >= 10900: # for QGIS >= 1.9
                        self.getStats ( layer, i , True )
                    else:
                        stat = layer.bandStatistics(i)

        if save_state:
            self.changeActive(Qt.Checked) # activate if necessary

    # get cached statistics for layer and band or None if not calculated
    def getStats ( self, layer, bandNo, force = False ):
      if self.stats.has_key( layer ):
        if self.stats[layer].has_key( bandNo ) : 
          return self.stats[layer][bandNo]
      else:
        self.stats[layer] = {}
      
      if force or layer.dataProvider().hasStatistics( bandNo, QgsRasterBandStats.Min | QgsRasterBandStats.Min, QgsRectangle(), self.statsSampleSize ):
        self.stats[layer][bandNo] = layer.dataProvider().bandStatistics( bandNo, QgsRasterBandStats.Min | QgsRasterBandStats.Min, QgsRectangle(), self.statsSampleSize )
        return self.stats[layer][bandNo]

      return None

    def printInTable(self):

        irow=0
        for row in self.values:
          layername,value=row
          
          # limit number of decimal places if requested
          if self.cbxDigits.isChecked():
              try:
                  value = str("{0:."+str(self.spinBox.value())+"f}").format(float(value))
              except ValueError:
                  pass

          if (self.tableWidget.item(irow,0)==None):
              # create the item
              self.tableWidget.setItem(irow,0,QTableWidgetItem())
              self.tableWidget.setItem(irow,1,QTableWidgetItem())

          self.tableWidget.item(irow,0).setText(layername)
          self.tableWidget.item(irow,1).setText(value)
          irow+=1


    def plot(self):

        numvalues=[]
        if ( self.hasqwt or self.hasmpl ):
            for row in self.values:
                layername,value=row
                try:
                    numvalues.append(float(value))
                except:
                    numvalues.append(0)

        ymin = self.ymin
        ymax = self.ymax
        if self.leYMin.text() != '' and self.leYMax.text() != '': 
            ymin = float(self.leYMin.text())
            ymax = float(self.leYMax.text())        

        if ( self.hasqwt and (self.plotSelector.currentText()=='Qwt') ):

            self.qwtPlot.setAxisMaxMinor(QwtPlot.xBottom,0)
            #self.qwtPlot.setAxisMaxMajor(QwtPlot.xBottom,0)
            self.qwtPlot.setAxisScale(QwtPlot.xBottom,1,len(self.values))
            #self.qwtPlot.setAxisScale(QwtPlot.yLeft,self.ymin,self.ymax)
            self.qwtPlot.setAxisScale(QwtPlot.yLeft,ymin,ymax)
            
            self.curve.setData(range(1,len(numvalues)+1), numvalues)
            self.qwtPlot.replot()
            self.qwtPlot.setVisible(len(numvalues)>0)

        elif ( self.hasmpl and (self.plotSelector.currentText()=='mpl') ):

            self.mplPlt.clear()
            self.mplPlt.plot(range(1,len(numvalues)+1), numvalues, marker='o', color='k', mfc='b', mec='b')
            self.mplPlt.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
            self.mplPlt.yaxis.set_minor_locator(ticker.AutoMinorLocator())
            self.mplPlt.set_xlim( (1-0.25,len(self.values)+0.25 ) )
            self.mplPlt.set_ylim( (ymin, ymax) ) 
            self.mplFig.canvas.draw()

            #disable optimizations - too many bugs, depending on mpl version!
#            if self.mplLine is None:
#                self.mplPlt.clear()
#                self.mplLine, = self.mplPlt.plot(range(1,len(numvalues)+1), numvalues, marker='o', color='k', mfc='b', mec='b', animated=True)
#                self.mplPlt.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
#                self.mplPlt.yaxis.set_minor_locator(ticker.AutoMinorLocator())
#                self.mplPlt.set_xlim( (1-0.25,len(self.values)+0.25 ) )
#                self.mplPlt.set_ylim( (self.ymin, self.ymax) )
#                self.mplFig.canvas.draw()
#                self.mplBackground = self.mplFig.canvas.copy_from_bbox(self.mplFig.bbox)
#            else:
#                # restore the clean slate background
#                self.mplFig.canvas.restore_region(self.mplBackground)
#                # update the data
#                self.mplLine.set_xdata(range(1,len(numvalues)+1))
#                self.mplLine.set_ydata(numvalues)
#                self.mplPlt.draw_artist(self.mplLine)
#                # just redraw the axes rectangle
#                self.mplFig.canvas.blit(self.mplFig.bbox)
#            self.mplPlot.setVisible(len(numvalues)>0)

        #try:
                #    attr = float(ident[j])
                #except:
                #    attr = 0
                #    print "Null cell value catched as zero!"  # For none values, profile height = 0. It's not elegant...

                    #nr = rastLayer.getRasterBandNumber(self.rastItems[field[1]][field[2]][0])

                    #print ident
            #for j in ident:
                #print j
                #if j.right(1) == str(nr):
       #attr = int(ident[j])
       #attr = float(ident[j])  ##### I MUST IMPLEMENT RASTER TYPE HANDLING!!!!
       #outFeat.addAttribute(i, QVariant(attr))


    def statsNeedChecked(self, indx):
        #self.statsChecked = False
        self.invalidatePlot()

    def invalidatePlot(self,replot=True):
        self.statsChecked = False
        if self.mplLine is not None:
            del self.mplLine
            self.mplLine = None
        #update empty plot
        if replot and self.cbxGraph.isChecked():
            #self.values=[]
            self.printValue( None )

    def resizeEvent(self, event):
        self.invalidatePlot()

