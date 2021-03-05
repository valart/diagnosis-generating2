import random


class Diagnosis:

    def __init__(self, code, age, next_diagnoses):
        self.code = code
        self.age = age
        self.next_diagnoses = next_diagnoses


def get_category_diagnosis(model, person, code):
    diagnoses = {i: model.get_diagnosis_by_code(i).age[person.get_age_range()][person.sex] for i in
                 model.graph[code]}
    diagnoses = dict(sorted(diagnoses.items(), key=lambda category: category[1]))

    probability = random.uniform(0, 1)
    previous = 0

    for code, prob in diagnoses.items():
        if prob + previous >= probability:
            return code
        else:
            previous += prob


def get_next_diagnosis(next_diagnoses):
    diagnoses = dict(sorted(next_diagnoses.items(), key=lambda category: category[1]))
    probability = random.uniform(0, 1)
    previous = 0
    for code, prob in diagnoses.items():
        if prob + previous >= probability:
            return code
        else:
            previous += prob
