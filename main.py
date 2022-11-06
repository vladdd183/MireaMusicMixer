# imports for mp3 files
import os
import sys
from pydub import AudioSegment


# mixer class to cut and mix mp3 files
class Mixer:
    # init class with path to mp3 files
    def __init__(self, path):
        self.path = path
        self.files = []
        for file in os.listdir(self.path):
            if file.endswith(".mp3"):
                self.files.append(file)

        self.cuted_files = {}

    # cut mp3 file
    def cut(self, file, start, end):
        song = AudioSegment.from_mp3(self.path + file)
        song = song[start * 1000:end * 1000]
        self.cuted_files[file] = song

    # print list of files
    def print_list(self):
        for idx, file in enumerate(self.files):
            print('===[' + str(idx) + ']', file)

    # mix all cuted files
    def mix(self):
        song = AudioSegment.empty()
        for file in self.cuted_files:
            song += self.cuted_files[file]
        song.export("result.mp3", format="mp3")

    # run function with menu
    def run(self):
        '''method to run menu
        menu:
            1) Choose file
            2) Mix files
            3) Exit
        '''
        while True:
            print('1) Choose file')
            print('2) Mix files')
            print('3) Exit')
            try:
                choice = int(input())
            except ValueError:
                print('Wrong input')
                continue
            if choice == 1:
                self.print_list()
                try:
                    choice = int(input())
                except ValueError:
                    print('Wrong input')
                    continue
                if choice >= len(self.files):
                    print('Wrong input')
                    continue
                file = self.files[choice]
                print('Start time:')
                try:
                    start = int(input())
                except ValueError:
                    print('Wrong input')
                    continue
                print('End time:')
                try:
                    end = int(input())
                except ValueError:
                    print('Wrong input')
                    continue
                self.cut(file, start, end)
            elif choice == 2:
                self.mix()
            elif choice == 3:
                sys.exit(0)
            else:
                print('Wrong input')


if __name__ == '__main__':
    app = Mixer("music/")
    app.run()
