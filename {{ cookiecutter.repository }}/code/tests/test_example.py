"""
Example test file. Use a docstring to describe what this tests.

All test functions need to start with "test_".
"""
import numpy.testing as npt
import numpy as np


def test_something():
    "This function is a test. It should raise an exception if it fails."
    result = 1 + 1
    assert result == 2, 'Failed addition test with result {}'.format(result)


def test_something_that_fails():
    "Tests floating point closeness and fails"
    result = 1.1*np.ones(10)
    true = 2*np.ones(10)
    npt.assert_allclose(result, true)
