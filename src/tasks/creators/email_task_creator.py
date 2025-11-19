from src.tasks.creators.task_creator import TaskCreator
from src.tasks.email_task import EmailTask

class EmailTaskCreator(TaskCreator):
    def create_task(self, name):
        return EmailTask(name)
