import numpy as np
import matplotlib.pyplot as plt
from SignalLoaderComposer import SignalLoaderComposer
from SignalSampler import SignalSampler
from SignalVisualizer import SignalVisualizer

# Example usage
loader = SignalLoaderComposer()
loader.add_sinusoidal_component(2, 1)
loader.add_sinusoidal_component(2, 0.5)
loader.compose_signal()

sampler = SignalSampler()
sampler.sample_signal(loader.signal, 6)
sampler.recover_signal()

visualizer = SignalVisualizer()
visualizer.plot_original_signal(loader.signal)
visualizer.plot_sampled_points(sampler.sampled_signal)
visualizer.plot_reconstructed_signal(sampler.reconstructed_signal)
visualizer.plot_difference_signal(loader.signal, sampler.reconstructed_signal)
visualizer.plot_frequency_domain(loader.signal)