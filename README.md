# Monte Carlo Option Pricing

This repository implements Monte Carlo simulation methods for pricing options under the Geometric Brownian Motion (GBM) model.  
The codebase is organized for both research-style experimentation (via Jupyter notebooks) and reusable modules (via `src/`), with an additional Flask web interface for interactive visualization.

---

## Contents

- European option pricing with Monte Carlo
- Vectorized vs loop-based simulation (performance comparison)
- Time-discretized GBM paths for path-dependent options
- Asian option pricing (arithmetic-average)
- Flask web interface for interactive simulation and visualization

---

## Mathematical Background

### Geometric Brownian Motion (risk-neutral measure)

Stock price dynamics:

$$
dS_t = r S_t\, dt + \sigma S_t\, dW_t
$$

where

- \( S_t \) is the stock price,
- \( r \) is the risk-free rate,
- \( \sigma \) is volatility,
- \( W_t \) is a standard Brownian motion.

#### One-step discretization (European options)

For maturity \( T \):

$$
S_T = S_0 \cdot \exp\left((r - 0.5\sigma^2)T + \sigma \sqrt{T} Z\right), \quad Z \sim \mathcal{N}(0, 1)
$$

European call payoff:

$$
C = e^{-rT} \cdot \max(S_T - K, 0)
$$

#### Time discretization (path-dependent options)

With \( N \) time steps, \( \Delta t = T / N \):

$$
S_{t_{i+1}} = S_{t_i} \cdot \exp\left((r - 0.5\sigma^2)\Delta t + \sigma \sqrt{\Delta t} Z_i\right), \quad Z_i \sim \mathcal{N}(0, 1)
$$

Asian call (arithmetic-average) payoff:

$$
C = e^{-rT} \cdot \max\left(\frac{1}{N} \sum_{i=1}^{N} S_{t_i} - K, 0\right)
$$

---

## Project Structure

```text
monte-carlo-option-pricing/
│
├── src/
│   ├── simulate_gbm.py        # Single-step GBM simulation (terminal price)
│   ├── path_simulation.py     # Time-discretized GBM paths
│   ├── option_pricing.py      # Monte Carlo pricing for European options
│   ├── asian_option.py        # Monte Carlo pricing for Asian options
│
├── notebooks/
│   ├── 01_basic_european_call.ipynb
│   ├── 02_vectorized_vs_nonvectorized.ipynb
│   ├── 03_time_discretization_asian_option.ipynb
│
├── flask_app/
│   ├── app.py                 # Flask application for interactive demo
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
│
├── examples/
│   └── run_pricing.py         # CLI example for European option pricing
│
├── docs/                      # (optional) figures, demo screenshots
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started
1. Command-line example (European Call / Put)
```
python -m examples.run_pricing \
    --option call \
    --S0 100 \
    --K 105 \
    --sigma 0.2 \
    --r 0.05 \
    --T 1 \
    --n_sim 100000
```
```
Arguments:
    --option : call or put
    --S0     : initial stock price
    --K      : strike price
    --sigma  : volatility
    --r      : risk-free rate
    --T      : time to maturity (in years)
    --n_sim  : number of Monte Carlo paths
```
2. Jupyter notebooks
From the project root:
```
jupyter notebook
```
Then open the notebooks in the `notebooks/` directory. Notebooks included:
- ```01_basic_european_call.ipynb```
Basic Monte Carlo pricing for a European call and comparison with the Black–Scholes formula.
- ```02_vectorized_vs_nonvectorized.ipynb```
Performance benchmark between a loop-based and a NumPy-vectorized Monte Carlo implementation.
- ```03_time_discretization_asian_option.ipynb```
Time-discretized GBM path simulation and pricing of an Asian call option, with visualizations of price paths and payoff distribution.

3. Flask interactive interface
From the project root:
```
python -m flask_app.app
```
Then open your web browser and navigate to `http://localhost:5000`. Below is a screenshot of the interface:

![Flask App Screenshot](docs/flask_app_screenshot.png)