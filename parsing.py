import yaml
import os
from models.category import Category
from models.diagnosis import Diagnosis
from models.model import Model
import utils.utils as utils


def get_diagnosis(filename):
    with open(filename) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        age = data['age']
        next_diagnoses = scale_next_diagnoses(data['next'])
        return Diagnosis(data['code'], age, next_diagnoses)


def get_category(filename):
    with open(filename) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        age = data['age']
        return Category(data['code'], age)


def scale_next_diagnoses(next_diagnoses):
    scaled = utils.scale_down([item for item in next_diagnoses.values()])
    index = 0
    for code in next_diagnoses:
        next_diagnoses[code] = scaled[index]
        index += 1
    return next_diagnoses


def scale_ages(objects):
    for sex in ["M", "W"]:
        for a in utils.AGES:
            scaled = utils.scale_down([obj.age[a][sex] for obj in objects])
            for index, value in enumerate(scaled):
                objects[index].age[a][sex] = value
    return objects


def emergence_probabilities():
    probs = yaml.load(open('data/probability/diagnosesProbability.yml'), Loader=yaml.FullLoader)
    summa = 0
    for sex in ["M", "W"]:
        for age in utils.AGES:
            summa += probs[age][sex]
    for sex in ["M", "W"]:
        for age in utils.AGES:
            probs[age][sex] /= summa
    return probs


def get_model(path=""):
    model = Model()
    for categoryFile in os.listdir(path + 'data/category/'):
        category = get_category(path + 'data/category/' + categoryFile)
        model.add_edge('INITIAL', category.code)
        model.add_category(category)
        diagnoses = []
        for diagnosisFile in os.listdir(path + 'data/diagnosis/' + categoryFile[:-4]):
            diagnosis = get_diagnosis(path + 'data/diagnosis/' + categoryFile[:-4] + '/' + diagnosisFile)
            for next_diagnosis in diagnosis.next_diagnoses:
                model.add_edge(diagnosis.code, next_diagnosis)
            model.add_diagnosis(diagnosis)
            diagnoses.append(diagnosis)
            model.add_edge(category.code, diagnosis.code)

        for diagnosis in scale_ages(diagnoses):
            model.add_diagnosis(diagnosis)
    model.categories = scale_ages(model.categories)
    emergence_probabilities()
    model.diagnoses_emergence_probabilities = emergence_probabilities()
    return model
