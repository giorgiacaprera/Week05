class Model():
    def __init__(self):
        self._currentVal = 0

    @property
    def currentVal(self):
        return self._currentVal

    @currentVal.setter
    def currentVal(self, value):
        self._currentVal = value
