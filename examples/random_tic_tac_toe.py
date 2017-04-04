import gym
import numpy as np
import gym_tic_tac_toe
import random

env = gym.make('tic_tac_toe-v0')

num_episodes = 20
num_steps_per_episode = 200

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
            break
        m = random.choice(moves)
        print ("m: ", m)
        a = env.action_space.sample()
        print (a[0])
        #sm = s['on_move']
        #print (sm)
        a = tuple((om, a[1]))
        s1, reward, done, _ = env.step(m)
        om = -om
        env.render()
        total_reward += reward
        s = s1
        if done:
            break
    collected_rewards.append(total_reward)
    print ("total reward ", total_reward, " after episode: ", j)
print ("average score: ", sum(collected_rewards) / num_episodes)
print("#########")
