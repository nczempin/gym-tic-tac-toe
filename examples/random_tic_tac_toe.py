import gym
import numpy as np
import gym_tic_tac_toe
import random


def random_plus_middle_move(moves, p):
    if ([p, 4] in moves):
        m = [p, 4]
    else:
        m = random_move(moves, p)
    return m
def random_move(moves, p):
    m = random.choice(moves)
    return m

env = gym.make('tic_tac_toe-v0')

num_episodes = 2000
num_steps_per_episode = 10

collected_rewards = []
for i in range(num_episodes):
    s = env.reset()
    print (s)
    print ("starting new episode")
    env.render()
    print ("started")
    total_reward = 0
    done = False
    om = 1
    for j in range(num_steps_per_episode):
        moves = env.move_generator()
        print ("moves: ", moves)
        if (not moves):
            print ("out of moves")
            break
        if (len(moves)==1):
            m = moves[0]
        else:
            if (om == 1):
                m = random_plus_middle_move(moves, om)
            else:
                m = random_move(moves, om)
        print ("m: ", m)
#         a = env.action_space.sample()
#         print (a[0])
#         #sm = s['on_move']
#         #print (sm)
#         a = tuple((om, a[1]))
        s1, reward, done, _ = env.step(m)
        om = -om
        env.render()
        total_reward += reward
        s = s1
        if done:
            print ("game over: ", reward)
            break
    collected_rewards.append(total_reward)
    print ("total reward ", total_reward, " after episode: ", i, ". steps: ", j+1)
print ("average score: ", sum(collected_rewards) / num_episodes)
print("#########")
