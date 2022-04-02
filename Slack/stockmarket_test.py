import win32com.client
 
# Check
objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("Plus cannot connect. ")
    exit()

objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
objStockMst.SetInputValue(0, 'A005930')  
objStockMst.BlockRequest()

rqStatus = objStockMst.GetDibStatus()
rqRet = objStockMst.GetDibMsg1()
print("Connection Status", rqStatus, rqRet)
if rqStatus != 0:
    exit()

offer = objStockMst.GetHeaderValue(16) 

import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2344240035522-2350453218004-uTHHb5qh2tZq5LnioSCSbl18"
 
post_message(myToken,"#stock","Price: " + str(offer))
