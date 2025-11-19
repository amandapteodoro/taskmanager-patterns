from abc import ABC, abstractmethod

class TaskCreator(ABC):

    @abstractmethod
    def create_task(self, name):
        """Factory Method — deve ser sobrescrito nas subclasses."""
        pass

    def execute_task(self, name):
        """Método de alto nível que usa o Factory Method."""
        task = self.create_task(name)
        return task.execute()
