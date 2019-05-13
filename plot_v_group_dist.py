import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, loadtxt, pi, sqrt, array
from lmfit import Model
from lmfit.models import LinearModel

font = {'family' : 'normal', 'size'   : 14}

plt.rc('font', **font)

freq = 930*np.power(10, 3)

data = loadtxt('analysis/v_group_by_dist.dat')

dist = data[:, 0]
dist_scale = data[:, 1]
dist_err = data[:, 2]
time = data[:, 3]
time_scale = data[:, 4]
time_err = data[:, 5]

dist_weights = 1/dist_err

def linear(x, a, b):
    return (a*x + b)

linear_model = Model(linear)
result = linear_model.fit(dist_scale, weights=dist_weights , x=time_scale, a=1, b=1)

print(result.fit_report())
print(result.chisqr)

a = result.params['a'].value
b = result.params['b'].value

print("$ phase velocity: ", a)

fig, ax = plt.subplots()

ax.set_xlabel(r'time [s]', fontsize=18)
ax.set_ylabel(r'distance [m]', fontsize=18)
plt.title('distance vs time', fontsize=20)

plt.plot(time_scale, dist_scale, '.C3', label='data points')
ax.errorbar(time_scale, dist_scale, yerr=dist_err, xerr=time_err, fmt='.k', capthick=2, label='uncertainties')
plt.plot(time_scale, linear(time_scale, a, b), 'C0--', label='linear fit: y=a*x+b')

plt.legend()
plt.show()