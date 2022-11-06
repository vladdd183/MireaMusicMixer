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
