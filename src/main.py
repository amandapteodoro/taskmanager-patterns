from src.storage.storage_singleton import StorageSingleton
from src.observer.logger_observer import LoggerObserver
from src.tasks.creators.email_task_creator import EmailTaskCreator
from src.tasks.creators.report_task_creator import ReportTaskCreator
from src.tasks.creators.backup_task_creator import BackupTaskCreator


def get_creator(task_type: str):
    """
    Retorna o ConcreteCreator correto com base no tipo da tarefa.
    """
    task_type = task_type.lower()

    if task_type == "email":
        return EmailTaskCreator()
    elif task_type == "relatorio":
        return ReportTaskCreator()
    elif task_type == "backup":
        return BackupTaskCreator()
    else:
        raise ValueError("Tipo de tarefa não suportado!")


def main():
    print("\n === BEM-VINDO AO TASKMANAGER ===")

    storage = StorageSingleton()
    logger = LoggerObserver()

    while True:
        print("\nEscolha uma das opções abaixo: (digite apenas o número)")
        print("1. Criar tarefa")
        print("2. Executar tarefas")
        print("3. Listar tarefas")
        print("0. Sair")

        op = input("Opção: ")
        print("\n")

        if op == "1":
            print("CRIAÇÃO DE NOVA TAREFA")
            tipo = input("Tipo da tarefa: (email/relatorio/backup): ").strip().lower()
            nome = input("Detalhamento: ").strip()

            try:
                creator = get_creator(tipo)
                task = creator.create_task(nome)

                task.attach(logger)      # Observer
                storage.add_task(task)   # Singleton

                print("\nTarefa criada com êxito!")

            except ValueError as e:
                print(f"Erro: {e}")

        elif op == "2":
            print("EXECUTANDO TODAS AS TAREFAS...")
            for t in storage.list_tasks():
                t.execute()
            print("Todas as tarefas foram executadas!")

        elif op == "3":
            print("LISTA DE TAREFAS EXISTENTES")
            for idx, t in enumerate(storage.list_tasks()):
                print(f"{idx+1}. {t.name}")

        elif op == "0":
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
