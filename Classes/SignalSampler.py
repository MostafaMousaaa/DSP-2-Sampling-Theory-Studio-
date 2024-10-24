import numpy as np

class SignalSampler:
    def __init__(self):
        self.sampled_signal = None
        self.reconstructed_signal = None
        self.sampling_frequency = None
        self.reconstruction_method = 'whittaker_shannon'

    def sample_signal(self, signal, sampling_frequency):
        # Sample the signal
        self.sampling_frequency = sampling_frequency
        sample_indices = np.arange(0, len(signal), int(len(signal) / sampling_frequency))
        self.sampled_signal = signal[sample_indices]

    def recover_signal(self, signal, method='whittaker_shannon'):
        # Recover the signal using the specified method
        self.reconstruction_method = method
        if method == 'whittaker_shannon':
            self.reconstructed_signal = self.whittaker_shannon_interpolation(signal)
        else:
            # Implement other methods if needed
            pass

    def whittaker_shannon_interpolation(self, signal):
        # Implement Whittaker-Shannon interpolation
        t = np.arange(len(signal))
        T = 1 / self.sampling_frequency
        sinc_matrix = np.sinc(t[:, None] - t[None, :] / T)
        return np.dot(sinc_matrix, signal)

    def set_sampling_frequency(self, frequency):
        self.sampling_frequency = frequency

    def choose_reconstruction_method(self, method):
        self.reconstruction_method = method

# Example usage
sampler = SignalSampler()
signal = np.sin(2 * np.pi * 2 * np.linspace(0, 1, 1000)) + 0.5 * np.sin(2 * np.pi * 6 * np.linspace(0, 1, 1000))
sampler.sample_signal(signal, 12)
sampler.recover_signal(sampler.sampled_signal)