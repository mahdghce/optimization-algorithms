import gc
from Problem2 import *
from random import *


def stochastic_hill_climbing(root):
    cur_n = root
    cur_n.create_neighbours()
    cur_n.evaluate()
    print("initial target: " + str(cur_n.value))
    while True:
        gc.collect()
        nex_n = best_neighbour(cur_n)
        cur_n = nex_n
        cur_n.create_neighbours()
        print("target: " + str(cur_n.value) + " " + str(cur_n.stack))
        if cur_n.value == 0:
            print(cur_n.stack)
            return


def best_neighbour(state):
    temp = []
    v = state.value
    s = state
    for node in state.neighbours:
        node.evaluate()
        if node.value < v:
            temp.append(node)
    if temp.__len__() >= 2:
        return temp.pop(randint(0, temp.__len__() - 1))
    elif temp.__len__() == 1:
        return temp.pop()
    else:
        return s


if __name__ == '__main__':
    p = Problem2()
    stochastic_hill_climbing(p.start_state)
