
from Synth_modules.synthModule import SynthModule

class ModuleChain(SynthModule):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, module):
        self.children.append(module)

    def remove(self, module):
        self.children.remove(module)

    def get_child(self, index):
        return self.children[index]

    def process(self, input_signal=None):
        # Process signal sequentially through child modules
        current_signal = input_signal
        for child in self.children:
            current_signal = child.process(current_signal)
        return current_signal