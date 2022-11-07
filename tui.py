from mixer import Mixer
import os


class Tui:
    def __init__(self, path):
        self.files = []
        self.path = path

        for file in os.listdir(self.path):
            if file.endswith(".mp3"):
                self.files.append(file)

        self.mixer = Mixer(path)
        self.menu = {
            '1': self.add,
            '2': self.mixer.mix,
            '3': exit
        }

    def show_menu(self):
        print('''
        1. Добавить трек
        2. Смешать треки
        3. Выход
        ''')

    def add(self):
        print('Выберите трек')
        self.printListFiles()
        choice = int(input('Выберите трек: '))
        file = self.files[choice]
        start = int(input('Введите начало трека: '))
        end = int(input('Введите конец трека: '))
        self.mixer.cut(file, start, end)
        print('Трек добавлен')

    def printListFiles(self):
        for idx, file in enumerate(self.files):
            print('===[' + str(idx) + ']', file)

    def run(self):
        while True:
            self.show_menu()
            choice = input('Выберите пункт меню: ')
            action = self.menu.get(choice)
            if action:
                action()
            else:
                print('Неверный пункт меню')


if __name__ == '__main__':
    tui = Tui('music/')
    tui.run()
