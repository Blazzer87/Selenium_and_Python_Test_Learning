from faker import *

def firstname():
     return Faker("ru_RU").first_name_female()               # Болеслав
print(firstname())

def lastname():
    return Faker("ru_RU").last_name_female()                  # Фадеев
print(lastname())

def secondname():
    return Faker("ru_RU").first_name_male() + 'овна'          # Викториновна
print(secondname())

def phone_number():
    return Faker("ru_RU").phone_number() - "("
print(phone_number())





