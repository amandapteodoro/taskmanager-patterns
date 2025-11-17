from src.tasks.task_factory import TaskFactory
from src.storage.storage_singleton import StorageSingleton
from src.observer.logger_observer import LoggerObserver


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
            tipo = input("Tipo da tarefa: (email/relatorio/backup): ")
            nome = input("Detalhamento: ")
            print("\nTarefa criada com êxito!")

            task = TaskFactory.create_task(tipo, nome)
            task.attach(logger)
            storage.add_task(task)

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
