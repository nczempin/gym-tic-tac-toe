import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class RandomWalkEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.action_space = spaces.Discrete(2)
    #print("init")
  def _step(self, action):
    #print("step")
    reward = 0
    done = False
    if (action == 0):
       self.state -= 1
    if (action == 1):
        self.state += 1
    if (self.state >= 6):
        reward = 1
        done = True
    if (self.state <= 0):
        done = True
    return np.array(self.state), reward, done, {}
  def _reset(self):
    #print("reset")
    self.state = 1 # TODO start in a random position
  def _render(self, mode='human', close=False):
    #print("render")
    print(self.state)
