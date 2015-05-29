# coding: utf8
# OeQ autogenerated lookup function for 'Window/Wall Ratio in correlation to year of construction, based on the source data of the survey for the "German Building Typology developed by the "Institut für Wohnen und Umwelt", Darmstadt/Germany, 2011-2013'

import math
import numpy as np
import oeqLookuptable as oeq
def window_wall_ratio_SDH_by_building_age_lookup(*xin):


    l_lookup = oeq.lookuptable(
[
1849,0.24,
1850,0.24,
1851,0.24,
1852,0.24,
1853,0.24,
1854,0.24,
1855,0.24,
1856,0.24,
1857,0.24,
1858,0.24,
1859,0.24,
1860,0.24,
1861,0.24,
1862,0.24,
1863,0.24,
1864,0.24,
1865,0.24,
1866,0.24,
1867,0.24,
1868,0.24,
1869,0.24,
1870,0.24,
1871,0.24,
1872,0.24,
1873,0.24,
1874,0.24,
1875,0.24,
1876,0.24,
1877,0.24,
1878,0.24,
1879,0.24,
1880,0.24,
1881,0.24,
1882,0.24,
1883,0.24,
1884,0.24,
1885,0.24,
1886,0.24,
1887,0.24,
1888,0.24,
1889,0.24,
1890,0.24,
1891,0.24,
1892,0.24,
1893,0.24,
1894,0.24,
1895,0.24,
1896,0.24,
1897,0.24,
1898,0.24,
1899,0.24,
1900,0.24,
1901,0.24,
1902,0.24,
1903,0.24,
1904,0.24,
1905,0.24,
1906,0.24,
1907,0.24,
1908,0.24,
1909,0.241,
1910,0.241,
1911,0.24,
1912,0.24,
1913,0.24,
1914,0.24,
1915,0.24,
1916,0.247,
1917,0.258,
1918,0.271,
1919,0.285,
1920,0.299,
1921,0.312,
1922,0.323,
1923,0.33,
1924,0.333,
1925,0.333,
1926,0.332,
1927,0.33,
1928,0.329,
1929,0.329,
1930,0.33,
1931,0.33,
1932,0.33,
1933,0.33,
1934,0.33,
1935,0.33,
1936,0.33,
1937,0.33,
1938,0.33,
1939,0.33,
1940,0.33,
1941,0.33,
1942,0.33,
1943,0.33,
1944,0.33,
1945,0.331,
1946,0.332,
1947,0.334,
1948,0.337,
1949,0.34,
1950,0.344,
1951,0.347,
1952,0.349,
1953,0.35,
1954,0.349,
1955,0.346,
1956,0.343,
1957,0.34,
1958,0.337,
1959,0.335,
1960,0.332,
1961,0.33,
1962,0.327,
1963,0.326,
1964,0.326,
1965,0.33,
1966,0.339,
1967,0.351,
1968,0.365,
1969,0.38,
1970,0.395,
1971,0.408,
1972,0.42,
1973,0.43,
1974,0.43,
1975,0.43,
1976,0.43,
1977,0.43,
1978,0.416,
1979,0.399,
1980,0.382,
1981,0.37,
1982,0.364,
1983,0.364,
1984,0.367,
1985,0.37,
1986,0.372,
1987,0.372,
1988,0.371,
1989,0.37,
1990,0.368,
1991,0.367,
1992,0.368,
1993,0.37,
1994,0.375,
1995,0.38,
1996,0.382,
1997,0.38,
1998,0.371,
1999,0.357,
2000,0.339,
2001,0.32,
2002,0.301,
2003,0.284,
2004,0.27,
2005,0.26,
2006,0.256,
2007,0.256,
2008,0.258,
2009,0.26,
2010,0.261,
2011,0.261,
2012,0.261,
2013,0.26,
2014,0.26,
2015,0.26,
2016,0.26,
2017,0.26,
2018,0.26,
2019,0.26,
2020,0.26,
2021,0.26])
    return(l_lookup.lookup(xin))
