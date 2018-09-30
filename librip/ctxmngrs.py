import time


# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно
class timer:
    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.clock() - self.start)

