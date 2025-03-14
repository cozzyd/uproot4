# BSD 3-Clause License; see https://github.com/scikit-hep/uproot4/blob/main/LICENSE


import numpy
import pytest
import skhep_testdata

import uproot


def test_TRefArray():
    with uproot.open(skhep_testdata.data_path("uproot-issue513.root"))["Delphes"] as t:
        array = t["GenJet.Particles"].array(entry_stop=1, library="np")[0]
        assert len(array) == 7
        assert array[0].refs.tolist() == [
            2396,
            2320,
            2075,
            2483,
            2479,
            2499,
            2259,
            1865,
            2078,
            2482,
            2503,
            2477,
            2502,
            2480,
            2061,
            2077,
            2393,
            2376,
            2496,
            2504,
            2495,
            2505,
            1318,
            1317,
            2506,
            2076,
            2346,
            2501,
            2107,
            1957,
            2241,
            1823,
            2242,
            1825,
            1863,
            2399,
            1824,
            1866,
            2497,
            1996,
            2345,
            1864,
            2243,
            1821,
            2244,
        ]
        assert array[1].refs.tolist() == [
            2370,
            1830,
            2371,
            2024,
            1412,
            2250,
            1530,
            2500,
            2498,
            2388,
            1949,
            1885,
            2055,
            2069,
            2368,
            2054,
            2059,
            2272,
            2053,
            2367,
        ]


def test_awkward_TRefArray():
    awkward = pytest.importorskip("awkward")
    with uproot.open(skhep_testdata.data_path("uproot-issue513.root"))["Delphes"] as t:
        assert t["GenJet.Particles"].array(entry_stop=1)[0].tolist() == [
            {
                "fName": "",
                "fSize": 45,
                "refs": [
                    2396,
                    2320,
                    2075,
                    2483,
                    2479,
                    2499,
                    2259,
                    1865,
                    2078,
                    2482,
                    2503,
                    2477,
                    2502,
                    2480,
                    2061,
                    2077,
                    2393,
                    2376,
                    2496,
                    2504,
                    2495,
                    2505,
                    1318,
                    1317,
                    2506,
                    2076,
                    2346,
                    2501,
                    2107,
                    1957,
                    2241,
                    1823,
                    2242,
                    1825,
                    1863,
                    2399,
                    1824,
                    1866,
                    2497,
                    1996,
                    2345,
                    1864,
                    2243,
                    1821,
                    2244,
                ],
            },
            {
                "fName": "",
                "fSize": 20,
                "refs": [
                    2370,
                    1830,
                    2371,
                    2024,
                    1412,
                    2250,
                    1530,
                    2500,
                    2498,
                    2388,
                    1949,
                    1885,
                    2055,
                    2069,
                    2368,
                    2054,
                    2059,
                    2272,
                    2053,
                    2367,
                ],
            },
            {
                "fName": "",
                "fSize": 21,
                "refs": [
                    2284,
                    1883,
                    2282,
                    2108,
                    1939,
                    2102,
                    2356,
                    2005,
                    2236,
                    1364,
                    1770,
                    1882,
                    1840,
                    2249,
                    2446,
                    1985,
                    1839,
                    2248,
                    1365,
                    1841,
                    1842,
                ],
            },
            {
                "fName": "",
                "fSize": 31,
                "refs": [
                    1379,
                    2123,
                    2090,
                    1378,
                    1593,
                    1836,
                    1862,
                    1859,
                    1904,
                    1984,
                    1322,
                    1383,
                    2074,
                    2257,
                    1591,
                    1382,
                    2357,
                    1954,
                    2066,
                    2256,
                    2010,
                    2011,
                    2490,
                    2251,
                    2343,
                    1993,
                    2344,
                    1846,
                    1992,
                    1843,
                    1845,
                ],
            },
            {
                "fName": "",
                "fSize": 26,
                "refs": [
                    1989,
                    1911,
                    1990,
                    1629,
                    2277,
                    2419,
                    2139,
                    2292,
                    1618,
                    2518,
                    2519,
                    2516,
                    2509,
                    2135,
                    2136,
                    2514,
                    2517,
                    2510,
                    2512,
                    2420,
                    2402,
                    1619,
                    1617,
                    2494,
                    1400,
                    2511,
                ],
            },
            {
                "fName": "",
                "fSize": 32,
                "refs": [
                    2082,
                    2445,
                    1868,
                    1893,
                    2384,
                    2081,
                    1512,
                    2263,
                    2261,
                    1870,
                    2398,
                    2017,
                    1849,
                    2401,
                    1875,
                    2387,
                    1872,
                    2315,
                    2260,
                    1873,
                    2386,
                    1522,
                    1874,
                    2083,
                    1775,
                    2086,
                    2237,
                    2087,
                    1876,
                    2084,
                    2264,
                    2265,
                ],
            },
            {
                "fName": "",
                "fSize": 26,
                "refs": [
                    2266,
                    1847,
                    1894,
                    2142,
                    2291,
                    1599,
                    1774,
                    1916,
                    2200,
                    2129,
                    2148,
                    2146,
                    2143,
                    2144,
                    2145,
                    1913,
                    2290,
                    2421,
                    1918,
                    1706,
                    2137,
                    1914,
                    2289,
                    1915,
                    1627,
                    1628,
                ],
            },
        ]


def test_same_names():
    with uproot.open(skhep_testdata.data_path("uproot-issue513.root"))["Delphes"] as t:
        one, two = t.values(filter_name="Particle_size")
        assert (
            one.cache_key
            == "ac4a884e-c931-11ea-a7a5-c78b2480beef:/Delphes;1:Particle_size(3)"
        )
        assert (
            two.cache_key
            == "ac4a884e-c931-11ea-a7a5-c78b2480beef:/Delphes;1:Particle_size(17)"
        )
        assert one.object_path == "/Delphes;1:Particle_size"
        assert two.object_path == "/Delphes;1:Particle_size"
