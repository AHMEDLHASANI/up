from requests import get
from random import sample
from colorama import Fore
from hashlib import md5
def NotExist(text):
    return Fore.RED+str(text)+Fore.WHITE
def Exist(text):
    return Fore.GREEN+str(text)+Fore.WHITE


codes = {"200":True,"403":False}
num = 17167076764867528
while True :
    num += 1
    g = md5(str(num).encode("UTF-8")).hexdigest()
    page = f"https://ug-drru.media.dbankcloud.ru/nsp-campaign-res-drru/campaignpreview/{g}/index.html?page=campaign&productId=&campaignId=147488&agChannel=share&shareTo=com.android.bluetooth&shareFrom=appmarket&shareIds=c5f800fd739f4a43a63e221759bec2ab_com.android.bluetooth&callType=SHARE"
    
    res = get(page).status_code
    if codes[str(res)]:
        print("[",Exist(page),"]","[",Exist(res),"]")
        with open("ExistingLinks.txt","a") as linksFile :
            linksFile.write("\n"+page)
    else :
        print("[",NotExist(page),"]","[",NotExist(res),"]")
