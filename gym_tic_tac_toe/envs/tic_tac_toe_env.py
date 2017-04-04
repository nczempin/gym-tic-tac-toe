import gym
from gym import spaces
import numpy as np

class TicTacToeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(9)
        self.observation_space = spaces.Discrete(9 * 3) # flattened
    def _step(self, action):
        done = False
        reward = 0

        p, square = action
        
       # p = p*2 - 1
        # check move legality
        board = self.state['board']
        proposed = board[square]
        om = self.state['on_move']
        if (proposed != 0):  # wrong player, not empty
            print("illegal move ", action, ". (square occupied): ", square)
            done = True
            reward = -2 * om  # player who did NOT make the illegal move
        if (p != om):  # wrong player, not empty
            print("illegal move  ", action, " not on move: ", p)
            done = True
            reward = -2 * om  # player who did NOT make the illegal move
        else:
            board[square] = p
            self.state['on_move'] = -p

        # check game over
        for i in range(3):
            # horizontals and verticals
            if ((board[i * 3] == p and board[i * 3 + 1] == p and board[i * 3 + 2 ] == p)
                or (board[i + 0] == p and board[i + 3] == p and board[i + 6] == p)):
                reward = p
                done = True
                break
                
        return np.array(self.state), reward, done, {}
    def _reset(self):
        self.state = {}
        self.state['board'] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.state['on_move'] = 1
        return self.state
    def _render(self, mode='human', close=False):
        if close:
            return
        print("on move: " , self.state['on_move'])
        for i in range (9):
            print (self.state['board'][i], end=" ")
        print()
    def hash_ttt(state):
        #of course this is just for the upper bound;
        #we should really take advantage of the redundancies
        # to reduce the number of states to 765 for the board
        # and who is on move really is implicit in how many
        # squares are occupied
        retval = 0
        low9 = 0
        high9 = 0
        lowmult = 2
        highmult = 1024
        board = state['board']
        if (state['on_move'] == -1):
            retval = 1
        for i in range(9):
            if (board[i] != 0):
                retval += lowmult #todo bitwise logic in python how?
                if (board[i] < 0):
                    retval += highmult
            lowmult *=2
            highmult *= 2
    def move_generator(self):
        moves = []
        for i in range (9):
            
            if (self.state['board'][i] == 0):
                p = self.state['on_move']
                m = [p, i]
                moves.append(m)
        return moves
                
