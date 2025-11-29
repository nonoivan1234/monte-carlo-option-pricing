import numpy as np

def simulate_gbm(S0: float, r: float, sigma: float, T: float, n_sim: int, seed: int = None):
    """
    Simulate terminal stock price using Geometric Brownian Motion (single-step model).
    Parameters:
        S0     – initial stock price
        r      – risk-free rate
        sigma  – volatility
        T      – time to maturity
        n_sim  – number of simulation paths
        seed   – random seed (optional)
    Returns:
        numpy array of simulated terminal stock prices
    """
    if seed is not None:
        np.random.seed(seed)

    Z = np.random.normal(0, 1, n_sim)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    return ST

if __name__ == "__main__":
    # Example usage
    S0 = 100      # initial stock price
    r = 0.05      # risk-free rate
    sigma = 0.2   # volatility
    T = 1.0       # time to maturity (1 year)
    n_sim = 10000 # number of simulations
    seed = 42     # random seed for reproducibility

    ST = simulate_gbm(S0, r, sigma, T, n_sim, seed)
    print(ST)