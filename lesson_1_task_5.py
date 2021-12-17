"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе. """


class StackClass:
    def __init__(self, max_value):
        self.stack_plates = []
        self.max_value = max_value

    def __str__(self):
        return f"{self.stack_plates}"

    def is_empty(self):
        return self.stacks_plates == [[]]

    def push_in(self, value):
        count_stacks = value // self.max_value
        i = 0
        while i < count_stacks:
            i = i + 1
            self.stack_plates.append([f'№{i}', self.max_value])
        if i == count_stacks and value % self.max_value != 0:
            self.stack_plates.append([f'№{i+1}', value - self.max_value*count_stacks])
        return self.stack_plates

    def pop_out(self):
        return self.stack_plates.pop()

    def get_val(self):
        return self.elems[len(self.stack_plates) - 1]

    def stack_size(self):
        return len(self.stack_plates)


if __name__ == '__main__':

    SC_OBJ = StackClass(12)
    SC_OBJ.push_in(28)
    print(SC_OBJ)

