import random


class Category:

    def __init__(self, code, age):
        self.code = code
        self.age = age


def get_category(model, person):
    categories = {i: model.get_category_by_code(i).age[person.get_age_range()][person.sex] for i in
                  model.graph['INITIAL']}
    categories = dict(sorted(categories.items(), key=lambda category: category[1]))

    probability = random.uniform(0, 1)
    previous = 0

    for code, prob in categories.items():
        if prob + previous >= probability:
            return code
        else:
            previous += prob
