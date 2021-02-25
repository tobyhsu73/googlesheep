import serial
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
auth_json_path = 'D:\lab\py2\idslab-d70a2e57470c.json'
gss_scopes = ['https://spreadsheets.google.com/feeds' ]
#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)
#開啟 Google Sheet 資料表
spreadsheet_key = '12zd8heVb3UrTjHjNx70Xy8ku5WWE4cY2TtDNwDRt6do'
sheet = gss_client.open_by_key(spreadsheet_key)
worksheet = sheet.add_worksheet(title="11111", rows="100", cols="20")
worksheet = sheet.get_worksheet(0)
sheet.del_worksheet(worksheet)


