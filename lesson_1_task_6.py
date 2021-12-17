"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!"""


class QueueClass:
    def __init__(self):
        self.base_tasks = []
        self.done = []
        self.for_revision = []

    def is_empty(self):
        return self.base_tasks == []

    def to_queue(self, item):
        self.base_tasks.insert(0, item)

    def from_queue(self):
        return self.base_tasks.pop()

    def to_done(self):
        self.done.insert(0, self.base_tasks.pop())

    def to_revision(self):
        self.for_revision.insert(0, self.base_tasks.pop())

    def from_revision_to_base(self):
        self.base_tasks.insert(0, self.for_revision.pop())

    def size(self):
        return len(self.base_tasks)


if __name__ == '__main__':
    SC_OBJ = QueueClass()
    SC_OBJ.to_queue('Чертеж 1 сдать')
    SC_OBJ.to_queue('Иправить чертеж 2')
    SC_OBJ.to_queue('Чертеж 3 исправлен')
    print(SC_OBJ.base_tasks)
    SC_OBJ.to_done()
    print(SC_OBJ.done)
    SC_OBJ.to_revision()
    print(SC_OBJ.base_tasks)
    print(SC_OBJ.for_revision)
    SC_OBJ.from_revision_to_base()
    print(SC_OBJ.for_revision)
    print(SC_OBJ.base_tasks)
