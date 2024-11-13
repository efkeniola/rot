#code created on nov 1 2024 bt fkteam 
#Donate to make thing easier for human being 
#insstall tools phonenumbers,requests,pyTelebot,PIL,python-dateutil
from importlib.resources import contents
import phonenumbers
from datetime import datetime,timedelta
import schedule
import time
from phonenumbers import geocoder
import requests,sys,datetime
import yt_dlp
import rembg
from rembg import remove
from PIL import Image
import requests
import io
import telebot
import tempfile
from telebot import util
import time,os
import pytube
from pytube import YouTube
api='7693576744:AAEQg0OHFtxeZ4SYk7AJ-Tyov-ORRX8ytG0'
bot=telebot.TeleBot(api)
#bot tg link
color=['red','blue','yellow','white','black','pink','purple','green']
cho_color={}
tempoary_store={}
tg=""
api_id = '28872791'
api_hash = 'e6e721e25cbfc65f62e37e781511acbb'
channel_username = 'fast_tool1'
#@bot.message_handler(func=lambda message:True)
@bot.message_handler(content_types='text')
def handle(message):
    username=message.from_user.username
    if message.text == '/subscribe':
        subs(message)
    elif message.text in ['hi','HI','HELLO','Hello','Good Day','xup','Xup']:
        bot.reply_to(message,'Welcome I am a bot created by Fk team how may i assist you use command (/new)')
    elif message.text.startswith('/'):
        with open('tg.txt','r+') as t:
            yo=t.read()
            if str(message.from_user.id) in yo:
                
            
                if message.text == '/start':
                    start(message)
                elif message.text == '/donate':
                    donate(message)
                elif message.text == '/premiumabout':
                    premium_plan(message)
                elif message.text == '/premium':
                    pre(message)
                elif message.text == '/renew':
                    ren(message)
                elif message.text == '/new':
                    new_user(message)
                elif message.text == '/phone_details':
                    phone_d(message)
                elif message.text == '/youtube':
                    ty(message)
                elif message.text == '/removebg':

                    change(message)
                #elif message.text == '/facebook':
                #    tf(message)
              #  elif message.text == '/instagram':
               #     ti(message)
                elif message.text == '/jpg':
                    jp(message)
                elif message.text == '/png':
                    pn(message)
                elif message.text == '/gif':
                    gf(message)
            
            
                else:
                    bot.reply_to(message,'Command was unable to detect (lower letter)')
            else:
                bot.reply_to(message,'Subscribe first using command (/subscribe)')
    else:
        if tempoary_store.get(message.chat.id) == 'youtube_st':
            if 'https://m.youtube.com/' in message.text:
                messag=util.split_string(message.text,4096)
                bot.reply_to(message,'Loadin... NB \n Make Sure your Have Strong Connection')
                for mes in messag:
                    youtube(mes,message)
            else:
                bot.reply_to(message,'enter a valid link eg https://m.youtube.com/')
        
        elif tempoary_store.get(message.chat.id) == 'facebook_st':
            if 'https://www.facebook.com/' in message.text:
                messag=util.split_string(message.text,4096)
                bot.reply_to(message,'Loadin... NB \n Make Sure your Have Strong Connection')
                for mes in messag:
                    facebook(mes,message)
            else:
                bot.reply_to(message,'enter a valid link eg https://www.facebook.com/')
        elif tempoary_store.get(message.chat.id) == 'instagram_st':
            if 'https://www.instagram.com/' in message.text:
                messag=util.split_string(message.text,4096)
                bot.reply_to(message,'Loadin... NB \n Make Sure your Have Strong Connection')
                for mes in messag:
                    instagram(mes,message)
            else:
                bot.reply_to(message,'enter a valid link eg https://www.instagram.com/')
        elif tempoary_store.get(message.chat.id) == 'phone_details':
            if message.text.startswith('+'):
                bot.reply_to(message,'Loadind....')
                track_phone(message)
            
            else:
                bot.reply_to(message,'Make Sure it is a valid number Start from +')
        elif tempoary_store.get(message.chat.id) == 'premium':
            if message.text.startswith('fast_tools-new'):
                bot.reply_to(message,'Loadind....')
                premium_subscribe(message)
            
            else:
                bot.reply_to(message,'This is not a valid token inpur properly')
        elif tempoary_store.get(message.chat.id) == 'renew':
            if message.text.startswith('fast_tool-renew'):
                bot.reply_to(message,'Loadind....')
                renew(message)
            
            else:
                bot.reply_to(message,'Not a valid renew token')
        

        elif tempoary_store.get(message.chat.id) == 'changebg':
            if  message.text in color:
                if cho_color:
                    cho_color.pop('color',None)
                    cho_color['color']=message.text
                    
                    bot.send_message(message.chat.id,'Color Saved Send Document to change bg')
                else:
                    
                    cho_color['color']=message.text
                    
                    bot.send_message(message.chat.id,'Color Saved Send Document to change bg')
            else:
                bot.send_message(message.chat.id,'Color Not available enter /colorlist to check\navailable color')
        elif tempoary_store.get(message.chat.id) == 'phone_details':
            pass
        else:
            bot.reply_to(message,f'{username} i was unable to detect your text enter command /new \n to understand the step \ncheck if you input any commander before starting\n Thanks')
