Euclid_VIS = {
    "pix_scale":0.1,
    "ls":'-',
    "depth":25.9, #23.9,#25.2,
    "main_band":"VIS",
    "bands":{
        "VIS": {
            "zp":25.9, "min_max":[550, 900], 'fwhm':0.17}
            }
             }

Euclid_NIR = {
    "pix_scale":0.3,
    "ls":'--',
    "fwhm":0.2, ##### VERIFY THIS, https://ui.adsabs.harvard.edu/abs/2020A%26A...644A..31E/abstract say somthing else
    "main_band":"J",
    "bands":{
        "Y": {
            "zp":25.04, "min_max":[920, 1146], 'fwhm':0.2}, # http://arxiv.org/abs/2203.01650
        "J": {
            "zp":25.26, "min_max":[1146, 1372], 'fwhm':0.2},
        "H": {
            "zp":25.21, "min_max":[1372, 2000], 'fwhm':0.2}
            }
            }

JWST_NIRCAM = {
    'pix_scale':0.031,
    'ls':'-',
    'fwhm':0.06,
    'main_band':'f200W',
    'bands':{
        'F070W':{
            "zp":28.7, "min_max":[621, 781], 'fwhm':0.03},  #zp is the one for f200w, psf fwhm are good
        'F090W':{
            "zp":None, "min_max":[795, 1005], 'fwhm':0.034},
        'F115W':{
            "zp":None, "min_max":[1013, 1282], 'fwhm':0.040},
        'F140M':{
            "zp":None, "min_max":[1331, 1479], 'fwhm':0.048},
        'F150W':{
            "zp":None, "min_max":[1331, 1668], 'fwhm':0.050},
        'F162M':{
            "zp":None, "min_max":[1542, 1713], 'fwhm':0.055},
        'F164NW':{
            "zp":None, "min_max":[1635, 1653], 'fwhm':0.056},
        'F150W2':{
            "zp":None, "min_max":[1008, 2334], 'fwhm':0.046},
        'F182M':{
            "zp":None, "min_max":[1722, 1968], 'fwhm':0.062},
        'F187N':{
            "zp":None, "min_max":[1863, 1884], 'fwhm':0.064},
        'F200W':{
            "zp":None, "min_max":[1755, 2226], 'fwhm':0.066},
        'F210M':{
            "zp":None, "min_max":[1992, 2201], 'fwhm':0.071},
        'F212N':{"zp":None, "min_max":[2109, 2134], 'fwhm':0.072},
        'F250M':{"zp":None, "min_max":[2503-180/2, 2503-180/2], 'fwhm':0.084},
        'F277W':{"zp":None, "min_max":[2762-683/2, 2762+683/2], 'fwhm':0.91},
        'F300M':{"zp":None, "min_max":[2989-315/2, 2989+315/2], 'fwhm':0.1},
        'F323N':{"zp":None, "min_max":[3237-38/2, 3237+38/2], 'fwhm':0.108},
        # 'F335N':{"zp":29.8, "min_max":[3237-38/2, 3237+38/2], 'fwhm':0.111},
        'F356M':{"zp":None, "min_max":[3362-352/2, 3362+352/2], 'fwhm':0.115},
        'F360M':{"zp":None, "min_max":[3624-370/2, 3624+370/2], 'fwhm':0.120},
        'F356W':{"zp":None, "min_max":[3568-781/2, 3568+781/2], 'fwhm':0.115},
        'F405N':{"zp":None, "min_max":[4052-45/2, 4052+45/2], 'fwhm':0.136},
        'F410M':{"zp":None, "min_max":[4082-438/2, 4082+438/2], 'fwhm':0.137},
        'F430M':{"zp":None, "min_max":[4281-228/2, 4281+228/2], 'fwhm':0.145},
        'F444W':{"zp":None, "min_max":[4408-1029/2, 4408+1029/2], 'fwhm':0.145},
        'F460M':{"zp":None, "min_max":[4630-229/2, 4630+229/2], 'fwhm':0.155},
        'F466N':{"zp":None, "min_max":[4654-54/2, 4654+54/2], 'fwhm':0.158},
        'F470N':{"zp":None, "min_max":[4708-51/2, 4708+51/2], 'fwhm':0.160},
        'F480M':{"zp":None, "min_max":[4874-300/2, 4874+300/2], 'fwhm':0.162},



            }
        }


