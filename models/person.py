from datetime import date
import random
from utils import utils


class Person:

    def __init__(self, code, sex):
        self.code = code
        self.sex = sex
        self.diagnoses = []
        self.today = date.today()
        self.alive = True
        self.categories = []

    def live(self, model):
        model.generate(self, 'INITIAL')

    def add_diagnosis(self, code):
        newDay = utils.get_random_date(self.today)
        self.today = newDay
        for categoryCode in utils.categories:
            if code in utils.categories[categoryCode]:
                self.categories.append((categoryCode, str(newDay)))
                break
        self.diagnoses.append((code, str(newDay)))

    def die(self):
        # http://andmebaas.stat.ee/Index.aspx?DataSetCode=RV56#
        age = self.today.year - date.today().year
        rand = random.uniform(0, 1)
        if age // 5 == 0:
            return rand <= 31/71235
        if age // 5 == 1:
            return rand <= 12/74176
        if age // 5 == 2:
            return rand <= 7/72512
        if age // 5 == 3:
            return rand <= 22/61227
        if age // 5 == 4:
            return rand <= 29/64692
        if age // 5 == 5:
            return rand <= 63/88133
        if age // 5 == 6:
            return rand <= 92/99574
        if age // 5 == 7:
            return rand <= 106/92945
        if age // 5 == 8:
            return rand <= 185/90701
        if age // 5 == 9:
            return rand <= 290/91347
        if age // 5 == 10:
            return rand <= 434/83105
        if age // 5 == 11:
            return rand <= 679/88719
        if age // 5 == 12:
            return rand <= 980/85106
        if age // 5 == 13:
            return rand <= 1381/77344
        if age // 5 == 14:
            return rand <= 1556/58104
        if age // 5 == 15:
            return rand <= 1951/51683
        if age // 5 == 16:
            return rand <= 2564/40544
        if age // 5 == 17:
            return rand <= 2623/23198
        if age // 5 == 18:
            return rand <= 1793/9170
        return True

    def new_year(self):
        age = self.today.year - date.today().year
        if age < 5:
            age += 15
        return random.randint(0, 100) >= age

    def new_diagnosis(self):
        age = self.today.year - date.today().year
        if age < 10:
            age = 55 - age
        return random.randint(0, 100) <= age

    def get_age_range(self):
        return utils.AGES[(self.today.year - date.today().year) // 5]
