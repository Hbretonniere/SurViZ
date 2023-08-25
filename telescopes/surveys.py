from telescopes.instruments import Euclid_VIS, Euclid_NIR
from telescopes.instruments import JWST_NIRCAM, JWST_MIRI
from telescopes.instruments import HST_ACS
from telescopes.instruments import Rubin_Wide_field_imager
from telescopes.instruments import SDSS_imaging_camera
from telescopes.instruments import Chandra_HRC
from telescopes.instruments import Fermi_LAT
from telescopes.instruments import DES_DECam

"""
############################ 
########   EUCLID   ########
############################
"""

Euclid_Wide = {
               'instruments':{"VIS":Euclid_VIS,
                              "NIR":Euclid_NIR},
                'sensitivity':{'VIS':[24.6, 10, 2, 4*590],  # mag depth (0) for n_sigma (1) aperture of (2)
                               'NIR':[23, 10, 2, 4*90]}, # texp J
                'std_noise':0.003,
                'area':15000} # approx from Euclid morpho challenge data

Euclid_Deep = {
               'instruments':{"VIS":Euclid_VIS,
                              "NIR":Euclid_NIR},
                'std_noise':0.0004,
                'sensitivity':{'VIS':[26.5, 10, 2, 93953],  # mag depth (0) for n_sigma (1) aperture of (2)
                               'NIR':[24.9, 10, 2, 93953/10]},  #approx exp time
                'area':53}

"""
############################ 
########    JWST    ########
############################
"""

JWST_Jades = {
              'instruments':{"NIRCAM":JWST_NIRCAM},
              'filters':['F090W', 'F115W', 'F150W', 'F200W', 'F277W', 'F335M', 'F356W', 'F410M', 'F444W']
             }

JWST_Cosmos_Web = {
              'instruments':{"NIRCAM":JWST_NIRCAM,
                            "MIRI":JWST_MIRI},
              'sensitivity':{"NIRCAM":[27.83, 5, 0.15, 515]}, # f444w, 2 exposures
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

"""
############################ 
########    HST     ########
############################
"""

HST_Cosmos = {
              'instruments':{"ACS":HST_ACS},
              'sensitivity':{"ACS":[27.3, 5, 0.24, 2028]}, # f444w, 2 exposures
              'std_noise':0.0042,
              'area':2
             }

HST_CANDELS = {'instruments':{"ACS":HST_ACS},
              'std_noise':None,
              'area':2.82}

"""
############################ 
########    LSST    ########
############################
"""

LSST = {'instruments':{"Wide-field-imager":Rubin_Wide_field_imager},
        'area':18000}


"""
############################ 
########    DES    ########
############################
"""

DES = {'instruments':{"Dark-Energy-Camera":DES_DECam},
        'area':50000}


"""
############################ 
########    SDSS    ########
############################
"""

SDSS_I = {'instruments':{"Imaging_camera":SDSS_imaging_camera},
          'sensitivity':{"Imaging_camera":[23, 5, 0.2, 55]}, # g' aperture and sigma aprroximated (unkown)
          'std_noise':0.093 # estimated from online data 
             }


"""
############################ 
########  CHANDRA   ########
############################
"""

Chandra_Deep_North = {
              'instruments':{"HRC":Chandra_HRC},
              'std_noise':None # estimated from online data 
             }


"""
############################ 
########    FERMI    ########
############################
"""
Fermi_all_sky = {
                'instruments':{'LAT':Fermi_LAT}
}