import numpy as np

def simulate_gbm_path(S0, r, sigma, T, n_steps, n_sim, seed=None):
    """
    Simulate full price paths of a stock following Geometric Brownian Motion (GBM).

    Parameters:
        S0      : initial stock price
        r       : risk-free interest rate
        sigma   : volatility
        T       : time to maturity
        n_steps : number of time intervals
        n_sim   : number of simulation paths
        seed    : random seed (optional)

    Returns:
        numpy array of shape (n_sim, n_steps + 1)
        Each row is one simulated price path.
    """
    if seed is not None:
        np.random.seed(seed)

    dt = T / n_steps
    Z = np.random.normal(0, 1, (n_sim, n_steps))

    paths = np.zeros((n_sim, n_steps + 1))
    paths[:, 0] = S0

    for t in range(1, n_steps + 1):
        paths[:, t] = paths[:, t - 1] * np.exp(
            (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[:, t - 1]
        )

    return paths