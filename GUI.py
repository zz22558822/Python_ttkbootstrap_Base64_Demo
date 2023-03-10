# 引入 tkinter 模組
import tkinter as tk
# 使用ttk主題
from ttkbootstrap import Style
style = Style(theme="darkly")
# 使用彈窗
from tkinter import messagebox
# 載入os套件，處理文件和目錄
import os




# -------------------------(視窗設定)-------------------------
# 使用 Tkinter 建立的視窗
# # 建立主視窗 Frame
# window = tk.Tk()

# 使用 ttkbootstrap 建立的視窗
window = style.master

# 設定視窗標題
window.title('GUI')
# 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)
window.geometry("300x200+250+150")
# 視窗是否可以縮放，寬、高
window.resizable(False, False)
# 設定視窗最大值
window.maxsize(600, 400)
# 設定視窗最小值
window.minsize(300, 200)
# # 設定視窗圖標 (打包時還須獨立檔案)
# window.iconbitmap('icon.ico')
# 設定視窗的背景顏色 可使用色碼或名稱
# window.configure(background='black')
# 把視窗變成ToolWindow Style，設置為 0 時關閉
window.attributes("-toolwindow", 0) 
# 將視窗設為置頂視窗，設置為 0 時關閉
window.attributes("-topmost", 0)
# 啟動時最大化
# window.state("zoomed")
# window.iconify() # 最小化使用方法
# window.deiconify() # 還原最小化


# -------------------------(將Icon加入的方法)-------------------------
# 這邊處理icon.py生成Base64的Icon圖標
from icon import img # 從icon.py中取得img變數
import base64 # 同樣需要base64函式庫
ico = open('icon.ico', 'wb+')
ico.write(base64.b64decode(img)) # 寫一個icon出來
ico.close()
window.iconbitmap('icon.ico') # 將icon嵌上視窗
os.remove('icon.ico') # 把剛剛用完的檔案刪掉
# -------------------------------------------------------------------


# -------------------------(主程式)-------------------------

# 彈窗函式
def pop_up():
    # 代表彈出視窗的標題(title)與要顯示的文字(index)
    messagebox.showinfo("測試使用", "成功")

# 建立按鈕
button = tk.Button(window,text = '測試使用按鈕',command = pop_up)

# 以預設方式排版按鈕
button.pack(side="bottom")
































# 程式常駐執行
window.mainloop()




# 打包的方法
# pyinstaller .\Python的GUI程式.py -F -i .\logo.ico -w --collect-all ttkbootstrap
# pyinstaller -F -w -i .\logo.ico .\Python的GUI程式.py