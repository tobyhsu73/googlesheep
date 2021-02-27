import serial
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
auth_json_path = 'D:\lab\py2\idslab-d70a2e57470c.json'#金鑰位址
gss_scopes = ['https://spreadsheets.google.com/feeds' ]#google sheet網址照抄

#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)
spreadsheet_key = '12zd8heVb3UrTjHjNx70Xy8ku5WWE4cY2TtDNwDRt6do'#剛剛網址中的那串代碼
sheet = gss_client.open_by_key(spreadsheet_key)#打開google sheet表格
#接著先增加一個工作表(標題，幾列，幾欄)
#worksheet = sheet.add_worksheet(title="one", rows="24", cols="4")
#刪除預設的工作表
#sheet.del_worksheet(sheet.get_worksheet(0))
#第一欄標題
#worksheet.insert_row(['資料順序','T1','T2','T3'], 1)
#每隔兩秒讀一次ds18b20資料，上傳至表格

port = 'COM15'
baud = 115200
ser = serial.Serial(port,baud)
worksheet = sheet.add_worksheet(title='1', rows="24", cols="4")
sheet.del_worksheet(sheet.get_worksheet(0))
for i in range(30):
    s=str(i+2)
    t=1
    
    worksheet.insert_row(['資料順序','T1','T2','T3'], 1)
   
   
        
    for a in range(24):
        
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
        worksheet.insert_row(listdata,t+1)
        t=t+1
        time.sleep(1.5)
        
    
    worksheet = sheet.add_worksheet(title=s, rows="24", cols="4")








