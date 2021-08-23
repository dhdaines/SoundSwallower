import os

def get_model_path():
    """ Return path to the model. """
    return os.path.join(os.path.dirname(__file__), 'model')
