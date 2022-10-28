from telescopes.instruments import Euclid_VIS, Euclid_NIR
from telescopes.instruments import JWST_NIRCAM
from telescopes.instruments import HST_ACS
from telescopes.instruments import Rubin_Wide_field_image


Euclid_Wide = {'depth':25.2,
               'zp':25.91,
               'instruments':{"VIS":Euclid_VIS,
                              "NIR":Euclid_NIR}}

Euclid_Deep = {'depth':27.2,
                'zp':21.58,
               'instruments':{"VIS":Euclid_VIS,
                              "NIR":Euclid_NIR}}

JWST_Jades = {'depth':28.2,
              'zp':27.9,
              'instruments':{"NIRCAM":JWST_NIRCAM}
             }

JWST_Cosmos_Web = {'depth':28.2,
              'instruments':{"NIRCAM":JWST_NIRCAM}
             }

HST_Cosmos = {'depth':25.2,
              'instruments':{"WCS":HST_ACS}
             }

LSST = {'depth':25.2,
              'instruments':{"Wide-field-imager":Rubin_Wide_field_image}
             }