@bot.message_handler(content_types='photo')
def pic_handle(message):
        if tempoary_store.get(message.chat.id) == 'png_st':
            png_handler(message)
        elif tempoary_store.get(message.chat.id) == 'jpg_st':
            jpg_handler(message)
        elif tempoary_store.get(message.chat.id) == 'gif_st':
            gif_handler(message)
        elif cho_color['color'] and tempoary_store.get(message.chat.id) == 'changebg':
            rem_bg(message)
        else:
            bot.reply_to(message,'Unable to detect document for converting tools /new commands to understand')
   # if 'https://www.youtube.com/' in message.text:
    #    youtube(message)
   # elif 'https://www.facebook.com/' in message.text:
        #facebook(message)
  #  elif 'https://www.instagram.com/' in message.text:
        #instagram(message)
   # else:
   #     bot.reply_to(message,f'{username} unable to detect message')
def progess(to,message):
    you=bot.send_message(message.chat.id,'Wait for a few min')
    if to['status'] == 'downloading':
        size=to.get('total_bytes',1)
        downloaded_size=to.get('downloaded_bytes',0)
        percent=downloaded_size / size * 100 if size > 0 else 0
        pg_message=f'Dwonload loading Progess rate: {percent:.2f} %'
        try:
            
            bot.edit_message_text(pg_message,message.chat.id,you.message_id)
        except Exception as e:
            print(f'Error occur  progess line {e}')
    elif to['status'] == 'finished':
        print('Download Complete')

subscribers=[]
def youtube_tool():
    download_path='C:/Users/User/Desktop'
    print(Fore.GREEN + 'Welcome to FK TEAM yotube file download')
    time.sleep(2)
    os.system('cls')
    print(Fore.GREEN + """
    Welcome to Fk team to contiue we will provide a input to provude the \n The yotube videio to download
    """)
    ip=str(input('Provide the url link: '))
    time.sleep(1)
    print(Fore.YELLOW + 'Loadin......')
    time.sleep(2)

    os.system('cls')
    with yt_dlp.YoutubeDL(tt) as tl:
        tl.download([ip])

#@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,f'Hello, {message.from_user.username}  Welcome to FAST \n We can assist you🎁\n FIRSTLY SUBSCRIBE USING COMMAND (/subscribe)✅\n COMMAND LIST↗️\n1. (/youtube) USE TO DOWNLOAD YOUTUBE VIDEO 🪐↗️\n2. (/phone_details) PHONE NUMBER TRACKING USER LOCATION(PREMIUM) 🪐↗️\n3. (/removebg) REMOVE BACKGROUND PHOTO(PREMIUM) 🪐\n4. (/jpg) CONVERT PHOTO TO JPG⚙️🗃️\n5. (/png) CONVERT PHOTO TO PNG ⚙️🗃️\n6. (/gif) CONVERT PHOTO TO GIF⚙️🗃️\nABOUT PREMIUM (/premiumabout) TO SWITH TO PREMIUM(/premium)\n🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁/nYOU CAN DONATE FOR US OR BUY ☕ FOR DEVELOPER (/donate)')
#@bot.message_handler(command=['new'])
def new_user(message):
   bot.reply_to(message,f'Hello, {message.from_user.username}  Welcome to FAST \n We can assist you🎁\n COMMAND LIST↗️\n1. (/youtube) USE TO DOWNLOAD YOUTUBE VIDEO 🪐↗️\n2. (/phone_details) PHONE NUMBER TRACKING USER LOCATION(PREMIUM) 🪐↗️\n3. (/removebg) REMOVE BACKGROUND PHOTO(PREMIUM) 🪐\n4. (/jpg) CONVERT PHOTO TO JPG⚙️🗃️\n5. (/png) CONVERT PHOTO TO PNG ⚙️🗃️\n6. (/gif) CONVERT PHOTO TO GIF⚙️🗃️\nABOUT PREMIUM (/premiumabout) TO SWITH TO PREMIUM(/premium)\n4. (/jpg) CONVERT PHOTO TO JPG⚙️🗃️\n5. (/png) CONVERT PHOTO TO PNG ⚙️🗃️\n6. (/gif) CONVERT PHOTO TO GIF⚙️🗃️\n🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁/nYOU CAN DONATE FOR US OR BUY ☕ FOR DEVELOPER (/donate)')
