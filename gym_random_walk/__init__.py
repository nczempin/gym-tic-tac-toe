from gym.envs.registration import register

register(
    id='random_walk-v0',
    entry_point='gym_random_walk.envs:RandomWalkEnv',
)
#register(
#    id='foo-extrahard-v0',
#    entry_point='gym_foo.envs:FooExtraHardEnv',
#)
