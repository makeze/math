import numpy as np
import matplotlib.pyplot as plt

# Define the continuous-time signal
t = np.linspace(0, 2, 1000)  # Time vector from 0 to 2 seconds
x_t = np.sin(2 * np.pi * t)  # Signal x(t) = sin(2πt)

# Plot the signal
plt.figure(figsize=(10, 4))
plt.plot(t, x_t, label="x(t) = sin(2πt)")
plt.title("Continuous-Time Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()

# Amplitude and frequency
amplitude = np.max(x_t)
frequency = 1  # From the equation x(t) = sin(2π * 1 * t)
print(f"Amplitude: {amplitude}")
print(f"Frequency: {frequency} Hz")