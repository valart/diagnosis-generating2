from parsing import get_model
from datetime import date
import random


class Person:

    def __init__(self, code, sex):
        self.code = code
        self.sex = sex
        self.diagnosis = []
        self.today = date.today()
        self.alive = True

    def live(self):
        model = get_model()
        diagnoses = 0
        age = 0
        while self.alive:
            if self.new_diagnosis():
                diagnoses += 1
                model.generate(self)
            if self.new_year():
                self.today = date(self.today.year + 1, 1, 1)
            if self.die():
                self.alive = False
                age = self.today.year - date.today().year
        print("Vanus: {}, diagnooside arv: {}".format(self.today.year - date.today().year, diagnoses))

    def die(self):
        # http://andmebaas.stat.ee/Index.aspx?DataSetCode=RV56#
        age = self.today.year - date.today().year
        rand = random.random()
        if age // 10 == 0:
            return rand <= 0.003
        if age // 10 == 1:
            return rand <= 0.002
        if age // 10 == 2:
            return rand <= 0.006
        if age // 10 == 3:
            return rand <= 0.013
        if age // 10 == 4:
            return rand <= 0.031
        if age // 10 == 5:
            return rand <= 0.072
        if age // 10 == 6:
            return rand <= 0.153
        if age // 10 == 7:
            return rand <= 0.227
        if age // 10 == 8:
            return rand <= 0.338
        if age // 10 == 9:
            return rand <= 0.156
        return True

    def new_year(self):
        age = self.today.year - date.today().year
        if age < 5:
            age += 10
        return random.randint(0, 100) <= 100 - age

    def new_diagnosis(self):
        age = self.today.year - date.today().year
        if age < 10:
            age = 15 - age
        age = 70
        return random.randint(0, 100) <= age
