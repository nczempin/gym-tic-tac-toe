# gym-random-walk

A minimal example of a custom environment for https://github.com/openai/gym, based on an example in the recordings of David Silver's lectures on Reinforcement Learning at UCL.

(0) - A - B - C - D - E - (+1)

You start off at one of the positions A to E, you can move right or left, reaching the "+1" terminal state gives you a reward of +1, and going all the way "to the left" will give you a terminal reward of 0.

Instead of calling them the above, I just made them the states 0, 1, ...6.
