# Bellman Equations for MDP

## Policy Evaluation Equation

![Policy Evaluation Equation](https://latex.codecogs.com/svg.image?v_\pi(s)%20=%20\sum_a%20\pi(a|s)%20\sum_{s'}%20p(s'|s,a)%20[r%20+%20\gamma%20v_\pi(s')] "Policy Evaluation")

## Bellman Optimality Equation

![Optimal Value Equation](https://latex.codecogs.com/svg.image?v_*(s)%20=%20\max_a%20\sum_{s'}%20p(s'|s,a)%20[r%20+%20\gamma%20v_*(s')] "Optimal Value")

## Policy Improvement

![Policy Improvement](https://latex.codecogs.com/svg.image?\pi_*(s)%20=%20\arg\max_a%20\sum_{s'}%20p(s'|s,a)%20[r%20+%20\gamma%20v_*(s')] "Policy Improvement")
