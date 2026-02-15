import math
import numpy as np
import pandas as pd
import pytest
from scipy.stats import norm
from unittest.mock import patch, MagicMock

import sys, os
sys.path.append(os.path.abspath(".."))

import equitytools_local.modeling as modelingtools

from importlib import reload
reload(modelingtools)

def test_factorial_zero():
    """factorial(0) should return 1."""
    assert modelingtools.factorial(0) == 1

def test_factorial_one():
    """factorial(1) should return 1."""
    assert modelingtools.factorial(1) == 1

def test_factorial_small_number():
    """factorial(5) should return 120."""
    assert modelingtools.factorial(5) == 120

def test_factorial_larger_number():
    """factorial(7) should return 5040."""
    assert modelingtools.factorial(7) == 5040

def test_e_power_neg_x_squared_with_int():
    """Function should compute exp(-x^2) for integer input."""
    assert modelingtools.e_power_neg_x_squared(2) == math.exp(-4)

def test_e_power_neg_x_squared_with_float():
    """Function should compute exp(-x^2) for float input."""
    assert modelingtools.e_power_neg_x_squared(1.5) == math.exp(-(1.5**2))

def test_e_power_neg_x_squared_zero():
    """exp(0) should be 1."""
    assert modelingtools.e_power_neg_x_squared(0) == 1.0

def test_erf_zero():
    """erf(0) should return 0."""
    assert modelingtools.erf(0) == 0

def test_e_power_neg_x_squared_int():
    """Should compute exp(-x^2) for integer input."""
    assert modelingtools.e_power_neg_x_squared(3) == math.exp(-9)

def test_e_power_neg_x_squared_float():
    """Should compute exp(-x^2) for float input."""
    assert modelingtools.e_power_neg_x_squared(1.25) == math.exp(-(1.25**2))

def test_e_power_neg_x_squared_zero():
    """exp(0) should equal 1."""
    assert modelingtools.e_power_neg_x_squared(0) == 1.0

def test_bs_call_matches_scipy():
    """Check that bs_call matches the standard Black‑Scholes formula."""
    S = 100
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.2

    expected = S * norm.cdf(
        (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    ) - K * math.exp(-r*T) * norm.cdf(
        (np.log(S/K) + (r - 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    )

    assert pytest.approx(modelingtools.bs_call(S, K, T, r, sigma), rel=1e-6) == expected

def test_bs_call_deep_in_the_money():
    """Call price should be close to intrinsic value when S >> K."""
    S = 1000
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2

    price = modelingtools.bs_call(S, K, T, r, sigma)
    assert price > S - K  # must exceed intrinsic value
    assert price < S      # cannot exceed stock price

def test_bs_call_deep_out_of_the_money():
    """Call price should be very small when S << K."""
    S = 10
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2

    price = modelingtools.bs_call(S, K, T, r, sigma)
    assert price < 1e-6

def test_bs_put_matches_scipy():
    """Check that bs_put matches the standard Black‑Scholes put formula."""
    S = 100
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.2

    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    expected = K * math.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    assert pytest.approx(modelingtools.bs_put(S, K, T, r, sigma), rel=1e-6) == expected


def test_dcf_valuation_basic_case():
    """Validate DCF output against manually computed expected value."""

    fcf = 100
    shares = 10
    growth = 0.05
    discount = 0.10
    terminal_growth = 0.02
    years = 5

    # Manually compute projected FCFs
    projected = [fcf * ((1 + growth) ** yr) for yr in range(1, years + 1)]

    # Discount them
    discounted = [
        projected[yr - 1] / ((1 + discount) ** yr)
        for yr in range(1, years + 1)
    ]

    # Terminal value (Gordon Growth)
    terminal_value = projected[-1] * (1 + terminal_growth) / (discount - terminal_growth)
    discounted_terminal = terminal_value / ((1 + discount) ** years)

    expected_intrinsic = (sum(discounted) + discounted_terminal) / shares

    result = modelingtools.dcf_valuation(
        fcf,
        shares,
        growth_rate=growth,
        discount_rate=discount,
        terminal_growth=terminal_growth,
        years=years,
    )

    assert pytest.approx(result, rel=1e-6) == expected_intrinsic
 
def test_dcf_valuation_negative_fcf_returns_none():
    """Non‑positive FCF should return None."""
    assert modelingtools.dcf_valuation(-50, 10) is None
    assert modelingtools.dcf_valuation(0, 10) is None

def test_dcf_valuation_exception_handling():
    """If an exception occurs, the function should return None."""
    # Force an exception by passing shares_outstanding = 0 (division by zero)
    result = modelingtools.dcf_valuation(100, 0)
    assert result is None



