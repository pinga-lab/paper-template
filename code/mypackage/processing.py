"""
Calculate a linear trend for the temperature data
"""
import numpy as np


class LinearTrend():
    """
    Calculate a linear trend for (year, temperature) data.
    """

    def __init__(self):
        self.linear_coef = None
        self.angular_coef = None

    def predict(self, year):
        """
        Predict temperatures based on the trend.

        Parameters
        ----------
        year : float or array
            The decimal year

        Returns
        -------
        temperature : float or array
           The predicted temperature based on the trend in C.

        """
        return self.linear_coef + year*self.angular_coef

    def fit(self, year, temperature, uncertainty):
        """
        Fit a linear trend to the temperature time series.

        Least-squares fit is weighted by the uncertainty.

        Parameters
        ----------
        year : array
            The decimal year
        temperature : array
           The temperature in C
        uncertainty : array
           The temperature uncertainty in C

        """
        assert year.ndim == 1
        assert temperature.ndim == 1
        assert year.shape == temperature.shape

        # Remove nans from the data. Numpy doesn't like them.
        not_nan = ~np.isnan(temperature)
        year = year[not_nan]
        temperature = temperature[not_nan]
        uncertainty = uncertainty[not_nan]

        ndata = year.size

        jacobian = np.empty((ndata, 2))
        jacobian[:, 0] = 1
        jacobian[:, 1] = year

        weights = np.diag(1/uncertainty**2)

        hessian = jacobian.T.dot(weights).dot(jacobian)
        gradient = jacobian.T.dot(weights).dot(temperature)

        coefs = np.linalg.solve(hessian, gradient)

        self.linear_coef = coefs[0]
        self.angular_coef = coefs[1]
        return self
