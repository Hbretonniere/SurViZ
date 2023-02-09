from matplotlib.patches import Circle
import numpy as np
import sys
sys.path.append('../utils/')

from utils.diverse_utils import init_sky, projection_dec, projection_ra #eq2gal, ecl2gal


def rad(x):
    " from degree to radian"
    return x*np.pi/180


def plot_Euclid_Deep_Survey(fig, ax, show_name=True):
    """
    Plot the three Euclid deep fields
    """

    ### Euclid Deep Field North (EDFN)
    # Define the ra dec
    edfn_ra = np.array([269.73])
    edfn_dec = np.array([66.01])

    # Create a circle at the appropriate ra dec (taking into account the plt shift)
    edfn = Circle((ax.projection_ra(edfn_ra), ax.projection_dec(edfn_dec)), np.sqrt(20/(np.pi))*np.pi/180, alpha=0.8, ls='--', edgecolor='black', facecolor='blue', label=r'Euclid Deep ($40\rm{deg}^2$)')
    # Plot the patch
    ax.add_patch(edfn)

    ### Euclid Fornax
    fornax_ra = np.array([52.93583333]) 
    fornax_dec = np.array([-28.08850000])    
    fornax = Circle((ax.projection_ra(fornax_ra), ax.projection_dec(fornax_dec)), rad(np.sqrt(10/(np.pi))), alpha=0.5, ls='--', edgecolor='black', facecolor='blue')
    ax.add_patch(fornax)

    ### Euclid Deep Field South
    edfs_ra= np.array([61.241])
    edfs_dec = np.array([-48.42300000])
    edfs = Circle((ax.projection_ra(edfs_ra), ax.projection_dec(edfs_dec)), rad(np.sqrt(10/(np.pi))), alpha=0.8, ls='--', edgecolor='black', facecolor='blue')
    ax.add_patch(edfs)

    # If show name, plot the three names above the circles
    if show_name:
        ax.text(ax.projection_ra(edfs_ra), ax.projection_dec(edfs_dec)+rad(3),'EDFS', color='darkblue')
        ax.text(ax.projection_ra(fornax_ra), ax.projection_dec(fornax_dec)-rad(8),'FORNAX', color='darkblue')
        ax.text(ax.projection_ra(edfn_ra), ax.projection_dec(edfn_dec)+rad(3),'EDFN', color='darkblue')

    return ax


def plot_Euclid_Wide_Survey(fig, ax, ecl_ra, ecl_dec, gal_ra, gal_dec):
    """
    Plot the Euclid Wide Survey

    This is a bit acrobatic... 
    
    We try to match the survey using the galactic and ecliptic plane,
    and thus define 4 regions: 
        - north of ecliptic
        - south of ecliptic,
        - between ecliptic and galactic (north)
        - between ecliptic and galactic (south)
    """

    # North Hole
    # Define where the hole starts reagrding the galactic plane,
    s, e = 10, 26

    # Margin between the start of the survey and the plane
    # (i.e. size) of the galactic extinction. It seems to match better
    # Euclid Survey if this margin is not constant
    margin = np.linspace(50, 20, e-s)

    # The region is defined as the area defined by this curve,
    # while it should taje into account the ecliptic plane too, it works quite good enough
    ax.fill(ax.projection_ra(gal_ra[s:e]), ax.projection_dec(gal_dec[s:e])-rad(margin), alpha=0.3, color='blue', label=r'Euclid Wide ($15 000 \rm{deg}^2$)')
    
    # South Hole
    # Same than North
    s, e = 55, 75
    margin = np.linspace(45, 25, e-s)
    ax.fill(ax.projection_ra(gal_ra[s:e]), ax.projection_dec(gal_dec[s:e])+rad(margin), alpha=0.3, color='blue')
    
    # South East
    # for this region we need to define two sub region
    # First, one below the ecliptic
    s, e, margin = 10, 84, 9.8
    ax.fill_between(ax.projection_ra(ecl_ra[s:e]), ax.projection_dec(ecl_dec[s:e])-rad(10), rad(-90), alpha=0.3, color='blue')
    # Second, below the galactic
    s, e, margin = 32, 61, 28
    ax.fill_between(ax.projection_ra(gal_ra[s:e]), ax.projection_dec(gal_dec[s:e])-rad(margin), rad(-90), alpha=0.3, color='blue')
    # Note that it creates a hole in the survey because of the resolution of the curves, they don t overlap perfectly

    # North West
    # works quite well with just above the ecliptic, but could be a bit better
    s, e, margin = 100, 190, 12
    # ax.plot(ax.projection_ra(ecl_ra[s:e]), ax.projection_dec(ecl_dec[s:e])+rad(margin), color='blue')
    ax.fill_between(ax.projection_ra(ecl_ra[s:e]), ax.projection_dec(ecl_dec[s:e])+rad(margin), rad(90), alpha=0.3, color='blue')
    
    return ax

