# **NPUA Reinforcement Learning Course Projects**

This repository contains a series of projects developed as part of the Reinforcement Learning (RL) course at the National Polytechnic University of Armenia (NPUA). The projects are based on the foundational concepts presented in [*Reinforcement Learning: An Introduction* by Sutton and Barto](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf). Each project focuses on implementing and analyzing key RL algorithms, emphasizing both theoretical understanding and practical application.

---

## **Projects Overview**

### Project 1: [Tic-Tac-Toe](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/01_tic_tac_toe) Game Implementation

* Implementation of a Tic-Tac-Toe environment.
* Reinforcement Learning agent trained using **Temporal-Difference Learning**.
* Supports human vs. AI and AI vs. AI gameplay scenarios.
  
 📘 *Based on Chapter 1, Section 1.5: An Extended Example – Tic-Tac-Toe*

---

### Project 2: [Multi-Armed Bandit](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/02_ten_armed_bandit) Problem

* Explores the **exploration–exploitation trade-off** in the multi-armed bandit problem.
* Implements and compares **ε-greedy**, **Upper Confidence Bound (UCB)**, and **Gradient Bandit** algorithms.
* Evaluates the effects of **optimistic initial values** and **sample-averages** versus **constant step-size updates**.
 
📘 *Based on Chapter 2: Multi-armed Bandits*

---

### Project 3: [Markov Decision Process](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/03_gridworld_mdp) in Grid-World

* Implements **Policy Evaluation** and **Value Iteration** for a 5×5 grid-world environment.
* Visualizes value function convergence under random and optimal policies.
* Demonstrates the use of **Bellman equations** in finite MDPs.

📘 *Based on Chapter 3: Finite Markov Decision Processes*

---

### Project 4: [Dynamic Programming](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/04_gridworld_dp) in Grid-World

* Implements **Iterative Policy Evaluation** and **Policy Improvement** in a 4×4 grid-world with terminal states.
* Compares **in-place** vs. **out-of-place** DP updates.
* Analyzes theoretical guarantees from the **Policy Improvement Theorem**.
  
📘 *Based on Chapter 4: Dynamic Programming*

---

### Project 5: [Gambler’s Problem](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/05_gambler_problem) – Value Iteration Approach

* Solves the **Gambler's Problem** using **Value Iteration** to maximize the probability of reaching a goal capital.
* Visualizes value function evolution and the final optimal policy.
 
📘 *Based on Chapter 4, Section 4.4: Value Iteration*

---

### Project 6: [Monte Carlo Methods](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/06_blackjack) in Blackjack

* Implements **On-Policy Monte Carlo**, **Off-Policy Monte Carlo** with importance sampling, and **Exploring Starts** for optimal policy discovery.
* Simulates a simplified Blackjack environment to visualize value functions and analyze convergence behavior.
  
📘 *Based on Chapter 5: Monte Carlo Methods*

---

### Project 7: [Infinite Variance in Off-Policy Evaluation](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/07_infinite_variance)

* Demonstrates the instability of **importance sampling** in off-policy evaluation.
* Shows how policy mismatch between behavior and target policies can lead to **infinite variance** in return estimates.
* Evaluates variance-reduction strategies, including **weighted** and **per-decision** importance sampling.
 
📘 *Based on Chapter 5, Section 5.5: Off-Policy Prediction via Importance Sampling*

---

### Project 8: [Random Walk](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/08_random_walk) – Monte Carlo vs. Temporal-Difference Methods

* Compares **Monte Carlo (MC)** and **Temporal-Difference (TD(0))** learning for value prediction.
* Analyzes the **bias–variance trade-off** and convergence behavior under batch updating.
* Provides analytical comparisons of sample efficiency, convergence speed, and RMSE performance.
 
📘 *Based on Chapter 6, Section 6.2: Prediction Example – Random Walk*

---

### Project 9: [Windy Gridworld](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/09_windy_gridworld) – SARSA Algorithm Implementation

* Implements the **SARSA control algorithm** in Windy Gridworld with deterministic wind disturbances.
* Demonstrates on-policy learning with an **ε-greedy** exploration strategy.
* Analyzes learning curves and final policy behavior, comparing results with textbook examples.

📘 *Based on Chapter 6, Section 6.5: Windy Gridworld Example*

