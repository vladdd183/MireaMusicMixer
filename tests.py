import unittest
from mixer import Mixer


class TestMixer(unittest.TestCase):
    def test_cut(self):
        mixer = Mixer('music/')
        file = mixer.cut('test.mp3', 0, 10)
        self.assertEqual(file, 'test.mp3')

    def test_mix(self):
        mixer = Mixer('music/')
        mixer.cut('test.mp3', 0, 10)
        mixer.cut('test.mp3', 10, 20)
        self.assertEqual(mixer.mix(), True)

    def test_cut_file_not_exists(self):
        mixer = Mixer('music/')
        file = mixer.cut('test3.mp3', 0, 10)
        self.assertEqual(file, False)


if __name__ == '__main__':
    unittest.main()
