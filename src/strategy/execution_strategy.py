from abc import ABC, abstractmethod

class ExecutionStrategy(ABC):

    @abstractmethod
    def run(self, task_name):
        pass
