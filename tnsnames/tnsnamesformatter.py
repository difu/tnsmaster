from tnsnames.tnsnamesListener import TnsnamesListener


# Base class for all format classes
class TnsnamesFormatter(TnsnamesListener):
    def __init__(self):
        self._lines = []

    @property
    def get_lines(self):
        return self._lines
