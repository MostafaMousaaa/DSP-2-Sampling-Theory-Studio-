# main.py
import numpy as np
from SignalLoaderComposer import SignalLoaderComposer
from SignalSampler import SignalSampler
from SignalVisualizer import SignalVisualizer

def main():
    # Initialize the classes
    loader = SignalLoaderComposer()
    sampler = SignalSampler()
    visualizer = SignalVisualizer()

    # Load or compose a signal
    loader.add_sinusoidal_component(2, 1)
    loader.add_sinusoidal_component(6, 0.5)
    loader.compose_signal()
    loader.add_noise(10)
    signal = loader.signal

    # Sample the signal
    sampling_frequency = 12
    sampler.sample_signal(signal, sampling_frequency)
    sampled_signal = sampler.sampled_signal

    # Recover the signal
    sampler.recover_signal(sampled_signal)
    reconstructed_signal = sampler.reconstructed_signal

    # Visualize the signals
    visualizer.plot_original_signal(signal)
    visualizer.plot_sampled_points(sampled_signal, np.arange(0, len(signal), int(len(signal) / sampling_frequency)))
    visualizer.plot_reconstructed_signal(reconstructed_signal)
    visualizer.plot_difference_signal(signal, reconstructed_signal)
    visualizer.plot_frequency_domain(signal, 1000)

if __name__ == "__main__":
    main()