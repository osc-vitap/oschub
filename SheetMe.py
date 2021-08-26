import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oschub.settings")

import django

django.setup()

import gspread
from google.oauth2 import service_account
from eventreg.models import EventUserData, Event
from accounts.models import MailList
import datetime
from decouple import config
import json


# creates a spreadSheet.
def createSpreadSheet(mailList, title="NewSpreadsheet"):
    try:
        global createdNewSpreadSheet
        if not createdNewSpreadSheet:
            sheet = service.create(title)
            print("[$] SpreadSheet ID: " + str(sheet.id))
            for index, emailid in enumerate(mailList):
                # Commented code cause Ownership Access error
                # if index == 0:
                #     sheet.share(emailid, perm_type="user", role="owner")
                # else:
                sheet.share(emailid, perm_type="user", role="writer", notify=True)
                print("Shared sheet to " + emailid)
            createdNewSpreadSheet = True
    except gspread.exceptions.APIError as error:
        print("API Error: Trying Again !!")
        print(error)
        createSpreadSheet(mailList, title)  # If API error then try again


def createSheet(title="EventName", row="10000", col="25"):
    try:
        global createdNewSpreadSheet
        sheet = service.open("Events")  # opens the file "Events"
        print("[x] Found spreadsheet 'Events' ")
        if createdNewSpreadSheet:
            sheet.add_worksheet(title, rows=row, cols=col)
            tmp = sheet.get_worksheet(0)
            sheet.del_worksheet(tmp)
            print(f"[!] Renamed default Sheet1 to {title}")
            createdNewSpreadSheet = False
        else:
            sheet.add_worksheet(title, rows=row, cols=col)
            print("[x] Added sheet - " + title)

        worksheet = sheet.worksheet(title)
        worksheet.append_row(["Reg No", "Name", "Email", "Registered", "Attended"])
        worksheet.format(
            "A1:E1", {"horizontalAlignment": "CENTER", "textFormat": {"bold": True}}
        )
        print(f"[x] Added Header data to the sheet {title}")
        return worksheet

    except gspread.exceptions.SpreadsheetNotFound:
        print('[!] "Events" SpreadSheet not found, attempting to create a new one')
        createSpreadSheet(admin_mail, "Events")
        createSheet(title)


def getCompletedEvents():
    # Filtering out the events that are over
    events = Event.objects.all().filter(
        eventDate__lt=datetime.date.today()
    )  # gets the events with date before today
    eventlist = []
    for event in events:
        eventlist.append(event.eventName.replace(':', '|'))
    events = Event.objects.filter(eventDate=datetime.date.today()).filter(
        eventEndTime__lt=datetime.datetime.now().strftime("%H:%M:%S")
    )
    for event in events:
        eventlist.append(event.eventName.replace(':', '|'))
    return eventlist


def updateData():
    admin_mail_latest = getAdminMail()
    event_list = getCompletedEvents()
    # If spreadsheet not found then make a new one
    try:
        sheet = service.open("Events")
    except gspread.exceptions.SpreadsheetNotFound:
        print('[!] "Events" SpreadSheet not found, attempting to create a new one')
        createSpreadSheet(admin_mail, "Events")

    sheet = service.open("Events")

    #  sharing the sheet once again to share the file with newly added user
    for email_id in admin_mail_latest:
        if email_id not in admin_mail:
            sheet.share(email_id, perm_type="user", role="writer", notify=True)
            print("Shared sheet to " + email_id)

    #  get all the available worksheets
    worksheet = sheet.worksheets()
    sheetList = []
    for work in worksheet:
        sheetList.append(work.title)

    # getting user data for the events that are over
    for event in event_list:
        studentList = []
        if event in sheetList:
            print(f"[!] Skipping the Sheet, the worksheet {event} already exists !!")
        else:
            students = EventUserData.objects.filter(eventName__eventName=event.replace('|', ':'))
            for student in students:
                studentList.append(
                    [
                        student.studentReg,
                        student.studentName,
                        student.studentEmail,
                        "Yes" if student.studentRegistered else "No",
                        "Yes" if student.studentCheckedIn else "No",
                    ]
                )
            worksheet = createSheet(event)
            worksheet.batch_update(
                [{"range": f"A2:E{len(studentList) + 1}", "values": studentList}]
            )
            print("[x] Added user data set to sheet " + event)


def getAdminMail():
    admin_mail = []
    mailList = MailList.objects.all()
    for mail in mailList:
        admin_mail.append(mail.email)

    return admin_mail


def delAllSpreadsheet():
    for spreadsheet in service.openall():
        service.del_spreadsheet(spreadsheet.id)
        print("deleted " + spreadsheet.title + " || " + spreadsheet.id)


# CAUTION: First Email is given owner access, rest all emails are given writer access due to API restrictions.
createdNewSpreadSheet = False
admin_mail = getAdminMail()
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

credential_info = json.loads(config("CREDENTIALS"))
credential = service_account.Credentials.from_service_account_info(credential_info, scopes=SCOPE)
service = gspread.authorize(credential)

if __name__ == "__main__":
    # Use the following method to update data to the google spreadsheet
    updateData()

    # Use the following method to delete all the existing spreadsheets of the bot account
    # delAllSpreadsheet()
