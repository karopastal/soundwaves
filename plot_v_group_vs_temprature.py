import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, loadtxt, pi, sqrt, array
from lmfit import Model

font = {'family' : 'normal', 'size'   : 14}

plt.rc('font', **font)

data = loadtxt('analysis/v_group_by_tempratures.dat')

temprature = data[:, 0]
v_group = data[:, 1]
v_group_err = data[:, 2]

v_group_weights = 1/v_group_err

def power(x, a, b):
    return (np.power(a*x, b))

power_model = Model(power)
result = power_model.fit(v_group, weights=v_group_weights , x=temprature, a=1, b=1)

print(result.fit_report())
print(result.chisqr)

a = result.params['a'].value
b = result.params['b'].value

fig, ax = plt.subplots()

ax.set_xlabel(r'temprature [Celsius]', fontsize=18)
ax.set_ylabel(r'group velocity [m/s]', fontsize=18)
plt.title('group velocity vs temprature', fontsize=20)

plt.plot(temprature, v_group, '.C3', label='data points')
ax.errorbar(temprature, v_group, yerr=v_group_err, xerr=1, fmt='.k', capthick=2, label='uncertainties')
plt.plot(temprature, power(temprature, a, b), 'C0--', label='power fit: y=a*x^b')

plt.legend()
plt.show()