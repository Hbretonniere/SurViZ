from telescopes.instruments import Euclid_VIS, Euclid_NIR
from telescopes.instruments import JWST_NIRCAM, JWST_MIRI
from telescopes.instruments import HST_ACS
from telescopes.instruments import Rubin_Wide_field_imager
from telescopes.instruments import SDSS_imaging_camera
from telescopes.instruments import Chandra_HRC

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
              'instruments':{"NIRCAM":JWST_NIRCAM},
              'filters':['F090W', 'F115W', 'F150W', 'F200W', 'F277W', 'F335M', 'F356W', 'F410M', 'F444W']
             }

JWST_Cosmos_Web = {
              'instruments':{"NIRCAM":JWST_NIRCAM,
                            "MIRI":JWST_MIRI},
              'std_noise':0.000595,
              'area':0.6,
              'filters':['F115W', 'F150W', 'F277W', 'F444W']
             }

JWST_CEERS = {
              'instruments':{"NIRCAM":JWST_NIRCAM,
                            "MIRI":JWST_MIRI},
              'std_noise':None,
              'area':0.03,
              'filters':['F115W', 'F150W', 'F277W', 'F444W']
             }

HST_Cosmos = {
              'instruments':{"ACS":HST_ACS},
              'std_noise':0.0042,
              'area':2
             }

HST_CANDELS = {'instruments':{"ACS":HST_ACS},
              'std_noise':None,
              'area':2.82}

LSST = {
              'instruments':{"Wide-field-imager":Rubin_Wide_field_imager},
             'area':18000}

SDSS_I = {
              'instruments':{"Imaging_camera":SDSS_imaging_camera},
              'std_noise':0.093 # estimated from online data 
             }


Chandra_Deep_north = {
              'instruments':{"HRC":Chandra_HRC},
              'std_noise':None # estimated from online data 
             }