---

### Project 10: [Cliff Walking](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/10_cliff_walking) – SARSA, Expected SARSA, and Q-Learning

* Compares **SARSA**, **Expected SARSA**, and **Q-Learning** in the Cliff Walking environment.
* Analyzes trade-offs between **exploration safety**, **learning stability**, and **policy optimality**.
* Includes visualizations of cumulative rewards, policy convergence, and learning-rate sensitivity.
  
📘 *Based on Chapter 6, Section 6.6: Cliff Walking Example*

---

### Project 11: [Maximization_bias](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/11_maximization_bias)

* Demonstrates **maximization bias** in value-based methods and how **Double Learning** (Double Q-Learning / Double Expected SARSA) mitigates it.
* Minimal two-state MDP where noise at a branching state causes classic max targets to **overestimate** and select a suboptimal branch.
* Compares **left-action frequency** across methods and visualizes convergence toward the unbiased baseline.
 
📘 *Based on Chapter 6: Maximization Bias & Double Learning*

---

### Project 12: [Random Walk — n-step TD](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/12_random_walk_ntd)

* Implements **n-step Temporal-Difference (TD(n))** prediction on the classic 19-state random walk.
* Compares horizons (n \in {1,2,4,8,16}) for **bias–variance** and **RMSE** over episodes.
* Shows that intermediate (n) often yields the best overall trade-off.
  
📘 *Based on Chapter 7: n-step Bootstrapping*

---

### Project 13: [Mazes — Dyna-Q, Dyna-Q+, Prioritized Sweeping](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/13_mazes)

* Studies **model-based planning** with a learned model: **Dyna-Q**, **Dyna-Q+** (time-aware bonus), and **Prioritized Sweeping**.
* Includes a **changing maze** scenario to test **adaptation** after obstacle changes.
* Compares **learning speed**, **cumulative reward**, and **backups-to-solution** across planning methods.
 
📘 *Based on Chapter 8: Planning and Acting (Dyna; Prioritized Sweeping)*

---

### Project 14: [Expectation vs. Sample Updates](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/14_updates_comparison)

* Compares **expectation backups** vs **sample backups** under a fixed compute budget and branching factor (b).
* Shows that for large (b), a few expectation evaluations (costing (b) each) **crush variance** and outperform incremental sampling.
* Reports **RMS error vs computations** for (b \in {2,10,100,1000}).
 
📘 *Based on Chapter 8: Expectation vs Sampling*

---

### Project 15: [Trajectory Sampling vs Uniform Expected Updates](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/15_trajectory_sampling)

* Compares **on-policy trajectory sampling** against **uniform expected updates** in large random MDPs (1k & 10k states).
* Measures **start-state value under the greedy policy** as computation (expected updates) grows.
* Finds that policy-focused trajectory sampling **dominates** uniform sweeps in large state spaces.
  
📘 *Based on Chapter 8: Planning Distributions & Trajectory Sampling*

---

### Project 16: [Random Walk with Function Approximation](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/16_random_walk_fa)

* Applies **linear function approximation** to the random-walk value-prediction task.
* Compares **semi-gradient TD** vs **(gradient) Monte Carlo** for stability, learning speed, and RMSE.
* Discusses the influence of **feature design** and **step size** on convergence.
 
📘 *Based on Chapter 9: On-Policy Prediction with Function Approximation*

---

### Project 17: [Coarse Coding (Square-Wave Approximation)](https://github.com/RuzGhandilian/Reinforcement_Learning_NPUA/tree/master/17_coarse_coding)

* Uses **overlapping interval features** (coarse coding) to approximate a **square-wave** target on ([0,2)).
* Studies how **feature width** and **sample count** shape the **bias–variance** trade-off and edge fidelity.
* Presents six-panel plots across sample regimes showing convergence to the ideal piecewise-constant function.
  
📘 *Based on Chapter 9: Gradient Methods & Representations (Coarse Coding)*

---

## **Project Structure**

Each project directory contains:

* `src/`: Source code for the implementation.
* `notebooks/`: Jupyter Notebooks for experiments and visualizations (if applicable).
* `generated_images/`: Experimental results, including plots and analysis.
* `README.md`: Project-specific documentation detailing setup instructions, methodology, and key findings.


