import processing
from PyQt5.QtCore import QTimer

# set workdir export files
workdir = 'C:/Users/soiqu/Desktop/test_pyQGIS/png/'
#define the scale of screenshoot
scale = 640

count = 0
fileName = "name"
feat = []
#timer in millisecond
sleepTime=100

# Select the layer witch is used for the mapCanvas extent (do it by hand)
layer = iface.activeLayer()


#def refresh_layers(self):
#    for layer in qgis.utils.iface.mapCanvas().layers():
#        layer.triggerRepaint()


def prepareMap(): # Arrange layers
  #feature = feat[count]
  layer.select(count) 
  #set trigger to zoom automaticaly on select's layers
  iface.actionZoomToSelected().trigger()
  qgis.utils.iface.mapCanvas().zoomScale(scale)
  layer.deselect(count)
  QTimer.singleShot(sleepTime, exportMap) # Wait a second and export the map



def exportMap():
  global count # We need this because we'll modify its value
  #refresh_layers(layer)
  iface.mapCanvas().saveAsImage(workdir + fileName + "_" + str(count) + ".png")
  print("Map with layer",count,"exported!")
  if count < len(feat)-1:
    QTimer.singleShot(sleepTime, prepareMap) # Wait a second and prepare next map
  count += 1


features = processing.features(layer)

for feature in features:
  feat.append(feature.id)


prepareMap()