import unittest

from upmixer.utils.ffmpegio import FFMPEGAudioIO


class FFMPEGAudioIOTest(unittest.TestCase):
    def test_load_audio_invalid_path(self):
        with self.assertRaises(IOError) as err:
            FFMPEGAudioIO.load_audio('assets/inv.path')
        self.assertTrue(str(err.exception) == 'Audio file is not found or invalid')

    def test_load_audio_not_mono(self):
        with self.assertRaises(ValueError) as err:
            FFMPEGAudioIO.load_audio('assets/test_wave_stereo.mp3')
        self.assertTrue(str(err.exception) == "Provided file has no mono audio stream")

    def test_load_audio_not_audio_file(self):
        with self.assertRaises(ValueError) as err:
            FFMPEGAudioIO.load_audio('assets/test_video.mp4')
        self.assertTrue(str(err.exception) == "Provided file has no mono audio stream")

    def test_load_audio(self):
        self.assertTrue(FFMPEGAudioIO.load_audio('assets/test_wave.mp3').size > 0)


if __name__ == '__main__':
    unittest.main()
