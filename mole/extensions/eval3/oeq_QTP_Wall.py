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
    dataset = {'WL_QTP': NULL}
    dataset.update(parameters)

    if not oeq_global.isnull([dataset['WL_AR'],dataset['WL_UP'],dataset['HHRS']]):
        dataset['WL_QTP']=float(dataset['WL_AR']) * float(dataset['WL_UP'])*float(dataset['HHRS'])/1000

    result = {}
    for i in dataset.keys():
        result.update({i: {'type': QVariant.Double,
                           'value': dataset[i]}})
    return result


extension = OeQExtension(
    extension_id=__name__,

    category='Evaluation',
    subcategory='Wall',
    extension_name='Wall Quality (QT, Present)',
    layer_name= 'QT Wall Present',
    extension_filepath=os.path.join(__file__),
    colortable = os.path.join(os.path.splitext(__file__)[0] + '.qml'),
    field_id='WL_QTP',
    source_type='none',
    par_in=['WL_AR','WL_UP','HHRS'],
    layer_in=config.data_layer_name,
    layer_out=config.data_layer_name,
    active=True,
    show_results=['WL_QTP'],
    description=u"Calculate the present Transmission Heat Loss of the Building's Walls",
    evaluation_method=calculation)

extension.registerExtension(default=True)