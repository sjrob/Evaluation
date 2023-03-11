import sys
import numpy as np

# define the field numbers in the .csv file, in .py format i.e. 0 start

# house_mosq_uuid
# Date_field = 11
# Species_name_field = 20
# Species_num_field = 22

# Datasheet_CDCLT_...
Date_field = 2
Species_name_field = 12
Species_num_field = 14


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
        if not ("Number_Caught" in line):
            fields = line.split(',')
            if not ("NA" in fields[Species_num_field]):
                num_found = int(fields[Species_num_field]) 
            else:
                num_found = 0                
            if (num_found>0):
                for m in range(len(dates)):
                    for n in range(len(species)):
                        if ((dates[m] in fields[Date_field]) and (species[n] in fields[Species_name_field])): 
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
