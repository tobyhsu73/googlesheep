import gspread
from oauth2client.service_account import ServiceAccountCredentials
auth_json_path = 'D:\lab\py2\idslab-d70a2e57470c.json'
gss_scopes = ['https://spreadsheets.google.com/feeds' ]
#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)
#開啟 Google Sheet 資料表

spreadsheet_key = '12zd8heVb3UrTjHjNx70Xy8ku5WWE4cY2TtDNwDRt6do'
sheet = gss_client.open_by_key(spreadsheet_key)
worksheet = sheet.get_worksheet(0)
worksheet.update_cell(1, 3, 'Bingo!')
worksheet.update('A1:B2', [[1, 2], [3, 4]])
listdata=["Liu","0912-345678"]
worksheet.insert_row(listdata)

worksheet.insert_row(listdata,5)
worksheet.insert_row(listdata,10)




#sheet = gss_client.open_by_key(spreadsheet_key).worksheet('2')
#sheet.update_acell('D2', '我我我')  #D2加入ABC
#sheet.update_cell(2, 4, '123')   #D2加入ABC(第2列第4行即D2)
#寫入一整列(list型態的資料)
#values = ['A','B','C','D']
#sheet.insert_row(values, 1) #插入values到第1列
#sheet.clear() # 清除 Google Sheet 資料表內容
