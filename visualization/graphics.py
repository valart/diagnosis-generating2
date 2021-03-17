import matplotlib.pyplot as plt
import csv
import ast
from utils import utils
from datetime import datetime
from scipy.ndimage.filters import gaussian_filter1d


def show_categories(category):
    if category == "category":
        categories = [category for category in utils.categories]
    else:
        categories = utils.categories[category]

    rng = [[0] * 100 for i in range(len(categories))]
    years = [i for i in range(100)]

    with open("output/diagnoses.csv", encoding="utf8") as file:
        read = csv.reader(file, delimiter="\t")
        next(read)
        for row in read:
            rowVal = row[6] if category == "category" else row[5]
            for cat in list(ast.literal_eval(rowVal)):
                if cat[0] in categories:
                    catIndex = categories.index(cat[0])
                    age = datetime.strptime(cat[1], '%Y-%m-%d').year - datetime.strptime(row[2], '%Y-%m-%d').year
                    rng[catIndex][age] += 1

    fig, ax = plt.subplots(figsize=(20, 5))
    for i in range(len(categories)):
        rng[i] = gaussian_filter1d(rng[i], sigma=2)

    ax.stackplot(years, rng, labels=categories, colors=utils.colors[:len(categories)])
    ax.set_title('Categories' if category == "category" else category)
    ax.legend(loc='upper right')
    ax.set_ylabel('Total patients')
    fig.tight_layout()
    plt.show()
