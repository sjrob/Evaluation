# format is
# l1 - most likely
# l2-l9 probs of aegypti(aedes) arabiensis(anoph) coustani(anoph) funestus(anoph) squamosus(anoph) pip_comp(culex)
# africanus(mansonia) uniformis(mansonia)

import sys

Nspecies = 8

# open up the file
with open(sys.argv[1], "rt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        # first line of each block is o/p with "Most_likely" string
        Ts = line.split('\t')[0]
        Te = line.split('\t')[1]
        RoL = line.split('\t')[2]
        if ("Most_likely" in RoL):
            MED_prob = RoL.split(',')[2]
            MSC_str = RoL.split(',')[3]
            idx = MSC_str.find("_P")
            MSC_prob = MSC_str[idx+2:-1]
            MSC_class = MSC_str[:idx]
            class_idx = 0
            MSC_all_probs = ""
        else:
            # this is one of the class prob lines
            MSC_str = RoL.split(',')[3]
            idx = MSC_str.find("_P")
            MSC_all_probs = '{} , {}'.format(MSC_all_probs,MSC_str[idx+2:-1])
            if (class_idx == Nspecies-1):
                print('{} , {} , {} , {} , {}  {}'.format(Ts,Te,MED_prob,MSC_prob.strip(),MSC_class.strip(),MSC_all_probs.strip()))
            else:
                class_idx += 1

#fout = open("out.txt", "wt")
#fout.write("hello")
#fout.close()
