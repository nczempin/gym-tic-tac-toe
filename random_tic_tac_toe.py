import math
import random
import gym_tic_tac_toe

import gym


def random_plus_middle_move(moves, p):
    if ([p, 4] in moves):
        m = [p, 4]
    else:
        m = random_move(moves, p)
    return m


def random_move(moves, p):
    m = random.choice(moves)
    return m


env = gym.make('tic_tac_toe-v1')

p1 = 0.48
p2 = 0.55
alpha = 0.01
beta = 0.01
# theta = math.log((p1*(1-p0)) / (p0*(1-p1)));

h1 = math.log((1 - alpha) / beta) / (math.log(p2 / p1) + math.log((1 - p1) / (1 - p2)))
h2 = math.log((1 - beta) / alpha) / (math.log(p2 / p1) + math.log((1 - p1) / (1 - p2)))
ss = math.log((1 - p1) / (1 - p2)) / (math.log(p2 / p1) + math.log((1 - p1) / (1 - p2)))
print("ss:", ss)
print("h1:", h1)
print("h2:", h2)

num_episodes = 300
num_steps_per_episode = 10

collected_rewards = []
oom = 1
for i in range(num_episodes):
    s = env.reset()
    # print (s)
    # print ("starting new episode")
    # env.render()
    # print ("started")
    total_reward = 0
    done = False
    om = oom;
    # run one episode
    # print("starting player: ", om);

    for j in range(num_steps_per_episode):
        moves = env.move_generator()
        # print ("moves: ", moves)
        if (not moves):
            # print ("out of moves")
            break
        if (len(moves) == 1):
            # only a single possible move
            m = moves[0]
        else:
            if (om == 1):
                m = random_plus_middle_move(moves, om)
                 #m = random_move(moves, om)
            else:
                m = random_move(moves, om)
        # print ("m: ", m)
        s1, reward, done, _ = env.step(m)
        om = -om
        # env.render()
        total_reward += reward
        s = s1
        if done:
            # print ("game over: ", reward)
            break
    # env.render()
    total_reward *= oom;
    collected_rewards.append(total_reward)
    # print ("total reward", total_reward, "after episode: ", i+1, ". steps: ", j+1)
    oom = -oom

    print("after " + str(i + 1) + " episodes:")
    
    average = sum(collected_rewards) / num_episodes
    percentage = round(100*(average + 1) / 2, 1)
    score = percentage/100 * (i+1);
    print("average score: ", average)
    print("percentage: ", percentage)
    print("score:", score)
    print()
    y1 = ss * (i+1) - h1
    print ("y1:", y1)
    y2 = ss * (i+1) + h2
    print ("y2:", y2)
    if (score <= y1):
        print("accept null hypothesis")
        break
    if (score >= y2):
        print("reject null hypothesis")
        break
print("#########")
