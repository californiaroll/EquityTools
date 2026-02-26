"""
modeling.py
Predictive modeling utilities for financial forecasting.
"""

__all__ = [    
    "factorial",
    "merton_jump_call",
    "bs_call",
    "inverse_normal",
    "dcf_valuation",
    "e_power_neg_x_squared",
    "erf",
    "get_simlation"
]

import sys
from scipy.stats import norm
import numpy as np
import math
from datetime import datetime
import random

def factorial(n):
  """Returns Factorial of a positive integer """
  if n == 0 or n == 1:
    return 1
  return n * factorial(n - 1)

def merton_jump_call(S, K, T, r, sigma, m, v, lam, N=40):
  """ Calculate Merton Jump Diffusion Call Value """
  price = 0.0
  for k in range(N):
    r_k = r - lam*(m - 1) + (k * np.log(m)) / T
    sigma_k = np.sqrt(sigma**2 + (k * v**2) / T)
    poisson_prob = np.exp(-m*lam*T) * ((m*lam*T)**k) / factorial(k)
    price += poisson_prob * bs_call(S, K, T, r_k, sigma_k)
  return price
    
def bs_call(S, K, T, r, sigma):
  """ Calculate Black Scholes Call Value """
  d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
  d2 = d1 - sigma*np.sqrt(T)
  return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

def bs_put(S, K, T, r, sigma):
  """ Calculate Black Scholes Put Value """
  d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
  d2 = d1 - sigma*np.sqrt(T)
  return K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def inverse_normal(probability, mean=0, std_dev=1):
    """
    Calculate the inverse normal (quantile) for a given probability,
    mean, and standard deviation.

    :param probability: Probability value between 0 and 1 (exclusive)
    :param mean: Mean of the normal distribution
    :param std_dev: Standard deviation of the normal distribution (must be > 0)
    :return: Quantile value corresponding to the given probability
    """
    # Input validation
    if not (0 < probability < 1):
        raise ValueError("Probability must be between 0 and 1 (exclusive).")
    if std_dev <= 0:
        raise ValueError("Standard deviation must be positive.")

    # Calculate inverse normal
    return norm.ppf(probability, loc=mean, scale=std_dev)

if __name__ == "__main__":
    try:
        # Example: mean=100, std_dev=15, probability=0.975
        mean = 100
        std_dev = 15
        probability = 0.975

        result = inverse_normal(probability, mean, std_dev)
        print(f"Inverse normal for p={probability}, mean={mean}, std_dev={std_dev} is: {result:.4f}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

def dcf_valuation(fcf, shares_outstanding, growth_rate=0.05, discount_rate=0.10, terminal_growth=0.02, years=5):
    """
    Performs a simple DCF valuation.
    """
    try:
        # Use the most recent FCF as base
        latest_fcf = fcf
        if latest_fcf <= 0:
            raise ValueError("Latest FCF is non-positive, DCF may not be meaningful.")

        # Project FCF for given years
        projected_fcfs = [latest_fcf * ((1 + growth_rate) ** year) for year in range(1, years + 1)]

        # Discount projected FCFs to present value
        discounted_fcfs = [fcf / ((1 + discount_rate) ** year) for year, fcf in enumerate(projected_fcfs, start=1)]

        # Terminal value using Gordon Growth Model
        terminal_value = (projected_fcfs[-1] * (1 + terminal_growth)) / (discount_rate - terminal_growth)
        discounted_terminal_value = terminal_value / ((1 + discount_rate) ** years)

        # Enterprise value
        enterprise_value = sum(discounted_fcfs) + discounted_terminal_value

        # Intrinsic value per share
        intrinsic_value_per_share = enterprise_value / shares_outstanding

        return intrinsic_value_per_share

    except Exception as e:
        print(f"Error in DCF calculation: {e}")
        return None

def e_power_neg_x_squared(x):
    """ Validate input type """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an integer or float")
    return math.exp(-x**2)   

def erf(x):
    """ numerical approximation of the error function, """
    if (x == 0):
        return 0
    
    # save the sign of x
    
    sign = 1 if x >= 0 else -1
    x = abs(x)

    # constants
    a1 =  0.254829592
    a2 = -0.284496736
    a3 =  1.421413741
    a4 = -1.453152027
    a5 =  1.061405429
    p  =  0.3275911

    # A&S formula 7.1.26
    t = 1.0/(1.0 + p*x)
    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*math.exp(-x*x)
    return sign*y # erf(-x) = -erf(x)

def get_simlation(numYears, val0, avg_market_rturn, sd_market_return):
    """ Given number of year, average market return and standard deviation of market return, simulate n years of returns.  """
    current_time = datetime.now()
    seed_value = int(current_time.timestamp() * 1_000_000)  # Convert to microseconds
    random.seed(seed_value)
    current_simul = []
    current_simul.append(val0)
    for num in range(1, 11): 
        if (num == 0):
            current_simul.append (val0 * ( 1 + inverse_normal (random.random(), avg_market_rturn, sd_market_return)))
        else:
            current_simul.append (current_simul[num - 1] * ( 1 + inverse_normal (random.random(), avg_market_rturn, sd_market_return)))

    return   current_simul    