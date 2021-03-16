from category import *
from diagnosis import *
from datetime import date
import random


class Model:

    def __init__(self):
        self.categories = []
        self.diagnoses = []
        self.diagnoses_emergence_probabilities = {}
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
        if random.random() <= self.diagnoses_emergence_probabilities[person.get_age_range()][person.sex]: #person.new_diagnosis():
            if code == 'INITIAL':
                category_code = get_category(self, person)
                diagnosis_code = get_category_diagnosis(self, person, category_code)
                if diagnosis_code is not None:
                    person.add_diagnosis(diagnosis_code)
                    code = diagnosis_code
                else:
                    code = 'INITIAL'
            else:
                if self.get_category_by_code(code) is not None:
                    diagnosis_code = get_category_diagnosis(self, person, code)
                    person.add_diagnosis(diagnosis_code)
                    code = diagnosis_code
                else:
                    next_diagnosis = get_next_diagnosis(self.get_diagnosis_by_code(code).next_diagnoses)
                    if next_diagnosis != 'INITIAL':
                        person.add_diagnosis(next_diagnosis)
                    code = next_diagnosis
        if person.new_year():
            person.today = date(person.today.year + 1, 1, 1)
        if person.die():
            person.alive = False
        self.generate(person, code)
