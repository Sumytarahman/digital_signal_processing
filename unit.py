import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Discrete-time axis
# -----------------------------
n = np.arange(-5, 10, 1)  # n from -5 to 9

# -----------------------------
# 1. Unit Sample (δ[n])
# -----------------------------
delta = np.zeros_like(n)
delta[n == 0] = 1

# -----------------------------
# 2. Unit Step (u[n])
# -----------------------------
u = np.zeros_like(n)
u[n >= 0] = 1

# -----------------------------
# 3. Unit Ramp (r[n])
# -----------------------------
r = np.zeros_like(n, dtype=float)
r[n >= 0] = n[n >= 0]

# -----------------------------
# 4. Real Exponential Signal
#    x[n] = a^n * u[n]
# -----------------------------
a = 0.8
x_exp_real = (a**n) * u

# -----------------------------
# 5. Complex Exponential Signal
#    x[n] = (a^n) * e^(j*ω0*n) * u[n]
# -----------------------------
a_complex = 0.9
omega0 = np.pi / 4
x_exp_complex = (a_complex**n) * np.exp(1j * omega0 * n) * u

# Separate real and imaginary parts
x_exp_complex_real = np.real(x_exp_complex)
x_exp_complex_imag = np.imag(x_exp_complex)

# -----------------------------
# Plot all signals
# -----------------------------
plt.figure(figsize=(12,10))

# Unit Sample
plt.subplot(3,2,1)
plt.stem(n, delta)
plt.title('Unit Sample δ[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Unit Step
plt.subplot(3,2,2)
plt.stem(n, u)
plt.title('Unit Step u[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Unit Ramp
plt.subplot(3,2,3)
plt.stem(n, r)
plt.title('Unit Ramp r[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Real Exponential
plt.subplot(3,2,4)
plt.stem(n, x_exp_real)
plt.title(f'Real Exponential x[n] = {a}^n u[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Complex Exponential
plt.subplot(3,2,5)
plt.stem(n, x_exp_complex_real, linefmt='r-', markerfmt='ro', basefmt='k-', label='Real Part')
plt.stem(n, x_exp_complex_imag, linefmt='b-', markerfmt='bo', basefmt='k-', label='Imag Part')
plt.title(f'Complex Exponential x[n] = {a_complex}^n e^(j*ω0*n) u[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
