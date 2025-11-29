import numpy as np

def price_asian_call_mc(paths, K, r, T):
    """
    Price Asian (arithmetic-average) Call option using Monte Carlo simulation.
    
    Parameters:
        paths : numpy array of shape (n_sim, n_steps + 1)
                Simulated GBM price paths
        K     : strike price
        r     : risk-free rate
        T     : time to maturity
        
    Returns:
        Estimated option price (float)
    """
    # Average over time steps, excluding the initial price if preferred
    avg_price = np.mean(paths[:, 1:], axis=1)
    payoffs = np.maximum(avg_price - K, 0)
    return np.exp(-r * T) * np.mean(payoffs)


def price_asian_put_mc(paths, K, r, T):
    """
    Price Asian (arithmetic-average) Put option using Monte Carlo simulation.
    """
    avg_price = np.mean(paths[:, 1:], axis=1)
    payoffs = np.maximum(K - avg_price, 0)
    return np.exp(-r * T) * np.mean(payoffs)

if __name__ == "__main__":
    # Example usage
    from src.path_simulation import simulate_gbm_path

    S0 = 100      # initial stock price
    K = 100       # strike price
    r = 0.05      # risk-free rate
    sigma = 0.2   # volatility
    T = 1.0       # time to maturity (1 year)
    n_steps = 50  # number of time steps
    n_sim = 10000 # number of simulations
    seed = 42     # random seed for reproducibility

    paths = simulate_gbm_path(S0, r, sigma, T, n_steps, n_sim, seed)

    asian_call_price = price_asian_call_mc(paths, K, r, T)
    asian_put_price = price_asian_put_mc(paths, K, r, T)

    print(f"Asian Call Option Price (MC): {asian_call_price}")
    print(f"Asian Put Option Price (MC): {asian_put_price}")