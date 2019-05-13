import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, loadtxt, pi, sqrt, array
from lmfit import Model
from lmfit.models import LinearModel

font = {'family' : 'normal', 'size'   : 14}

plt.rc('font', **font)

freq = 930*np.power(10, 3)

data = loadtxt('analysis/v_by_dist.dat')

dist = data[:, 0]
dist_err = data[:, 1]
dist_scale = data[:, 2]
phase_rad = data[:, 3]
phase_err = data[:, 4]

phase_weights = 1/phase_err

def linear(x, a, b):
    return (a*x + b)

linear_model = Model(linear)
result = linear_model.fit(phase_rad, weights=phase_weights , x=dist_scale, a=1, b=1)

print(result.fit_report())
print(result.chisqr)

a = result.params['a'].value
b = result.params['b'].value

print("$ phase velocity: ", ((2*np.pi*freq)/a))

fig, ax = plt.subplots()

ax.set_xlabel(r'distance [m]', fontsize=18)
ax.set_ylabel(r'phase [rad]', fontsize=18)
plt.title('phase vs distance', fontsize=20)

plt.plot(dist_scale, phase_rad, '.C3', label='data points')
ax.errorbar(dist_scale, phase_rad, yerr=0.26, xerr=dist_err, fmt='.k', capthick=2, label='uncertainties')
plt.plot(dist_scale, linear(dist_scale, a, b), 'C0--', label='linear fit: y=a*x+b')

plt.legend()
plt.show()