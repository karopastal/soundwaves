import numpy as np

fname = 'data/v_by_freq_data.csv'
foutname = 'analysis/v_by_freq.dat'

outfile = open(foutname, "w+")

outfile.write("# freq freq_scale freq_err phase_rad phase_err phase_deg\n")
freq_err = np.power(10, -4.0)
phase_err = np.radians(15)

with open(fname) as f:
    content = f.readlines()

for row in content:
    row_data = row.split(",")

    freq = float(row_data[0])
    freq_scale = freq*np.power(10, 3)

    phase_deg = float(row_data[1])
    phase_rad = np.radians(phase_deg)

    str1 = str(freq) + " " + str(freq_err) + " " + str(freq_scale)
    str2 = " " + str(phase_rad) + " " + str(phase_err) + " " + str(phase_deg) + "\n"

    print(str1 + str2)

    outfile.write(str1 + str2)

outfile.close()