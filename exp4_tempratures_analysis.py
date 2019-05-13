import numpy as np
from numpy import exp, loadtxt, pi, sqrt, array
from lmfit import Model
from lmfit.models import LinearModel

foutname = 'analysis/v_group_by_tempratures.dat'
outfile = open(foutname, "w+")
outfile.write("# temprature v_group v_group_err v_group_chi_sqr\n")

tempratures = [22, 29, 36, 43, 50, 57, 65]
dist_err = np.power(10.0, -2.0)

def linear(x, a, b):
    return (a*x + b)

def calculate_group_velocity(temprature):
    data = loadtxt('analysis/v_group_by_temprature_' + str(temprature) + '.dat')
    dist_scale = data[:, 1]
    dist_err = data[:, 2]
    time_scale = data[:, 4]
    dist_weights = 1/dist_err

    linear_model = Model(linear)
    result = linear_model.fit(dist_scale, weights=dist_weights , x=time_scale, a=1, b=1)

    v_group = result.params['a'].value
    v_group_err = result.params['a'].stderr
    v_group_chi_sqr = result.chisqr
    print("temprature: ", temprature, ", group velocity: ", v_group)

    str1 = str(temprature) + " " + str(v_group) + " " + str(v_group_err) + " " + str(v_group_chi_sqr) + "\n"
    outfile.write(str1)

def analyze_temprature(temprature):
    fname = 'data/v_group_by_tempratures/' + str(temprature) + '.csv'
    fout_by_temprature = 'analysis/v_group_by_temprature_' + str(temprature) + '.dat'
    
    outfile_by_temprature = open(fout_by_temprature, "w+")
    outfile_by_temprature.write("# dist dist_scale dist_err time time_scale time_err\n")

    with open(fname) as f:
        content = f.readlines()

    for row in content:
        row_data = row.split(",")

        dist = float(row_data[0])
        dist_scale = dist/np.power(10, 2)

        min_time = float(row_data[1])
        max_time = float(row_data[2])
        time = (max_time + min_time)/2.0
        time_scale = time*np.power(10.0, -6.0)
        time_err = np.power(10.0, -9.0)

        str1 = str(dist) + " " + str(dist_scale) + " " + str(dist_err)
        str2 = " " + str(time) + " " + str(time_scale) + " " + str(time_err) + "\n"
        outfile_by_temprature.write(str1 + str2)

    outfile_by_temprature.close()

for temprature in tempratures:
    analyze_temprature(temprature)
    calculate_group_velocity(temprature)

outfile.close()