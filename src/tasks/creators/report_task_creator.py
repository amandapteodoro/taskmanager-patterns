from src.tasks.creators.task_creator import TaskCreator
from src.tasks.report_task import ReportTask

class ReportTaskCreator(TaskCreator):
    def create_task(self, name):
        return ReportTask(name)
