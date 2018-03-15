"""
Functions for loading the data
"""
import numpy as np
import pandas as pd


def load_berkeley_earth_data(fname):
    """
    Load monthly temperature data from a Berkeley Earth file.

    The moving average columns are ignored. For convenience, reads the
    reference temperature and calculates the absolute temperature as well. Also
    calculates decimal years for calculating trends and plotting.

    Parameters
    ----------
    fname : str
        The name/path of the data file.

    Returns
    -------
    data : pandas.DataFrame
        The data in a pandas.DataFrame with columns: year, month, year_decimal,
        monthy_anomaly, monthly_error, monthly_temperature.

    """
    # Used to find the absolute temperature in the header
    marker = '% Estimated Jan 1951-Dec 1980 absolute temperature (C):'
    with open(fname) as datafile:
        # Read the absolute temperature from the header
        for line in datafile:
            if line.startswith(marker):
                numbers = line.split(':')[1]
                abs_temp = float(numbers.split('+/-')[0].strip())
                break
        # Load the rest of the data into a DataFrame
        year, month, anom, error = np.loadtxt(datafile, comments='%',
                                              usecols=[0, 1, 2, 3],
                                              unpack=True)
    columns = dict(year=year.astype(np.int),
                   month=month.astype(np.int),
                   monthly_anomaly=anom,
                   monthly_error=error,
                   year_decimal=year + (month - 1)/12,
                   monthly_temperature=anom + abs_temp)
    data = pd.DataFrame(columns)
    return data
