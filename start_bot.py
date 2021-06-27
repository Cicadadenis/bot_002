from os import system
import os, sys, time
import io
import os, sys
import time

import io
import subprocess
import time


id_us = {}
tk = {}



def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")
        
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
    
    
def backtomenu_option():
	backtomenu = input("    Ваш Выбор > ")

	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print("\nОШИБКА: неверный ввод")
		time.sleep(1)
		restart_program()
 
re = ("\033[1;31m")
gr = "\033[1;31m"
cy = ("\033[1;36m")
 

print(f"""
      
    {re} _{cy}
   {re} / {cy}
   {re} \_{cy}
      
      """)
   
os.system('clear')
time.sleep(0.047)

print(f"""
       
    {re} __{cy}
   {re} / _{cy}
   {re} \__{cy}

        """)

    
os.system('clear')
time.sleep(0.047)
print(f"""
        
     {re}___{cy}
    {re}/ __{cy}
  {re}  \__/{cy}

        """)
        
      
os.system('clear')
time.sleep(0.047)
print(f"""
     
     {re}____({cy}
   {re} / __/ {cy}
    {re}\__/_/{cy}

            """)
      
os.system('clear')
time.sleep(0.047)
print(f"""
         {re} _ {cy}
    {re} ____(_){cy}
    {re}/ __/ / {cy}
    {re}\__/_/\_{cy}
            
  """)


      
os.system('clear')
time.sleep(0.047)

print(f"""
        {re}  _ {cy}   
    {re} ____(_)___{cy}
   {re} / __/ / __/{cy}
   {re} \__/_/\__/\{cy}

                """)


   
os.system('clear')
time.sleep(0.047)

print(f"""
        {re}  _       {cy}
    {re} ____(_)______{cy}
   {re} / __/ / __/ _ {cy}
   {re} \__/_/\__/\_,_{cy}
                  
                  """)


     
os.system('clear')
time.sleep(0.047)

print(f"""
         {re} _          {cy}
     {re}____(_)______ __{cy}
    {re}/ __/ / __/ _ `/ {cy}
    {re}\__/_/\__/\_,_/\_{cy}
                     
                        """)


     
os.system('clear')
time.sleep(0.047)

print(f"""
         {re} _             _{re}
     {re}____(_)______ ____/ {re}
    {re}/ __/ / __/ _ `/ _  /{re}
    {re}\__/_/\__/\_,_/\_,_/\{re}
                         
                         """)


 
os.system('clear')
time.sleep(0.047) 

print(f"""
         {re} _             __   {cy}
     {re}____(_)______ ____/ /__ {cy}
    {re}/ __/ / __/ _ `/ _  / _ `{cy}
    {re}\__/_/\__/\_,_/\_,_/\_,_/{cy}
             
""")


    
os.system('clear')
time.sleep(0.047)

print(f"""
         {re} _             __ {cy}     
     {re}____(_)______ ____/ /__ __{cy}_
    {re}/ __/ / __/ _ `/ _  / _ `/ _{cy}
    {re}\__/_/\__/\_,_/\_,_/\_,_/\__{cy}
                                    {cy}
                                """)


   
os.system('clear')
time.sleep(0.047)


print(f"""
         {re} _             __          {cy}
     {re}____(_)______ ____/ /__ _______{cy}
    {re}/ __/ / __/ _ `/ _  / _ `/ __/ _{cy}
    {re}\__/_/\__/\_,_/\_,_/\_,_/\__/_/ {cy}
                                        {cy}
                                    """)



    
os.system('clear')
time.sleep(0.047)



print(f"""
        {re}      _             __              {cy}
         {re}____(_)______ ____/ /__ ___________{cy}
        {re}/ __/ / __/ _ `/ _  / _ `/ __/ __/ /{cy}
        {re}\__/_/\__/\_,_/\_,_/\_,_/\__/_/  \_,{cy}
        {re}                                /___{cy}
        {re}                            
                                    """)
   



os.system('clear')
time.sleep(0.047)



print(f"""
         {re} _             __                  {cy}
     {re}____(_)______ ____/ /__ ___________ ___{cy}
    {re}/ __/ / __/ _ `/ _  / _ `/ __/ __/ // / {cy}
    {re}\__/_/\__/\_,_/\_,_/\_,_/\__/_/  \_, / .{cy}
                          {re}          /___/_/ {cy}
                                    """)


      
os.system('clear')
time.sleep(0.047)

print(f"""
         {re} _             __                     {cy}
     {re}____(_)______ ____/ /__ ___________ _____ {cy}
    {re}/ __/ / __/ _ `/ _  / _ `/ __/ __/ // / _ \/{cy}
    {re}\__/_/\__/\_,_/\_,_/\_,_/\__/_/  \_, / .__/{cy}
 {re}                                   /___/_/    {cy}
                                    """)


   
os.system('clear')
time.sleep(0.047)

print(f"""
         {re} _             __                       __{cy} 
     {re}____(_)______ ____/ /__ ___________ _____  / /_{cy}
    {re}/ __/ / __/ _ `/ _  / _ `/ __/ __/ // / _ \/ __/{cy}
    {re}\__/_/\__/\_,_/\_,_/\_,_/\__/_/  \_, / .__/\__/{cy}
               {re}                     /___/_/         {cy}
                                                        """)



     
