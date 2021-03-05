from person import *
import csv
from datetime import date


def save_into_file(data):
    with open('diagnoses.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Code", "Sex", "Birthday", "Died", "Age", "Diagnoses"])
        for person in data:
            writer.writerow([person.code, person.sex, date.today(), person.today, person.today.year - date.today().year, person.diagnoses])


def generate():
    data = []
    for i in range(0, 200, 2):
        man = Person(str(i+1), "M")
        man.live()
        woman = Person(str(i+2), "W")
        woman.live()
        data.append(man)
        data.append(woman)
    save_into_file(data)


if __name__ == '__main__':
    generate()
