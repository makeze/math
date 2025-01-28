from scipy.fft import fft, fftfreq
from matplotlib import pyplot as plt
import numpy as np

# Discrete-time signal
N = 50  # Number of samples
n = np.arange(N)
x_n = np.sin(2 * np.pi * 10 * n / N)  + np.sin(2 * np.pi * 15 * n / N) + np.cos(2 * np.pi * 5 * n / N)

# Compute DFT
X_k = fft(x_n)
frequencies = fftfreq(N, 1/N)

# Plotting
plt.figure(figsize=(10, 4))
plt.stem(frequencies[:N//2], np.abs(X_k[:N//2]), use_line_collection=True)
plt.title("Frequency Domain Representation")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()