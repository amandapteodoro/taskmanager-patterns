from src.strategy.execution_strategy import ExecutionStrategy

class EmailStrategy(ExecutionStrategy):
    def run(self, task_name):
        return f"Enviando email para tarefa '{task_name}'"
