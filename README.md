
# **NPUA Reinforcement Learning Course Projects**

This repository contains a series of projects developed as part of the **Reinforcement Learning (RL)** course at the National Polytechnic University of Armenia (NPUA). The projects are based on the foundational concepts presented in [*Reinforcement Learning: An Introduction* by Sutton and Barto](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf). Each project focuses on implementing and analyzing key RL algorithms, emphasizing both theoretical understanding and practical application.

---

## **Projects Overview**

### Project 1: [Tic-Tac-Toe](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/01_tic_tac_toe) — Game Implementation

* Implementation of a Tic-Tac-Toe environment.
* RL agent trained using **Temporal-Difference Learning**.
* Supports human vs. AI and AI vs. AI gameplay scenarios.


📘 *Based on Chapter 1, §1.5: An Extended Example – Tic-Tac-Toe*

---

### Project 2: [Multi-Armed Bandit](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/02_ten_armed_bandit)

* Explores the **exploration–exploitation** trade-off.
* Implements and compares **$\epsilon$-greedy**, **UCB**, and **Gradient Bandit**.
* Evaluates **optimistic initial values**, **sample-averages** vs **constant step-size**.

📘 *Based on Chapter 2: Multi-armed Bandits*

---

### Project 3: [Markov Decision Process](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/03_gridworld_mdp) — Grid-World

* **Policy Evaluation** and **Value Iteration** for a $5\times5$ grid.
* Value function convergence under random and optimal policies.
* Demonstrates **Bellman equations** in finite MDPs.

📘 *Based on Chapter 3: Finite Markov Decision Processes*

---

### Project 4: [Dynamic Programming](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/04_gridworld_dp) — Grid-World

* **Iterative Policy Evaluation** and **Policy Improvement** in a $4\times4$ grid with terminals.
* **In-place** vs **out-of-place** DP updates.
* Ties to the **Policy Improvement Theorem**.

📘 *Based on Chapter 4: Dynamic Programming*

---

### Project 5: [Gambler’s Problem](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/05_gambler_problem) — Value Iteration

* Solves the Gambler’s Problem with **Value Iteration** to maximize success probability.
* Visualizes value evolution and the final optimal policy.

📘 *Based on Chapter 4, §4.4: Value Iteration*

---

### Project 6: [Monte Carlo Methods](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/06_blackjack) — Blackjack

* **On-Policy MC**, **Off-Policy MC** (importance sampling), and **Exploring Starts**.
* Simplified Blackjack environment with value visualizations and convergence analysis.

📘 *Based on Chapter 5: Monte Carlo Methods*

---

### Project 7: [Infinite Variance in Off-Policy Evaluation](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/07_infinite_variance)

* Demonstrates instability of **importance sampling** off-policy.
* Shows how behavior–target policy mismatch can yield **infinite variance**.
* Tests **weighted** and **per-decision** importance sampling.

📘 *Based on Chapter 5, §5.5: Off-Policy Prediction via Importance Sampling*

---

### Project 8: [Random Walk](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/08_random_walk) — MC vs TD(0)

* Compares **Monte Carlo** and **TD(0)** for value prediction.
* Analyzes **bias–variance** and batch convergence.
* Reports sample efficiency, speed, and RMSE.

📘 *Based on Chapter 6, §6.2: Prediction Example – Random Walk*

---

### Project 9: [Windy Gridworld](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/09_windy_gridworld) — SARSA

* On-policy **SARSA** control with deterministic wind.
* **$\epsilon$-greedy** exploration; learning curves and final policies.

📘 *Based on Chapter 6, §6.5: Windy Gridworld Example*

---

### Project 10: [Cliff Walking](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/10_cliff_walking) — SARSA, Expected SARSA, Q-Learning

* Compares **SARSA**, **Expected SARSA**, and **Q-Learning**.
* Trade-offs among **safety**, **stability**, and **optimality**.
* Cumulative rewards, policy convergence, and learning-rate sensitivity.

📘 *Based on Chapter 6, §6.6: Cliff Walking Example*

---

### Project 11: [Maximization Bias](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/11_maximization_bias)

* Shows **maximization bias** and mitigation via **Double Learning**.
* Minimal two-state MDP with noisy branch; classic max overestimates.
* Tracks **left-action frequency** vs unbiased baselines.

📘 *Based on Chapter 6: Maximization Bias & Double Learning*

---

### Project 12: [Random Walk — $n$-step TD](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/12_random_walk_ntd)

* **$n$-step TD** prediction on the 19-state random walk.
* Horizons $n\in{1,2,4,8,16}$; bias–variance and RMSE trends.
* Intermediate $n$ often best overall.

📘 *Based on Chapter 7: $n$-step Bootstrapping*

---

