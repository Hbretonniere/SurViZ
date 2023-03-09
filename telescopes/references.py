filters_refs = """
References:
- Euclid:
    - NISP: https://sci.esa.int/web/euclid/-/euclid-nisp-instrument
    - VIS: https://sci.esa.int/web/euclid/-/euclid-vis-instrument
- JWST:
    - NIRCAM: https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-instrumentation/nircam-filters
- HST:
    - ACS: https://etc.stsci.edu/etcstatic/users_guide/appendix_b_acs.html
- Rubin:
    - https://ui.adsabs.harvard.edu/abs/2009arXiv0912.0201L
- SDSS: https://www.astro.princeton.edu/PBOOK/camera/camera.htm 
"""

mirrors_refs = """
References:
- Euclid: 
    - Mirror: https://sci.esa.int/web/euclid/-/57042-euclid-primary-mirror
    - FOV: https://sci.esa.int/web/euclid/-/euclid-vis-instrument
- JWST:
    - Mirror: https://webb.nasa.gov/content/observatory/ote/mirrors/index.html
    - FOV: https://jwst-docs.stsci.edu/jwst-near-infrared-camera
    
- HST: 
    - Mirror: https://www.nasa.gov/content/goddard/hubble-space-telescope-optics-system
    - FOV: https://www.nasa.gov/content/hubble-space-telescope-advanced-camera-for-surveys
- SDSS: 
    - Mirror and FOV: https://www.sdss.org/instruments/
- Rubin LSST:
    - Mirror: https://www.lsst.org/about/tel-site/mirror
    - FOV: https://www.lsst.org/about/camera

"""

footprint_refs = """

References:
Projection use utils from https://desiutil.readthedocs.io/en/latest/_modules/desiutil/plots.html
- SDSS:
    - SDSS-I: https://classic.sdss.org/dr7/coverage/index.html https://classic.sdss.org/dr7/start/aboutdr7.html
- JWST:
    - CEERS: https://ceers.github.io/obs.html
- HST:
    - CANDELS: https://www.researchgate.net/figure/World-Coordinate-System-Information-for-Each-CANDELS-HST-Mosaic_tbl4_230951842
    """

image_quality_refs = """

References:
Simulated galaxy image: https://www.tng-project.org/data/
- Euclid:
    - zero points: http://arxiv.org/abs/2203.01650 (NIR), None (VIS)
    - FWHM: http://arxiv.org/abs/2209.12906 (NIR), https://ui.adsabs.harvard.edu/abs/2010SPIE.7731E..1JC/abstract (VIS) 
- JWST:
    - FWHM: https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-performance/nircam-point-spread-functions (NIRCAM)
    - zero-points: Mirage, https://github.com/spacetelescope/mirage/blob/master/mirage/config/NIRCam_zeropoints.list (NIRCAM)
    """

image_depth_refs = """
References:
- Euclid: 
    - zero points: http://arxiv.org/abs/2203.01650 (NIR), None (VIS)
    - FWHM: http://arxiv.org/abs/2209.12906 (NIR), https://ui.adsabs.harvard.edu/abs/2010SPIE.7731E..1JC/abstract (VIS) 
    - sensitivities: http://arxiv.org/abs/2209.12906
- JWST:
    - FWHM: https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-performance/nircam-point-spread-functions (NIRCAM)
    - zero-points: Mirage, https://github.com/spacetelescope/mirage/blob/master/mirage/config/NIRCam_zeropoints.list (NIRCAM)

    - sensitivity: - cosmos web : https://ui.adsabs.harvard.edu/abs/2022arXiv221107865C/abstract
                   - Internal communication (JADES)
- SDSS:
    - zero points: https://www.sdss.org/dr12/algorithms/magnitudes/
    - FWHM : aprrox from https://arxiv.org/abs/1111.6619
    - noise level: computed from online data (SDSS-I, must verify this...)
- HST:
    - zero points: https://acszeropoints.stsci.edu/ 
    - FWHM: https://hst-docs.stsci.edu/wfc3ihb/chapter-6-uvis-izping-with-wfc3/6-6-uvis-optical-performance
    - std: need to compute

- Rubin-LSST:
    - https://github.com/aboucaud/galcheat/blob/main/galcheat/data/LSST.yaml and refs
    
"""