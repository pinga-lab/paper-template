"""
Test the processing functions
"""
import numpy as np
import numpy.testing as npt

from mypackage.processing import LinearTrend


def test_trend_no_uncertainty():
    "Test the trend estimation with unit uncertainties"
    year = np.linspace(1800, 2018, 100)
    a, b = 0.1, 2
    temperature = year*a + b
    error = np.ones_like(year)
    trend = LinearTrend().fit(year, temperature, error)

    npt.assert_allclose(trend.angular_coef, a)
    npt.assert_allclose(trend.linear_coef, b)
    npt.assert_allclose(trend.predict(year), temperature)
