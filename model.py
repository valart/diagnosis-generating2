from category import *
from diagnosis import *
from datetime import date


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
                person.categories.append((category_code, str(person.today.year - date.today().year)))
                diagnosis_code = get_category_diagnosis(self, person, category_code)
                if diagnosis_code is not None:
                    person.add_diagnosis(diagnosis_code)
                    code = diagnosis_code
                else:
                    code = 'INITIAL'
            else:
                if self.get_category_by_code(code) is not None:
                    person.categories.append((code, str(person.today.year - date.today().year)))
                    diagnosis_code = get_category_diagnosis(self, person, code)
                    person.add_diagnosis(diagnosis_code)
                    code = diagnosis_code
                else:
                    person.add_diagnosis(code)
                    next_diagnosis = get_next_diagnosis(self.get_diagnosis_by_code(code).next_diagnoses)
                    code = next_diagnosis
        if person.new_year():
            person.today = date(person.today.year + 1, 1, 1)
        if person.die():
            person.alive = False
        self.generate(person, code)
