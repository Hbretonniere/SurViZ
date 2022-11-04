from telescopes.instruments import Euclid_VIS, Euclid_NIR
from telescopes.instruments import JWST_NIRCAM, JWST_MIRI
from telescopes.instruments import HST_ACS
from telescopes.instruments import Rubin_Wide_field_imager
from telescopes.instruments import SDSS_imaging_camera


Euclid_Wide = {'depth':25.2,
               'zp':25.91,
               'instruments':{"VIS":Euclid_VIS,
                              "NIR":Euclid_NIR}}

Euclid_Deep = {'depth':27.2,
                'zp':21.58,
               'instruments':{"VIS":Euclid_VIS,
                              "NIR":Euclid_NIR}}

JWST_Jades = {'depth':28.2, #VERIFY
              'zp':29.8,
              'instruments':{"NIRCAM":JWST_NIRCAM}
             }

JWST_Cosmos_Web = {'depth':28.2, #VERIFY
              'instruments':{"NIRCAM":JWST_NIRCAM,
                            "MIRI":JWST_MIRI}
             }

HST_Cosmos = {'depth':None,
              'instruments':{"ACS":HST_ACS}
             }

LSST = {'depth':None,
              'instruments':{"Wide-field-imager":Rubin_Wide_field_imager}
             }

SDSS_I = {'depth':None,
              'instruments':{"Imaging_camera":SDSS_imaging_camera}
             }
