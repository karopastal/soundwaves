import numpy as np

fname = 'data/v_group_by_distance_data.csv'
foutname = 'analysis/v_group_by_dist.dat'

outfile = open(foutname, "w+")

outfile.write("# dist dist_scale dist_err time time_scale time_err\n")

dist_err = np.power(10.0, -2.0)
phase_err = np.radians(5)

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
    time_err = np.power(10.0, -6.0)

    str1 = str(dist) + " " + str(dist_scale) + " " + str(dist_err)
    str2 = " " + str(time) + " " + str(time_scale) + " " + str(time_err) + "\n"

    print(str1 + str2)

    outfile.write(str1 + str2)

outfile.close()