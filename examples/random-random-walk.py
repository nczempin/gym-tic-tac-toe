import gym
import numpy as np
import gym_random_walk

env = gym.make('random_walk-v0')

num_episodes = 20
num_steps_per_episode = 200

collected_rewards = []
for i in range(num_episodes):
    s = env.reset()
    print ("starting new episode")
    env.render()
    print ("started")
    total_reward = 0
    done = False
    for j in range(num_steps_per_episode):
        a = np.random.randint(env.action_space.n)
        s1, reward, done, _ = env.step(a)
        env.render()
        total_reward += reward
        s = s1
        if done:
            break
    collected_rewards.append(total_reward)
    print ("total reward ", total_reward, " after episode: ", j)
print ("average score: ", sum(collected_rewards) / num_episodes)
print("#########")
