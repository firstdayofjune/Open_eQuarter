# -*- coding: utf-8 -*-

from qgis.core import NULL
from mole.project import config

def calculation(self=None, parameters={}):
        return self.decode_color(parameters['FLRS_R'],
                                 parameters['FLRS_G'],
                                 parameters['FLRS_B'],
                                 parameters['FLRS_a'],
                                 ['FLOORS'],
                                 'average')


import os
from mole.extensions import OeQExtension

extension = OeQExtension(
    extension_id=__name__,
    category='Import',
    subcategory='WMS',
    extension_name='Floors (ALK, WMS)',
    field_id='FLRS',   #used for point sampling tool
    par_in=['FLRS_R','FLRS_G','FLRS_B','FLRS_a'],
    source_type='wms',
    layer_name='Floors (WMS Capture)',
    layer_in=config.pst_output_layer_name,
    layer_out=config.data_layer_name,
    active=True,
    description=u'',
    source='crs=EPSG:4326&dpiMode=7&format=image/png&layers=2&styles=&url=http://fbinter.stadt-berlin.de/fb/wms/senstadt/alk_gebaeude',
    extension_filepath=os.path.join(__file__),
    colortable = os.path.join(os.path.splitext(__file__)[0] + '.qml'),
    evaluation_method=calculation)

extension.registerExtension(default=True)
