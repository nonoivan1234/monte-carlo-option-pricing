from flask import Flask, request, render_template
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Prevent GUI backend issues on macOS
import matplotlib.pyplot as plt
import io
import base64

from src.option_pricing import price_european_call_mc
from src.path_simulation import simulate_gbm_path
from src.asian_option import price_asian_call_mc

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    img_data = None

    if request.method == "POST":
        S0 = float(request.form["S0"])
        K = float(request.form["K"])
        r = float(request.form["r"])
        sigma = float(request.form["sigma"])
        T = float(request.form["T"])
        n_sim = int(request.form["n_sim"])
        option_type = request.form["option_type"]
        n_steps = int(request.form["n_steps"])

        if option_type == "european":
            result = price_european_call_mc(S0, K, r, sigma, T, n_sim, seed=42)

        elif option_type == "asian":
            paths = simulate_gbm_path(S0, r, sigma, T, n_steps, n_sim, seed=42)
            result = price_asian_call_mc(paths, K, r, T)

            # Plot paths
            time_grid = np.linspace(0, T, n_steps + 1)
            plt.figure(figsize=(7, 4))
            for i in range(min(10, n_sim)):
                plt.plot(time_grid, paths[i])
            plt.title("Simulated GBM Paths")
            plt.xlabel("Time")
            plt.ylabel("Stock Price")
            plt.tight_layout()

            buf = io.BytesIO()
            plt.savefig(buf, format="png")
            plt.close()
            buf.seek(0)
            img_data = base64.b64encode(buf.getvalue()).decode("utf-8")

    return render_template("index.html", price=result, img_data=img_data)

if __name__ == "__main__":
    app.run(debug=True)