from gym.envs.registration import register

register(
    id='tic_tac_toe-v1',
    entry_point='gym_tic_tac_toe.envs:TicTacToeEnv',
)
