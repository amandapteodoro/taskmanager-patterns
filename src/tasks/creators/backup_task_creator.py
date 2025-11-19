from src.tasks.creators.task_creator import TaskCreator
from src.tasks.backup_task import BackupTask

class BackupTaskCreator(TaskCreator):
    def create_task(self, name):
        return BackupTask(name)
