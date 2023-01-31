from abc import ABC, abstractmethod

class framework(ABC):
    @abstractmethod
    def __init__(self, matrix):
        pass

    @abstractmethod
    def find_start(self):
        pass

    @abstractmethod
    def actions(self, state):
        pass

    @abstractmethod
    def result(self, state, action):
        pass

    @abstractmethod
    def goalTest(self, state):
        pass

    @abstractmethod
    def stepCost(self,state,action):
        pass

    @abstractmethod
    def pathCost(self, path, begin, end):
        pass
    