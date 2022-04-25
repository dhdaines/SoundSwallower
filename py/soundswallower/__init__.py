"""Main module for the SoundSwallower speech recognizer.

SoundSwallower is a small and not particularly powerful speech
recognition engine for constrained grammars.  It can also be used to
align text to audio.  Most of the functionality is contained in the
`Decoder` class.  Basic usage::

  from soundswallower import Decoder, get_model_path
  decoder = soundswallower.Decoder(hmm=get_model_path("en-us"),
                                   dict=get_model_path("en-us.dict"),
                                   jsgf="some_grammar_file.gram")
  hyp, seg = decoder.decode_file("example.wav")
  print("Recognized text:", hyp)
  for word, start, end in seg:
      print("Word %s from %.3f to %.3f" % (word, start, end))

"""
import wave
import os

from ._soundswallower import Config
from ._soundswallower import Decoder
from ._soundswallower import FsgModel
from ._soundswallower import Segment
from ._soundswallower import Hypothesis


def get_model_path(subpath=None):
    """Return path to the model directory, or optionally, a specific file
    or directory within it.

    Args:
        subpath: An optional path to add to the model directory.

    Returns:
        The requested path within the model directory."""
    model_path = os.path.join(os.path.dirname(__file__), 'model')
    if subpath is not None:
        return os.path.join(model_path, subpath)
    else:
        return model_path


def get_audio_data(input_file):
    """Try to get single-channel audio data in the most portable way
    possible.

    Currently suports only single-channel WAV and raw audio.

    Args:
        input_file: Path to an audio file.

    Returns:
        (Raw data as bytes, sample_rate) where `sample_rate` is None
        for a raw file.
    """
    try:
        with wave.open(input_file) as wavfile:
            if wavfile.getnchannels() != 1:
                raise ValueError("Only supporting single-channel WAV")
            data = wavfile.readframes(wavfile.getnframes())
            sample_rate = wavfile.getframerate()
            return data, sample_rate
    except wave.Error:
        with open(input_file, "rb") as rawfile:
            return rawfile.read(), None
