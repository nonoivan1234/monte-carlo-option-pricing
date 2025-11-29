import argparse
from src.option_pricing import price_european_call_mc, price_european_put_mc

def main():
    parser = argparse.ArgumentParser(description="Monte Carlo Option Pricing")
    parser.add_argument("--option", type=str, choices=["call", "put"], required=True)
    parser.add_argument("--S0", type=float, default=100.0)
    parser.add_argument("--K", type=float, default=105.0)
    parser.add_argument("--r", type=float, default=0.05)
    parser.add_argument("--sigma", type=float, default=0.2)
    parser.add_argument("--T", type=float, default=1.0)
    parser.add_argument("--n_sim", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=None)

    args = parser.parse_args()

    if args.option == "call":
        price = price_european_call_mc(args.S0, args.K, args.r, args.sigma, args.T, args.n_sim, args.seed)
    else:
        price = price_european_put_mc(args.S0, args.K, args.r, args.sigma, args.T, args.n_sim, args.seed)

    print(f"Monte Carlo {args.option.upper()} option price: {price:.4f}")

if __name__ == "__main__":
    main()