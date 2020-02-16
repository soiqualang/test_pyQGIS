import os
from pathlib import Path
import subprocess
from osgeo import gdal, ogr, osr
from pathlib import Path


# Em config cho lai lai nhe!

# Thu muc chua anh can cat
foin = Path('C:/Users/soiqu/Desktop/2000/')
# Duong dan den shapefile lam ranh cat
shp_path='C:/Users/soiqu/Desktop/shp/gialai.shp'
# Thu muc luu ket qua
foout='C:/Users/soiqu/Desktop/cutting/'


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
    cmd='"gdalwarp" -cutline "'+str(shp_path)+'" -crop_to_cutline -of GTiff -dstnodata -9999.0 -overwrite "'+str(raster_file)+'" "'+fout+'t_'+getFname(str(raster_file))+'.tif"'
    print(cmd)
    subprocess.Popen(cmd,shell=True)