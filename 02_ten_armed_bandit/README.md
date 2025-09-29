# Multi-Armed Bandit Reinforcement Learning Project

This project explores various strategies for solving the **Multi-Armed Bandit (MAB)** problem, a classic reinforcement learning challenge. The MAB problem involves an agent making sequential decisions to maximize cumulative rewards by balancing **exploration** (trying new actions) and **exploitation** (leveraging known information). The project implements and compares several algorithms, including **epsilon-greedy**, **optimistic initialization**, **Upper Confidence Bound (UCB)**, and **Gradient Bandit Algorithm (GBA)**, to understand their performance in stationary environments.

---

## Features
- **Customizable Bandit Simulation**: Simulates multi-armed bandit problems with adjustable parameters like epsilon values, step sizes, and initial action values.
- **Multiple Algorithms**: Implements and compares epsilon-greedy, optimistic initialization, UCB, and gradient bandit algorithms.
- **Visualization**: Generates plots for average reward and percentage of optimal actions over time.
- **Flexible Methods**: Supports both **sample-averages** and **constant step-size** methods for action-value estimation.

---

## How It Works
1. **Bandit Class**: Implements the core logic for action selection and value updates using different strategies.
2. **Simulation**: Runs multiple independent runs with varying parameters to evaluate performance.
3. **Plotting**: Visualizes results using `matplotlib` and saves plots as high-resolution images for analysis.

---

## Requirements
You can see the requirements in `requirements.txt`

---

## Results and Findings

---

##  **Greedy Action Selection vs ε-greedy Action Selection**
**Exploration vs. Exploitation**: 
     - Higher epsilon values (`ε = 0.10`) encourage more exploration, which helps discover better actions early but may reduce long-term performance.
     - Lower epsilon values (`ε = 0.01`) strike a balance, leading to better long-term results by gradually increasing the percentage of optimal actions.
     - Greedy strategy (`ε = 0.00`) performs poorly due to lack of exploration.
   - **Optimal Strategy**: A small amount of exploration (`ε = 0.01`) is ideal for maximizing both average reward and the percentage of optimal actions over time.

<img src="https://github.com/user-attachments/assets/f96a748d-1179-477d-92ef-4828d0e1b068" alt="Epsilon-Greedy Results" width="500"/>

**Optimal Strategy**:
   - A small amount of exploration (`ε = 0.01`) is optimal for maximizing both average reward and the percentage of optimal actions over time.

---

## **Optimistic Initial Values vs. Realistic Initial Values**
   - **Optimistic Initialization (`ε = 0, Q₁(a) = 5`)**: Represents a greedy strategy with optimistic initial values.
   - **Realistic Initialization (`ε = 0.1, Q₁(a) = 0`)**: Represents an epsilon-greedy strategy with realistic initial values.

   ![Optimistic vs. Realistic](https://github.com/user-attachments/assets/9b01d312-d812-460b-a7b3-50aa9d0ab5f1)

   Optimistic initialization performs better in stationary environments because it efficiently balances exploration and exploitation without requiring indefinite exploration.

---

## **Upper Confidence Bound (UCB) Action Selection**
   - **UCB Algorithm**: Balances exploration and exploitation by prioritizing under-explored actions using a confidence-based term (`c = 2`).
   - **Simulation Results**: UCB achieves higher rewards compared to epsilon-greedy (`ε = 0.1`) by focusing exploration where it is most needed.

   ![UCB Results](https://github.com/user-attachments/assets/02d38a28-7073-4998-b9a7-8c0b0c7903cf)

UCB dynamically adjusts exploration based on uncertainty, making it more efficient in stationary environments.

---

##  **Gradient Bandit Algorithm (GBA)**
   - **GBA Algorithm**: Adjusts action probabilities dynamically using **preference scores** and a **learning rate (α)**. It incorporates a **baseline reward** for stability.
   - **Simulation Results**:
     - Higher learning rates (`α = 0.4`) lead to faster learning but may reduce stability.
     - Using a baseline reward improves performance by providing a reference point for updates.

   ![GBA Results](https://github.com/user-attachments/assets/f305ed46-5c97-40c9-bb09-d26692dd843a)

GBA is effective for adapting to changing environments but requires careful tuning of parameters.

---

## Conclusion
This project demonstrates the effectiveness of different strategies for solving the multi-armed bandit problem in stationary environments. Key takeaways include:
1. **Epsilon-Greedy**: A small amount of exploration (`ε = 0.01`) provides a good balance between exploration and exploitation.
2. **Optimistic Initialization**: Works best in stationary environments by encouraging early exploration without requiring indefinite exploration.
3. **UCB**: Outperforms epsilon-greedy by dynamically adjusting exploration based on uncertainty.
4. **GBA**: Offers flexibility and adaptability but requires careful parameter tuning.

These findings highlight the importance of choosing the right strategy based on the problem's characteristics, such as whether the environment is stationary or non-stationary.

---

This project provides a comprehensive exploration of multi-armed bandit algorithms, offering insights into their strengths and weaknesses in different scenarios. By visualizing the results, users can better understand the trade-offs between exploration and exploitation and apply these concepts to real-world decision-making problems.
