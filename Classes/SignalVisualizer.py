import matplotlib.pyplot as plt
import numpy as np

class SignalVisualizer:
    def __init__(self):
        pass

    def plot_original_signal(self, signal):
        plt.figure()
        plt.plot(signal)
        plt.title('Original Signal')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

    def plot_sampled_points(self, sampled_signal, sampling_indices):
        plt.figure()
        plt.stem(sampling_indices, sampled_signal, use_line_collection=True)
        plt.title('Sampled Points')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

    def plot_reconstructed_signal(self, reconstructed_signal):
        plt.figure()
        plt.plot(reconstructed_signal)
        plt.title('Reconstructed Signal')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

    def plot_difference_signal(self, original_signal, reconstructed_signal):
        difference = original_signal - reconstructed_signal
        plt.figure()
        plt.plot(difference)
        plt.title('Difference Signal')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

    def plot_frequency_domain(self, signal, sampling_rate):
        freq_domain = np.fft.fft(signal)
        freq = np.fft.fftfreq(len(signal), d=1/sampling_rate)
        plt.figure()
        plt.plot(freq, np.abs(freq_domain))
        plt.title('Frequency Domain')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')
        plt.grid(True)
        plt.show()

# Example usage
visualizer = SignalVisualizer()
signal = np.sin(2 * np.pi * 2 * np.linspace(0, 1, 1000)) + 0.5 * np.sin(2 * np.pi * 6 * np.linspace(0, 1, 1000))
sampling_indices = np.arange(0, len(signal), int(len(signal) / 12))
sampled_signal = signal[sampling_indices]
reconstructed_signal = signal  # This should be the actual reconstructed signal

visualizer.plot_original_signal(signal)
visualizer.plot_sampled_points(sampled_signal, sampling_indices)
visualizer.plot_reconstructed_signal(reconstructed_signal)
visualizer.plot_difference_signal(signal, reconstructed_signal)
visualizer.plot_frequency_domain(signal, 1000)