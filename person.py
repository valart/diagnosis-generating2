from parsing import get_model
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

    def live(self):
        model = get_model()
        model.generate(self, 'INITIAL')

    def die(self):
        # http://andmebaas.stat.ee/Index.aspx?DataSetCode=RV56#
        age = self.today.year - date.today().year
        rand = random.uniform(0, 1)
        if age // 5 == 0:
            return rand <= 0.002
        if age // 5 == 1:
            return rand <= 0.0008
        if age // 5 == 2:
            return rand <= 0.0005
        if age // 5 == 3:
            return rand <= 0.0014
        if age // 5 == 4:
            return rand <= 0.0019
        if age // 5 == 5:
            return rand <= 0.0041
        if age // 5 == 6:
            return rand <= 0.006
        if age // 5 == 7:
            return rand <= 0.0069
        if age // 5 == 8:
            return rand <= 0.012
        if age // 5 == 9:
            return rand <= 0.0188
        if age // 5 == 10:
            return rand <= 0.0511
        if age // 5 == 11:
            return rand <= 0.0282
        if age // 5 == 12:
            return rand <= 0.0441
        if age // 5 == 13:
            return rand <= 0.0636
        if age // 5 == 14:
            return rand <= 0.0897
        if age // 5 == 15:
            return rand <= 0.101
        if age // 5 == 16:
            return rand <= 0.1267
        if age // 5 == 17:
            return rand <= 0.1665
        if age // 5 == 18:
            return rand <= 0.1703
        if age // 5 == 19:
            return rand <= 0.1164
        return True

    def new_year(self):
        age = self.today.year - date.today().year
        if age < 5:
            age += 10
        return random.randint(0, 100) <= 100 - age

    def new_diagnosis(self):
        age = self.today.year - date.today().year
        if age < 10:
            age = 55 - age
        return random.randint(0, 100) <= age

    def get_age_range(self):
        return utils.AGES[(self.today.year - date.today().year) // 5]
