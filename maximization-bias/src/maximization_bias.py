import numpy as np

# region Hyper-parameters

# States
states = dict(A = 0, B = 1, terminal = 2)

# Start state
start = states['A']

# Possible actions from state A
actions_A = dict(right = 0, left = 1)

# Possible actions from state B (e.g., 10 actions (will affect the curves))
actions_B = range(0, 10)

# All possible actions
actions = [[actions_A["right"], actions_A["left"]], actions_B]

# State-action pair values. The value of a terminal state is always 0
state_action_values = [np.zeros(2), np.zeros(len(actions_B)), np.zeros(1)]

# Destination for each state and each action
transition = [[states["terminal"], states['B']], [states["terminal"]] * len(actions_B)]

# Exploration probability (denoted as 𝜀)
exploration_probability = 0.1

# Step-size parameter (denoted as 𝛼)
step_size = 0.1

# Discount rate for max value (denoted as 𝛾)
discount = 1.0

# endregion Hyper-parameters

# region Functions

def choose_action(action_value_estimates, state):
    # region Summary
    """
    Chooses an action based on 𝜀-greedy algorithm
    :param action_value_estimates: Action-value estimates (denoted as 𝑄(𝑆_𝑡, 𝐴_𝑡))
    :param state: State
    :return: Action
    """
    # endregion Summary

    # region Body

    # ε-greedy action selection: every once in a while, with small probability ε, select randomly from among all the actions with equal probability, independently of the action-value estimates.
    if np.random.binomial(n=1, p=exploration_probability) == 1:
        action = np.random.choice(actions[state])

    # Greedy action selection: select one of the actions with the highest estimated value, that is, one of the greedy actions.
    # If there is more than one greedy action, then a selection is made among them in some arbitrary way, perhaps randomly.
    else:
        values = action_value_estimates[state]
        action = np.random.choice([act for act, val in enumerate(values) if val == np.max(values)])

    return action

    # endregion Body

def take_action(state, action):
    # region Summary
    """
    Takes an action in state and gets reward
    :param state: State
    :param action: Action
    :return: Reward
    """
    # endregion Summary

    # region Body

    # The reward from state A is 0 regardless of the action
    if state == states['A']:
        return 0

    # The reward from state B is drawn from a normal distribution with 𝜇 = -0.1 mean and 𝜎 = 1.0 variance for all possible actions
    return np.random.normal(-0.1, 1)

    # endregion Body

def q_learning(first_action_value_estimates, second_action_value_estimates = None):
    # region Summary
    """
    Counts the number of "left" action for Q-learning or Double Q-learning
    :param first_action_value_estimates: 1st action-value estimates (denoted as 𝑄_1(𝑎))
    :param second_action_value_estimates: 2nd action-value estimates (denoted as 𝑄_2(𝑎)). If not None, then this function is Double Q-learning; otherwise, it is classic Q-learning
    :return: Number of "left" action in state A
    """
    # endregion Summary

    # region Body

    # Initialize state at the start


    # Track the number of action "left" in state A


    # Keep going until getting to the terminal state

        # choose an action for classic Q-learning


        # choose an action for Double Q-learning

            # for example, an 𝜀-greedy policy for Double Q-learning could be based on the average (or sum) of the 2 action-value estimates


        # check if agent chose "left" action in state A


        # get the reward


        # get the next state


        # for classic Q-learning

            # set action-value estimate to update


            # set target


        # for Double Q-learning, divide the time steps in 2, perhaps by flipping a coin on each step

            # if the coin comes up heads

                # set the estimate to update to 𝑄_1


                # set the target estimate to 𝑄_2


            # if the coin comes up tails, then the same update is done with 𝑄_1 and 𝑄_2 switched, so that 𝑄_2 is updated

                # set the estimate to update to 𝑄_2


                # set the target estimate to 𝑄_1


            # get the best action


            # get the target


        # Q-learning update (Equation (6.8))


        # move to the next state




    # endregion Body

# endregion Functions