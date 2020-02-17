<<<<<<< HEAD
import os
from pathlib import Path
import subprocess
from osgeo import gdal, ogr, osr
from pathlib import Path


# Em config cho lai lai nhe!

# Thu muc chua anh can cat
foin = Path('C:/Users/soiqu/Desktop/test_pyQGIS/2000/')
# Duong dan den shapefile lam ranh cat
shp_path='C:/Users/soiqu/Desktop/test_pyQGIS/Ranhgioi_songBa_final_shp/RanhGioi_songBa_final.shp'
# Thu muc luu ket qua
foout='C:/Users/soiqu/Desktop/test_pyQGIS/kq/'


def getFname(path):
    #/content/2000/216_TVDI_200008.tif
    if('/' in path):
        arr1=path.split('/')
    else:
        arr1=path.split('\\')
    return arr1[len(arr1)-1]

for raster_file in foin.glob('*.tif'):
    # print(raster_file)
    #cmd='"gdalwarp -of GTiff -dstnodata -9999.0 -overwrite -cutline '+str(shp_path)+' -crop_to_cutline '+str(raster_file)+' '+getFname(str(raster_file))+'"'
    cmd='"gdalwarp" -cutline "'+str(shp_path)+'" -crop_to_cutline -of GTiff -dstnodata -9999.0 -overwrite "'+str(raster_file)+'" "'+foout+'t_'+getFname(str(raster_file))+'.tif"'
    #print(cmd)
=======
import os
from pathlib import Path
import subprocess
from osgeo import gdal, ogr, osr
from pathlib import Path


# Em config cho lai lai nhe!

# Thu muc chua anh can cat
foin = Path('C:/Users/soiqu/Desktop/test_pyQGIS/2000/')
# Duong dan den shapefile lam ranh cat
shp_path='C:/Users/soiqu/Desktop/test_pyQGIS/shp/gialai.shp'
# Thu muc luu ket qua
foout='C:/Users/soiqu/Desktop/test_pyQGIS/kq/'


def getFname(path):
    #/content/2000/216_TVDI_200008.tif
    if('/' in path):
        arr1=path.split('/')
    else:
        arr1=path.split('\\')
    return arr1[len(arr1)-1]

for raster_file in foin.glob('*.tif'):
    # print(raster_file)
    #cmd='"gdalwarp -of GTiff -dstnodata -9999.0 -overwrite -cutline '+str(shp_path)+' -crop_to_cutline '+str(raster_file)+' '+getFname(str(raster_file))+'"'
    cmd='"gdalwarp" -cutline "'+str(shp_path)+'" -crop_to_cutline -of GTiff -dstnodata -9999.0 -overwrite "'+str(raster_file)+'" "'+foout+'t_'+getFname(str(raster_file))+'.tif"'
    #print(cmd)
>>>>>>> 22cd75c443460d3981125f46b7d9c5f879c5dce3
    subprocess.Popen(cmd,shell=True)