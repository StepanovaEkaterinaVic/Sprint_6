from faker import Faker
import random
from datetime import datetime, timedelta


def generate_registration_data():
    faker = Faker('ru_RU')
    gender = random.choice(['male', 'female'])
    if gender == 'male':
        name = faker.first_name_male()
        last_name = faker.last_name_male()
    else:
        name = faker.first_name_female()
        last_name = faker.last_name_female()
    street = faker.street_name()
    phone_number = '+7' + ''.join([str(random.randint(0, 9)) for _ in range(10)])
    return name, last_name, street, phone_number


def generate_start_order_data():
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    formatted_date = tomorrow.strftime("%d.%m.%Y")
    return formatted_date

