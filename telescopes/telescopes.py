from telescopes.surveys import Euclid_Wide, Euclid_Deep
from telescopes.surveys import JWST_Jades, JWST_Cosmos_Web
from telescopes.surveys import HST_Cosmos
from telescopes.surveys import LSST
from telescopes.surveys import SDSS_I
from telescopes.instruments import Euclid_VIS, Euclid_NIR, JWST_NIRCAM, JWST_MIRI, HST_ACS, Rubin_Wide_field_imager, SDSS_imaging_camera

Euclid = {"marker":'o',
          "fov": [34, 34],
          "color": "blue",
          "mirror": 1.2,
          "surveys": {"Wide-Survey":Euclid_Wide,
                     "Deep-Survey":Euclid_Deep },
          "instruments":{
                "VIS":Euclid_VIS,
                "NIR":Euclid_NIR}
        }

JWST = {"marker":'X',
          "fov": [2.2, 2.2],
          "color": "red",
          "mirror": 6.5,
          "surveys":{"Jades":JWST_Jades,
                     "Cosmos-Web":JWST_Cosmos_Web},
          'instruments':{'NIRCAM':JWST_NIRCAM,
                        'MIRI':JWST_MIRI}}

HST = {"marker":'x',
        "fov": [3.3, 3.3],
        "mirror": 2.4,
        "color": "orange",
        "surveys":{"HST-Cosmos":HST_Cosmos},
        "instruments":{"ACS":HST_ACS}}

Rubin = {"marker":"D",
        "fov": [210, 210],
        "mirror": 8.4,
        "color": "green",
        "major_band":"z",
        "surveys":{"LSST":LSST},
        "instruments":{"Wide_field_imager":Rubin_Wide_field_imager},
        }

SDSS = {"marker":".",
        "fov": [150, 150],
        "mirror": 2.5,
        "color": "purple",
        "surveys":{"SDSS-I":SDSS_I},
        "instruments":{"Imaging_camera":SDSS_imaging_camera},
        }
        # "HST": {"marker":'x',
#                 "fov": [3.3, 3.3],
#                 "mirror": 2.4,
#                 "color": "red",
#                 "instruments": {"ACS":{'pix_scale':0.03,
#                                         "noise_level":0.007,
#                                        'ls':'-',
#                                        'depth':25,
#                                        'fwhm':0.067,
#                                        'major_band':'f606W',
#                                        'bands':{'F220W':{"mag":23.5, "min_max":[185.4, 298.1], 'fwhm':0.08}, # PSFs are approximated by a table giving PSF/lambda (https://hst-docs.stsci.edu/wfc3ihb/chapter-6-uvis-imaging-with-wfc3/6-6-uvis-optical-performance()
#                                                 'F250W':{"mag":23.7, "min_max":[209.4, 353.4], 'fwhm':0.075}, # mag are zero points, calculated on WCS when available
#                                                 'F330W':{"mag":24.06, "min_max":[295.8, 371.9], 'fwhm':0.075},
#                                                 # 'F344N':{"mag":21.5, "min_max":[295.8, 371.9], 'fwhm':0.075},
#                                                 # 'FR338N':{"mag":, "min_max":[381.0, 395.0], 'fwhm':0.075},
#                                                 'F435W':{"mag":25.648, "min_max":[359.3, 486.0], 'fwhm':0.07},
#                                                 # 'FR459M':{"mag":, "min_max":[428.0, 490.7], 'fwhm':0.07},
#                                                 'F475W':{"mag":26.04, "min_max":[385.7, 555.9], 'fwhm':0.067},
#                                                 'F502N':{"mag":22.28, "min_max":[496.6, 507.9], 'fwhm':0.067},
#                                                 'FR550N':{"mag":24.84, "min_max":[495.5, 514.5], 'fwhm':0.067},
#                                                 'F555W':{"mag":25.70, "min_max":[458.0, 619.3], 'fwhm':0.067},
#                                                 'F550M':{"mag":24.85, "min_max":[524.6, 592.9], 'fwhm':0.067},
#                                                 'F606W':{"mag":26.48, "min_max":[462.5, 717.8], 'fwhm':0.067}
#                                                 }
#                                    }
#                                  },
#                 },
#         # "Roman": {"instruments":{"Roman":{"MAG":28.5, 'bands':[['F062', 620, 760], ['F087', 760, 977], ['F106', 927, 1192], ['F129', 1131, 1454], ['F158', 1380, 1774], ['F184', 1683, 2000], ['F213', 1950, 2300], ['F146', 927, 2000]],  'ls':'-'}},
#         #           "marker":'*',
#         #           "fov": [45, 23],
#         #           "mirror": 2.4,
#         #           "color": "purple",},

#         
# # Euclid 10sigma magnitudes: https://ui.adsabs.harvard.edu/abs/2020A%26A...644A..31E/abstract
# # some of LSST 10sigma magnitudes: https://ui.adsabs.harvard.edu/abs/2020A%26A...644A..31E/abstract
# # LSST infos: https://smtn-002.lsst.io/ (5 sigma AB mag can be found here)
# # NISP infos: https://sci.esa.int/web/euclid/-/euclid-nisp-instrument
# # NISP zeropoints: https://ui.adsabs.harvard.edu/abs/2022A&A...662A..92E/abstract
# # HST ACS PSFs: https://hst-docs.stsci.edu/wfc3ihb/chapter-6-uvis-imaging-with-wfc3/6-6-uvis-optical-performance
# # HST ACS zeropoints: https://acszeropoints.stsci.edu/?Detector_all=WFC
# # Zero points mags: https://www.researchgate.net/figure/Zero-points-in-AB-magnitudes-for-HST-ACS-blue-JWST-NIRCAM-green-Keck-NIRC2_fig1_279310158