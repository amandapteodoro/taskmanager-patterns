from src.tasks.task import Task
from src.strategy.email_strategy import EmailStrategy

class EmailTask(Task):
    def __init__(self, name):
        super().__init__(name, EmailStrategy())
