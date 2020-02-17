from PyQt5.QtCore import QTimer

filePath = 'C:/Users/soiqu/Desktop/test_pyQGIS/png/' # exported is a prefix for the file names
#prefixes = ['t_216_TVDI_200003.tif', 't_216_TVDI_200012.tif', 't_216_TVDI_200011.tif']
prefixes = []
count = 0

#scale = 640
layers = []
for layer in QgsProject.instance().mapLayers().values():
    #if layer.name().startswith("probe_"):
    #layers.append(layer)
    #print(layer.id());
    print(layer.name());
    prefixes.append(layer.name())

# print(layers[0].extent())
# map.setExtent(layers[0].extent())
# map.setRect(20, 20, 20, 20)

def prepareMap(): # Arrange layers
    layers = []
    layers = QgsProject.instance().mapLayers()

    # First, turn off all layers
    for layer in layers:
        QgsProject.instance().layerTreeRoot().findLayer(layer).setItemVisibilityChecked(False)

    # Second, get the layer to export
    exportLayers = []
    for layer in QgsProject.instance().mapLayers().values():
        if layer.name().startswith(prefixes[count]):
            QgsProject.instance().layerTreeRoot().findLayer(layer).setItemVisibilityChecked(True)
            # iface.actionZoomToSelected().trigger()
            # qgis.utils.iface.mapCanvas().zoomScale(scale)

    QTimer.singleShot(1000, exportMap) # Wait a second and export the map

def exportMap(): # Save the map as a PNG
    global count # We need this because we'll modify its value
    iface.mapCanvas().saveAsImage( filePath + prefixes[count] + ".png" )
    print("Map with layer",count,"exported!")
    if count < len(prefixes)-1:
        QTimer.singleShot(1000, prepareMap) # Wait a second and prepare next map
    count += 1

prepareMap() # Let's start the fun