# quantitative-finance-models
This repository contains Python implementations of foundational quantitative finance models. As a pure mathematics student, I built these engines to translate theoretical financial mathematics (both discrete and continuous-time) into code.

The first script prices a European Call Option by simulating 10000 stock price paths under a risk neautral measure. I used numpy vectorization instead of for loops. It generates standard normal variables and calculates the exponential payoffs for all parallel universes simultaneously to optimize computational speed. 

The second script prices an American Put option, specifically calculating the optimal stopping time and early exercise premium. Uses the Cox-Ross-Rubinstein model and a 1D numpy "array" with replacing values to simulate backwards induction.
