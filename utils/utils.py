import numpy as np

def create_psf(fwhm, pxscale):

    N = 256
    X = np.linspace(-127, 127, N)
    Y = np.linspace(-127, 127, N)
    X, Y = np.meshgrid(X, Y)

    # Mean vector and covariance matrix
    mu = np.array([0, 0.])
    Sigma = np.array([[ fwhm/pxscale , 0], [0,  fwhm/pxscale]])

    # Pack X and Y into a single 3-dimensional array
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y
    n = mu.shape[0]
    Sigma_det = np.linalg.det(Sigma)
    Sigma_inv = np.linalg.inv(Sigma)
    N = np.sqrt((2*np.pi)**n * Sigma_det)
    # This einsum call calculates (x-mu)T.Sigma-1.(x-mu) in a vectorized
    # way across all the input variables.
    fac = np.einsum('...k,kl,...l->...', pos-mu, Sigma_inv, pos-mu)
    
    return np.exp(-fac/ 2) / N #* np.exp(-fac2/ 2) / N2
