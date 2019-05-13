import numpy as np

fname = 'data/v_by_distance_data.csv'
foutname = 'analysis/v_by_dist.dat'

outfile = open(foutname, "w+")

outfile.write("# dist dist_scale dist_err phase_rad phase_err phase_deg\n")

dist_err = np.power(10, -4.0)
phase_err = np.radians(5)

with open(fname) as f:
    content = f.readlines()

for row in content:
    row_data = row.split(",")

    dist = float(row_data[0])
    dist_scale = float(row_data[1])

    phase_deg = float(row_data[2])
    phase_rad = np.radians(phase_deg)

    str1 = str(dist) + " " + str(dist_err) + " " + str(dist_scale)
    str2 = " " + str(phase_rad) + " " + str(phase_err) + " " + str(phase_deg) + "\n"

    print(str1 + str2)

    outfile.write(str1 + str2)

outfile.close()