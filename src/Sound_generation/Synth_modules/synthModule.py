class SynthModule:
    def __init__(self, name):
        self.name = name

    def process(self, input_signal=None):
        raise NotImplementedError("Must be implemented by subclass.")

    def add(self, module):
        pass

    def remove(self, module):
        pass

    def get_child(self, index):
        pass