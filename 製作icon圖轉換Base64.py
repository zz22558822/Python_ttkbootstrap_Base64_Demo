import base64 # base64可以將binary檔案轉成unicode格式
icon = open('icon.ico', 'rb') # 使用binary的格式讀入icon
b64str = base64.b64encode(icon.read()) # 轉成unicode格式
icon.close()
write = 'img = %s' % b64str # 放到名為img的變數
f = open('icon.py', 'w+') # 寫到icon.py中
f.write(write)
f.close()