# Multi-Armed Bandit Reinforcement Learning Project

This project simulates the behavior of a multi-armed bandit problem using epsilon-greedy strategies. It generates plots to visualize the average reward and percentage of optimal actions over time for different epsilon values.

---
## Features
- Simulates multi-armed bandit problems with customizable epsilon values.
- Generates plots for average reward and percentage of optimal actions.
- Supports sample-averages and constant step-size methods for action-value estimation.

---
## How It Works
1. **Bandit Class**: Implements the epsilon-greedy algorithm for action selection and updates action values based on rewards.
2. **Simulation**: Runs multiple independent runs with different epsilon values and calculates mean rewards and optimal actions.
3. **Plotting**: Visualizes the results using `matplotlib` and saves the plots as high-resolution images.

---
## Requirements

You can see the requirements in `requirements.txt`

---
## How to Run
1. Install dependencies:
   ```bash
   pip install numpy matplotlib tqdm
   
2. Run the ten_armed_testbed.ipynb notebook:

   ```bash
   python ten_armed_testbed.ipynb
   
3. Generated plots are saved in `../generated_images/`.