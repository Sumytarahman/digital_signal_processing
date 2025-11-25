import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# (1) Create "analog" signal
# -------------------------------
fs_analog = 200000     # very high rate to simulate analog
duration = 0.01
t_analog = np.arange(0, duration, 1/fs_analog)

xa = (3*np.cos(2000*np.pi*t_analog)
      + 5*np.sin(6000*np.pi*t_analog)
      + 10*np.cos(12000*np.pi*t_analog))

# -------------------------------
# (2) Improper Sampling (aliasing)
# -------------------------------
fs_sample_bad = 8000   # BELOW 12 kHz → improper sampling
Ts_bad = 1/fs_sample_bad
n_bad = np.arange(0, duration, Ts_bad)

xs_bad = (3*np.cos(2000*np.pi*n_bad)
          + 5*np.sin(6000*np.pi*n_bad)
          + 10*np.cos(12000*np.pi*n_bad))

# -------------------------------
# (3) Plot analog vs undersampled
# -------------------------------
plt.figure(figsize=(10,5))

plt.plot(t_analog, xa, label='Analog-like signal (xa)', linewidth=1)

plt.stem(n_bad, xs_bad, linefmt='g-', markerfmt='go', basefmt=" ",
         label='Improperly Sampled Signal (Aliasing)')

plt.title("Improper Sampling of xa(t) — Aliasing Occurs")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
