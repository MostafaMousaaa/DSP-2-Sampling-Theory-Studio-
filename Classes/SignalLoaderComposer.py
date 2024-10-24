import numpy as np

class SignalLoaderComposer:
    def __init__(self):
        self.signal = None
        self.components = []

    def load_signal_from_file(self, file_path):
        # Load signal from file
        self.signal = np.loadtxt(file_path)

    def compose_signal(self):
        # Compose signal from components
        self.signal = sum(self.components)

    def add_sinusoidal_component(self, frequency, magnitude):
        # Add sinusoidal component
        t = np.linspace(0, 1, 1000)
        component = magnitude * np.sin(2 * np.pi * frequency * t)
        self.components.append(component)

    def remove_sinusoidal_component(self, index):
        # Remove sinusoidal component
        if 0 <= index < len(self.components):
            self.components.pop(index)

    def add_noise(self, snr):
        # Add noise to the signal
        noise = np.random.normal(0, np.std(self.signal) / snr, self.signal.shape)
        self.signal += noise

# Example usage
loader = SignalLoaderComposer()
loader.add_sinusoidal_component(2, 1)
loader.add_sinusoidal_component(6, 0.5)
loader.compose_signal()
loader.add_noise(10)