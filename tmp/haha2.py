from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#import config

pathToFile = "C:/Users/soiqu/Desktop/test_pyQGIS/png/"

# app = QgsApplication([], True)
# QgsApplication.setPrefixPath(config.qgis_path, True)
# QgsApplication.initQgis()

# mlr = QgsMapLayerRegistry.instance()
crs = QgsCoordinateReferenceSystem(3857)

layerSet = []
for layer in QgsProject.instance().mapLayers().values():
    #if layer.name().startswith("probe_"):
    layerSet.append(layer)

# creating a single layer
# layer = QgsVectorLayer(config.data_dir + 'ZASRO.shp', 'ZASRO', 'ogr')
# if not layer.isValid():
    # print "layer failed to load !"
# layer.setCrs(crs)
# mlr.addMapLayer(layer)

layerSet = [layer.id()]

# map renderer
renderer = QgsMapRenderer()
renderer.setDestinationCrs(crs)
renderer.setLayerSet(layerSet)
renderer.setExtent(layer.extent())

# composition
comp = QgsComposition(renderer)
comp.setPlotStyle(QgsComposition.Print)
comp.setPaperSize(420.0, 297.0)
comp.setPrintResolution(300)

# composer map
composerMap = QgsComposerMap(comp, 0, 0, 420.0, 297.0)
#composerMap.setNewExtent(renderer.fullExtent())
composerMap.zoomToExtent(extent)
comp.addComposerMap(composerMap)

# pdf rendering
comp.exportAsPDF(pathToFile + "out.pdf")

#QgsApplication.exitQgis()