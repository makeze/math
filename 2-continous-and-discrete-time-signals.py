import numpy as np
import matplotlib.pyplot as plt

# Define the discrete-time signal
n = np.arange(0, 16)  # Discrete time points from 0 to 15
x_n = np.sin(2 * np.pi * n / 8)  # Signal x[n] = sin(2πn/8)

# Plot the signal
plt.figure(figsize=(10, 4))
plt.stem(n, x_n, label="x[n] = sin(2πn/8)", use_line_collection=True)
plt.title("Discrete-Time Signal")
plt.xlabel("Time (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()

# Period of the signal
period = 8  # From the equation x[n] = sin(2πn/8)
print(f"Period: {period} samples")