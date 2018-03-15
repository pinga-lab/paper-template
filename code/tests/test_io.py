"""
Test the input and output functions
"""
import pathlib
import numpy.testing as npt

from mypackage.io import load_berkeley_earth_data


DATADIR = pathlib.Path(__file__).parent.parent.parent.joinpath('data')


def test_berkeley_earth():
    "Make sure the data is loaded properly"
    fname = DATADIR.joinpath('hawaii-TAVG-Trend.txt')
    data = load_berkeley_earth_data(fname)
    assert len(data) == 1569
    npt.assert_allclose(data.monthly_temperature.mean(), 22.439276)
