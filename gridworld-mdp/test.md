## **Algorithms Implemented**  
### 1. **Policy Evaluation**  
Solves the **Bellman Expectation Equation** for a fixed random policy π:

![Policy Evaluation Equation](https://latex.codecogs.com/svg.image?\color{cyan}v_\pi(s)%20=%20\sum_a%20\pi(a|s)%20\sum_{s'}%20p(s'|s,a)%20[r%20+%20\gamma%20v_\pi(s')])

---

### 2. **Value Iteration**  
Solves the **Bellman Optimality Equation**:

![Optimal Value Equation](https://latex.codecogs.com/svg.image?\color{orange}v_*(s)%20=%20\max_a%20\sum_{s'}%20p(s'|s,a)%20[r%20+%20\gamma%20v_*(s')])
