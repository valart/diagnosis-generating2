import csv
import yaml
import os
import utils.utils as utils


def sum_str(arr):
    return sum([int(float(i)) for i in arr])


with open("data.tsv", encoding="utf8") as file:
    read = csv.reader(file, delimiter="\t")
    for _ in range(15):
        next(read)

    category = dict()
    diagnosis = dict()

    for row in read:
        if row[2] == '' and row[3] == '' and row[5] == 'patients' and row[6] == 'tot':  # Category
            code = row[1]
            sex = 'M' if row[4] == 'M' else 'W'

            if code not in category:
                category[code] = {'code': code, 'age': {}}

            for i in range(19):
                age = str(i * 5) + '-' + str(i * 5 + 4)
                if age not in category[code]['age']:
                    category[code]['age'][age] = {}
                if sex not in category[code]['age'][age]:
                    category[code]['age'][age][sex] = sum_str(row[i * 5 + 8:i * 5 + 8 + 5])
                else:
                    category[code]['age'][age][sex] += sum_str(row[i * 5 + 8:i * 5 + 8 + 5])

        elif row[2] != '' and row[3] != '' and row[5] == 'patients' and row[6] == 'tot':  # Diagnosis
            code = row[1]
            parent = row[3]
            sex = 'M' if row[4] == 'M' else 'W'

            if code not in diagnosis:
                diagnosis[code] = {'code': code, 'parent': parent, 'age': {}}

            for i in range(19):
                age = str(i * 5) + '-' + str(i * 5 + 4)
                if age not in diagnosis[code]['age']:
                    diagnosis[code]['age'][age] = {}
                if sex not in diagnosis[code]['age'][age]:
                    diagnosis[code]['age'][age][sex] = sum_str(row[i * 5 + 8:i * 5 + 8 + 5])
                else:
                    diagnosis[code]['age'][age][sex] += sum_str(row[i * 5 + 8:i * 5 + 8 + 5])
            diagnosis[code]['next'] = {'INITIAL': 1}

for value in diagnosis.values():
    for age in utils.AGES:
        if 'M' not in value['age'][age]:
            value['age'][age]['M'] = 0
        elif 'W' not in value['age'][age]:
            value['age'][age]['W'] = 0

for value in category.values():
    for age in utils.AGES:
        if 'M' not in value['age'][age]:
            value['age'][age]['M'] = 0
        elif 'W' not in value['age'][age]:
            value['age'][age]['W'] = 0


if not os.path.exists('../data/category'):
    os.makedirs('../data/category')

if not os.path.exists('../data/diagnosis'):
    os.makedirs('../data/diagnosis')

for cat in category:
    with open('../data/category/' + cat + '.yml', 'w') as file:
        documents = yaml.dump(category[cat], file, sort_keys=False)

for diag in diagnosis:
    with open('../data/diagnosis/' + diagnosis[diag]['parent'] + '/' + diag + '.yml', 'w') as file:
        documents = yaml.dump(diagnosis[diag], file, sort_keys=False)


