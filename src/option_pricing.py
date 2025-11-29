import numpy as np
from src.simulate_gbm import simulate_gbm

def price_european_call_mc(S0, K, r, sigma, T, n_sim=10000, seed=None):
    """
    Price European Call option using Monte Carlo simulation.
    """
    ST = simulate_gbm(S0, r, sigma, T, n_sim, seed)
    payoffs = np.maximum(ST - K, 0)
    return np.exp(-r * T) * np.mean(payoffs)

def price_european_put_mc(S0, K, r, sigma, T, n_sim=10000, seed=None):
    """
    Price European Put option using Monte Carlo simulation.
    """
    ST = simulate_gbm(S0, r, sigma, T, n_sim, seed)
    payoffs = np.maximum(K - ST, 0)
    return np.exp(-r * T) * np.mean(payoffs)

if __name__ == "__main__":
    # Example usage
    S0 = 100      # initial stock price
    K = 100       # strike price
    r = 0.05      # risk-free rate
    sigma = 0.2   # volatility
    T = 1.0       # time to maturity (1 year)
    n_sim = 10000 # number of simulations
    seed = 42     # random seed for reproducibility

    call_price = price_european_call_mc(S0, K, r, sigma, T, n_sim, seed)
    put_price = price_european_put_mc(S0, K, r, sigma, T, n_sim, seed)

    print(f"European Call Option Price (MC): {call_price}")
    print(f"European Put Option Price (MC): {put_price}")