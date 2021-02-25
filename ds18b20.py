import serial
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
port = 'COM15'
baud = 115200
t=0
ser = serial.Serial(port,baud)
auth_json_path = 'D:\lab\py2\idslab-d70a2e57470c.json'
gss_scopes = ['https://spreadsheets.google.com/feeds' ]
#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)
#開啟 Google Sheet 資料表
spreadsheet_key = '1SP5U7RmoU-_cDnrPJNAp2gkWDRq4bSE8JrOllBJzr9k'
sheet = gss_client.open_by_key(spreadsheet_key).sheet1
sheet.clear()
listtitle=["時間","溫度1","溫度2","溫度3"]
sheet.append_row(listtitle)
while True:
    
    ser.flushInput()
    tem1 = ser.read(5)
    t1=bytes.decode(tem1)
    print(tem1)
    tem2 = ser.read(5)
    t2=bytes.decode(tem2)
    print(tem2)
    tem3 = ser.read(5)
    t3=bytes.decode(tem3)
    print(tem3)

    listdata=[t,t1,t2,t3]
    sheet.append_row(listdata)
    t=t+1
    time.sleep(2)


