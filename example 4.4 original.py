import numpy as np
import matplotlib.pyplot as plt

# Time settings
fs = 200000        # high sampling rate to model analog signal
duration = 0.01    # 10 ms
t = np.arange(0, duration, 1/fs)

# Original analog signal xa(t)
xa = 3*np.cos(2000*np.pi*t) + 5*np.sin(6000*np.pi*t) + 10*np.cos(12000*np.pi*t)

# Plot
plt.figure(figsize=(10,4))
plt.plot(t, xa)
plt.title("Original Signal: xa(t) = 3cos(2000πt) + 5sin(6000πt) + 10cos(12000πt)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
