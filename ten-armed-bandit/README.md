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

# Results 
## Greedy Action Selection VS ε-greedy Action Selection

1. **Exploration vs. Exploitation**:
   - Higher epsilon (`ε = 0.10`) leads to more exploration, which helps discover better actions early but reduces long-term performance.
   - Lower epsilon (`ε = 0.01`) leads to better long-term results. The percentage of optimal actions increases steadily and converges to a higher value, indicating a good balance between exploration and exploitation.
   - Greedy strategy (`ε = 0.00`) performs poorly because it lacks exploration.

2. **Optimal Strategy**:
   - A small amount of exploration (`ε = 0.01`) is optimal for maximizing both average reward and the percentage of optimal actions over time.

<img src="https://github.com/user-attachments/assets/f96a748d-1179-477d-92ef-4828d0e1b068" width="400" />

---

## Optimistic Initial Values VS Realistic Initial Values

The simulation calculates the percentage of optimal actions over time for each bandit. The results are plotted as follows:

1. **Bandit 1 (`ε = 0, 𝑄₁(𝑎) = 5`)**: Represents a greedy strategy with optimistic initial values.
2. **Bandit 2 (`ε = 0.1, 𝑄₁(𝑎) = 0`)**: Represents an epsilon-greedy strategy with realistic initial values.

<img src="https://github.com/user-attachments/assets/9b01d312-d812-460b-a7b3-50aa9d0ab5f1" width="400" />


 - In **stationary environments**, this method forces early exploration: actions with high initial values eventually get corrected if they’re not actually optimal.
 - In **nonstationary environments**, this method fails because the agent stops exploring new possibilities once it settles on one action.

### My Findings: Why Optimistic Initialization Worked Best in this Case  

After extending the simulation, I found that **the optimistic method (`ε = 0, Q₁(a) = 5`) performed better** because my problem is **stationary**—the true rewards **do not change over time**.  


- The **high initial values** encourage early exploration by making all actions seem promising at first.  
- Once the agent discovers the **best action**, it **sticks to it**, maximizing rewards.  
- The **ε-greedy method (`ε = 0.1, Q₁(a) = 0`) continues exploring**, even after finding the optimal action, leading to **unnecessary losses**.  

Because **exploration isn’t needed indefinitely** in a stationary environment, the **optimistic greedy approach** proves to be more efficient.  

## Upper Confidence Bound (UCB) Action Selection

The **UCB algorithm** selects actions by balancing **exploration** and **exploitation** using a confidence-based approach.  
- It prioritizes under-explored actions based on an **uncertainty term (c = 2)**.  
- Over time, exploration decreases as the agent becomes more confident in the best action.  

### Simulation:
- **Bandit 1:** UCB (`c = 2`), sample-average method.  
- **Bandit 2:** ε-greedy (`ε = 0.1`), sample-average method.  
- **Result:** UCB achieves **higher rewards** by focusing exploration where needed.  

<img src="https://github.com/user-attachments/assets/02d38a28-7073-4998-b9a7-8c0b0c7903cf" width="400" />


---

## Gradient Bandit Algorithm (GBA)

The **Gradient Bandit algorithm** dynamically adjusts action probabilities based on **policy gradient techniques**.  
- Uses **preference scores** rather than value estimates.  
- Incorporates a **learning rate (α)** and **baseline reward** for better adaptation.  

### Simulation:
- **Variations tested:**  
  - `α = 0.1` and `α = 0.4`  
  - With and without **baseline reward**  
- **Result:** Higher `α` leads to **faster learning**, while using a baseline improves stability.

<img src="https://github.com/user-attachments/assets/bf90ec58-b7af-4229-8cf7-86a0dea06682" width="400" />



---
## How to Run
1. Install dependencies:
   ```bash
   pip install numpy matplotlib tqdm
   
2. Run the ten_armed_testbed.ipynb notebook:

   ```bash
   python ten_armed_testbed.ipynb
   
3. Generated plots are saved in `../generated_images/`.