def plot_HST_cosmos_Survey(fig, ax, show_name=True):
    cosmos_ra = np.array([150.11916667])
    cosmos_dec= np.array([2.20583333])

    cosmos = Circle((ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)), rad(np.sqrt(2/(np.pi))), edgecolor='black', facecolor='orange', alpha=0.5, hatch='/', label=r'HST cosmos (2deg$^2$)')
    zoom_cosmos = Circle((ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)), rad(np.sqrt(2/(np.pi))), edgecolor='black', facecolor='orange', alpha=0.5, hatch='/', label=r'HST cosmos (2deg$^2$)')
    ax.add_patch(cosmos)

    if show_name:
        ax.text(ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)+rad(5),'COSMOS', color='darkorange')
    return ax, zoom_cosmos

def plot_JWST_CEERS_Survey(fig, ax, show_name):
    ceers_ra = np.array([214])
    ceers_dec = np.array([52]) #eq2gal(14.28, 53)
    ceers = Circle((ceers_ra, ceers_dec), rad(np.sqrt((1/6)/(2*np.pi))), edgecolor='black', ls='--', facecolor='red', alpha=0.5, label=r'JWST CEERS (0.02 deg$^2$)')
    zoom_ceers = Circle((ceers_ra, ceers_dec), rad(np.sqrt((1/6)/(2*np.pi))), edgecolor='black', facecolor='red', alpha=0.5)
    ax.add_patch(ceers)
    if show_name:
        ax.text(ax.projection_ra(ceers_ra), ax.projection_dec(ceers_dec)-rad(7),'CEERS', color='red')
    return ax, zoom_ceers

def plot_cosmos_Web_Survey(fig, ax, show_name):
    cosmos_ra = np.array([150.11916667])
    cosmos_dec= np.array([2.20583333])

    cosmos = Circle((ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)), rad(np.sqrt(0.6/(np.pi))), edgecolor='black', facecolor='red', alpha=0.5, label=r'Cosmos-Web (0.6deg$^2$)')
    zoom_cosmos_web = Circle((ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)), rad(np.sqrt(0.6/(np.pi))), edgecolor='black', facecolor='red', alpha=0.5)
    ax.add_patch(cosmos)
    if show_name:
        ax.text(ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)-rad(7),'COSMOS-Web', color='red')

    return ax, zoom_cosmos_web

def plot_Fermi_all_sky_Survey(fig, ax):

    ax.fill_between(np.linspace(-180, 180), rad(90), rad(-90), alpha=0.2, color='tomato', label=r'Fermi all sky ($41253\rm{deg}^2$)')
    return ax

def plot_Rubin_LSST_Survey(fig, ax):

    ax.fill_between(np.linspace(-180, 180), rad(30), rad(-90), alpha=0.3, color='green', label=r'Rubin LSST ($18 000\rm{deg}^2$)')
    return ax

