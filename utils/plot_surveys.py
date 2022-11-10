from matplotlib.patches import Circle
import numpy as np
import sys
sys.path.append('../utils/')

from utils.diverse_utils import eq2gal, ecl2gal

def rad(x):
    return x*np.pi/180

def plot_Euclid_Deep_Survey(fig, ax):

    edfn_rad = eq2gal(269.73291667, 66.01769444)
#
    edfn = Circle((edfn_rad[0], edfn_rad[1]), rad(np.sqrt(20/(2*np.pi))), ls='--', edgecolor='black', facecolor='blue')
    ax.add_patch(edfn)

    fornax_rad = eq2gal(52.93583333, -28.08850000)
    fornax = Circle((fornax_rad[0], fornax_rad[1]), rad(np.sqrt(10/(2*np.pi))), ls='--', edgecolor='black', facecolor='blue')
    ax.add_patch(fornax)
    # plt.scatter(fornax_rad[0], fornax_rad[1], s=30, c='red')


    edfs_rad = eq2gal(61.241, -48.42300000)
    edfs = Circle((edfs_rad[0], edfs_rad[1]), rad(np.sqrt(23/(2*np.pi))), ls='--', edgecolor='black', facecolor='blue', label='Euclid Deep Survey')
    ax.add_patch(edfs)
    return ax

def plot_Euclid_Wide_Survey(fig, ax):
    
    lon_ecl = np.linspace(0, 360, 100)
    lat_ecl = np.zeros(100)

    l_ecl_gal, b_ecl_gal = ecl2gal(lon_ecl, lat_ecl)
    #north
    x_north_line = np.concatenate(([rad(180)], l_ecl_gal[30:71], [rad(-180)]))
    y_north_line = np.concatenate(([b_ecl_gal[30]+0.18], b_ecl_gal[30:71]+0.18, [b_ecl_gal[70]+0.18]))
    ax.plot(x_north_line, y_north_line, c='blue')
    ax.fill_between(x_north_line, y_north_line, rad(90), interpolate=True, color='blue', alpha=0.5)

    x_hole_north = np.concatenate(([l_ecl_gal[61]], l_ecl_gal[37:62]))
    y_hole_north = np.concatenate(([b_ecl_gal[61]-0.18], b_ecl_gal[37:62]-0.18))
    ax.plot(x_hole_north, y_hole_north, c='blue')
    ax.plot([l_ecl_gal[37], l_ecl_gal[61]], [b_ecl_gal[37]-0.18, b_ecl_gal[61]-0.18] , c='blue')
    ax.fill_between(x_hole_north, y_hole_north, b_ecl_gal[61]-0.18, color='blue', alpha=0.5)


    # #south
    x_south_line = np.concatenate(([rad(180)], l_ecl_gal[-20:], l_ecl_gal[:20], [rad(-180)]))
    y_south_line = np.concatenate(([b_ecl_gal[-20]-0.18], b_ecl_gal[-20:]-0.18, b_ecl_gal[:20]-0.18, [rad(-29.8)]))
    ax.plot(x_south_line, y_south_line, c='blue')
    ax.fill_between(x_south_line, y_south_line, rad(-90), interpolate=True, color='blue', alpha=0.5)

    x_hole_south = np.concatenate((l_ecl_gal[:12], l_ecl_gal[-12:]))
    y_hole_south = np.concatenate((b_ecl_gal[:12]+0.18, b_ecl_gal[-12:]+0.18))
    ax.plot(x_hole_south, y_hole_south, color='blue')
    ax.fill_between(x_hole_south, y_hole_south,  b_ecl_gal[-12]+0.18, color='blue', alpha=0.5, label='Euclid Wide Survey')
    return ax

def plot_HST_cosmos_Survey(fig, ax):
    cosmos_rad = eq2gal(150.11916667,2.20583333)
    cosmos = Circle((cosmos_rad[0], cosmos_rad[1]), rad(np.sqrt(2/(2*np.pi))), edgecolor='black', facecolor='red', label='HST Cosmos')
    ax.add_patch(cosmos)
    return ax

def plot_Rubin_LSST_Survey(fig, ax):
    lon_ecl = np.linspace(0, 360, 100)
    lat_ecl = np.zeros(100)

    l_ecl_gal, b_ecl_gal = ecl2gal(lon_ecl, lat_ecl)
    start=22
    end=100
    start2=0
    end2=22
    ax.fill_between(l_ecl_gal[start:end], b_ecl_gal[start:end]+0.2, rad(-90), color='green', alpha=0.5, hatch="/", label='Rubin LSST')
    ax.fill_between(l_ecl_gal[start2:end2], b_ecl_gal[start2:end2]+0.2, rad(-90), color='green', alpha=0.5, hatch="/")
    return ax