#@bot.message_handler(commands=[''])
#def send(message):
   # bot.reply_to(message,f'Hi, {message.chat.id} Welcome to DOWNLOAD BOT press /new to start')
#@bot.message_handler(command=['youtube'])
def ty(message):
    if message.chat.id in tempoary_store:
        tempoary_store.pop(message.chat.id)
        tempoary_store[message.chat.id]='youtube_st'
        bot.reply_to(message,'Enter the link to download youtube link ')
    else:
        tempoary_store[message.chat.id]='youtube_st'
        bot.reply_to(message,'Enter the link to download youtube link ')
#@bot.message_handler(command=['facebook'])
def tf(message):
    if message.chat.id in tempoary_store:
        tempoary_store.pop(message.chat.id)
        tempoary_store[message.chat.id]='facebook_st'
        bot.reply_to(message,'Enter the link to download facebook link ')
    else:
        tempoary_store[message.chat.id]='facebook_st'
        bot.reply_to(message,'Enter the link to download faceboook link ')
#@bot.message_handler(command=['instagram'])
def ti(message):
    if message.chat.id in tempoary_store:
        tempoary_store.pop(message.chat.id)
        tempoary_store[message.chat.id]='instagram_st'
        bot.reply_to(message,'Enter the link to download instagram link ')
    else:
        tempoary_store[message.chat.id]='instagram_st'
        bot.reply_to(message,'Enter the link to download instagram link ')
def pre(message):
    if message.chat.id in tempoary_store:
        tempoary_store.pop(message.chat.id)
        tempoary_store[message.chat.id]='premium'
        bot.reply_to(message,'Enter Subscribtion Code to process or press /premiumknow to know more ')
    else:
        tempoary_store[message.chat.id]='premium'
        bot.reply_to(message,'Enter Subscribtion Code to process or press /premiumknow to know more ')
def change(message):
    if message.chat.id in tempoary_store:
        tempoary_store.pop(message.chat.id)
        tempoary_store[message.chat.id]='changebg'
        bot.reply_to(message,'Select color to change too')
    else:
        tempoary_store[message.chat.id]='changebg'
        bot.reply_to(message,'Select color to change too ')
def ren(message):
    if message.chat.id in tempoary_store:
        tempoary_store.pop(message.chat.id)
        tempoary_store[message.chat.id]='renew'
        bot.reply_to(message,'Enter Renew code to access ')
    else:
        tempoary_store[message.chat.id]='renew'
        bot.reply_to(message,'Enter Renew code to acces ')
def phone_d(message):
    if message.chat.id in tempoary_store:
        tempoary_store.pop(message.chat.id)
        tempoary_store[message.chat.id]='phone_details'
        bot.reply_to(message,'Enter Phone Number to get details eg +41283940 ')
    else:
        tempoary_store[message.chat.id]='phone_details'
        bot.reply_to(message,'Enter Phone Number to get details eg +41283940')
#@bot.message_handler(command=['jpg'])
def jp(message):
    if message.chat.id in tempoary_store:
        tempoary_store.pop(message.chat.id)
        tempoary_store[message.chat.id]='jpg_st'
        bot.reply_to(message,'Send the document to convert to jpg ')
    else:
        tempoary_store[message.chat.id]='jpg_st'
        bot.reply_to(message,'Send the document to convert to jpg')
#@bot.message_handler(command=['png'])
def pn(message):
    if message.chat.id in tempoary_store:
        tempoary_store.pop(message.chat.id)
        tempoary_store[message.chat.id]='png_st'
        bot.reply_to(message,'Send the document to convert to png')
    else:
        tempoary_store[message.chat.id]='png_st'
        bot.reply_to(message,'Send the document to convert to png ')
