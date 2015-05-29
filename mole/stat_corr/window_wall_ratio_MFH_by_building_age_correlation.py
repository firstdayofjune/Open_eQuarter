# OeQ autogenerated correlation for 'Window/Wall Ratio in Correlation to the Building Age'

import math
import numpy as np
import oeqCorrelation as oeq
def window_wall_ratio_MFH_by_building_age_correlation(*xin):

    # OeQ autogenerated correlation for 'Window to Wall Ratio in all Directions'
    A_WIN_BY_AW= oeq.correlation(
    const= -38790.5022018,
    a=     79.0503866069,
    b=     -0.0603881990871,
    c=     2.04958423547e-05,
    d=     -2.60775001815e-09,
    mode= "lin")

    return dict(A_WIN_BY_AW=A_WIN_BY_AW.lookup(*xin))

