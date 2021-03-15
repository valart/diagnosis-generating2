import matplotlib.pyplot as plt
import csv
import ast

categories = [
    'A00-B99',
    'C00-D48',
    'D50-D89',
    'E00-E90',
    'F00-F99',
    'G00-G99',
    'H00-H59',
    'H60-H95',
    'I00-I99',
    'J00-J99',
    'K00-K93',
    'L00-L99',
    'M00-M99',
    'N00-N99',
    'O00-O99',
    'P00-P96',
    'Q00-Q99',
    'R00-R99',
    'S00-T98',
    'U00-U99',
    'Z00-Z99'
]

rng = [[0]*100 for i in range(len(categories))]
years = [i for i in range(100)]

with open("../diagnoses.csv", encoding="utf8") as file:
    read = csv.reader(file, delimiter="\t")
    next(read)

    for row in read:
        for cat in list(ast.literal_eval(row[6])):
            catIndex = categories.index(cat[0])
            age = int(cat[1])
            rng[catIndex][age] += 1

fig, ax = plt.subplots(figsize=(20, 5))
ax.stackplot(years, rng, labels=categories)
ax.set_title('Estonian specialized medical care')
ax.legend(loc='upper right')
ax.set_ylabel('Total patients')
fig.tight_layout()
plt.show()
