# Tic-Tac-Toe Reinforcement Learning Project

This project implements **Reinforcement Learning (RL)** for the classic **Tic-Tac-Toe** game. The goal of the project is to train an RL agent to play Tic-Tac-Toe optimally. The agent can then compete against another RL agent or a human player. This implementation demonstrates **Temporal-Difference Learning** and **ε-greedy strategies**.

---

## **Features**

| **Feature**                | **Description**                                                                                                                                     |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Reinforcement Learning Player (RLPlayer)** | - Uses **Temporal-Difference Learning** to estimate state values. <br> - Explores moves with the **ε-greedy strategy** during training. <br> - Saves and loads learned policies for reuse. |
| **Human Player**            | Allows a human to play against the trained RL agent for testing its performance.                                                                    |
| **Judge**                   | Manages the game flow, ensuring turns are followed correctly and determining the winner.                                                            |
| **State Management**        | - Represents the Tic-Tac-Toe board and generates unique state hashes. <br> - Checks for **win**, **lose**, or **tie** conditions after every move. |

---

## **How It Works**

### **Training Process**

1. **Training the Agent**:
   - Two RL agents play against each other for a specified number of epochs.
   - The agents adjust their strategies based on game outcomes (win/loss/tie).
   - The **win rates** are tracked and displayed periodically.

2. **RL Agent vs RL Agent**:
   - After training, the agents compete against each other to evaluate how well they learned to play Tic-Tac-Toe optimally.

3. **Human vs RL Agent**:
   - A human player can compete against the trained RL agent, which continuously adapts to the human's moves.


---

## **File Structure**

| **File**                 | **Description**                                                                 |
|--------------------------|---------------------------------------------------------------------------------|
| `state.py`               | Defines the Tic-Tac-Toe board state, including state representation and game-ending conditions. |
| `player.py`              | Contains the RLPlayer class that uses Temporal-Difference Learning with the ε-greedy strategy. |
| `judge.py`               | Manages the game flow, including turns and win/loss/tie determination. |
| `tic_tac_toe.py`         | The main script to run the training, competition, or human-agent interaction. |

---

## **Training Parameters**

| **Parameter**            | **Description**                                                                            | **Default Value** |
|--------------------------|--------------------------------------------------------------------------------------------|-------------------|
| **Epochs**               | Number of training games played between two RL agents.                                     | 1000 games        |
| **Exploration Rate (ε)** | The exploration rate for the ε-greedy strategy (balance between exploration and exploitation). | 0.1 (10% exploration) |
| **Learning Rate**        | The rate at which the agent updates its policy based on new experiences.                   | 0.5               |
| **Discount Factor (γ)**  | The weight given to future rewards relative to immediate rewards.                          | 0.9               |
