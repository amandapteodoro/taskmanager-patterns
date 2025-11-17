class StorageSingleton:
    _instance = None
    _tasks = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StorageSingleton, cls).__new__(cls)
        return cls._instance

    def add_task(self, task):
        self._tasks.append(task)

    def list_tasks(self):
        return self._tasks
