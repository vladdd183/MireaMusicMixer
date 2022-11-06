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
