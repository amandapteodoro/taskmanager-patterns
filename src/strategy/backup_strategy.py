from src.strategy.execution_strategy import ExecutionStrategy

class BackupStrategy(ExecutionStrategy):
    def run(self, task_name):
        return f"Realizando backup para '{task_name}'"
