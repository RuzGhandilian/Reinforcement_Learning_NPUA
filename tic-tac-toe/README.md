# Tic-Tac-Toe Reinforcement Learning Project

This project is a **Reinforcement Learning (RL)** implementation of the classic Tic-Tac-Toe game. It was developed as part of my university program at **NPUA (National Polytechnic University of Armenia)**. The goal is to train an RL agent to play Tic-Tac-Toe optimally and compete against another RL agent or a human player.

---

## **Features**

- **Reinforcement Learning Player (RLPlayer)**:
  - Uses Temporal-Difference Learning to estimate state values.
  - Explores moves with ε-greedy strategy during training.
  - Saves and loads learned policies for reuse.

- **Human Player**:
  - Allows a human to play against the trained RL agent.

- **Judge**:
  - Manages the game flow between two players (RL vs RL or RL vs Human).

- **State Management**:
  - Represents the Tic-Tac-Toe board and calculates unique hash values for each state.
  - Checks for game-ending conditions (win, lose, or tie).

---

## **How It Works**

1. **Training**:
   - Two RL players train by playing against each other for a specified number of epochs.
   - The win rates are tracked and printed periodically.

2. **Competition**:
   - Two trained RL players compete against each other to evaluate their performance.

3. **Play Mode**:
   - A human can play against the trained RL agent to test its performance.



---

## **How to Run**

1. Clone the repository or download the files:
   - `state.py`
   - `player.py`
   - `judge.py`
   - `tic_tac_toe.py`

2. Run the main script:
   ```bash
   python tic_tac_toe.py
