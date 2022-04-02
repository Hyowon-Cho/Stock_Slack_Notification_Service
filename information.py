import win32com.client
 

objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("Plus cannot connect. ")
    exit()
 
# # Finding the object price
objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
objStockMst.SetInputValue(0, 'A005930')   #For example, Samsung
objStockMst.BlockRequest()
 
# Communication Error?
rqStatus = objStockMst.GetDibStatus()
rqRet = objStockMst.GetDibMsg1()
print("Communication Status", rqStatus, rqRet)
if rqStatus != 0:
    exit()
 
#price
code = objStockMst.GetHeaderValue(0)  # CODE
name= objStockMst.GetHeaderValue(1)  # NAME
time= objStockMst.GetHeaderValue(4)  # TIME
cprice= objStockMst.GetHeaderValue(11) # END
diff= objStockMst.GetHeaderValue(12)  # DIFF
open= objStockMst.GetHeaderValue(13)  # OPEN
high= objStockMst.GetHeaderValue(14)  # HIGH
low= objStockMst.GetHeaderValue(15)   # LOW
offer = objStockMst.GetHeaderValue(16)  # OFFER
bid = objStockMst.GetHeaderValue(17)   # BID
vol= objStockMst.GetHeaderValue(18) # VOLUME
vol_value= objStockMst.GetHeaderValue(19)  # VOL_VAL
 
# EXPECTATION
exFlag = objStockMst.GetHeaderValue(58) #EXFLAG
exPrice = objStockMst.GetHeaderValue(55) #EXPRICE
exDiff = objStockMst.GetHeaderValue(56) #EXDIFF
exVol = objStockMst.GetHeaderValue(57) #EXVOL
 
 
print("CODE", code)
print("NAME", name)
print("TIME", time)
print("CPRICE", cprice)
print("DIFF", diff)
print("OPEN", open)
print("HIGH", high)
print("LOW", low)
print("OFFER", offer)
print("BID", bid)
print("VOL", vol)
print("VOL_VAL", vol_value)
 
 
if (exFlag == ord('0')):
    print("WHEN: Simultaneous Call and Non-Occupational Time")
elif (exFlag == ord('1')) :
    print("WHEN: Simultaneous Call Time")
elif (exFlag == ord('2')):
    print("When: Done or Doing")
 
print("VOLUME COMPARED TO EXPECTED PRICE")
print("EXPECTED PRICE", exPrice)
print("EXPECTED PRICE DIFFERANCE", exDiff)
print("EXPECTED VOLUME", exVol)
