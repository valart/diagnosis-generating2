from category import *
from diagnosis import *
from datetime import date
import utils.utils as utils


class Model:

    def __init__(self):
        self.categories = []
        self.diagnoses = []
        self.graph = dict()

    def add_diagnosis(self, diagnosis):
        if diagnosis not in self.diagnoses:
            self.diagnoses.append(diagnosis)

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_edge(self, start, end):
        if start not in self.graph:
            self.graph[start] = [end]
        else:
            self.graph[start].append(end)

    def get_category_by_code(self, code):
        return next(filter(lambda category: category.code == code, self.categories), None)

    def get_diagnosis_by_code(self, code):
        return next(filter(lambda diagnosis: diagnosis.code == code, self.diagnoses), None)

    def generate(self, person, code):
        if not person.alive:
            return
        if person.new_diagnosis():
            if code == 'INITIAL':
                category_code = get_category(self, person)
                diagnosis_code = get_category_diagnosis(self, person, category_code)
                newDay = utils.get_random_date(person.today)
                person.today = newDay
                person.diagnoses.append((diagnosis_code, str(newDay)))
                code = diagnosis_code
            else:
                if self.get_category_by_code(code) is not None:
                    diagnosis_code = get_category_diagnosis(self, person, code)
                    newDay = utils.get_random_date(person.today)
                    person.today = newDay
                    person.diagnoses.append((diagnosis_code, str(newDay)))
                    code = diagnosis_code
                else:
                    next_diagnosis = get_next_diagnosis(self.get_diagnosis_by_code(code).next_diagnoses)
                    newDay = utils.get_random_date(person.today)
                    person.today = newDay
                    person.diagnoses.append((code, str(newDay)))
                    code = next_diagnosis
        if person.new_year():
            person.today = date(person.today.year + 1, 1, 1)
        if person.die():
            person.alive = False
        self.generate(person, code)
