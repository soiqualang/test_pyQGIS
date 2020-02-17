from PyQt5.QtCore import QTimer

#Lưu ý là vùng tấm ảnh xuất bằng với vùng map đang mở trên QGIS
#Do vậy chỉnh vùng hiện bản đồ trên QGIS cho phù hợp rồi hãy xuất

#Cấu hình thư mục chứa ảnh
filePath = 'C:/Users/soiqu/Desktop/test_pyQGIS/png/'



#prefixes = ['t_216_TVDI_200003.tif', 't_216_TVDI_200012.tif', 't_216_TVDI_200011.tif']
prefixes = []
count = 0

#scale = 640
layers = []
for layer in QgsProject.instance().mapLayers().values():
    #layers.append(layer)
    #print(layer.id());
    print(layer.name());
    #Chỉ lấy những lớp bắt đầu bằng chữ t_
    if layer.name().startswith("t_"):
        prefixes.append(layer.name())
    

# print(layers[0].extent())
# map.setExtent(layers[0].extent())
# map.setRect(20, 20, 20, 20)

# Lên danh sách layer
def prepareMap():
    layers = []
    #layers = QgsProject.instance().mapLayers()
    for layer in QgsProject.instance().mapLayers().values():
        #Chỉ lấy những lớp bắt đầu bằng chữ t_
        if layer.name().startswith("t_"):
            layers.append(layer)

    # Tắt hết layer
    for layer in layers:
        QgsProject.instance().layerTreeRoot().findLayer(layer).setItemVisibilityChecked(False)

    # Chọn lớp cần xuất
    exportLayers = []
    for layer in QgsProject.instance().mapLayers().values():
        if layer.name().startswith(prefixes[count]):
            QgsProject.instance().layerTreeRoot().findLayer(layer).setItemVisibilityChecked(True)
            # iface.actionZoomToSelected().trigger()
            # qgis.utils.iface.mapCanvas().zoomScale(scale)

    QTimer.singleShot(1000, exportMap) # Chờ 1 giây đẻ export

def exportMap(): # Save as a PNG
    global count
    iface.mapCanvas().saveAsImage( filePath + prefixes[count] + ".png" )
    print("Layer",prefixes[count],"Đã xuất!")
    if count < len(prefixes)-1:
        QTimer.singleShot(1000, prepareMap) # Chờ 1s để xuất layer tiếp
    count += 1

prepareMap()