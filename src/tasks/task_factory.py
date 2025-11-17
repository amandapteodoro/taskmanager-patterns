from src.tasks.email_task import EmailTask
from src.tasks.report_task import ReportTask
from src.tasks.backup_task import BackupTask


class TaskFactory:

    @staticmethod
    def create_task(task_type, name):
        task_type = task_type.lower()

        if task_type == "email":
            return EmailTask(name)
        elif task_type == "relatorio":
            return ReportTask(name)
        elif task_type == "backup":
            return BackupTask(name)
        else:
            raise ValueError("Tipo de tarefa não suportado!")
