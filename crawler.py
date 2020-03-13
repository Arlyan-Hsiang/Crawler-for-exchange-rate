import sys
from PyQt5.QtWidgets import QDialog, QApplication 
from ExchangeUI import Ui_NZDtoTWD
import urllib.request as req
import bs4
class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NZDtoTWD()
        self.ui.setupUi(self)
        #Click
        self.ui.pushButton.clicked.connect(self.pushButton_Click)
        self.show()
    
    def pushButton_Click(self):
        #read the websit
        url="http://rate.megabank.com.tw/bulletin02_02.asp"
        #Establish request object
        request=req.Request(url)
        with req.urlopen(request) as response:
            data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        #find the target cell
        exchange_details=root.find_all("tr", class_="tbcolor2")
        read=0
        for exchange_detail in exchange_details:
             exchange_lists = exchange_detail.find_all("td")
             if(read ==5):break
             for exchange_list in exchange_lists:
                if(read > 0 and read < 5):
                    if(read == 1):
                        self.ui.labelA.setText(exchange_list.string)
                    elif(read == 2):
                        self.ui.labelB.setText(exchange_list.string)
                    elif(read == 3):
                        self.ui.labelC.setText(exchange_list.string)
                    else:
                        self.ui.labelD.setText(exchange_list.string)
                    read += 1
                if(exchange_list.string == "紐西蘭幣[NZD]"):
                    read = 1
                
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())


   #更人性爬蟲
    # request=req.Request(url,headers={
    #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"})
    

    #找出匯率欄位
    #  exchange_details=root.find_all("tr")
    #  with open("Exchange.txt", mode="w", encoding="utf-8") as file:
    #      file.writelines(thead+"\n")
    #      for exchange_detail in exchange_details:
    #          exchange_lists = exchange_detail.find_all("td")
    #          currency_detail = ""
    #          for exchange_list in exchange_lists:
    #              currency_detail += exchange_list.string + "             "
    #          file.writelines(currency_detail+"\n")



    
