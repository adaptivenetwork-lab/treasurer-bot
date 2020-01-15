import gspread
import config
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials/credentials.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open(config.GDRIVE_SHEET_NAME)

def get_worksheet():
    worksheet_list = spreadsheet.worksheets()
    return [worksheet.title for worksheet in worksheet_list]

def getKas(year):
    kas_worksheet = spreadsheet.worksheet(year)
    kas_lists = kas_worksheet.get_all_records()
    return kas_lists