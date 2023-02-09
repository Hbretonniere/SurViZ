from telescopes.surveys import Euclid_Wide, Euclid_Deep
from telescopes.surveys import JWST_Jades, JWST_Cosmos_Web, JWST_CEERS
from telescopes.surveys import HST_Cosmos, HST_CANDELS
from telescopes.surveys import LSST
from telescopes.surveys import SDSS_I
from telescopes.surveys import Chandra_Deep_North
from telescopes.surveys import Fermi_all_sky
from telescopes.instruments import Euclid_VIS, Euclid_NIR, JWST_NIRCAM, JWST_MIRI
from telescopes.instruments import HST_ACS, Rubin_Wide_field_imager, SDSS_imaging_camera, Chandra_HRC, Fermi_LAT

Euclid = {"marker":'o',
          "fov": [45, 45], #0.57deg^2
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
          "surveys":{"Cosmos-Web":JWST_Cosmos_Web,
                     "Jades":JWST_Jades,
                     'CEERS':JWST_CEERS,
                     },
          'instruments':{'NIRCAM':JWST_NIRCAM,
                        'MIRI':JWST_MIRI}}

HST = {"marker":'x',
        "fov": [3.3, 3.3], #202''
        "mirror": 2.4,
        "color": "orange",
        "surveys":{"HST-Cosmos":HST_Cosmos,
                   "HST-CANDELS": HST_CANDELS},
        "instruments":{"ACS":HST_ACS}}

Rubin = {"marker":"D",
        "fov": [210, 210], #3.5deg*3.5deg
        "mirror": 8.4,
        "color": "green",
        "major_band":"z",
        "surveys":{"LSST":LSST},
        "instruments":{"Wide_field_imager":Rubin_Wide_field_imager},
        }

SDSS = {"marker":".",
        "fov": [150, 150], #2.5deg*2.5deg
        "mirror": 2.5,
        "color": "purple",
        "surveys":{"SDSS-I":SDSS_I},
        "instruments":{"Imaging_camera":SDSS_imaging_camera},
        }

Chandra = {"marker":"O",
        "fov": [15, 15],
        "mirror": 1.23, #carefull, x rays are different regardind the mirrors
        "color": "gray",
        "surveys":{"Deep-North":Chandra_Deep_North},
        "instruments":{"HRC":Chandra_HRC},
        }
# . https://cxc.harvard.edu/cdo/about_chandra/

Fermi = {"marker":"*",
        "fov": [5436, 5436],  #2.5sr ~ 8207deg^2 > 90.5x90.5deg > 5436'
        "mirror": None,
        "color": "tomato",
        "surveys":{'All_sky':Fermi_all_sky},
        "instruments":{"LAT":Fermi_LAT},
        }
# https://fermi.gsfc.nasa.gov/ssc/data/analysis/documentation/Cicerone/Cicerone_Introduction/LAT_overview.html