def plot_HST_CANDELS_Survey(fig, ax, show_name=True):
    # rad_goods-s = 37000 pix = 558'' = 0.3deg
    goods_s_ra = np.array([53])
    goods_s_dec= np.array([-27.8])
    goods_s = Circle((ax.projection_ra(goods_s_ra), ax.projection_dec(goods_s_dec)), rad(np.sqrt(0.3/(np.pi))), edgecolor='black', facecolor='orange', alpha=0.5, label=r'HST CANDELS (2.82deg$^2$)')
    ax.add_patch(goods_s)

    # rad_goods-n = same good s
    goods_n_ra = np.array([189])
    goods_n_dec= np.array([62])
    goods_n = Circle((ax.projection_ra(goods_n_ra), ax.projection_dec(goods_n_dec)), rad(np.sqrt(0.3/(np.pi))), edgecolor='black', facecolor='orange', alpha=0.5)
    ax.add_patch(goods_n)

    # rad EGS = 22673 = 0.12deg
    EGS_ra = np.array([214.8])
    EGS_dec= np.array([52.8])
    EGS = Circle((ax.projection_ra(EGS_ra), ax.projection_dec(EGS_dec)), rad(np.sqrt(0.12/(np.pi))), edgecolor='black', facecolor='orange', alpha=0.5)
    ax.add_patch(EGS)

    # rad UDS = 19829 = 0.16deg
    UDS_ra = np.array([34])
    UDS_dec= np.array([-5.2])
    UDS = Circle((ax.projection_ra(UDS_ra), ax.projection_dec(UDS_dec)), rad(np.sqrt(0.11/(np.pi))), edgecolor='black', facecolor='orange', alpha=0.5)
    ax.add_patch(UDS)

    # rad UDS = 19829 = 0.16deg
    cosmos_ra = np.array([150.11916667])
    cosmos_dec= np.array([2.20583333])
    cosmos = Circle((ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)), rad(np.sqrt(2/(np.pi))), edgecolor='black', facecolor='orange', alpha=0.5)
    ax.add_patch(cosmos)

    if show_name:
        ax.text(ax.projection_ra(goods_s_ra), ax.projection_dec(goods_s_dec)+rad(2),'GOODS-S', color='darkorange')
        ax.text(ax.projection_ra(goods_n_ra), ax.projection_dec(goods_n_dec)+rad(1),'GOODS-N', color='darkorange')
        ax.text(ax.projection_ra(UDS_ra), ax.projection_dec(UDS_dec)+rad(1),'UDS', color='darkorange')
        ax.text(ax.projection_ra(EGS_ra), ax.projection_dec(EGS_dec)+rad(1),'EGS', color='darkorange')
        ax.text(ax.projection_ra(cosmos_ra), ax.projection_dec(cosmos_dec)+rad(5),'COSMOS', color='darkorange')

    return ax

def plot_SDSS_I_Survey(fig, ax):
    ax.fill_between(ax.projection_ra(np.linspace(120, 240, 2)), 0, rad(70), color='purple', hatch='/', alpha=0.5, label=r'SDSS-I ($10886\rm{deg}^2$)')#
    
    ax.fill_between(ax.projection_ra(np.linspace(320, 360, 2)), rad(1), -rad(1), color='purple', hatch='/', alpha=0.5)
    ax.fill_between(ax.projection_ra(np.linspace(0, 60, 2)), rad(1), -rad(1), color='purple', hatch='/', alpha=0.5)
    
    ax.fill_between(ax.projection_ra(np.linspace(0, 30, 2)), np.array([rad(11), rad(8)]), [rad(13), rad(10)], color='purple', hatch='/', alpha=0.5)
    ax.fill_between(ax.projection_ra(np.linspace(320, 360, 2)), np.array([rad(17), rad(13)]), [rad(15), rad(11)], color='purple', hatch='/', alpha=0.5)

    ax.fill_between(ax.projection_ra(np.linspace(0, 60, 2)), np.array([rad(-8.45), rad(-3)]), [rad(-10.45), rad(-5)], color='purple', hatch='/', alpha=0.5)
    ax.fill_between(ax.projection_ra(np.linspace(320, 360, 2)), np.array([rad(-12), rad(-8.45)]), [rad(-14), rad(-10.45)], color='purple', hatch='/', alpha=0.5)

    return ax

def plot_Chandra_Deep_North_Survey(fig, ax, show_name):
    #12 36 48.0 +62 13 00
    deep_ra = np.array([189.2])
    deep_dec= np.array([62.2])
    CDN = Circle((ax.projection_ra(deep_ra), ax.projection_dec(deep_dec)), rad(np.sqrt(0.11/(np.pi))), edgecolor='gray', facecolor='gray', alpha=0.5, label='Chandra')
    ax.add_patch(CDN)
    if show_name:
        ax.text(ax.projection_ra(deep_ra)+rad(10), ax.projection_dec(deep_dec)+rad(-8),'Deep Field North', color='gray')

    return ax