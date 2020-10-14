from enum import Enum
import copy


class Color(Enum):
    red = "red"
    green = "green"
    blue = "blue"


class Node:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class State:
    def __init__(self, stack, graph):
        self.graph = graph
        self.stack = stack
        self.neighbours = []
        self.value = 20

    def create_neighbours(self):

        i = 0
        while i < 22:
            self.neighbours.append(State(copy.deepcopy(self.stack), self.graph))
            i = i + 1

        temp = 0
        for i in self.stack:
            if i == "blue":
                self.neighbours[temp].stack[int(temp / 2)] = "red"
                self.neighbours[temp + 1].stack[int(temp / 2)] = "green"
            if i == "red":
                self.neighbours[temp].stack[int(temp / 2)] = "blue"
                self.neighbours[temp + 1].stack[int(temp / 2)] = "green"
            if i == "green":
                self.neighbours[temp].stack[int(temp / 2)] = "blue"
                self.neighbours[temp + 1].stack[int(temp / 2)] = "red"
            temp += 2

    def evaluate(self):

        interposition = 0
        i = 0
        for n in self.graph:
            n.color = self.stack[i]
            i += 1

        for node in self.graph:
            for neighbour in self.graph[node]:
                if node.color == neighbour.color:
                    interposition += 1
        self.value = interposition / 2


class Problem2:
    def __init__(self):
        self.graph = Graph().graph
        i = 0
        lst = []

        # initialize default color to red
        while i < 11:
            lst.append("red")
            i += 1
        self.start_state = State(lst, self.graph)


class Graph:

    def __init__(self):

        a = Node("a", "red")
        b = Node("b", "red")
        c = Node("c", "red")
        d = Node("d", "red")
        e = Node("e", "red")
        f = Node("f", "red")
        g = Node("g", "red")
        h = Node("h", "red")
        i = Node("i", "red")
        j = Node("j", "red")
        k = Node("k", "red")

        self.graph = {a: [c, d, i, k],
                      b: [c, f, e, k],
                      c: [a, g, b],
                      d: [g, a, e],
                      e: [d, h, i, b],
                      f: [b, g, i],
                      g: [d, c, f, j, h],
                      h: [e, g, k],
                      i: [f, j, e, a],
                      j: [g, i, k],
                      k: [h, j, a, b]
                      }
