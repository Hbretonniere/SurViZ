from telescopes.instruments import Euclid_VIS, Euclid_NIR
from telescopes.instruments import JWST_NIRCAM, JWST_MIRI
from telescopes.instruments import HST_ACS
from telescopes.instruments import Rubin_Wide_field_imager
from telescopes.instruments import SDSS_imaging_camera


Euclid_Wide = {
               'instruments':{"VIS":Euclid_VIS,
                              "NIR":Euclid_NIR},
                'std_noise':0.003,
                'area':15000} # approx from Euclid morpho challenge data

Euclid_Deep = {
               'instruments':{"VIS":Euclid_VIS,
                              "NIR":Euclid_NIR},
                'std_noise':0.0004,
                'area':53}

JWST_Jades = {
              'instruments':{"NIRCAM":JWST_NIRCAM}
             }

JWST_Cosmos_Web = {
              'instruments':{"NIRCAM":JWST_NIRCAM,
                            "MIRI":JWST_MIRI},
              'std_noise':0.000595,
              'area':0.6
             }

HST_Cosmos = {
              'instruments':{"ACS":HST_ACS},
              'std_noise':0.0042,
              'area':2
             }

LSST = {
              'instruments':{"Wide-field-imager":Rubin_Wide_field_imager},
             'area':18000}

SDSS_I = {
              'instruments':{"Imaging_camera":SDSS_imaging_camera},
              'std_noise':0.093 # estimated from online data 
             }