#@bot.message_handler(command=['gif'])
def gf(message):
    if message.chat.id in tempoary_store:
        tempoary_store.pop(message.chat.id)
        tempoary_store[message.chat.id]='gif_st'
        bot.reply_to(message,'Send the document to convert to gif')
    else:
        tempoary_store[message.chat.id]='png_st'
        bot.reply_to(message,'Send the document to convert to gif ')
#@bot.message_handler(commands=['/subscribe'])
def subs(message):
    bot_token='7693576744:AAEQg0OHFtxeZ4SYk7AJ-Tyov-ORRX8ytG0'
    channel_username='fast_tool1'
    url =f"https://api.telegram.org/bot{bot_token}/getChatMember"
    params = {"chat_id": '@fast_tool1', "user_id": f'{message.chat.id}'}
    response = requests.get(url, params=params)
    
    
    data = response.json()
    print(data)
    if data['ok']:
      if data['result']['status'] != 'left' and data['result']['status'] != 'kicked':
        
      
        with open('tg.txt','r+') as t:
            yo=t.read()
            if str(message.from_user.id) in yo:
                bot.reply_to(message,'Already Subscribe')
            else:
                from pathlib2 import Path
                fileo=Path('tg.txt')
                with fileo.open('a') as ro:

                            ro.write(f'{message.chat.id}\n') 
                            bot.reply_to(message,'Added to subsciber welcome to the team \n /new to see command list')
      else:
        bot.reply_to(message,'You need to join this channel firs\n @fast_tool1')
    else:
        bot.reply_to(message,'You need to join this channel firs\n @fast_tool1')
    
#@bot.message_handler(commands=['/youtube'])
#def send(message):
 #   bot.reply_to(message,f'Welcom to youtube download tools \n Enter The videio link sameple https://www.youtube.com/watch=?efk')

def youtube(mes,message):
    if mes.startswith("https://m.youtube") == True:

        bot.reply_to(message,f'Download for {mes} will start soon after verification')
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
        tt={
        'format':'best',
        'outtmpl':tempfile.gettempdir() + 'downloads/%(title)s.%(ext)s',
        'cookiefile':'C:/Users/User/Desktop/cookies.txt',
        'progress_hooks': [lambda to:progess(to,message)],
            }
        try:
            with yt_dlp.YoutubeDL(tt) as r:
                info=r.extract_info(mes,download=True)
                title=info.get('title',None)
                import random
                ido=random.randrange(100,900)
                video_file=r.prepare_filename(info)
                with open(video_file,'rb') as video_loc:
                    bot.send_video(message.chat.id,video_loc,caption=f'Please Donate(/donate) for us.\n Title of the video:{title} ,')
                    bot.reply_to(message.chat.id,'Download Complete..!')
        except Exception as e:
            print(f'this is the error {e}')
            bot.reply_to(message,f' An error ocuur (not neccesary)')
        finally:
            if os.path.exists('downloads'):
               # os.chmod(video_file,0o777)
                os.remove(video_file)

    else:
        bot.reply_to(mes,'This is not a valid yotube addresss')

def facebook(mes,message):
    if message.text.startswith("https://www.facebook") == True:

        bot.reply_to(message,f'Download for #{mes} will start soon after verification')
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
        import random
        fil=random.randrange(1000,9000)
        filop=f'download{fil}.mp4'
       
        try:
            with tempfile.TemporaryDirectory() as temp_dir:


                url=YouTube(mes)
                
                tmp_file=os.path.join(temp_dir,'facebook_reel.mp4')
                #name=tmp_file.name
                video_get=url.streams.get_highest_resolution()
                video_get.download(output_path=temp_dir,filename='facebook_reel.mp4')
                import shutil
                name=shutil.copy(tmp_file,tempfile.mktemp(suffix='.mp4'))
                with open(name,'rb') as send:
                    bot.send_message(message.chat.id,send)
                
        except Exception as e:
            print(f'this is the error {e}')
            bot.reply_to(message,f' An error ocuur  (not neccesary)')
        
    else:
        bot.reply_to(message,'This is not a valid Facebook addresss')

