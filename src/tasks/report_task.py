from src.tasks.task import Task
from src.strategy.report_strategy import ReportStrategy

class ReportTask(Task):
    def __init__(self, name):
        super().__init__(name, ReportStrategy())
