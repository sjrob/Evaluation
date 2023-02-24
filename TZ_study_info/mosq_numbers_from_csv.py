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

# open and read the file (or pipe) data csv
with open(sys.argv[1], "rt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        if not ("Phone.ID" in line):
            fields = line.split(',')
            if not ("NA" in fields[22]):
                num_found = int(fields[22]) # fields[22] is the number
            else:
                num_found = 0                
            if (num_found>0):
                for m in range(len(dates)):
                    for n in range(len(species)):
                        if ((dates[m] in fields[11]) and (species[n] in fields[20])): # [11]-dates, [20]-species
                            counts[m,n] += num_found
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
