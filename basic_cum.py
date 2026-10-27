import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1000
bits = np.random.randint(0, 2, N)
bpsk_signal = 2 * bits - 1

# SNR and Noise Setup
SNR_dB = 5
SNR = 10 ** (SNR_dB / 10)
noise_variance = 1 / (2 * SNR)
noise = np.sqrt(noise_variance) * np.random.randn(N)

# Received Signal and Demodulation
received_signal = bpsk_signal + noise
received_bits = (received_signal > 0).astype(int)

# Bit Error Rate (BER) Calculation
errors = np.sum(bits != received_bits)
BER = errors / N

print("Number of Errors:", errors)
print("Bit Error Rate (BER):", BER)

# --- Plot 1: Original Bits ---
plt.figure(figsize=(10, 3))
plt.stem(bits[:20])
plt.title("Original Bits")
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.grid(True)
plt.show()

# --- Plot 2: BPSK Modulated Signal ---
plt.figure(figsize=(10, 3))
plt.plot(bpsk_signal[:50], marker='o')
plt.title("BPSK Modulated Signal")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# --- Plot 3: Received Signal with AWGN ---
plt.figure(figsize=(10, 3))
plt.plot(received_signal[:50], marker='o')
plt.title("Received Signal with AWGN")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()