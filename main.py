from person import *
import csv
from datetime import date
from parsing import get_model


def save_into_file(data):
    with open('diagnoses.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Code", "Sex", "Birthday", "Died", "Age", "Diagnoses", "Categories"])
        for person in data:
            writer.writerow([person.code, person.sex, date.today(), person.today, person.today.year - date.today().year, person.diagnoses, person.categories])


def generate():
    data = []
    model = get_model()
    for i in range(0, 10000, 2):
        man = Person(str(i+1), "M")
        man.live(model)
        woman = Person(str(i+2), "W")
        woman.live(model)
        data.append(man)
        data.append(woman)
        print(i)
    save_into_file(data)


if __name__ == '__main__':
    generate()
    # print(sys.argv)
