from telescopes.instruments import Euclid_VIS, Euclid_NIR
from telescopes.instruments import JWST_NIRCAM, JWST_MIRI
from telescopes.instruments import HST_ACS
from telescopes.instruments import Rubin_Wide_field_imager
from telescopes.instruments import SDSS_imaging_camera


Euclid_Wide = {
               'instruments':{"VIS":Euclid_VIS,
                              "NIR":Euclid_NIR},
                'std_noise':0.003} # approx from Euclid morpho challenge data

Euclid_Deep = {
               'instruments':{"VIS":Euclid_VIS,
                              "NIR":Euclid_NIR},
                'std_noise':0.0004}

JWST_Jades = {
              'instruments':{"NIRCAM":JWST_NIRCAM}
             }

JWST_Cosmos_Web = {
              'instruments':{"NIRCAM":JWST_NIRCAM,
                            "MIRI":JWST_MIRI}
             }

HST_Cosmos = {
              'instruments':{"ACS":HST_ACS}
             }

LSST = {
              'instruments':{"Wide-field-imager":Rubin_Wide_field_imager}
             }

SDSS_I = {
              'instruments':{"Imaging_camera":SDSS_imaging_camera}
             }
