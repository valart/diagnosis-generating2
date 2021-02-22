import datetime
import random


def scale_down(probabilities):
    maximum = sum(probabilities)
    return [x / maximum for x in probabilities] if maximum > 0 else probabilities


def get_random_date(today):
    end_date = datetime.date(today.year + 1, 1, 1)
    time_between_dates = end_date - today
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return today + datetime.timedelta(days=random_number_of_days)


AGES = [
    '0-9',
    '10-19',
    '20-29',
    '30-39',
    '40-49',
    '50-59',
    '60-69',
    '70-79',
    '80-89',
    '90-99',
]