JWST_MIRI = {'pix_scale':0.031,
    'ls':'--',
    'fwhm':0.40,
    'bands':{
        'F560W':{
            "zp":None, "min_max":[5600-120/2, 5600+120/2], 'fwhm':0.22},  #all good but zp
        'F770W':{
            "zp":None, "min_max":[7700-220/2, 7700+220/2], 'fwhm':0.25},
        'F1000W':{
            "zp":None, "min_max":[10000-200/2, 10000+200/2], 'fwhm':0.32},
        'F1130M':{
            "zp":None, "min_max":[11300-70/2, 11300+70/2], 'fwhm':0.36},
        'F1280W':{
            "zp":None, "min_max":[12800-240/2, 12800+240/2], 'fwhm':0.41},
        'F1500M':{
            "zp":None, "min_max":[15000-300/2, 15000+300/2], 'fwhm':0.48},
        'F1800NW':{
            "zp":None, "min_max":[18000-300/2, 18000+300/2], 'fwhm':0.58},
        'F2100W':{
            "zp":None, "min_max":[21000-500/2, 21000+500/2], 'fwhm':0.67,
        'F2250M':{
            "zp":None, "min_max":[22500-400/2, 22500+400/2], 'fwhm':0.82}
        # 'F2250WR':{
        #     "zp":29.8, "min_max":[2250-400, 2250+400], 'fwhm':0.82}
        #     }
        }}}


HST_ACS={
    'pix_scale':0.03,
    'ls':'-',
    'fwhm':0.067,
    'main_band':'F606W',
    'bands':{
        'F220W':{
            "zp":23.5, "min_max":[185.4, 298.1], 'fwhm':0.08}, # PSFs are approximated by a table giving PSF/lambda (https://hst-docs.stsci.edu/wfc3ihb/chapter-6-uvis-izping-with-wfc3/6-6-uvis-optical-performance()
        'F250W':{
            "zp":23.7, "min_max":[209.4, 353.4], 'fwhm':0.075}, # zp are good, calculated on WCS when available
        'F330W':{
            "zp":24.06, "min_max":[295.8, 371.9], 'fwhm':0.075},
        # 'F344N':{"zp":21.5, "min_max":[295.8, 371.9], 'fwhm':0.075},
        # 'FR338N':{"zp":, "min_max":[381.0, 395.0], 'fwhm':0.075},
        'F435W':{
            "zp":25.648, "min_max":[359.3, 486.0], 'fwhm':0.07},
        # 'FR459M':{"zp":, "min_max":[428.0, 490.7], 'fwhm':0.07},
        'F475W':{
            "zp":26.04, "min_max":[385.7, 555.9], 'fwhm':0.067},
        'F502N':{
            "zp":22.28, "min_max":[496.6, 507.9], 'fwhm':0.067},
        'FR550N':{
            "zp":24.84, "min_max":[495.5, 514.5], 'fwhm':0.067},
        'F555W':{
            "zp":25.70, "min_max":[458.0, 619.3], 'fwhm':0.067},
        'F550M':{
            "zp":24.85, "min_max":[524.6, 592.9], 'fwhm':0.067},
        'F606W':{
            "zp":26.48, "min_max":[462.5, 717.8], 'fwhm':0.067}
            }
        }

Rubin_Wide_field_imager = {
    'pix_scale':0.08, #verified
    'ls':'-',
    'depth':24.5,
    'fwhm':0.8, #verified
    'bands':{"u":{"zp":23.39, "min_max":[320, 400], 'fwhm':0.92}, # zps look to small, need to check.
            "g":{"zp":24.51, "min_max":[400, 552], 'fwhm':0.87},
            "r":{"zp":24.49, "min_max":[552, 691], 'fwhm':0.83},
            "i":{"zp":24.37, "min_max":[691, 818], 'fwhm':0.80},
            "z":{"zp":24.21, "min_max":[818, 922], 'fwhm':0.78},
            "y":{"zp":23.77, "min_max":[950, 1080], 'fwhm':0.76},
            }
                        }

SDSS_imaging_camera = {
    'pix_scale':0.4, #verified
    'ls':'-',
    'fwhm':1.2, #median verified
    'bands':{"u '":{"zp":23.39, "min_max":[354-57/2, 354+57/2], 'fwhm':1.35},  # fwhm aprrox from https://arxiv.org/abs/1111.6619
            "g '":{"zp":24.51, "min_max":[477-137/2, 477+137/2], 'fwhm':1.3}, #filters shapes from https://www.astro.princeton.edu/PBOOK/camera/camera.htm
            "r '":{"zp":24.8, "min_max":[623-137/2, 623+137/2], 'fwhm':1.15}, # zero points https://www.sdss.org/dr12/algorithms/magnitudes/
            "i '":{"zp":24.37, "min_max":[763-153/2, 763+153/2], 'fwhm':1.08},
            "z '":{"zp":24.21, "min_max":[913-95/3, 913+95/2], 'fwhm':1.15},
            }
                        }