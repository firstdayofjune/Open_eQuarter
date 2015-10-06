# -*- coding: utf-8 -*-

import os,math
from qgis.core import NULL
from mole import oeq_global
from mole.project import config
from mole.extensions import OeQExtension
from mole.stat_corr import contemporary_base_uvalue_by_building_age_lookup

def calculation(self=None, parameters={}):
    from scipy.constants import golden
    from math import floor, ceil
    from PyQt4.QtCore import QVariant
    # factor for golden rule
    dataset = {'BS_QTP': NULL}
    dataset.update(parameters)

    if not oeq_global.isnull([dataset['BS_AR'],dataset['BS_UP'],dataset['HHRS']]):
        dataset['BS_QTP']=float(dataset['BS_AR']) * float(dataset['BS_UP'])*float(dataset['HHRS'])/1000 *0.35 #correction factor


    result = {}
    for i in dataset.keys():
        result.update({i: {'type': QVariant.Double,
                           'value': dataset[i]}})
    return result

extension = OeQExtension(
    extension_id=__name__,

    category='Evaluation',
    subcategory='Present Transm. Heat Loss',
    extension_name='Base Quality (QT, Present)',
    layer_name= 'QT Base Present',
    extension_filepath=os.path.join(__file__),
    colortable = os.path.join(os.path.splitext(__file__)[0] + '.qml'),
    field_id='BS_QTP',
    source_type='none',
    par_in=['BS_AR','BS_UP','HHRS'],
    layer_in=config.data_layer_name,
    layer_out=config.data_layer_name,
    active=True,
    show_results=['BS_QTP'],
    description=u"Calculate the present Transmission Heat Loss of the Building's baseplate",
    evaluation_method=calculation)

extension.registerExtension(default=True)
