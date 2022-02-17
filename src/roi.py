""" A module for storing some sample ROIs for creating Landsat/GOES timelapse.
"""

from shapely.geometry import Polygon

goes_rois = {
    "Creek Fire, CA (2020-09-05)": {
        "region": Polygon(
            [
                [-121.003418, 36.848857],
                [-121.003418, 39.049052],
                [-117.905273, 39.049052],
                [-117.905273, 36.848857],
                [-121.003418, 36.848857],
            ]
        ),
        "start_time": "2020-09-05T15:00:00",
        "end_time": "2020-09-06T02:00:00",
    },
    "Bomb Cyclone (2021-10-24)": {
        "region": Polygon(
            [
                [-159.5954, 60.4088],
                [-159.5954, 24.5178],
                [-114.2438, 24.5178],
                [-114.2438, 60.4088],
            ]
        ),
        "start_time": "2021-10-24T14:00:00",
        "end_time": "2021-10-25T01:00:00",
    },
    "Hunga Tonga Volcanic Eruption (2022-01-15)": {
        "region": Polygon(
            [
                [-192.480469, -32.546813],
                [-192.480469, -8.754795],
                [-157.587891, -8.754795],
                [-157.587891, -32.546813],
                [-192.480469, -32.546813],
            ]
        ),
        "start_time": "2022-01-15T03:00:00",
        "end_time": "2022-01-15T07:00:00",
    },
    "Hunga Tonga Volcanic Eruption Closer Look (2022-01-15)": {
        "region": Polygon(
            [
                [-178.901367, -22.958393],
                [-178.901367, -17.85329],
                [-171.452637, -17.85329],
                [-171.452637, -22.958393],
                [-178.901367, -22.958393],
            ]
        ),
        "start_time": "2022-01-15T03:00:00",
        "end_time": "2022-01-15T07:00:00",
    },
}


landsat_rois = {
    "Aral Sea": Polygon(
        [
            [57.667236, 43.834527],
            [57.667236, 45.996962],
            [61.12793, 45.996962],
            [61.12793, 43.834527],
            [57.667236, 43.834527],
        ]
    ),
    "Dubai": Polygon(
        [
            [54.541626, 24.763044],
            [54.541626, 25.427152],
            [55.632019, 25.427152],
            [55.632019, 24.763044],
            [54.541626, 24.763044],
        ]
    ),
    "Hong Kong International Airport": Polygon(
        [
            [113.825226, 22.198849],
            [113.825226, 22.349758],
            [114.085121, 22.349758],
            [114.085121, 22.198849],
            [113.825226, 22.198849],
        ]
    ),
    "Las Vegas, NV": Polygon(
        [
            [-115.554199, 35.804449],
            [-115.554199, 36.558188],
            [-113.903503, 36.558188],
            [-113.903503, 35.804449],
            [-115.554199, 35.804449],
        ]
    ),
    "Pucallpa, Peru": Polygon(
        [
            [-74.672699, -8.600032],
            [-74.672699, -8.254983],
            [-74.279938, -8.254983],
            [-74.279938, -8.600032],
        ]
    ),
    "Sierra Gorda, Chile": Polygon(
        [
            [-69.315491, -22.837104],
            [-69.315491, -22.751488],
            [-69.190006, -22.751488],
            [-69.190006, -22.837104],
            [-69.315491, -22.837104],
        ]
    ),
}

modis_rois = {
    "World": Polygon(
        [
            [-171.210938, -57.136239],
            [-171.210938, 79.997168],
            [177.539063, 79.997168],
            [177.539063, -57.136239],
            [-171.210938, -57.136239],
        ]
    ),
    "Africa": Polygon(
        [
            [-18.6983, 38.1446],
            [-18.6983, -36.1630],
            [52.2293, -36.1630],
            [52.2293, 38.1446],
        ]
    ),
    "USA": Polygon(
        [
            [-127.177734, 23.725012],
            [-127.177734, 50.792047],
            [-66.269531, 50.792047],
            [-66.269531, 23.725012],
            [-127.177734, 23.725012],
        ]
    ),
}

ocean_rois = {
    "Gulf of Mexico": Polygon(
        [
            [-101.206055, 15.496032],
            [-101.206055, 32.361403],
            [-75.673828, 32.361403],
            [-75.673828, 15.496032],
            [-101.206055, 15.496032],
        ]
    ),
    "North Atlantic Ocean": Polygon(
        [
            [-85.341797, 24.046464],
            [-85.341797, 45.02695],
            [-55.810547, 45.02695],
            [-55.810547, 24.046464],
            [-85.341797, 24.046464],
        ]
    ),
    "World": Polygon(
        [
            [-171.210938, -57.136239],
            [-171.210938, 79.997168],
            [177.539063, 79.997168],
            [177.539063, -57.136239],
            [-171.210938, -57.136239],
        ]
    ),
}