import gc
from Problem2 import *
from random import *
from os import *


def hill_climbing(root):
    cur_n = root
    cur_n.create_neighbours()
    cur_n.evaluate()
    print("initial target: " + str(cur_n.value))
    while True:
        gc.collect()
        next_n = best_neighbour(cur_n)
        cur_n = next_n
        cur_n.create_neighbours()
        print("target:" + str(cur_n.value) + " " + str(cur_n.stack))
        if cur_n.value == 0:
            print(cur_n.stack)
            return


def best_neighbour(state):
    v = state.value
    s = state
    for node in state.neighbours:
        node.evaluate()
        if node.value < v:
            s = node
            v = node.value
    if s != state:
        return s
    else:
        return random_start(state)


def random_start(state):
    temp = []
    seed(urandom(100))
    i = 0
    while i < 11:
        n = randint(0, 2)
        if n == 0:
            temp.append("blue")
        elif n == 1:
            temp.append("red")
        else:
            temp.append("green")
        i += 1
    s = State(temp, state.graph)
    s.evaluate()
    return s


if __name__ == '__main__':
    p = Problem2()
    hill_climbing(p.start_state)
