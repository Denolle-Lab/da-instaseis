"""
Tests for da_instaseis.waveforms module.
"""

import numpy as np
import pytest

from da_instaseis.waveforms import convolve_stf


class MockTrace:
    def __init__(self, data):
        self.data = np.array(data, dtype=float)
        self.stats = type("Stats", (), {"channel": "BHZ"})()

    def copy(self):
        t = MockTrace(self.data.copy())
        return t


class MockStream:
    def __init__(self, traces):
        self.traces = traces

    def __iter__(self):
        return iter(self.traces)

    def __len__(self):
        return len(self.traces)

    def copy(self):
        return MockStream([t.copy() for t in self.traces])


def test_convolve_stf_preserves_length():
    """Convolution output should have the same length as the input data."""
    data = np.ones(100)
    stf = np.array([0.5, 0.5])
    dt = 0.01
    st = MockStream([MockTrace(data)])
    st_conv = convolve_stf(st, stf, dt)
    for tr in st_conv:
        assert len(tr.data) == 100


def test_convolve_stf_zero_stf():
    """Convolving with a zero STF should produce zeros."""
    data = np.random.randn(50)
    stf = np.zeros(5)
    dt = 0.1
    st = MockStream([MockTrace(data)])
    st_conv = convolve_stf(st, stf, dt)
    for tr in st_conv:
        np.testing.assert_array_almost_equal(tr.data, np.zeros(50))
