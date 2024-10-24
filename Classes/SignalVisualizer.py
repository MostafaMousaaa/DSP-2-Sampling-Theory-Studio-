import numpy as np
import matplotlib.pyplot as plt
class SignalVisualizer:
    def __init__(self):
        pass

    def plot_original_signal(self, signal):
        plt.figure()
        plt.plot(signal)
        plt.title('Original Signal')
        plt.show()

    def plot_sampled_points(self, sampled_signal):
        plt.figure()
        plt.stem(sampled_signal)
        plt.title('Sampled Points')
        plt.show()

    def plot_reconstructed_signal(self, reconstructed_signal):
        plt.figure()
        plt.plot(reconstructed_signal)
        plt.title('Reconstructed Signal')
        plt.show()

    def plot_difference_signal(self, original_signal, reconstructed_signal):
        difference = original_signal - reconstructed_signal
        plt.figure()
        plt.plot(difference)
        plt.title('Difference Signal')
        plt.show()

    def plot_frequency_domain(self, signal):
        freq_domain = np.fft.fft(signal)
        plt.figure()
        plt.plot(np.abs(freq_domain))
        plt.title('Frequency Domain')
        plt.show()
