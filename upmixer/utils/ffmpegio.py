import ffmpeg
import numpy as np
from numpy import ndarray

from upmixer.interfaces.audioio import AudioIOInterface


class FFMPEGAudioIO(AudioIOInterface):
    def save_audio(
            self,
            path
    ) -> bool:
        raise NotImplementedError()

    @classmethod
    def load_audio(
            cls,
            path
    ) -> ndarray:
        try:
            probe = ffmpeg.probe(path)
        except ffmpeg._run.Error:
            raise IOError('Audio file is not found or invalid')
        if 'streams' not in probe or len(probe['streams']) == 0:
            raise ValueError('File does not contain any streams')
        try:
            stream = next(stream for stream in probe['streams'] if
                          stream['codec_type'] == 'audio' and stream['channel_layout'] == 'mono')
        except StopIteration:
            raise ValueError('Provided file has no mono audio stream')
        process = (
            ffmpeg
            .input(path)
            .output("pipe:", format='f32le', map=stream['index'])
            .run_async(pipe_stdout=True, pipe_stderr=True)
        )
        data, _ = process.communicate()
        return np.frombuffer(data, dtype="<f4").reshape(-1, 1)