def instagram(mes,message):
    if message.text.startswith("https://www.instagram") == True:

        bot.reply_to(message,f'Download for {mes} will start soon after verification')
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
        tt={
        'format':'best',
        'outtmpl':tempfile.gettempdir() + 'downloads/%(title)s.%(ext)s',
        #'cookiefile':'C:/Users/User/Desktop/cookiesins.txt',
        'progress_hooks': [lambda to:progess(to,message)],
            }
        try:
            with yt_dlp.YoutubeDL(tt) as r:
                info=r.extract_info(mes,download=True)
                title=info.get('title',None)
                import random
                ido=random.randrange(100,900)
                video_file=r.prepare_filename(info)
                with open(video_file,'rb') as video_loc:
                    bot.send_video(message.chat.id,video_loc,caption=f'Please Donate(/donate) for us.\n Title of the video:{title} ,')
                    bot.reply_to(message.chat.id,'Download Complete..!')
        except Exception as e:
            print(f'this is the error {e}')
            bot.reply_to(message,f' An error ocuur (not neccesary)')
        finally:
            if os.path.exists('downloads'):
               # os.chmod(video_file,0o777)
                os.remove(video_file)
    else:
        bot.reply_to(message,'This is not a valid Instagram addresss')
@bot.message_handler(content_type=[''])
def handle_image(message):
    file_id=message.photo[-1].file_id
    file_info=bot.get_file(file_id)
    try:
        bot.reply_to(message,'Image is processing to Jpg')
        download_file=bot.download_file(file_info.file_path)
        time.sleep(3)
        file_path=f"convert_img_by_fkteamz{file_id}.jpg"
        with open(file_path,'wb') as change:
            change.write(download_file)
            bot.reply_message(message,'Convertin.....')
        with open(file_path,'rb') as send:
            bot.send_document(message.chat.id,send)
    except Exception as e:
        bot.reply_to(message,f'Error ode {e}')
    finally:
        bot.reply_to(message,'Successfull Convert')


def jpg_handler(message):
    #image handler for the file27056925284
    file_id=message.photo[-1].file_id
    #get file for bot
    file_info=bot.get_file(file_id)
    bot.reply_to(message,'Processing JPG')
    file_url = f'https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}'
    file_data = requests.get(file_url).content

    # Open the file with PIL and convert it to JPG
    with Image.open(io.BytesIO(file_data)) as img:
        # Convert image mode to RGB (required for JPG format)
        img = img.convert("RGB")
        
        # Save it to a BytesIO object in JPG format
        jpg_data = io.BytesIO()
        img.save(jpg_data, format="JPEG")
        jpg_data.seek(0)
        import random
        y=random.randrange(100000,999999)
        filename=f'convert_fkteam @tgbotid={y}.jpg'
        jpg_data.name=filename
        try:
            with open(f"{filename}",'wb') as tex:
                tex.write(jpg_data.getbuffer())
            # Send the JPG file back to the user
            bot.send_document(message.chat.id,jpg_data,caption='THis is the convert new file')
            bot.reply_to(message,'Kindly Donate for using command  /donate ')
        except Exception as e:
            bot.reply_to(message,'Error occur')
        finally:
            if os.path.exists(filename):
                os.remove(filename)
            else:
                pass

def png_handler(message):
   #image handler for the file
    file_id=message.photo[-1].file_id
    #get file for bot
    file_info=bot.get_file(file_id)
    bot.reply_to(message,'Processing PNG')
    file_url = f'https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}'
    file_data = requests.get(file_url).content

    # Open the file with PIL and convert it to JPG
    with Image.open(io.BytesIO(file_data)) as img:
        # Convert image mode to RGB (required for JPG format)
        img = img.convert("RGB")
        
        # Save it to a BytesIO object in JPG format
        png_data = io.BytesIO()
        img.save(png_data, format="PNG")
        png_data.seek(0)
        import random
        y=random.randrange(100000,999999)
        filename=f'convert_fkteam @tgbot-id={y}.png'
        png_data.name=filename
        try:
            with open(f"{filename}",'wb') as tex:
                tex.write(png_data.getbuffer())
            # Send the JPG file back to the user
            bot.send_document(message.chat.id,png_data,caption='THis is the convert new file')
            bot.reply_to(message,'Kindly Donate for using command  /donate ')
        except Exception as e:
            bot.reply_to(message,'Error occur')
        finally:
            if os.path.exists(filename):
                os.remove(filename)
            else:
                pass

