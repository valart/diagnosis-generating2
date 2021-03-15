import matplotlib.pyplot as plt
import csv
import ast
from utils import utils
from datetime import date, datetime

categories = [category for category in utils.categories]

rng = [[0]*100 for i in range(len(categories))]
years = [i for i in range(100)]

with open("../diagnoses.csv", encoding="utf8") as file:
    read = csv.reader(file, delimiter="\t")
    next(read)

    for row in read:
        # if row[1] == 'M':
        for cat in list(ast.literal_eval(row[6])):
            catIndex = categories.index(cat[0])
            age = int(cat[1])
            rng[catIndex][age] += 1

fig, ax = plt.subplots(figsize=(20, 5))

ax.stackplot(years, rng, labels=categories, colors=utils.colors[:len(categories)])
ax.set_title('Estonian specialized medical care')
ax.legend(loc='upper right')
ax.set_ylabel('Total patients')
fig.tight_layout()
plt.show()


# A = utils.categories['A00-B99']
# rng = [[0]*100 for i in range(len(A))]
# years = [i for i in range(100)]
#
# with open("../diagnoses.csv", encoding="utf8") as file:
#     read = csv.reader(file, delimiter="\t")
#     next(read)
#
#     for row in read:
#         for cat in list(ast.literal_eval(row[5])):
#             if cat[0] in A:
#                 catIndex = A.index(cat[0])
#                 age = datetime.strptime(cat[1], '%Y-%m-%d').year - date.today().year
#                 rng[catIndex][age] += 1
#
# fig, ax = plt.subplots(figsize=(20, 5))
#
# from random import randint
# colors = []
# for i in range(len(A)):
#     colors.append('#%06X' % randint(0, 0xFFFFFF))
#
# ax.stackplot(years, rng, labels=A, colors=colors)
# ax.set_title('Estonian specialized medical care')
# ax.legend(loc='upper right')
# ax.set_ylabel('Total patients')
# fig.tight_layout()
# plt.show()
