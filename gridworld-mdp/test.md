Here’s the completed and unified explanation of Bellman Equations and their associated algorithms, with all equations in white.

---

# **Bellman Equations and Reinforcement Learning Algorithms**

## **Bellman Equations**

### **Policy Evaluation**  
Solves the Bellman Expectation Equation for a given policy \( \pi \):

\[
v_\pi(s) = \sum_a \pi(a|s) \sum_{s'} p(s'|s,a) [r + \gamma v_\pi(s')]
\]

This equation computes the value function \( v_\pi(s) \), which represents the expected return when following policy \( \pi \).

---

### **Optimal Value Function**  
Solves the Bellman Optimality Equation to find the best possible value function \( v_*(s) \):

\[
v_*(s) = \max_a \sum_{s'} p(s'|s,a) [r + \gamma v_*(s')]
\]

This equation determines the highest possible value for each state, assuming an optimal policy is followed.

---

### **Policy Improvement**  
Defines the optimal policy \( \pi_* \) by selecting actions that maximize expected returns:

\[
\pi_*(s) = \arg\max_a \sum_{s'} p(s'|s,a) [r + \gamma v_*(s')]
\]

This equation determines the best action to take in each state based on the optimal value function.

---

## **Algorithms Implemented**

### **1. Policy Evaluation**  
- Solves the **Bellman Expectation Equation** for a fixed policy \( \pi \).
- Iteratively updates \( v_\pi(s) \) until convergence.
- Given a uniform random policy \( \pi(a|s) = 0.25 \ \forall a \), the algorithm produces the corresponding value function.

---

### **2. Value Iteration**  
- Solves the **Bellman Optimality Equation** by iteratively updating \( v(s) \) and improving the policy.
- At each iteration, the update rule is:

\[
v(s) \leftarrow \max_a \sum_{s'} p(s'|s,a) [r + \gamma v(s')]
\]

- Once \( v(s) \) converges, the optimal policy is derived as:

\[
\pi_*(s) = \arg\max_a \sum_{s'} p(s'|s,a) [r + \gamma v_*(s')]
\]

- The algorithm returns both the optimal value function and the optimal policy.

---

These methods are fundamental to **Dynamic Programming** in Reinforcement Learning, providing a way to evaluate policies and find optimal strategies for decision-making in Markov Decision Processes (MDPs).