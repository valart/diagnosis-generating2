import utils.utils as utils
import random
from datetime import date
from diagnosis import get_diagnosis


class Category:

    def __init__(self, code, age, categories, diagnoses, period):
        self.code = code
        self.age = age
        self.categories = categories
        self.diagnoses = diagnoses
        self.period = period

    def generate(self, person):
        power = random.uniform(0, 1)
        previous = 0
        age = person.today.year - date.today().year

        self.categories.sort(key=lambda x: x.age[utils.AGES[age // 10]][person.sex])
        for category in self.categories:
            probability = category.age[utils.AGES[age // 10]][person.sex]
            if probability + previous >= power:
                diagnosis = get_diagnosis(category.diagnoses, person)
                newDay = utils.get_random_date(person.today)
                person.today = newDay
                print(diagnosis + " " + str(newDay))
                break
            else:
                previous += probability
