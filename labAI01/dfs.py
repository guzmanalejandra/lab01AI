from framework import framework

class dfs(framework):
    def __init__(self, matrix):
        self.matrix = matrix

        start = self.find_start()
        path = self.DFS(start)
    
        self.path = path

    def find_start(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 2:
                    return (i, j)
        return None

    def actions(self, state):
        x, y = state
        actions = []
        if x > 0 and self.matrix[x-1][y] != 0:
            actions.append("up")
        if x < len(self.matrix)-1 and self.matrix[x+1][y] != 0:
            actions.append("down")
        if y > 0 and self.matrix[x][y-1] != 0:
            actions.append("left")
        if y < len(self.matrix[0])-1 and self.matrix[x][y+1] != 0:
            actions.append("right")
        return actions

    def result(self, state, action):
        x, y = state
        if action == "up":
            return (x-1, y)
        elif action == "down":
            return (x+1, y)
        elif action == "left":
            return (x, y-1)
        elif action == "right":
            return (x, y+1)

    def goalTest(self, state):
        x, y = state
        return self.matrix[x][y] == 3

    def stepCost(self, state=None, action=None):
        return 1 # all steps have the same cost

    def pathCost(self, path, begin=None, end=None):
        return len(path) - 1

    def DFS(self, start):
        stack = [(start, [start])]
        visited = set()
        while stack:
            state, path = stack.pop()
            if self.goalTest(state):
                return path
            if state in visited:
                continue
            visited.add(state)
            for action in self.actions(state):
                new_state = self.result(state, action)
                new_path = path + [new_state]
                stack.append((new_state, new_path))
        return None

