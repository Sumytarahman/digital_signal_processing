import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# (1) Create the "analog" signal
# -------------------------------
fs_analog = 200000     # very high rate to simulate analog
duration = 0.01        # 10 ms
t_analog = np.arange(0, duration, 1/fs_analog)

xa = (3*np.cos(2000*np.pi*t_analog)
      + 5*np.sin(6000*np.pi*t_analog)
      + 10*np.cos(12000*np.pi*t_analog))


# -------------------------------
# (2) Proper Sampling
# -------------------------------
fs_sample = 20000      # >= 12000 Hz (Nyquist)
Ts = 1/fs_sample
n = np.arange(0, duration, Ts)

xs = (3*np.cos(2000*np.pi*n)
      + 5*np.sin(6000*np.pi*n)
      + 10*np.cos(12000*np.pi*n))


# -------------------------------
# (3) Plot analog vs sampled
# -------------------------------
plt.figure(figsize=(10,5))

# Analog signal
plt.plot(t_analog, xa, label='Analog-like signal (xa)', linewidth=1)

# Sampled signal (fixed)
plt.stem(n, xs, linefmt='r-', markerfmt='ro', basefmt=" ", label='Sampled signal (xs)')

plt.title("Proper Sampling of xa(t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
