import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from astropy.io import fits
import streamlit as st
import seaborn as sns

import sys
sys.path.append('../utils/')
from utils.plot_surveys import *


def plot_bands(info, telescopes, instruments, bands, selected_survey, fill=True, log=False):
    sns.reset_orig()
    plt.rcParams.update({"font.size": 22})

    fig, ax = plt.subplots(figsize=(15, 10))
    for i, telescope in enumerate(telescopes):
        j = i+1
        k = 0
        for instrument in instruments[telescope]:
            
            ax.plot([], [], ls=info[telescope]['instruments'][instrument]['ls'], color=info[telescope]['color'], label=f'{telescope} {instrument}')
            for i, band in enumerate(bands[telescope][instrument]):                
                k += 1
                band_info = info[telescope]['instruments'][instrument]['bands'][band]
                min_, max_ = band_info["min_max"]
                
                ax.hlines(10-j-k/10, min_, max_, color=info[telescope]['color'], ls=info[telescope]['instruments'][instrument]['ls'], alpha=0.7, lw=3)
                ax.vlines([min_, max_], ymin=0, ymax=[10-j-k/10, 10-j-k/10], color=info[telescope]['color'], ls=info[telescope]['instruments'][instrument]['ls'], alpha=0.7, lw=3)
                if fill:
                    ax.fill_between([min_, max_], 10-j-k/10, 0, color=info[telescope]['color'], alpha=0.5)

                plt.text((max_+min_)/2, 10-j-k/10+0.2, band, c=info[telescope]['color'], rotation=90, size=10)  #10-j+((10-j)/30)-k/30
    ax.set_ylim([-1, 10])
    min_ = ax.get_xticks()[0]
    max_ = ax.get_xticks()[-1]

    ax.set_yticks([])
    if log:
        ax.set_xscale('log')
    else:
        ax.set_xscale('linear')
    ax.set_xlabel('Wavelength (nm)', fontsize=20)
    plt.legend(bbox_to_anchor = (1, -0.1), ncol=max(1, len(instruments)//2), fontsize=20)
    return fig

def plot_mirrors(info, telescopes):
    sns.reset_orig()
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect("equal")
    ds = []
    for telescope in telescopes:
        d = info[telescope]["mirror"]
        if d in ds:
            ls = "--"
        else:
            ls = "-"
        mirror = plt.Circle(
            (0, 0),
            d / 2,
            fill=False,
            lw=2,
            ec=info[telescope]["color"],
            label=telescope,
            alpha=0.8,
            ls=ls,
        )
        ax.add_patch(mirror)
        ds.append(d)
        plt.legend()

    dmax = np.max(ds) + 1
    ax.set_xlim(-dmax / 2, dmax / 2)
    ax.set_ylim(-dmax / 2, dmax / 2)
    ax.set_xticks([])
    ax.set_yticks([])
    human_axes = ax.inset_axes(
        [-1.8 / 2, -1.8 / 2, 1.8, 1.8], transform=ax.transData, zorder=0
    )
    human_axes.imshow(mpimg.imread("./data/human.png"), alpha=0.3, aspect="auto")
    human_axes.axis("off")
    human_axes.set_xticks([])
    human_axes.set_yticks([])
    plt.title("Primary Mirror Size")
    return fig

# @st.cache
def plot_fovs(info, telescope):
    sns.reset_orig()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")

    if "Rubin" in telescope:
        lims = 120
    else:
        lims = 30

    ax.set_xlim(-lims, lims)
    ax.set_ylim(-lims, lims)
    ax.add_patch(
        plt.Rectangle(
            (-lims, -lims), 2 * lims, 2 * lims, fc="black", ec="red", zorder=0
        )
    )

    for survey in telescope:
        x, y = info[survey]["fov"]
        fov = plt.Rectangle(
            (-x / 2, -y / 2),
            x,
            y,
            fc=info[survey]["color"],
            ec="white",
            lw=2,
            label=survey,
            alpha=0.3,
        )
        ax.add_patch(fov)
        plt.legend()
    moon_axes = ax.inset_axes(
        [-31 / 2, -31 / 2, 31, 31], transform=ax.transData, zorder=0
    )
    moon_axes.imshow(mpimg.imread("./data/moon.png"), aspect="auto")

    moon_axes.set_xticks([])
    moon_axes.set_yticks([])
    # ax.set_xticks([])
    # ax.set_yticks([])
    # xrange = ax.get_xlim()
    # yrange = ax.get_ylim()
    # print(xrange, yrange)
    ax.errorbar([-31/2, 31/2], [0, 0], yerr=[2, 2], c='darkred')
    ax.text(-2.2, 1, "31'", color='darkred')

    plt.title("Field Of View")

    return fig

from astropy.visualization import ZScaleInterval

def plot_fields(telescopes, surveys, instruments, info, nb_to_plot, bands=None):
    plt.rcParams.update({"font.size": 10})
    sns.reset_orig()

    nb_lines = int(np.ceil(nb_to_plot / 2))
    fig, ax  = plt.subplots(nb_lines, 2, figsize=(10, nb_lines * 5))
    ax = ax.flatten()
    k = 0
    # contrast = st.slider('Constrast', 0., 3., 0.7, 0.05)
    images = {}
    mins = []
    maxs = []
    for telescope in telescopes:
        images[telescope] = {}
        for survey in surveys[telescope]:
            images[telescope][survey] = {}
            for instrument in instruments[telescope][survey]:
                try:
                    images[telescope][survey] = fits.open(f'./data/fields/{telescope}_{instrument}_{survey}.fits')[0].data
                    interval = ZScaleInterval()
                    a = interval.get_limits(images[telescope][survey])
                    mins.append(a[0])
                    maxs.append(a[1])
                except OSError:
                    images[telescope][survey] = np.diag(np.ones(128))
                    images[telescope][survey] += np.fliplr(images[telescope][survey])

                    st.write(f'Sorry, {telescope} {survey} {instrument} is not implemented yet!')
                    st.write(f'Sorry, ./data/fields/{telescope}_{instrument}_{survey}.fits is not implemented yet!')

    min_v, max_v = np.min(mins), np.max(maxs)
    # print(mins, min_v)
    if len(mins) >= 2:
        mins.remove(min_v)
        maxs.remove(max_v)
    # print(mins)
    min_2, max_2 = np.min(mins), np.max(maxs)
    contrast2 = st.checkbox('Other Contrast')
    if contrast2:
        min_v, max_v = min_2, max_2
    for telescope in telescopes:
        if (telescope == 'HST') or (telescope == 'SDSS'):
            warning = 'Warning: The noise level is unsure (need to be checked)'
        else:
            warning = ""
        for survey in surveys[telescope]:
            for instrument in instruments[telescope][survey]:
                # img = fits.open(f'./data/{telescope}_{instrument}_{survey}.fits')[0].data
                ax[k].imshow(images[telescope][survey], cmap='bone', vmin=min_v, vmax=max_v)
                filter = info[telescope]['surveys'][survey]['instruments'][instrument]['main_band']
                ax[k].set_title(f"{telescope}, {survey} {instrument} ({filter} filter), \n {warning}", fontsize=10)
                k += 1
    if nb_to_plot % 2 != 0:
        ax[-1].set_visible(False)
    return fig


def plot_galaxies(info, telescopes, instruments, nb_to_plot, bands=None):
    sns.reset_orig()
    same_size = st.checkbox('Same size image')
    plt.rcParams.update({"font.size": 10})

    nb_lines = int(np.ceil(nb_to_plot / 2))
    fig, ax  = plt.subplots(nb_lines, 2, figsize=(10, nb_lines * 5))
    ax = ax.flatten()
    k = 0
    # contrast = st.slider('Constrast', 0., 3., 0.7, 0.05)
    sizes = []
    images = {}
    for telescope in telescopes:
        images[telescope] = {}
        for instrument in instruments[telescope]:
                try:
                    images[telescope][instrument] = np.load(f'./data/individual_galaxies/gal_{telescope}_{instrument}.npy', allow_pickle=True)
                    sizes.append(237 * 0.03/info[telescope]['instruments'][instrument]['pix_scale'])
                except OSError:
                    st.write(f'Sorry, {telescope} {instrument} is not implemented yet!')
                    st.write(f'Sorry, ./data/individual_galaxies/gal_{telescope}_{instrument}.npy is not implemented yet!')

                    images[telescope][instrument] = np.diag(np.ones(128))
                    images[telescope][instrument] += np.fliplr(images[telescope][instrument])
                    # st.write(np.max(images[telescope][survey][instrument]))
                
    max_size = np.max(sizes)
    for telescope in telescopes:
            for instrument in instruments[telescope]:
                img = images[telescope][instrument]
                # st.write(f'./data/gal_{telescope}_{instrument}_{survey}.npy')
                if same_size:
                    padding = int((max_size - np.shape(img)[0])/2)
                    img = np.pad(img, ((padding, padding), (padding, padding)), constant_values=0)

                ax[k].imshow(img, cmap='bone')
                ax[k].set_title(f'{telescope}, {instrument}', fontsize=10)
                k += 1
    if nb_to_plot % 2 != 0:
        ax[-1].set_visible(False)
    return fig

# import proplot

def plot_surveys(telescopes, selected_surveys):
    sns.set()

    # fig = plt.figure(figsize=(14,7))
    fig, ax, ecliptic, galactic = init_sky()
    ecliptic_ra_deg = np.concatenate((ecliptic.ra.degree[160:], ecliptic.ra.degree[:160], ))
    ecliptic_dec_deg = np.concatenate(( ecliptic.dec.degree[160:], ecliptic.dec.degree[:160],))
    galactic_ra_deg = np.concatenate((galactic.ra.degree[14:], galactic.ra.degree[:14]))
    galactic_dec_deg = np.concatenate((galactic.dec.degree[14:], galactic.dec.degree[:14]))
    ax.plot(ax.projection_ra(ecliptic_ra_deg), ax.projection_dec(ecliptic_dec_deg), color='black', alpha=0.5, ls='--', lw=0.7)
    ax.plot(ax.projection_ra(galactic_ra_deg), ax.projection_dec(galactic_dec_deg), color='black', alpha=0.5, lw=0.7)
    lines = ax.get_lines()
    legend1 = plt.legend([lines[i] for i in [0,1]], ['Ecliptic', 'Galactic'], fontsize=15, bbox_to_anchor = (1, 1.2))
    ax.add_artist(legend1)

    nb_to_plot = 0
    cosmos_patches = []
    for telescope in telescopes:
        for survey in selected_surveys[telescope]:
            print(f'{telescope}-{survey}')
            if f'{telescope}-{survey}' == 'Euclid-Deep-Survey':
                ax = plot_Euclid_Deep_Survey(fig, ax)
            elif f'{telescope}-{survey}' == 'Euclid-Wide-Survey':
                ax = plot_Euclid_Wide_Survey(fig, ax, ecliptic_ra_deg, ecliptic_dec_deg, galactic_ra_deg, galactic_dec_deg)
            elif f'{telescope}-{survey}' == 'HST-HST-Cosmos':
                ax, cosmos_patch = plot_HST_cosmos_Survey(fig, ax)
                cosmos_patches.append(cosmos_patch)
            elif f'{telescope}-{survey}' == 'Rubin-LSST':
                ax = plot_Rubin_LSST_Survey(fig, ax)
            elif f'{telescope}-{survey}' == 'JWST-Cosmos-Web':
                ax, cosmos_patch = plot_cosmos_Web_Survey(fig, ax)
                cosmos_patches.append(cosmos_patch)
            elif f'{telescope}-{survey}' == 'JWST-CEERS':
                ax, cosmos_patch = plot_JWST_CEERS_Survey(fig, ax)
                cosmos_patches.append(cosmos_patch)
            else:
                st.markdown(f'Sorry, {telescope} {survey} is not yet available... Stay Tuned!')

            nb_to_plot += 1
    if ('HST' in telescopes) | ('JWST' in telescopes):
        cosmos_zoom = st.checkbox('Zoom on Cosmos')
        if cosmos_zoom:
            zoom = ax.inset_axes([0.05, 1.15, 0.2, 0.4])#, transform=ax.transData)
            sx = 1
            sy = 1
            [zoom.add_patch(patch) for patch in cosmos_patches]
            zoom.set_xlim(rad(-40)-rad(sx), rad(-40)+rad(sx))
            zoom.set_ylim(rad(2)-rad(sy), rad(2)+rad(sy))
            xticks = list(zoom.get_xticks())
            yticks = list(zoom.get_yticks())
            zoom_xticks = [xticks[0], (xticks[-1] + xticks[0]) / 2, xticks[-1]]
            zoom_yticks = [yticks[0], (yticks[-1] + yticks[0]) / 2, yticks[-1]]
            zoom.set_xticks(zoom_xticks)
            zoom.set_yticks(zoom_yticks)
            zoom.set_xticklabels([np.round(150.12+sx, 2), np.round(150.12, 2), np.round(150.22-sx, 2)])
            zoom.set_yticklabels([np.round(2.20-sy, 2), np.round(2.20, 2), np.round(2.20+sy, 2)])
            zoom.set_xlabel('RA')
            zoom.set_ylabel('DEC')
            zoom.annotate('', xy=(0.6, 0), xycoords='axes fraction', xytext=(1.7, -1.55), arrowprops=dict(arrowstyle="<-", color='gray', alpha=0.9, lw=2))

    plt.legend(bbox_to_anchor = (1, -0.1), ncol=2, fontsize=20)
    
    return fig