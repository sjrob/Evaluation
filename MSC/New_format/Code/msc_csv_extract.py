import sys
import numpy as np

# open and read the text file with the species names
with open("species.txt", "rt") as f_species:
    species = []
    while True:
        line = f_species.readline()
        if not line:
            break
        if not ("#" in line):
            species.append(line.strip())
f_species.close()

# open and read the text file with the dates
with open("dates.txt", "rt") as f_dates:
    dates = []
    while True:
        line = f_dates.readline()
        if not line:
            break
        if not ("#" in line):
            dates.append(line.strip())
f_dates.close()

# set the counter to zero across all species and dates
counts = np.zeros((len(dates),len(species)))
probs = np.zeros((1,len(species)))

# open and read the file (or pipe) data csv
# format is
# 0 uuid
# 1 datetime_recorded
# 2 med_start_time
# 3 med_prob
# 4 msc_start_time
# 5 msc_end_time
# 6 med_stop_time
# 7-14 ae aegypti,an arabiensis,an coustani,an funestus ss,an squamosus,culex pipiens complex,ma africanus,ma uniformis
with open(sys.argv[1], "rt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        else:
            fields = line.split(',')
            for m in range(len(dates)):
                if (dates[m] in fields[1]):
                    for n in range(len(species)):
                        counts[m,n] += float(fields[7+n])
f.close()

# print the results
print("date", end='')
for n in range(len(species)):
    print(", %s" % (species[n]), end='')
print("\r")

for m in range(len(dates)):
    print("%s" % (dates[m]), end='')
    for n in range(len(species)):
        print(", %d" % (counts[m,n]), end='')
    print("\r")