def gif_handler(message):
   #image handler for the file
    file_id=message.photo[-1].file_id
    #get file for bot
    file_info=bot.get_file(file_id)
    bot.reply_to(message,'Processing GIF')
    file_url = f'https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}'
    file_data = requests.get(file_url).content

    # Open the file with PIL and convert it to GIF
    with Image.open(io.BytesIO(file_data)) as img:
        # Convert image mode to RGB (required for JPG format)
        img = img.convert("RGB")
        
        # Save it to a BytesIO object in JPG format
        gif_data = io.BytesIO()
        img.save(gif_data, format="GIF")
        gif_data.seek(0)
        import random
        y=random.randrange(100000,999999)
        filename=f'convert_fkteam @tgbot-id={y}.gif'
        gif_data.name=filename
        try:
            with open(f"{filename}",'wb') as tex:
                tex.write(gif_data.getbuffer())
            # Send the JPG file back to the user
            bot.send_document(message.chat.id,gif_data,caption='THis is the convert new file')
            bot.reply_to(message,'Kindly Donate for using command  /donate ')
        except Exception as e:
            bot.reply_to(message,'Error occur')
        finally:
            if os.path.exists(filename):
                os.remove(filename)
            else:
                pass

@bot.message_handler(commads=['unsubscribe'])
def unsub_handle(message):
    if message.chat.id in subscribers:
        subscribers.remove(message.chat.id)
        bot.reply_to(message,'You Have Unsubscribe Successfull')
    else:
        bot.reply_to(message,'You are not our subscriber before')
#@bot.message_handler(commads=['donate'])
def donate(message):
    messages=f"""
DONATE FOR FK TEAM HERE💻↗️\nPAYPAL: efkeniola8505@gmail.com \n NIGERIA🇳🇬 \nBANK: PALMPAY⚙️\nACC  NO: 8109094849\n THANKS FOR THE DONATION ✅🤝
"""
    bot.reply_to(message,messages)
