"""
Waveform utilities for da-instaseis.

Provides helpers to extract Green's functions via instaseis and
convolve them with source time functions.
"""

import numpy as np


def get_greens_function(db, source, receiver):
    """
    Extract a Green's function seismogram from an instaseis database.

    Parameters
    ----------
    db : instaseis.InstaseisDB
        Open instaseis database.
    source : instaseis.Source
        Seismic source definition.
    receiver : instaseis.Receiver
        Seismic receiver definition.

    Returns
    -------
    st : obspy.Stream
        Three-component seismogram stream.
    """
    return db.get_seismograms(source=source, receiver=receiver)


def convolve_stf(st, stf, dt):
    """
    Convolve a seismogram stream with a source time function.

    Parameters
    ----------
    st : obspy.Stream
        Input seismogram stream.
    stf : array_like
        Source time function samples.
    dt : float
        Sampling interval in seconds.

    Returns
    -------
    st_conv : obspy.Stream
        Convolved seismogram stream (copy).
    """
    stf = np.asarray(stf, dtype=float)
    st_conv = st.copy()
    for tr in st_conv:
        tr.data = np.convolve(tr.data, stf * dt, mode="full")[: len(tr.data)]
    return st_conv
