from abc import ABC, abstractmethod


class RewardFunction(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def get_reward(self, state):
        raise NotImplementedError

    @abstractmethod
    def get_final_reward(self, state):
        raise NotImplementedError