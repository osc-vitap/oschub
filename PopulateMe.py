import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oschub.settings')

import django

django.setup()

from faker import Faker
import random


def genReg(num=1000):
    regList = []
    while len(regList) < 1000:
        regList.append(
            random.choice(['17', '18', '19', '20']) + random.choice(['BCE', 'MIS', 'BEC', 'DAF', 'BBA']) + str(
                random.randint(1111, 9999)))
        regList = list(set(regList))

    return list(set(regList))


def populateEventUserData(num=1000):
    fake = Faker()

    nameList = [fake.first_name() for i in range(num + 1)]
    regList = genReg()
    # Email Generation
    emailList = []
    for i in range(num):
        emailList.append(nameList[i].lower() + '.' + regList[i].lower() + '@vitap.ac.in')
    # Student Data List generation
    studentData = []
    for i in range(num):
        student = [nameList[i], regList[i], emailList[i]]
        studentData.append(student)

    return studentData


if __name__ == '__main__':
    print(populateEventUserData())
