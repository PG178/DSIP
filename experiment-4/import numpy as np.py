import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, bilinear, freqz, cheby1
def design_butterworth_filter(filter_order, cutoff_frequency, sampling_frequency): # Design the analog Butterworth filter
analog_b, analog_a = butter(filter_order, cutoff_frequency, analog=True, btype='low') # Perform the bilinear transformation
digital_b, digital_a = bilinear(analog_b, analog_a, sampling_frequency) return digital_b, digital_a
def design_chebyshev_filter(filter_order, cutoff_frequency, sampling_frequency, ripple): # Design the analog Chebyshev filter
analog_b, analog_a = cheby1(filter_order, ripple, cutoff_frequency, analog=True, btype='low') # Perform the bilinear transformation
digital_b, digital_a = bilinear(analog_b, analog_a, sampling_frequency) return digital_b, digital_a

def plot_filter_response(digital_b, digital_a, sampling_frequency): # Compute the frequency response of the filter
frequency, magnitude_response = freqz(digital_b, digital_a, fs=sampling_frequency) # Plot the magnitude response
plt.figure(figsize=(10, 6))
plt.plot(frequency, np.abs(magnitude_response)) plt.title('Filter Magnitude Response') plt.xlabel('Frequency (Hz)') plt.ylabel('Magnitude')
plt.grid(True) plt.show()
# Compute the impulse response of the filter
_, impulse_response = freqz(digital_b, digital_a, fs=sampling_frequency, worN=4096) # Plot the impulse response
plt.figure(figsize=(10, 6)) plt.plot(impulse_response) plt.title('Filter Impulse Response')

plt.xlabel('Samples') plt.ylabel('Amplitude') plt.grid(True) plt.show()

# Specify the desired filter specifications filter_order = 4 # Filter order
cutoff_frequency = 1000 # Cutoff frequency in Hz sampling_frequency = 8000 # Sampling frequency in Hz ripple = 0.5 # Ripple factor for Chebyshev filter
# Design the Butterworth filter
digital_b, digital_a = design_butterworth_filter(filter_order, cutoff_frequency, sampling_frequency) # Plot the Butterworth filter's magnitude response and impulse response plot_filter_response(digital_b, digital_a, sampling_frequency)

# Design the Chebyshev filter
digital_b, digital_a = design_chebyshev_filter(filter_order, cutoff_frequency, sampling_frequency, ripple) # Plot the Chebyshev filter's magnitude response and impulse response
plot_filter_response(digital_b, digital_a, sampling_frequency)

# Save the filter coefficients (optional) filter_path = 'filter_coefficients.txt'
np.savetxt(filter_path, np.vstack((digital_b, digital_a)), delimiter=',') print(f"Filter coefficients saved at: {filter_path}")



Task-1
#Task 1 — Generate 1 kHz, 2 kHz, 3 kHz and 4 kHz sine waves and plot all import numpy as np
import matplotlib.pyplot as plt

fs = 10000
t = np.arange(0, 0.01, 1/fs)
x1 = np.sin(2*np.pi*1000*t) x2 = np.sin(2*np.pi*2000*t) x3 = np.sin(2*np.pi*3000*t) x4 = np.sin(2*np.pi*4000*t)

plt.figure(figsize=(10,8))

plt.subplot(4,1,1) plt.stem(t,x1)
plt.title("1 kHz Sine Wave") plt.grid()

plt.subplot(4,1,2) plt.stem(t,x2)
plt.title("2 kHz Sine Wave") plt.grid()

plt.subplot(4,1,3) plt.stem(t,x3)
plt.title("3 kHz Sine Wave") plt.grid()

plt.subplot(4,1,4) plt.stem(t,x4)
plt.title("4 kHz Sine Wave") plt.grid()

plt.tight_layout() plt.show()

Task-2
#Task 2 — Add all four signals and plot in time and frequency domain import numpy as np
import matplotlib.pyplot as plt

fs = 10000
t = np.arange(0, 0.01, 1/fs)
x1 = np.sin(2*np.pi*1000*t) x2 = np.sin(2*np.pi*2000*t) x3 = np.sin(2*np.pi*3000*t) x4 = np.sin(2*np.pi*4000*t)
x = x1 + x2 + x3 + x4 # Time domain
plt.figure(figsize=(10,4))
plt.stem(t,x)
plt.title("Added Signal - Time Domain")

plt.xlabel("Time (s)") plt.ylabel("Amplitude") plt.grid()
plt.show()

# Frequency domain X = np.fft.fft(x)
freq = np.fft.fftfreq(len(x),1/fs)
plt.figure(figsize=(10,4)) plt.stem(freq[:len(freq)//2],np.abs(X[:len(X)//2])) plt.title("Added Signal - Frequency Domain") plt.xlabel("Frequency (Hz)") plt.ylabel("Magnitude")
plt.grid() plt.show()

Task-3

#Task 3 — Pass the signal through Butterworth digital filter with cutoff 2 kHz import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import butter, filtfilt
fs = 10000
t = np.arange(0, 0.01, 1/fs)

x1 = np.sin(2*np.pi*1000*t) x2 = np.sin(2*np.pi*2000*t) x3 = np.sin(2*np.pi*3000*t) x4 = np.sin(2*np.pi*4000*t)
x = x1 + x2 + x3 + x4 # Butterworth filter
b,a = butter(4,2000/(fs/2),btype='low') y = filtfilt(b,a,x)
# Time domain plt.figure(figsize=(10,4)) plt.plot(t,y)
plt.title("Butterworth Output - Time Domain") plt.xlabel("Time (s)")
plt.ylabel("Amplitude") plt.grid()
plt.show()
# Frequency domain Y = np.fft.fft(y)
freq = np.fft.fftfreq(len(y),1/fs)

plt.figure(figsize=(10,4)) plt.plot(freq[:len(freq)//2],np.abs(Y[:len(Y)//2])) plt.title("Butterworth Output - Frequency Domain") plt.xlabel("Frequency (Hz)") plt.ylabel("Magnitude")
plt.grid() plt.show()

Task-4
#Task 4 — Pass the signal through Chebyshev digital filter with cutoff 3 kHz import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cheby1, filtfilt

fs = 10000
t = np.arange(0, 0.01, 1/fs)

x1 = np.sin(2*np.pi*1000*t) x2 = np.sin(2*np.pi*2000*t) x3 = np.sin(2*np.pi*3000*t) x4 = np.sin(2*np.pi*4000*t)
x = x1 + x2 + x3 + x4 # Chebyshev filter
b,a = cheby1(4,0.5,3000/(fs/2),btype='low') y = filtfilt(b,a,x)

# Time domain plt.figure(figsize=(10,4)) plt.plot(t,y)
plt.title("Chebyshev Output - Time Domain") plt.xlabel("Time (s)") plt.ylabel("Amplitude")
plt.grid() plt.show()
# Frequency domain Y = np.fft.fft(y)
freq = np.fft.fftfreq(len(y),1/fs)
plt.figure(figsize=(10,4)) plt.plot(freq[:len(freq)//2],np.abs(Y[:len(Y)//2])) plt.title("Chebyshev Output - Frequency Domain") plt.xlabel("Frequency (Hz)") plt.ylabel("Magnitude")
plt.grid() plt.show()
