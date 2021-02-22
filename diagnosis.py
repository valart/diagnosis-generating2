import utils.utils as utils
import random
from datetime import date


class Diagnosis:

    def __init__(self, code, age):
        self.code = code
        self.age = age


def get_diagnosis(diagnoses, person):
    power = random.uniform(0, 1)
    previous = 0
    age = person.today.year - date.today().year

    diagnoses.sort(key=lambda x: x.age[utils.AGES[age // 10]][person.sex])
    for diagnosis in diagnoses:
        probability = diagnosis.age[utils.AGES[age // 10]][person.sex]
        if probability + previous >= power:
            return diagnosis.code
        else:
            previous += probability
    return None
