from PyQt5.QtCore import QTimer

fileName = 'C:/Users/soiqu/Desktop/test_pyQGIS/png/' # exported is a prefix for the file names
boundaryLayer = QgsMapLayerRegistry.instance().mapLayersByName('boundary')[0]
climitsLayer = QgsMapLayerRegistry.instance().mapLayersByName('climits')[0]
otherLayers = ['t_216_TVDI_200003.tif']
count = 0

iface.legendInterface().setLayerVisible(boundaryLayer, True)
iface.legendInterface().setLayerVisible(climitsLayer, True)

def prepareMap(): # Arrange layers
    iface.actionHideAllLayers().trigger() # make all layers invisible
    iface.legendInterface().setLayerVisible(QgsMapLayerRegistry.instance().mapLayersByName( otherLayers[count] )[0], True)
    QTimer.singleShot(1000, exportMap) # Wait a second and export the map

def exportMap(): # Save the map as a PNG
    global count # We need this because we'll modify its value
    iface.mapCanvas().saveAsImage( fileName + "_" + str(count) + ".png" )
    print("Map with layer",count,"exported!")
    if count < len(otherLayers)-1:
        QTimer.singleShot(1000, prepareMap) # Wait a second and prepare next map
    count += 1

prepareMap() # Let's start the fun