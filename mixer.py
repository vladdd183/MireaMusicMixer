# imports for mp3 files
from pydub import AudioSegment
import os


# mixer class to cut and mix mp3 files
class Mixer:
    # init class with path to mp3 files
    def __init__(self, path):
        self.path = path
        self.cuted_files = {}

    # cut mp3 file
    def cut(self, file, start, end):
        if not os.path.exists(self.path + file):
            return False
        song = AudioSegment.from_mp3(self.path + file)
        song = song[start * 1000:end * 1000]
        self.cuted_files[file] = song
        return file

    # mix all cuted files
    def mix(self):
        song = AudioSegment.empty()

        if len(self.cuted_files) == 0:
            return False

        for file in self.cuted_files:
            song += self.cuted_files[file]
        song.export("result.mp3", format="mp3")

        return True
