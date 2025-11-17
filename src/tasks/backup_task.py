from src.tasks.task import Task
from src.strategy.backup_strategy import BackupStrategy

class BackupTask(Task):
    def __init__(self, name):
        super().__init__(name, BackupStrategy())
