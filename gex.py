import gspread
from oauth2client.service_account import ServiceAccountCredentials
auth_json_path = 'D:\lab\py2\idslab-d70a2e57470c.json'
gss_scopes = ['https://spreadsheets.google.com/feeds' ]
#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)
#開啟 Google Sheet 資料表

spreadsheet_key = '1SP5U7RmoU-_cDnrPJNAp2gkWDRq4bSE8JrOllBJzr9k'
sheet = gss_client.open_by_key(spreadsheet_key).sheet1
#sheet = gss_client.open_by_key(spreadsheet_key).worksheet('2')
#sheet.update_acell('D2', '我我我')  #D2加入ABC
#sheet.update_cell(2, 4, '123')   #D2加入ABC(第2列第4行即D2)
#寫入一整列(list型態的資料)
#values = ['A','B','C','D']
#sheet.insert_row(values, 1) #插入values到第1列
sheet.clear() # 清除 Google Sheet 資料表內容
listtitle=["姓名","電話",11111]
sheet.append_row(listtitle)  # 標題
listdata=["Liu","0912-345678",1111]
listdata=["Liu","0912-345678",1111]
sheet.append_row(listdata)
sheet.append_row(listdata)
x=sheet.get_all_values()# 資料內容
print(x)