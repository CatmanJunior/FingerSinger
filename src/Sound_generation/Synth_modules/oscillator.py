from .synthModule import SynthModule
from ..generate_wavetable import generate_sine_wave

class Oscillator(SynthModule):
    def __init__(self, name, frequency, waveform="sine"):
        super().__init__(name)
        self.frequency = frequency
        self.waveform = waveform

    
    def process(self, input_signal):
        if self.waveform == "sine":
            return generate_sine_wave(self.frequency, 1)
        else:
            raise NotImplementedError("Waveform not implemented yet.")