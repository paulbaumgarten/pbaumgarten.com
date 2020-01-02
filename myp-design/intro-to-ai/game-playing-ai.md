# Game playing AI


## Summary

## Unit information

Key concept:

Related concepts:

Global context:

Statement of inquiry:

Factual questions:

Conceptual questions:

Debatable questions:

Assessment objectives:
A,D? Research and evaluate

## Lesson overviews

12 lessons as follows:

1. Install tools, understand basic ideas of AI
2. The CartPole problem - with a random agent
3. The CartPole problem - with simple logic
4. Intro to ML theory
5. The CartPole problem - with a neural network
6. The Mountain Car problem - converting continuous to discrete actions
7. Simple game - complete demo
8. Simple game - training
9. Simple game - tweak and retrain
10. Analysis

Play Any OpenAI Gym Environment with a Single Agent - TheComputerScientist (4:21)
https://youtu.be/nvhWfk7R0RM

How Machines Learn - CGP Grey (9m)
https://www.youtube.com/watch?v=R9OHn5ZF4Uo

# 1. Install tools, understand basics of AI

    TO DO

# 2. The CartPole problem - with a random agent

Environment: MountainCarContinuous-v0

Documentation at
https://github.com/openai/gym/wiki/CartPole-v0

Observation: Box 4
 * 0 = Cart position -2.4 to 2.4
 * 1 = Cart velocity -infinity to +infinity
 * 2 = Pole angle -41.8 degrees to +41.8 degrees
 * 3 = Pole velocity at top -infinity to +infinity
Action: Discrete 1
 * 0 = Push left, 1 = Push right


```python
import gym
import random

class Agent():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print(f"Number of actions available: {self.action_size}")

    def get_action(self, state):
        action = random.randint(0, self.action_size-1)
        return action

# Load the game environment
env_name = "CartPole-v1"
env = gym.make(env_name)
# Create our AI player agent (see class code above)
agent = Agent(env)
# Reset the game environment
state = env.reset()
# Play the "game" 200 times
for timestep in range(200):
    # Get a random action from the list available
    action = agent.get_action(state)
    # Apply that action to the environment
    print(f"for round {timestep}, taking action {action}")
    state, reward, done, info = env.step(action)
    env.render()
```

# 3. The CartPole problem - with simple logic

state documentation at https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py

```python
import gym
import random

class Agent():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print(f"Number of actions available: {self.action_size}")

    def get_action(self, state):
        pole_angle = state[2]
        if pole_angle < 0:
            return 0
        else:
            return 1

# Load the game environment
env_name = "CartPole-v1"
env = gym.make(env_name)
# Create our AI player agent (see class code above)
agent = Agent(env)
# Reset the game environment
state = env.reset()
# Play the "game" 200 times
for timestep in range(200):
    # Get a random action from the list available
    action = agent.get_action(state)
    # Apply that action to the environment
    print(f"for round {timestep}, taking action {action}")
    state, reward, done, info = env.step(action)
    env.render()
```

# 4. The Mountain Car problem - Continuous action spaces

## Mountain Car - Discrete

```python
import gym
import random

class Agent():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print(f"Number of actions available: {self.action_size}")

    def get_action(self, state):
        action = random.randint(0, self.action_size-1)
        return action

env_name = "MountainCar-v0"
env = gym.make(env_name)
agent = Agent(env)
state = env.reset()
for timestep in range(200):
    # Get a random action from the list available
    action = agent.get_action(state)
    print(f"for round {timestep}, taking action {action}")
    # Apply that action to the environment
    state, reward, done, info = env.step(action)
    env.render()
```

## Mountain Car - Continuous

Environment: MountainCarContinuous-v0

Documentation at
https://github.com/openai/gym/wiki/MountainCarContinuous-v0

Observation: Box 2
 * 0 = Car position from -1.2 to 0.6
 * 1 = Car velocity from -0.07 to 0.07
Action: Box 1
 * Negative push left, positive push right


```python
import gym
import random
import numpy as np

class Agent():
    def __init__(self, env):
        print("Contineous action space")
        self.low = float(env.action_space.low)
        self.high = float(env.action_space.high)
        self.action_shape = env.action_space.shape
        print(f"Actions range available: from {self.low} to {self.high}")

    def get_action(self, state):
        action = [random.uniform(self.low, self.high)]
        return action

env_name = "MountainCarContinuous-v0"
env = gym.make(env_name)
# agent = Agent(env)
agent = Agent(env)
for episode in range(100):
    state = env.reset()
    done = False
    while not done:
        # Get a random action from the list available
        action = agent.get_action(state)
        print(f"episode {episode}: taking action {action}")
        # Apply that action to the environment
        next_state, reward, done, info = env.step(action) 
        state = next_state
        env.render()
```

# 4. Q Learning

    TO DO

# 5. The CartPole problem - with a neural network


# 7. Simple game - complete demo

# 8. Simple game - training

# 9. Simple game - tweak and retrain

# 10. Analysis


## References

Lesson 1 & 2 derived from 

"Getting Started With OpenAI Gym" by TheComputerScientist, 2018
https://youtu.be/8MC3y7ASoPs

Lesson 3 derived from 

"Play Any OpenAI Gym Environment with a Single Agent" by TheComputerScientist, 2018
https://www.youtube.com/watch?v=nvhWfk7R0RM

Lesson 4 derived from

"Q learning with just numpy | solving the Mountain car | Tutorial" by Machine Learning with Phil, 2019
https://www.youtube.com/watch?v=rBzOyjywtPw
"Youtube-Code-Repository/ReinforcementLearning/mountaincar.py" by philtabor, 2019
https://github.com/philtabor/Youtube-Code-Repository/blob/master/ReinforcementLearning/mountaincar.py


refer to gym-openai-tutorial/demo4-breakout.py. should just need to add discrete action spaces to it.

https://becominghuman.ai/lets-build-an-atari-ai-part-1-dqn-df57e8ff3b26
STC/Resources/Machine Learning/teenslc-intro-to-ai-master.zip

https://machinelearningmastery.com/index-slice-reshape-numpy-arrays-machine-learning-python/

## Thoughts

Or Minimax? Tic-tac-toe, cards, connect 4, battleship, chess

