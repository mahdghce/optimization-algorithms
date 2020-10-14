from math import exp
import gc
from Problem2 import *
from random import *
from os import *


def simulated_annealing(root):
    temp = 10000000
    seed(urandom(100))
    cur_state = root
    chance = False
    cur_state.create_neighbours()
    cur_state.evaluate()
    print("initial target: " + str(cur_state.value))
    while temp > 0:
        gc.collect()
        random_index = randint(0, 21)
        next_state = cur_state.neighbours[random_index]
        next_state.evaluate()
        num = "?"
        if next_state.value < cur_state.value:
            cur_state = next_state
            cur_state.create_neighbours()
            chance = False
        else:
            num = exp(float(-100000 * (cur_state.neighbours[random_index].value - cur_state.value)) / temp)
            random_num = random()
            if random_num <= num:
                next_state = cur_state.neighbours[random_index]
                cur_state = next_state
                cur_state.create_neighbours()
                chance = True
        temp = temp - 1
        print("target: " + str(cur_state.value) + " with the possibility of " + str(num) + " by chance: " + str(chance)
              + " " + str(cur_state.stack))
        if cur_state.value == 0:
            print(cur_state.stack)
            return


if __name__ == '__main__':
    p = Problem2()
    simulated_annealing(p.start_state)
