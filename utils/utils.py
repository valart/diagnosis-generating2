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
    '0-4',
    '5-9',
    '10-14',
    '15-19',
    '20-24',
    '25-29',
    '30-34',
    '35-39',
    '40-44',
    '45-49',
    '50-54',
    '55-59',
    '60-64',
    '65-69',
    '70-74',
    '75-79',
    '80-84',
    '85-89',
    '90-94'
]
