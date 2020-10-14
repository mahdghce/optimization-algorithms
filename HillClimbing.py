import gc
from Problem2 import *


def hill_climbing(root):
    cur_state = root
    cur_state.create_neighbours()
    cur_state.evaluate()
    print("initial target: " + str(cur_state.value))
    while True:
        gc.collect()
        next_state = best_neighbour(cur_state)
        cur_state = next_state
        cur_state.create_neighbours()
        print("target: " + str(cur_state.value) + " " + str(cur_state.stack))
        if cur_state.value == 0:
            print(cur_state.stack)
            return


def best_neighbour(state):
    v = state.value
    s = state
    for node in state.neighbours:
        node.evaluate()
        if node.value < v:
            s = node
            v = node.value
    return s


if __name__ == '__main__':
    p = Problem2()
    hill_climbing(p.start_state)
