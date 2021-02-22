import yaml
import os
from category import Category
from diagnosis import Diagnosis
import utils.utils as utils


def get_diagnosis(filename):
    with open(filename) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        age = data['age']
        return Diagnosis(data['code'], age)


def get_category(filename, diagnoses):
    with open(filename) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        age = data['age']
        return Category(data['code'], age, None, diagnoses, None)


def scale_ages(objects):
    for sex in ["M", "W"]:
        for a in utils.AGES:
            scaled = utils.scale_down([obj.age[a][sex] for obj in objects])
            for index, value in enumerate(scaled):
                objects[index].age[a][sex] = value
    return objects


def get_model():
    categories = []
    category_by_code = dict()
    for categoryFile in os.listdir('../data/category/'):
        diagnoses = []
        for diagnosisFile in os.listdir('../data/diagnosis/' + categoryFile[:-4]):
            diagnoses.append(get_diagnosis('../data/diagnosis/' + categoryFile[:-4] + '/' + diagnosisFile))
        diagnoses = scale_ages(diagnoses)
        category = get_category('../data/category/' + categoryFile, diagnoses)
        category_by_code[category.code] = category
        categories.append(category)

    categories = scale_ages(categories)

    initial = Category('INITIAL', None, categories, None, None)
    return initial
