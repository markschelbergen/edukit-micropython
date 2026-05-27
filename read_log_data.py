import matplotlib.pyplot as plt
import numpy as np
import pickle
from scipy.io import savemat
import pprint

sampling_time = .05
# filename = 'log_data_20260320-155137'  # u = 8*log_counter
filename = 'log_data_20260320-160459'  # u = 10*log_counter

# Load the pickle file
with open(filename+".pickle", "rb") as f:
    data = pickle.load(f)

savemat(filename+".mat", {"data": data})

microsteps = data[:, 0]
microsteps_per_rev = 3200
encoder_ticks = data[:, 1]
ticks_per_rev = 2400
control = data[:, 2]
period_timer = 10000. / (control)
time = np.arange(data.shape[0]) * sampling_time

fig, ax = plt.subplots(4, 1, sharex=True, figsize=[6.4, 6.4])
for a in ax: a.grid()
plt.subplots_adjust(top=.99, bottom=.0711, left=.14, right=.98)
pos = (microsteps - microsteps[0]) / microsteps_per_rev * 2 * np.pi
ax[0].plot(time, pos * 180/np.pi)
ax[0].set_ylabel('Stepper\nhoekstand [deg]')
ax[1].plot(time, -encoder_ticks/ticks_per_rev * 360)
ax[1].set_ylabel('Slinger\nhoek [deg]')
ax[2].plot(time, control)
ax[2].set_ylabel('Invoer\nvariable [-]')
ax[3].plot(time, 2 * np.pi * control * 5/microsteps_per_rev, label='Invoer')
ax[3].plot(time[1:], (pos[1:]-pos[:-1])/sampling_time, label='Afgeleide hoek')
ax[3].set_ylabel('Stepper snelheid\n[rad/s]')
ax[3].legend()
plt.xlabel('Tijd (s)')
for a in ax: a.grid()

sampling_time = .025
# filename = 'log_data_20260320-155722'  # u = 4*log_counter
filename = 'log_data_20260320-160402'  # u = 5*log_counter

# Load the pickle file
with open(filename+".pickle", "rb") as f:
    data = pickle.load(f)

# savemat(filename+".mat", {"data": data})

microsteps = data[:, 0]
microsteps_per_rev = 3200
encoder_ticks = data[:, 1]
ticks_per_rev = 2400
control = data[:, 2]
period_timer = 10000. / (control)
time = np.arange(data.shape[0]) * sampling_time

pos = (microsteps - microsteps[0]) / microsteps_per_rev * 2 * np.pi
ax[0].plot(time, pos * 180/np.pi)
ax[0].set_ylabel('Stepper\nhoekstand [deg]')
ax[1].plot(time, -encoder_ticks/ticks_per_rev * 360)
ax[1].set_ylabel('Slinger\nhoek [deg]')
ax[2].plot(time, control)
ax[2].set_ylabel('Invoer\nvariable [-]')
ax[3].plot(time, 2 * np.pi * control * 5/microsteps_per_rev, label='Invoer')
ax[3].plot(time[1:], (pos[1:]-pos[:-1])/sampling_time, label='Afgeleide hoek')
ax[3].set_ylabel('Stepper snelheid\n[rad/s]')
ax[3].legend()
plt.xlabel('Tijd (s)')
for a in ax: a.grid()
plt.show()