### Project 13: [Mazes — Dyna-Q, Dyna-Q+, Prioritized Sweeping](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/13_mazes)

* **Model-based planning** with learned models.
* **Changing maze** for adaptation after obstacle switch.
* Learning speed, cumulative reward, and backups-to-solution.

📘 *Based on Chapter 8: Planning and Acting (Dyna; Prioritized Sweeping)*

---

### Project 14: [Expectation vs. Sample Updates](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/14_updates_comparison)

* **Expectation backups** vs **sample backups** under fixed compute and branching $b$.
* For large $b$, a few expectation evaluations (costing $b$ each) **crush variance**.
* RMS error vs computations for $b\in{2,10,100,1000}$.

📘 *Based on Chapter 8: Expectation vs Sampling*

---

### Project 15: [Trajectory Sampling vs Uniform Expected Updates](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/15_trajectory_sampling)

* **On-policy trajectory sampling** vs **uniform expected updates** in large random MDPs (1k & 10k states).
* Measures **greedy start-state value** vs expected updates.
* Trajectory sampling **dominates** uniform sweeps in large spaces.

📘 *Based on Chapter 8: Planning Distributions & Trajectory Sampling*

---

### Project 16: [Random Walk with Function Approximation](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/16_random_walk_fa)

* **Linear FA** for random-walk prediction.
* **Semi-gradient TD** vs **(gradient) MC**: stability, speed, RMSE.
* Effects of **feature design** and **step size**.

📘 *Based on Chapter 9: On-Policy Prediction with Function Approximation*

---

### Project 17: [Coarse Coding (Square-Wave Approximation)](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/17_coarse_coding)

* **Overlapping interval features** to approximate a square wave on $[0,2)$.
* How **feature width** and **sample count** shape bias–variance and edge fidelity.
* Six-panel plots across data regimes approaching the piecewise-constant target.

📘 *Based on Chapter 9: Gradient Methods & Representations (Coarse Coding)*

---

### Project 18: [Access-Control Scheduling (Queueing DP)](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/18_access_control)

* Finite-horizon **dynamic programming** with limited servers.
* State: number of free servers; jobs have **priority levels**. Action: **accept** or **reject**.
* Optimal policy and **differential action values** vs free servers by priority.

📘 *Based on Chapter 10: Finite-Horizon DP / Control Examples*

---

### Project 19: [Mountain Car — $n$-step SARSA with Tile Coding](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/19_mountain_car)

* Control with **$n$-step SARSA** ($n\in{1,2,4,8,16}$) and **tile-coded** $Q(s,a)$.
* Steps/episode vs $\alpha$ and $n$; **cost-to-go** surface snapshots.
* Moderate $n$ and tiling-scaled $\alpha$ learn fastest.

📘 *Based on Chapter 10: $n$-step Control with Function Approximation*

---

### Project 20: [Off-Policy TD in Baird’s Counterexample](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/20_counter_examples)

* Reproduces **Baird’s counterexample**: semi-gradient off-policy TD **diverges** with linear FA.
* Compares **TDC/GTD2** and **Emphatic TD**.
* Weight trajectories, $\sqrt{\overline{\mathrm{VE}}}$, and **Projected Bellman Error**: Emphatic TD **converges**.

📘 *Based on Chapter 11: Off-Policy Learning & Divergence; Gradient-TD & Emphatic methods*

---

### Project 21: [Eligibility Traces in Random Walk — TD($\lambda$) & $\lambda$-return](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/21_random_walk_et)

* **TD($\lambda$)** vs **off-line** and **on-line $\lambda$-return**.
* Sweeps over $\alpha$ and $\lambda$; **end-of-episode RMSE** over the first 10 episodes.
* **Intermediate $\lambda$** (e.g., $0.8$) often best; stable $\alpha$ depends on method.

📘 *Based on Chapter 12: Eligibility Traces; Forward/Backward Views*

---

### Project 22: [Mountain Car — SARSA($\lambda$) with Eligibility Traces](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/22_mountain_car_et)

* SARSA($\lambda$) with tile coding; **accumulating**, **replacing**, **replacing+clearing**, and **dutch** traces.
* Sensitivity to $\alpha\times\text{tilings}$ and $\lambda$; early-performance curves.
* **Dutch** and **replacing** traces perform best after tuning; very large $\lambda$ can be unstable at high $\alpha$.

📘 *Based on Chapter 12: Traces in Control; Tile Coding in Mountain Car*

---

## **Project Structure**

Each project directory contains:

* `src/`: Source code for the implementation.
* `notebooks/`: Jupyter notebooks for experiments and visualizations (if applicable).
* `generated_images/`: Experimental results, including plots and analysis.
* `README.md`: Project-specific documentation with setup, methodology, and key findings.

---
