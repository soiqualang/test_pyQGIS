from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

imageType = "png"
pathToFile = "C:/Users/soiqu/Desktop/test_pyQGIS/png/"

# create image
img = QImage(QSize(800,600), QImage.Format_ARGB32_Premultiplied)

# set image's background color
color = QColor(255,255,255)
img.fill(color.rgb())

# create painter
p = QPainter()
p.begin(img)
p.setRenderHint(QPainter.Antialiasing)

renderer = QgsMapRenderer()
# set layer set
lst = []


layers = iface.legendInterface().layers()
for layer in layers:
	lst.append(layer.id())

renderer.setLayerSet(lst)
print("Set rendered")

# set extent
rect = QgsRectangle(renderer.fullExtent())
rect.scale(1.1)
renderer.setExtent(rect)

# set output size
renderer.setOutputSize(img.size(), img.logicalDpiX())

print("Prepared to render")

# do the rendering
renderer.render(p)

print("rendered")
p.end()
print("painter ended")
# save image
img.save(pathToFile + 'hahaha' + "." + imageType ,imageType)
#img.save(pathToFile + self.activeLayer.name() + "." + imageType ,imageType)