"""
PocketSphinx compatibility Decoder class.
"""

DEFAULT_CONFIG = {
}


class Decoder:
    def __init__(self, *args, **kwargs):
        pass

    def default_config():
        return DEFAULT_CONFIG.copy()

    def start_utt(self):
        pass

    def process_raw(self, data, no_search=False, full_utt=False):
        pass

    def end_utt(self):
        pass

    def get_prob(self):
        pass

    def add_word(self, word, phones, update=True):
        pass

    def load_dict(self, dictfile, fdictfile=None, format=None):
        pass

    def save_dict(self, dictfile, format=None):
        pass

    def hyp(self):
        pass

    def seg(self):
        pass

    def get_in_speech(self):
        pass
