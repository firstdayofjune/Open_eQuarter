from platform import system
from qgis.core import QgsRectangle

# Project information
project_crs = 'EPSG:3857'

### Information needed to use external plugins
# OpenStreetMap plugin
ol_plugin_name = 'openlayers_plugin'
open_layer_type_id = 4
# id=0 - Google Physical
# id=1 - Google Streets
# id=4 - OpenStreetMap

# Point Sampling Tool
pst_plugin_name = 'pointsamplingtool'
pst_output_layer_name = 'pst_out'
pst_input_layer_name = 'pst_points_of_interest'

### Default values
# default extent is set, after the OSM-layer was loaded (currently: extent of Germany)
x = 10.447683
y = 51.163375
scale = 4
default_extent = QgsRectangle(x - scale, y - scale, x + scale, y + scale)
default_extent_crs = 'EPSG:4326'

# name of the shapefile which will be created to define the investigation area
investigation_shape_layer_name = 'Investigation Area'
housing_layer_name = 'Floor plan'
housing_coordinate_layer_name = ''
# name of the wms-raster which will be loaded and is the basis for the clipping
clipping_raster_layer_name = 'Investigation Area - raster'


def qgis_prefix_path():
    if system() == 'Windows':
        return 'D:/OSGEO4~1/apps/qgis'
    else:
        return '/Applications/QGIS.app/Contents/MacOS'