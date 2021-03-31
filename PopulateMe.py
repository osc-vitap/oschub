import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oschub.settings")

import django

django.setup()

from faker import Faker
import random
from eventreg.models import Event, EventUserData
from SheetMe import getCompletedEvents


def genReg(num=1000):
    regList = []
    while len(regList) < 1000:
        regList.append(
            random.choice(["17", "18", "19", "20"])
            + random.choice(["BCE", "MIS", "BEC", "DAF", "BBA"])
            + str(random.randint(1111, 9999))
        )
        regList = list(set(regList))

    return list(set(regList))


def populateEventUserData(num=1000):
    fake = Faker()

    nameList = [fake.name() for i in range(num + 1)]
    regList = genReg()
    # Email Generation
    emailList = []
    for i in range(num):
        emailList.append(
            nameList[i].split(" ")[0].lower()
            + "."
            + regList[i].lower()
            + "@vitap.ac.in"
        )
    # Student Data List generation
    studentData = []
    eventList = []
    completedEvents = getCompletedEvents()
    events = Event.objects.all()

    for event in events:
        eventList.append(event.eventName)

    for event in [temp for temp in eventList if temp not in completedEvents]:
        for eventData in Event.objects.filter(eventName=event):
            for i in range(num):
                student = [
                    eventData,
                    nameList[i],
                    regList[i],
                    emailList[i],
                    True,
                    random.choice([True, False]),
                ]
                studentData.append(student)

    return studentData


if __name__ == "__main__":
    modelData = populateEventUserData(500)
    for data in modelData:
        row = EventUserData(
            eventName=data[0],
            studentName=data[1],
            studentReg=data[2],
            studentEmail=data[3],
            studentRegistered=data[4],
            studentCheckedIn=data[5],
        )
        row.save()
    print("Added data, check database.")