os.system('clear')
time.sleep(0.047)

print(f"""
         {re} _             __                       __   {cy}
     {re}____(_)______ ____/ /__ ___________ _____  / /___{cy}
    {re}/ __/ / __/ _ `/ _  / _ `/ __/ __/ // / _ \/ __/ _{cy}
    {re}\__/_/\__/\_,_/\_,_/\_,_/\__/_/  \_, / .__/\__/\__{cy}
     {re}                               /___/_/           {cy}
                                    
                                                        """)



     
os.system('clear')
time.sleep(0.047)


print(f"""
         {re} _             __                       __       /*******/ {cy}
     {re}____(_)______ ____/ /__ ___________ _____  / /____  /*******/{cy}
    {re}/ __/ / __/ _ `/ _  / _ `/ __/ __/ // / _ \/ __/ _ \/{cy}
    {re}\__/_/\__/\_,_/\_,_/\_,_/\__/_/  \_, / .__/\__/\___/{cy}
         {re}                           /___/_/            {cy}
                                                        """)

time.sleep(0.047)

menu = (f"""

         {re} _             __                       __       /*******/ {cy}
     {re}____(_)______ ____/ /__ ___________ _____  / /____  /*******/{cy}
    {re}/ __/ / __/ _ `/ _  / _ `/ __/ __/ // / _ \/ __/ _ \/{cy}
    {re}\__/_/\__/\_,_/\_,_/\_,_/\__/_/  \_, / .__/\__/\___/{cy}
         {re}                           /___/_/            {cy}
                                                        

  {re} Выберите из меню: {cy}
  
	01) Установка Зависимостей  (установка нужных программ и библиотек)
	02) Настройка Токена
	03) Добавления Администрации 
	04) Список Администрации
        05) Изменить Список Администрации
	06) Старт бота в режиме Screen
    
        xx) Выход
    """)
 
 
clearscreen()

print(menu)       
while True:
    try:
        santet = input("    Ваш Выбор >>> ")
        
        # Установка Зависимостей
        if santet == "01" or santet == "1":
            print('\nУстановка Зависимостей')
            os.system('apt update')
            os.system('apt install python3.9 -y')
            os.system('apt install python3-pip - y')
            os.system('apt install screen -y') 
            os.system('pip3 install aiogram')
            os.system('pip3 install requests')
            os.system('pip3 install bs4')
            os.system('pip3 install pyqiwip2p')
            os.system('pip3 install pyminifier')
            os.system('pip3 install asyncio')
            os.system('pip3 install db-sqlite3')
            restart_program()
            
        # Токен    
        elif santet == "02" or santet == "2":
            print('\nУстановить или Изменить Токен бота')
            import configparser
            import requests
            
            tk = input('Введите токен бота: ')
            config = configparser.ConfigParser()
            config.read("settings.ini")
            config.set("settings", "token", tk)
            with open("settings.ini", "w") as f:
                config.write(f)
                
            
            MethodGetMe = (f'''https://api.telegram.org/bot{tk}/GetMe''')
            response = requests.post(MethodGetMe)
            tttm = response.json()
            namme = (tttm['result']['first_name'])
            id_adm = (tttm['result']['id'])
            usik = (tttm['result']['username'])
            clearscreen()
            print(f"""
            Имя Бота: {re}{namme}{cy}
            id Владельца: {re}{id_adm}{cy} 
            username: {re}{usik}{cy}
            url bota: {gr}https://t.me/{usik}{cy}
            
            Скопируй id и перейди в меню добавления Администраторов""")
            input('\n\n     Продолжить "Enter"') 
            
            
            restart_program()
            
            
        #  Добавления Администрации        
        elif santet == "03" or santet == "3":
            print('\n        Добавления Администрации')
            print(f"""   ----------------------------------""")
            print('бот берет id с Токена и автоматом присваевает в Админы')
            print(f"""   **********************************\n\n""")
            import configparser  
            
            config = configparser.ConfigParser()     
            config.read("settings.ini")	
            ddd = (config["settings"]["admin_id"]) 
            tk = input('Введите id admina:')
            adm = ddd + ',' + tk
            config.set("settings", "admin_id", adm )


            with open("settings.ini", "w") as f:
                config.write(f)
                
            restart_program()    
        
        #  Список Администрации
        elif santet == "04" or santet == "4":
            import configparser 
            config = configparser.ConfigParser() 
            config.read("settings.ini")
            ddd = (f"""{config["settings"]['token'], config["settings"]['admin_id']}""")
            print(f"""\n\n\n Вот список id у кого есть доступ к админ меню \n\n{ddd}""")
            input('\n\nДля выхода из меню просмотра списка администрации нажми Enter')
            restart_program()
            
            
        # Изменить Список Администрации   
        elif santet == "05" or santet == "5":    
            os.system(f"""/mnt/c/Program\ Files\ \(x86\)/Notepad++/notepad++.exe -multiInst -notabbar -nosession  settings.ini """)
            restart_program()
            
        # Старт бота в режиме Screen
        elif santet == "06" or santet == "6":
            os.system('screen -S botcicada python3 main.py')
            
        elif santet == "xx" or santet == "x":
            os.system(exit)


    except Exception as e:
        print('Error')
        