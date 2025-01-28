from scipy.fft import fft, fftfreq
from matplotlib import pyplot as plt
import numpy as np

# Complex exponential signal
t = np.linspace(0, 1, 1000)
x_t = np.exp(1j * 2 * np.pi * 5 * t)  # 5 Hz complex exponential

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(t, np.real(x_t), label="Real Part")
plt.plot(t, np.imag(x_t), label="Imaginary Part")
plt.title("Complex Exponential Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()