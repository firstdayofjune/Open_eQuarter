# coding: utf8
# OeQ autogenerated lookup function for 'U-Values of Roofs as Projection (method 2) in correlation to year of construction, based on the source data of the survey for the "German Building Typology developed by the "Institut für Wohnen und Umwelt", Darmstadt/Germany, 2011-2013'

import math
import numpy as np
import oeqLookuptable as oeq
def present_roofprj2_uvalue_SFH_by_building_age_lookup(*xin):


    l_lookup = oeq.lookuptable(
[
1849,1.746,
1850,1.746,
1851,1.75,
1852,1.75,
1853,1.75,
1854,1.75,
1855,1.75,
1856,1.714,
1857,1.66,
1858,1.595,
1859,1.525,
1860,1.455,
1861,1.39,
1862,1.336,
1863,1.3,
1864,1.284,
1865,1.283,
1866,1.291,
1867,1.3,
1868,1.304,
1869,1.304,
1870,1.302,
1871,1.3,
1872,1.299,
1873,1.299,
1874,1.299,
1875,1.3,
1876,1.3,
1877,1.3,
1878,1.3,
1879,1.3,
1880,1.3,
1881,1.3,
1882,1.3,
1883,1.3,
1884,1.3,
1885,1.3,
1886,1.3,
1887,1.3,
1888,1.3,
1889,1.3,
1890,1.3,
1891,1.3,
1892,1.3,
1893,1.3,
1894,1.3,
1895,1.3,
1896,1.3,
1897,1.3,
1898,1.3,
1899,1.3,
1900,1.3,
1901,1.3,
1902,1.3,
1903,1.3,
1904,1.3,
1905,1.301,
1906,1.301,
1907,1.3,
1908,1.298,
1909,1.297,
1910,1.297,
1911,1.3,
1912,1.306,
1913,1.311,
1914,1.311,
1915,1.3,
1916,1.276,
1917,1.24,
1918,1.197,
1919,1.15,
1920,1.103,
1921,1.06,
1922,1.024,
1923,1,
1924,0.989,
1925,0.989,
1926,0.994,
1927,1,
1928,1.003,
1929,1.003,
1930,1.002,
1931,1,
1932,0.999,
1933,0.999,
1934,1,
1935,1,
1936,1,
1937,1,
1938,1,
1939,1,
1940,1.001,
1941,1.001,
1942,1.001,
1943,1,
1944,0.997,
1945,0.993,
1946,0.989,
1947,0.984,
1948,0.98,
1949,0.977,
1950,0.973,
1951,0.967,
1952,0.957,
1953,0.94,
1954,0.916,
1955,0.885,
1956,0.849,
1957,0.81,
1958,0.769,
1959,0.73,
1960,0.699,
1961,0.68,
1962,0.676,
1963,0.68,
1964,0.685,
1965,0.68,
1966,0.66,
1967,0.628,
1968,0.588,
1969,0.545,
1970,0.503,
1971,0.465,
1972,0.434,
1973,0.41,
1974,0.396,
1975,0.392,
1976,0.397,
1977,0.41,
1978,0.429,
1979,0.446,
1980,0.452,
1981,0.44,
1982,0.403,
1983,0.352,
1984,0.3,
1985,0.26,
1986,0.25,
1987,0.25,
1988,0.25,
1989,0.26,
1990,0.264,
1991,0.264,
1992,0.262,
1993,0.26,
1994,0.261,
1995,0.264,
1996,0.268,
1997,0.27,
1998,0.27,
1999,0.267,
2000,0.264,
2001,0.26,
2002,0.257,
2003,0.254,
2004,0.251,
2005,0.25,
2006,0.25,
2007,0.25,
2008,0.25,
2009,0.25,
2010,0.25,
2011,0.25,
2012,0.25,
2013,0.25,
2014,0.25,
2015,0.25,
2016,0.25,
2017,0.25,
2018,0.25,
2019,0.25,
2020,0.25,
2021,0.25])
    return(l_lookup.lookup(xin))
