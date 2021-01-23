import gspread
from oauth2client.service_account import ServiceAccountCredentials


# creates a spreadSheet.
def createSpreadSheet(mailList, title='NewSpreadsheet'):
    try:
        global createdNewSpreadSheet
        sheet = service.create(title)
        print('[$] SpreadSheet ID: ' + str(sheet.id))
        for emailid in mailList:
            sheet.share(emailid, 'user', 'owner')
        createdNewSpreadSheet = True
    except gspread.exceptions.APIError:
        createSpreadSheet(mailList, title)  # If API error then try again


def createSheet(title='EventName'):
    try:
        global createdNewSpreadSheet
        sheet = service.open('Events')  # opens the file "Events"
        print("[x] Found spreadsheet 'Events' ")
        if createdNewSpreadSheet:
            sheet.add_worksheet(title, rows='10000', cols='20')
            tmp = sheet.get_worksheet(0)
            sheet.del_worksheet(tmp)
            print(f'[!] Renamed Sheet1 to {title}')
            createdNewSpreadSheet = False
        else:
            sheet.add_worksheet(title, rows='10000', cols='20')
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


# client email: kodereaper@gsheettesting-160850134856.iam.gserviceaccount.com
admin_mail = ["kodetester.gsheets@gmail.com"]  # add all the admin emails to share the sheet with them
createdNewSpreadSheet = False
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
service = gspread.authorize(credential)

if __name__ == '__main__':
    createSheet('TestingSheet')
