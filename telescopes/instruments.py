Euclid_VIS = {
    "pix_scale":0.1,
    "ls":'-',
    "noise_level":0.007,
    "depth":24.5, #23.9,#25.2,
    "fwhm":0.17,
    "major_band":"VIS",
    "bands":{
        "VIS": {
            "mag":25.2, "min_max":[550, 900], 'fwhm':0.17}
            }
             }

Euclid_NIR = {
    "pix_scale":0.3,
    "noise_level":0.009,
    "ls":'--',
    "depth":24,
    "fwhm":0.2, ##### VERIFY THIS, https://ui.adsabs.harvard.edu/abs/2020A%26A...644A..31E/abstract say somthing else
    "major_band":"J",
    "bands":{
        "Y": {
            "mag":24, "min_max":[920, 1046], 'fwhm':0.2},
        "J": {
            "mag":24, "min_max":[1146, 1372], 'fwhm':0.2},
        "H": {
            "mag":24, "min_max":[1372, 2000], 'fwhm':0.2}
            }
            }

JWST_NIRCAM = {
    'pix_scale':0.031,
    "noise_level":0.0001,
    'ls':'-',
    'depth':28,
    'fwhm':0.06,
    'major_band':'f606W',
    'bands':{
        'F070W':{
            "mag":28, "min_max":[621, 781], 'fwhm':0.08},  #mag is 10sigma point sources limit
        'F090W':{
            "mag":23.5, "min_max":[795, 1005], 'fwhm':0.08},
        'F115W':{
            "mag":23.5, "min_max":[1013, 1282], 'fwhm':0.08},
        'F140M':{
            "mag":23.5, "min_max":[1331, 1479], 'fwhm':0.08},
        'F150W':{
            "mag":23.5, "min_max":[1331, 1668], 'fwhm':0.08},
        'F162M':{
            "mag":23.5, "min_max":[1542, 1713], 'fwhm':0.08},
        'F164NW':{
            "mag":23.5, "min_max":[1635, 1653], 'fwhm':0.08},
        'F150W2':{
            "mag":23.5, "min_max":[1008, 2334], 'fwhm':0.08},
        'F182M':{
            "mag":23.5, "min_max":[1722, 1968], 'fwhm':0.08},
        'F187N':{
            "mag":23.5, "min_max":[1863, 1884], 'fwhm':0.08},
        'F200W':{
            "mag":23.5, "min_max":[1755, 2226], 'fwhm':0.08},
        'F210M':{
            "mag":23.5, "min_max":[1992, 2201], 'fwhm':0.08},
        'F212NW':{"mag":23.5, "min_max":[2109, 2134], 'fwhm':0.08},

            }
        }

HST_ACS={
    'pix_scale':0.03,
    "noise_level":0.007,
    'ls':'-',
    'depth':25,
    'fwhm':0.067,
    'major_band':'f606W',
    'bands':{
        'F220W':{
            "mag":23.5, "min_max":[185.4, 298.1], 'fwhm':0.08}, # PSFs are approximated by a table giving PSF/lambda (https://hst-docs.stsci.edu/wfc3ihb/chapter-6-uvis-imaging-with-wfc3/6-6-uvis-optical-performance()
        'F250W':{
            "mag":23.7, "min_max":[209.4, 353.4], 'fwhm':0.075}, # mag are zero points, calculated on WCS when available
        'F330W':{
            "mag":24.06, "min_max":[295.8, 371.9], 'fwhm':0.075},
        # 'F344N':{"mag":21.5, "min_max":[295.8, 371.9], 'fwhm':0.075},
        # 'FR338N':{"mag":, "min_max":[381.0, 395.0], 'fwhm':0.075},
        'F435W':{
            "mag":25.648, "min_max":[359.3, 486.0], 'fwhm':0.07},
        # 'FR459M':{"mag":, "min_max":[428.0, 490.7], 'fwhm':0.07},
        'F475W':{
            "mag":26.04, "min_max":[385.7, 555.9], 'fwhm':0.067},
        'F502N':{
            "mag":22.28, "min_max":[496.6, 507.9], 'fwhm':0.067},
        'FR550N':{
            "mag":24.84, "min_max":[495.5, 514.5], 'fwhm':0.067},
        'F555W':{
            "mag":25.70, "min_max":[458.0, 619.3], 'fwhm':0.067},
        'F550M':{
            "mag":24.85, "min_max":[524.6, 592.9], 'fwhm':0.067},
        'F606W':{
            "mag":26.48, "min_max":[462.5, 717.8], 'fwhm':0.067}
            }
        }

Rubin_Wide_field_image = {
    'pix_scale':0.08,
    "noise_level":0.001,
    'ls':'-',
    'depth':24.5,
    'fwhm':0.8,
    'bands':{"u":{"mag":23.39, "min_max":[350, 400], 'fwhm':0.92},
            "g":{"mag":24.51, "min_max":[400, 552], 'fwhm':0.87},
            "r":{"mag":24.49, "min_max":[552, 691], 'fwhm':0.83},
            "i":{"mag":24.37, "min_max":[691, 818], 'fwhm':0.80},
            "z":{"mag":24.21, "min_max":[818, 922], 'fwhm':0.78},
            "y":{"mag":23.77, "min_max":[948, 1060], 'fwhm':0.76},
            }
                        }