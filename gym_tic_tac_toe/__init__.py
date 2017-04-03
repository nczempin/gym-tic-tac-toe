from gym.envs.registration import register

register(
    id='tic_tac_toe-v0',
    entry_point='gym_tic_tac_toe.envs:TicTacToeEnv',
)
