from PyQt5.QtWidgets import QApplication

workdir = 'C:/Users/soiqu/Desktop/test_pyQGIS/png/'
layer = iface.activeLayer()
for f in layer.getFeatures():
    layer.setSelectedFeatures([f.id()])
    iface.mapCanvas().zoomToSelected(layer)
    QApplication.processEvents()
    iface.mapCanvas().saveAsImage(workdir + "feature_" + str(f.id()) + ".png")