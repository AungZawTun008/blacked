def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "→".join(uuid)
  server = requests.get('https://raw.githubusercontent.com/AungZawTun007/star/main/Paid.txt ').text
  
 

  os.system(" clear")                          
  print("""\033[1;97m
                                         
\033[1;96m  ______   ________  ______   _______  
\033[1;96m /      \ /        |/      \ /       \ 
\033[1;92m/$$$$$$  |$$$$$$$$//$$$$$$  |$$$$$$$  |
\033[1;92m$$ \__$$/    $$ |  $$ |__$$ |$$ |__$$ |
\033[1;96m$$      \    $$ |  $$    $$ |$$    $$< 
\033[1;96m $$$$$$  |   $$ |  $$$$$$$$ |$$$$$$$  |
\033[1;94m/  \__$$ |   $$ |  $$ |  $$ |$$ |  $$ |\033[1;34m𝐏 \033[1;37m
\033[1;94m$$    $$/    $$ |  $$ |  $$ |$$ |  $$ |\033[1;31m 𝐑\033[1;37m
\033[1;96m $$$$$$/     $$/   $$/   $$/ $$/   $$/   \033[1;35m𝐎 \033[1;37m 
                                                                                                                   
                                   
\033[1;96m--------------------------------------------------\033[0m
[👌] \033[1;96mAuthor   : STAR
[👌]\033[1;91m Facebook : STAR
[👌]\033[1;93m Tool     : Test
[👌] \033[1;91mVersion  : \033[1;92m1.0\033[0m
\033[1;96m----------------------------------------------\033[0m""")
  print(f" \033[1;33m  THIS TOOLS IS PAID SO YOU NEED GET APPROVED FIRST\033[1;37m\n")
  print(f"")
  print(f"\x1b[1;92m   contract Admin to Buy this Tools                                                               ");time.sleep (0.1) 
  print(f"")
  print(f"\033[1;32     YOUR  KEY : "+id)
  print(f"")
  print(f"\033[1;31m   COPY YOUR KEY AND SEND TO ADMIN  ");time.sleep(0.1)
  print(f"")
  try:
    httpCaht = requests.get("https://raw.githubusercontent.com/AungZawTun007/star/main/Paid.txt").text
    if id in httpCaht:
      print("\033[1;92m   YOUR KEY APROVED   ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      print(f"\x1b[1;92m    Sorry Bro Your Key not Aproved  ")
      print(f"    Send Wave or Kpay  to Admin and get aproval"); time.sleep(2)
      os.system(f'xdg-open https://wa.me/+959676429641?text='+id)
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == 'main':
     print(logo)
     menu_apikey()
menu_apikey()
logo=("""\033[1;97m
                                         
\033[1;96m  ______   ________  ______   _______  
\033[1;96m /      \ /        |/      \ /       \ 
\033[1;92m/$$$$$$  |$$$$$$$$//$$$$$$  |$$$$$$$  |
\033[1;92m$$ \__$$/    $$ |  $$ |__$$ |$$ |__$$ |
\033[1;96m$$      \    $$ |  $$    $$ |$$    $$< 
\033[1;96m $$$$$$  |   $$ |  $$$$$$$$ |$$$$$$$  |
\033[1;94m/  \__$$ |   $$ |  $$ |  $$ |$$ |  $$ |\033[1;34m𝐏 \033[1;37m
\033[1;94m$$    $$/    $$ |  $$ |  $$ |$$ |  $$ |\033[1;31m 𝐑\033[1;37m
\033[1;96m $$$$$$/     $$/   $$/   $$/ $$/   $$/   \033[1;35m𝐎 \033[1;37m 
                                                                                                                   
                                   
\033[1;96m--------------------------------------------------\033[0m
[👌] \033[1;96mAuthor   : STAR
[👌]\033[1;91m Facebook : STAR
[👌]\033[1;93m Tool     : Test
[👌] \033[1;91mVersion  : \033[1;92m1.0\033[0m
\033[1;96m----------------------------------------------\033[0m""")