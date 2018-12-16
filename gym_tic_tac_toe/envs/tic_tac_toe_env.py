import gym
from gym import spaces
import numpy as np

class TicTacToeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    symbols = ['O', ' ', 'X'];

    def __init__(self):
        self.action_space = spaces.Discrete(9)
        self.observation_space = spaces.Discrete(9*3*2) # flattened
    def step(self, action):
        done = False
        reward = 0

        p, square = action
        
        # check move legality
        board = self.state['board']
        proposed = board[square]
        om = self.state['on_move']
        if (proposed != 0):  # wrong player, not empty
            print("illegal move ", action, ". (square occupied): ", square)
            done = True
            reward = -1 * om  # player who did NOT make the illegal move
        if (p != om):  # wrong player, not empty
            print("illegal move  ", action, " not on move: ", p)
            done = True
            reward = -1 * om  # player who did NOT make the illegal move
        else:
            board[square] = p
            self.state['on_move'] = -p

        # check game over
        for i in range(3):
            # horizontals and verticals
            if ((board[i * 3] == p and board[i * 3 + 1] == p and board[i * 3 + 2] == p)
                or (board[i + 0] == p and board[i + 3] == p and board[i + 6] == p)):
                reward = p
                done = True
                break
        # diagonals
        if((board[0] == p and board[4] == p and board[8] == p)
            or (board[2] == p and board[4] == p and board[6] == p)):
                reward = p
                done = True
                
        return self.state, reward, done, {}
    def reset(self):
        self.state = {}
        self.state['board'] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.state['on_move'] = 1
        return self.state
    def render(self, mode='human', close=False):
        if close:
            return
        print("on move: " , self.symbols[self.state['on_move']+1])
        for i in range (9):
            print (self.symbols[self.state['board'][i]+1], end=" ");
            if ((i % 3) == 2):
                print();
    def move_generator(self):
        moves = []
        for i in range (9):
            if (self.state['board'][i] == 0):
                p = self.state['on_move']
                m = [p, i]
                moves.append(m)
        return moves
                
