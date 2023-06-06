import pyautogui as pg
import schedule
import time


index = 1
scheduleIndex = 0
cusmin = int(input("Set Routine Min : "))

def job():

    print("schedule started ")

    httpfriends = pg.locateOnScreen('image/httpfriends.PNG',confidence = 0.6)  
    if(httpfriends != None) :
        print("httpfriends : ", httpfriends)
        
        pg.moveTo(httpfriends.left+500, httpfriends.top+10)    
        pg.click()
        time.sleep(1)
        pg.press('enter')        
    else:
        print("There is no httpfriends")

    nft = 20
    for i in range(nft):
        j = 0
        for j in range(5):        
            luggage = pg.locateOnScreen('image/findyourluggage.PNG',confidence = 0.8)
            if(luggage != None):
                print("luggage : ", luggage)            
                pg.moveTo(luggage.left+10, luggage.top+10)
                pg.click()                            
                break
            else:
                print("Nothing to get")
                time.sleep(1)
                if(j == 4):
                    i = nft                      
                    break

        if(i == nft):
            break        
        
        j = 0
        for j in range(10):        
            time.sleep(2)            
            allow = pg.locateOnScreen('image/allow.PNG',confidence = 0.8)
            if(allow != None):
                print("allow : ", allow)    
                time.sleep(5)            
                pg.moveTo(allow.left, allow.top)
                pg.click()
                break
            else:
                print("allow is none ")

        for k in range(10):        
            time.sleep(1)
            ok = pg.locateOnScreen('image/ok.PNG',confidence = 0.8)
            if(ok != None):
                print("ok : ", ok)                
                pg.moveTo(ok.left, ok.top)
                pg.click()
                break
            else:
                print("ok is none : ")

        httpfriends = pg.locateOnScreen('image/httpfriends.PNG',confidence = 0.6)  
        if(httpfriends != None) :
            print("httpfriends : ", httpfriends)
            
            pg.moveTo(httpfriends.left+500, httpfriends.top+10)    
            pg.click()
            time.sleep(1)
            pg.press('enter')        
            time.sleep(1)
        else:
            print("There is no httpfriends")
                

    httpfriends = pg.locateOnScreen('image/httpfriends.PNG',confidence = 0.6)  
    if(httpfriends != None) :
        print("httpfriends : ", httpfriends)        
        pg.moveTo(httpfriends.left+500, httpfriends.top+10)    
        pg.click()
        time.sleep(1)
        pg.press('enter')        
    else:
        print("There is no httpfriends")

    i = 0
    for i in range(nft):
            
        for k in range(5):     
            time.sleep(1)          
            start = pg.locateOnScreen('image/startatour.PNG',confidence = 0.8)
            if(start != None) :
                print("start : ", start)                
                pg.moveTo(start.left, start.top)
                pg.click() 
                break     
            else:
                if(k == 4):
                    i = nft        
                print("Can't Start a Tour")

        if(i == nft):
            break

        time.sleep(1)
        oknext = pg.locateOnScreen('image/oknext.PNG',confidence = 0.8)  
        if(oknext != None) :
            print("oknext : ",oknext)            
            pg.moveTo(oknext.left, oknext.top)
            pg.click()   
        else:
            print("There is no ok next")


        time.sleep(1)
        spacetour = pg.locateOnScreen('image/spacetour.PNG',confidence = 0.9)  
        if(spacetour != None) :
            print("spacetour : ", spacetour)            
            pg.moveTo(spacetour.left, spacetour.top)
            pg.click()   
        else:
            print("There is no space tour")


        time.sleep(1)
        selectKIKI = pg.locateOnScreen('image/selectKIKI.PNG',confidence = 0.8)  
        if(selectKIKI != None) :
            print("selectKIKI : ", selectKIKI)            
            pg.moveTo(selectKIKI.left, selectKIKI.top)
            pg.click()   
        else:
            print("There is no selectKIKI")


        time.sleep(1)
        selectyourfriend = pg.locateOnScreen('image/selectyourfriend.PNG',confidence = 0.8)  
        if(selectyourfriend != None) :
            print("selectyourfriend : ", selectyourfriend)            
            pg.moveTo(selectyourfriend.left, selectyourfriend.top+200)
            pg.click()   
        else:
            print("There is no selectyourfriend")

        time.sleep(1)
        close = pg.locateOnScreen('image/close.PNG',confidence = 0.8)  
        if(close != None) :
            print("close : ", close)     
            i = nft
            break
        else:
            print("There is no close")

        if(i == nft):
            break


        time.sleep(1)
        confirm = pg.locateOnScreen('image/confirm.PNG',confidence = 0.8)  
        if(confirm != None) :
            print("confirm : ", confirm)            
            pg.moveTo(confirm.left, confirm.top)
            pg.click()   
        else:
            print("There is no confirm")

        time.sleep(1)
        Ikikihave = pg.locateOnScreen('image/Ikikihave.PNG',confidence = 0.8)  
        if(Ikikihave != None) :
            print("Ikikihave : ", Ikikihave)            
            pg.moveTo(Ikikihave.left+10, Ikikihave.top+15)
            pg.click()  
            
        else:
            print("There is no Ikikihave")

        time.sleep(1)
        complete = pg.locateOnScreen('image/complete.PNG',confidence = 0.8)  
        if(complete != None) :
            print("complete : ", complete)            
            pg.moveTo(complete.left, complete.top)
            pg.click()   
        else:
            print("There is no complete")

        j =0
        for j in range(10):        
            time.sleep(2)            
            allow = pg.locateOnScreen('image/allow.PNG',confidence = 0.8)
            if(allow != None):
                print("allow : ", allow)
                time.sleep(5)                            
                pg.moveTo(allow.left, allow.top)
                time.sleep(1)
                pg.click()
                break
            else:
                print("allow is none ")
  
    firstx = pg.locateOnScreen('image/firstx.PNG',confidence = 0.8)  
    if(firstx != None) :
        print("firstx : ", firstx)        
        pg.moveTo(firstx.left+10, firstx.top+10)
        pg.click()   
    else:
        print("There is no firstx")

    j =0
    for j in range(5):    
        time.sleep(1)                       
        secondx = pg.locateOnScreen('image/secondx.PNG',confidence = 0.8)  
        if(secondx != None) :
            print("secondx : ", secondx)            
            pg.moveTo(secondx.left+15, secondx.top+15)
            pg.click()
            break
        else:
            print("There is no secondx")

    global scheduleIndex
    print("Job Done : ", scheduleIndex)
    print("waiting for next schedule")
    scheduleIndex += 1


def alram():
    global index
    print("alram : ", index * 10)
    index += 1

def start_job():   
   job()   
   schedule.every(cusmin).minutes.do(job)
   schedule.every(10).minutes.do(alram)

start_job()

while True:
    schedule.run_pending()
    time.sleep(1)