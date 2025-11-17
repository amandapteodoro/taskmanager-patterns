from src.observer.observer import Observer

class LoggerObserver(Observer):

    def update(self, message):
        print(f"[LOG] {message}")
