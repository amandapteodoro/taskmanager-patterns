from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)

    def execute(self):
        result = self.strategy.run(self.name)
        self.notify(f"Tarefa '{self.name}' executada: {result}")
        return result
