import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oschub.settings')

import django

django.setup()

import gspread
from google.oauth2 import service_account
from eventreg.models import EventUserData


# from django.db import models


# creates a spreadSheet.
def createSpreadSheet(mailList, title='NewSpreadsheet'):
    try:
        global createdNewSpreadSheet
        if not createdNewSpreadSheet:
            sheet = service.create(title)
            print('[$] SpreadSheet ID: ' + str(sheet.id))
            for emailid in mailList:
                sheet.share(emailid, 'user', 'owner')
                print('Shared sheet to ' + emailid)
            createdNewSpreadSheet = True
    except gspread.exceptions.APIError:
        print('API Error: Trying Again !!')
        createSpreadSheet(mailList, title)  # If API error then try again


def createSheet(title='EventName', row='10000', col='25'):
    try:
        global createdNewSpreadSheet
        sheet = service.open('Events')  # opens the file "Events"
        print("[x] Found spreadsheet 'Events' ")
        if createdNewSpreadSheet:
            sheet.add_worksheet(title, rows=row, cols=col)
            tmp = sheet.get_worksheet(0)
            sheet.del_worksheet(tmp)
            print(f'[!] Renamed default Sheet1 to {title}')
            createdNewSpreadSheet = False
        else:
            sheet.add_worksheet(title, rows=row, cols=col)
            print('[x] Added sheet - ' + title)

        worksheet = sheet.worksheet(title)
        worksheet.append_row(["Reg No", "Name", "Email", "Registered", "Attended"])
        worksheet.format('A1:E1', {'horizontalAlignment': 'CENTER', 'textFormat': {'bold': True}})
        print(f'[x] Added Header data to the sheet {title}')

        # add code below to batchupadte data to sheets
    except gspread.exceptions.SpreadsheetNotFound:
        print('[!] "Events" SpreadSheet not found, attempting to create a new one')
        createSpreadSheet(admin_mail, 'Events')
        createSheet(title)


def getModel(obj, eventID):
    data = obj.objects.filter(eventName=eventID)
    val = data[0]
    print(val.studentEmail)


# client email: kodereaper@gsheettesting-160850134856.iam.gserviceaccount.com
admin_mail = ['kodetester.gsheets@gmail.com']  # add all the admin emails to share the sheet with them
createdNewSpreadSheet = False
SCOPE = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credential = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPE)
service = gspread.authorize(credential)

if __name__ == '__main__':
    createSheet('TestNewSheet')
