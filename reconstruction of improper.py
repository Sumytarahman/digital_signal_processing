import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# (1) Create analog-like signal
# -----------------------------------
fs_analog = 200000
duration = 0.01
t = np.arange(0, duration, 1/fs_analog)

xa = (3*np.cos(2000*np.pi*t)
      + 5*np.sin(6000*np.pi*t)
      + 10*np.cos(12000*np.pi*t))


# -----------------------------------
# (2) Improper Sampling (fs = 8 kHz)
# -----------------------------------
fs = 8000      # BELOW Nyquist → aliasing
Ts = 1/fs
n = np.arange(0, duration, Ts)

xs = (3*np.cos(2000*np.pi*n)
      + 5*np.sin(6000*np.pi*n)
      + 10*np.cos(12000*np.pi*n))


# -----------------------------------
# (3) Ideal Sinc Reconstruction
# -----------------------------------
def sinc_reconstruct(xn, n, Ts, t):
    return np.sum(xn[:, None] * np.sinc((t - n[:, None]) / Ts), axis=0)

xr = sinc_reconstruct(xs, n, Ts, t)


# -----------------------------------
# (4) Plot
# -----------------------------------
plt.figure(figsize=(10,6))

plt.plot(t, xa, label='Original xa(t)', linewidth=1, alpha=0.5)
plt.plot(t, xr, 'g', label='Reconstructed (Improper Sampling)')
plt.title("Improper Sampling and Distorted Reconstruction (Aliasing)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.show()
