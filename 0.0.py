import serial
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
auth_json_path = 'D:\lab\py2\idslab-d70a2e57470c.json'
gss_scopes = ['https://spreadsheets.google.com/feeds' ]
#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)
sh = gss_client.create('A new spreadsheet')