def track_phone(message):
    if message.text.startswith('+'):
        
        from phonenumbers import geocoder,carrier,timezone
        user_id=message.from_user.id
        addp=[]
        user_id=message.from_user.id
        import datetime
        current_date=datetime.date.today()
        pret=open('pre_subscriber.txt','r')
        from pathlib2 import Path
        pl=Path('pre_subscriber.txt')
        
        preto=pret.readlines()
        for pro in preto:
            lo=pro.strip()
            
            
            if str(user_id) in lo:
                expr_dt=lo.split('=')
                from datetime import datetime
                
                if str(current_date) >expr_dt[1]:
                    bot.send_message(user_id,'Subscribtion Expire (/renew)')
                else:
                    phone_number=message.text
                    t=phonenumbers.parse(phone_number)
                    location=geocoder.description_for_number(t,"en")
                    country=location
                    country_code=phonenumbers.region_code_for_number(t)
                    network_user=carrier.name_for_number(t,'en')
                    is_valid=phonenumbers.is_valid_number(t)
                    is_possible=phonenumbers.is_possible_number(t)
                    international_format=phonenumbers.format_number(t,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                    mobile_format=phonenumbers.format_number_for_mobile_dialing(t,region_calling_from='Unknow',with_formatting=True)
                    number_type=phonenumbers.number_type(t)
                    timezone1=timezone.time_zones_for_number(t)
                    timezonshow=','.join(timezone1)
                    sendmessage=f"RESULT OF TRACKING....:\nCOUNTRY:{country}\nCODE:{country_code}\nNETWORK:{network_user}\nVALID NUMBER:{is_valid}\nPOSSIBLE NUMBER:{is_possible}\nInternational Format:{international_format}\nMobileFormat:{mobile_format}\nNUMBER TYPE:{number_type}\nTimezone:{timezonshow}\nOriginal Number:{t.national_number}\n MORE DETAILS ABOUT PHONE NUMBER IS KEEP PRIVATE"
                    bot.send_message(message.chat.id,sendmessage)
                    if number_type == phonenumbers.PhoneNumberType.MOBILE:
                        bot.send_message(message.chat.id,f"Phone number Type: Mobile")
                    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                        bot.send_message(message.chat.id,f"Phone number Type: FIXED LINE")
                    else:
                        bot.send_message(message.chat.id,f"Phone number Type: THis is another type of number")
                
            else:
                bot.send_message(message.chat.id,'You are not a premium user activate using  (/premium)\n only for Premium user only(ignore if load)')

    else:
        bot.reply_to(message,'Number must starts with country code  eg +1 ')
def premium_subscribe(message):
    from pathlib2 import Path
    import re
    files=Path('pre_subscriber.txt')
    with files.open('r') as sub:
        red=files.read_text()
        user_id=message.from_user.id
        
      #  print(red)
       # print(f'{user_id}')
       # if f'{user_id}' in red:
      #      print('YEs it was here')
       # else:
        #    print('KNow it was not theree')
        if f'{user_id}' in red:
            bot.send_message(user_id,'You are Already a Premium Subscriber')
        else:
            from pathlib2 import Path
            with open('subscriber_code.txt','r') as code:
                y=code.readlines()
                t=code.read()
                print(y)
                if f'{message.text}\n' in y:
                        
                        fileo=Path("pre_subscriber.txt")
                        #datap=fileo.read_text()
                        import datetime
                        date=datetime.date.today() +  timedelta(days=30)
                        with fileo.open('a') as ro:

                            ro.write(f'{user_id}={date}\n') 
                        

                        
                        from pathlib2 import Path
                        file=Path("subscriber_code.txt")
                        data=file.read_text()
                        data=data.replace(message.text,f'{message.text}=used')
                        file.write_text(data)
                        bot.send_message(message.chat.id,'Verifying....')
                        time.sleep(1)
                        bot.send_message(message.chat.id,'Your Plan was Successfull expire next month')
                else:
                        bot.send_message(message.chat.id,'Verifying....')
                        time.sleep(1)
                        bot.send_message(message.chat.id,'Sorry this Code is invalid or been used')
def renew(message):
        import datetime
        current_date=datetime.date.today()
        user_id=message.from_user.id
        addp=[]
        pret=open('pre_subscriber.txt','r')
        from pathlib2 import Path
        pl=Path('pre_subscriber.txt')
        
        preto=pret.readlines()
        for pro in preto:
            lo=pro.strip()
            
            
            if str(user_id) in lo:
                expr_dt=lo.split('=')
                from datetime import datetime
                
                if str(current_date) >expr_dt[1]:
                    with open('subscriber_code.txt') as code:
                        y=code.readlines()
                        if message.text in y:
                            new_exp_date=current_date + timedelta(days=30)
                            data=pl.read_text()
                            data=data.replace(f'{user_id}={expr_dt[1]}',f'{user_id}={new_exp_date}')
                            pl.write_text(data)
                            bot.send_message(message.chat.id,f'You Subscribtion has renew {new_exp_date}')
                        else:
                            pass
                else:
                    addp.append(pro)
                    bot.send_message(message.chat.id,f'You Subscribtion Has not Expired, Expiration Date: {expr_dt[1]}')
            else:
                bot.send_message(message.chat.id,f'NPt founf')
    
def rem_bg(message):
        file_id=message.photo[-1].file_id
        #get file for bot
        file_info=bot.get_file(file_id)
        bot.reply_to(message,'Processing PNG')
        file_url = f'https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}'
        lo=requests.get(file_url)
        
        file_data = requests.get(file_url).content
        user_file=file_data
        user_id=message.from_user.id
        import datetime
        current_date=datetime.date.today()
        pret=open('pre_subscriber.txt','r')
        from pathlib2 import Path
        pl=Path('pre_subscriber.txt')
        
        preto=pret.readlines()
        for pro in preto:
            lo=pro.strip()
            
            
            if str(user_id) in lo:
                expr_dt=lo.split('=')
                from datetime import datetime
                
                if str(current_date) >expr_dt[1]:
                    bot.send_message(message.chat.id,'Subscription Has Expired Subscribe')
                else:
                    import random,io
                    try:
                            idot=random.randrange(200,5000)
                            output_file=f'{idot}_bg_chg@fasttool.png'
                            #t_file=Image.open(user_file)
                        
                            file_get=remove(user_file)
                            #t.file.save(by,format="PNG")
                           # image_data=by.getvalue()
                           # output_data=
                            by_img=Image.open(io.BytesIO(file_get))
                            if by_img != 'RGBA':
                                by_img=by_img.convert('RGBA')
                            bg_red=(255,0,0,255)
                            bg_yellow=(255,255,0,255)
                            bg_blue=(0,0,255,255)
                            bg_black=(0,0,0,255)
                            bg_green=(0,255,0,255)
                            bg_white=(255,255,255,255)
                            bg_pink=(255,192,203,255)
                            bg_purple=(128,0,128,255)
                            width,height=by_img.size
                            if cho_color['color'] == 'black':
                                new_img=Image.new('RGBA',(width,height),bg_black)
                                new_img.paste(by_img,(0,0),by_img)
                                new_img.save(output_file,format='PNG')
                                with open(output_file,'rb') as out:
                                   
                                    
                                    bot.send_document(message.from_user.id,out,caption='BG change done @FAST TOOLS')
                            elif cho_color['color'] == 'white':
                                new_img=Image.new('RGBA',(width,height),bg_white)
                                new_img.paste(by_img,(0,0),by_img)

                                new_img.save(output_file,format='PNG')
                                with open(output_file,'rb') as out:
                                   
                                    
                                    bot.send_document(message.from_user.id,out,caption='BG change done @FAST TOOLS')
                            elif cho_color['color'] == 'red':
                                print('redd')
                                new_img=Image.new('RGBA',(width,height),bg_red)
                                new_img.paste(by_img,(0,0),by_img)

                                new_img.save(output_file,format='PNG')
                                with open(output_file,'rb') as out:
                                   
                                    
                                    bot.send_document(message.from_user.id,out,caption='BG change done @FAST TOOLS')
                            elif cho_color['color'] == 'purple':
                                new_img=Image.new('RGBA',(width,height),bg_purple)
                                new_img.paste(by_img,(0,0),by_img)

                                new_img.save(output_file,format='PNG')
                                with open(output_file,'rb') as out:
                                   
                                    
                                    bot.send_document(message.from_user.id,out,caption='BG change done @FAST TOOLS')
                            elif cho_color['color'] == 'yellow':
                                new_img=Image.new('RGBA',(width,height),bg_yellow)
                                new_img.paste(by_img,(0,0),by_img)
                                new_img.save(output_file,format='PNG')
                                with open(output_file,'rb') as out:
                                   
                                    
                                    bot.send_document(message.from_user.id,out,caption='BG change done @FAST TOOLS')
                            elif cho_color['color'] == 'blue':
                                new_img=Image.new('RGBA',(width,height),bg_blue)
                                new_img.paste(by_img,(0,0),by_img)

                                new_img.save(output_file,format='PNG')
                                with open(output_file,'rb') as out:
                                   
                                    
                                    bot.send_document(message.from_user.id,out,caption='BG change done @FAST TOOLS')
                            elif cho_color['color'] == 'green':
                                new_img=Image.new('RGBA',(width,height),bg_green)
                                new_img.paste(by_img,(0,0),by_img)

                                new_img.save(output_file,format='PNG')
                                with open(output_file,'rb') as out:
                                   
                                    
                                    bot.send_document(message.from_user.id,out,caption='BG change done @FAST TOOLS')
                            elif cho_color['color'] == 'pink':
                                new_img=Image.new('RGBA',(width,height),bg_pink)
                                new_img.paste(by_img,(0,0),by_img)

                                new_img.save(output_file,format='PNG')
                                with open(output_file,'rb') as out:
                                   
                                    
                                    bot.send_document(message.from_user.id,out,caption='BG change done @FAST TOOLS')
                            else:
                                bot.send_message(message.chat.id,'Start again and also check available color /changebg')

                    except Exception as e:
                        print(f'{e}')
                        bot.send_message(message.chat.id,'Error occur unable to convert')
                    finally:
                        if os.path.exists(output_file):
                            os.remove(output_file)
            else:
                bot.send_message(message.chat.id,'You are not a Premium use (/premium) to be a memeber')

def premium_plan(message):
    let_text='Welcome to Fast Tools \n About our PREMIUM TOOLS \n BENEFIT OF USING PREMIUM SERVIE\n 1. GET ACCESS TO NEW TOOLS \n 2. MORE FAST THEN BASIC USER \n 3. ACCESS TO OUR PRIVATE CHANNEL FOR QUICK UPDATE OR MONEY UPDATE\n TO MAKE PAYMENT ENTER (/donate)\nOR CHAT ADMIN @EFK$$$\n WHATSAPP NUMBER(ADMIN): +2348057091133\n NB: SUBSCRIBTION IS MONTHLY PLAN FOR PRICE SEND DM TO ANY OF THE ADMIN  @EfkeniolaWebDeveloper  '
    bot.send_message(message.chat.id,let_text)
            
from fastapi import FastAPI, Request


#bot = telebot.TeleBot("YOUR_BOT_TOKEN")
app = FastAPI()

@app.post("/")
async def receive_update(request: Request):
    json_str = await request.body()
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return {"status": "ok"}

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
