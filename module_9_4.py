from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'
func = lambda x, y: x == y
print(list(map(func, first, second)))

def get_advanced_writer(file_name):

    def write_everythihg(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
              for w in data_set:
                  file.write(str(w))
                  file.write('\n')
    return write_everythihg

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())