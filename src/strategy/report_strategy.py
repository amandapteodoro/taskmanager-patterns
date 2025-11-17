from src.strategy.execution_strategy import ExecutionStrategy

class ReportStrategy(ExecutionStrategy):
    def run(self, task_name):
        return f"Gerando relatório da tarefa '{task_name}'"
