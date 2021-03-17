from models.person import *
import csv
from datetime import date
from parsing import get_model
import sys
from visualization import visualization, graphics
import os


def save_into_file(data):
    if not os.path.exists('output'):
        os.makedirs('output')
    with open('output/diagnoses.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Code", "Sex", "Birthday", "Died", "Age", "Diagnoses", "Categories"])
        for person in data:
            writer.writerow([person.code, person.sex, date.today(), person.today, person.today.year - date.today().year,
                             person.diagnoses, person.categories])


def generate(population=10):
    print("Creating {} people".format(population))
    data = []
    model = get_model()
    for i in range(population):
        human = Person(str(i + 1), random.choice(['M', 'W']))
        human.live(model)
        data.append(human)
        print(i+1)
    save_into_file(data)
    print("Created {} people into output folder diagnoses.csv file".format(population))


def show_model(age, sex):
    visualization.show_model(age, sex)


def show_plot(category):
    graphics.show_categories(category)


if __name__ == '__main__':
    if "-p" in sys.argv:
        generate(int(sys.argv[sys.argv.index("-p") + 1]))
    elif "-model" in sys.argv:
        show_model(sys.argv[sys.argv.index("-model") + 1], sys.argv[sys.argv.index("-model") + 2])
    elif "-plot" in sys.argv:
        show_plot(sys.argv[sys.argv.index("-plot") + 1])
    else:
        generate()
