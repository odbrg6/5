import requests
import telebot
from telebot import types
# Rest insta By : L7N ↝@g_4_q

Tok = "6381239282:AAHwp3Ha6SBQi1J3XkWZkjYBhvAJoD2A1dE"
L7N = telebot.TeleBot(Tok)

@L7N.message_handler(commands=['start'])
def start(message):
            	L7N1 = types.InlineKeyboardMarkup()
            	L7Ntele = types.InlineKeyboardButton('✨ Dev ✨',url ='https://t.me/n_p_ii')
            	L7N1.add(L7Ntele)
            	photo = f"t.me/{message.from_user.username}"
            	L7Ncall = f"[{message.from_user.first_name}]({photo})"
            	text = f"- Hello {L7Ncall} ! To Bot Rest instagram "
            	L7N.send_photo(message.chat.id,photo,text,parse_mode='Markdown',reply_markup=L7N1)
            	L7N.reply_to(message,'<strong>-قم بأرسال يوزر مستخدم بدون @ :</strong> ',parse_mode='html')
            	@L7N.message_handler(func=lambda m: True)
            	def L7N_send(message):
            				L7Nmes = message.text
            				url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
            				head ={
'Host': 'i.instagram.com',
'Connection': 'Keep-Alive',
'Cookie': 'mid=YgzPXAABAAFpu2FvBU3Nz814ooE5; csrftoken=DVpBRlGfuAZ0E7JtTnLD71F0mcnNV2tW',
'Cookie2': '$Version=1',
'Accept-Language': 'en-GB, en-US',
'X-IG-Connection-Type': 'WIFI',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip'
}
            				data ={
"user_email":f"{L7Nmes}",
"device_id":"android-ae9d37a73aa41d00",
"guid":"d038a34e-1663-4f2b-af9d-aae995d105c4",
"_csrftoken":"DVpBRlGfuAZ0E7JtTnLD71F0mcnNV2tW"
}
            				req =requests.post(url,headers = head, data = data)
            				if '"status":"ok"' in req.text:
            					rL7N = req.json()['obfuscated_email']
            					L7N.send_message(message.chat.id,f'''
<strong>- Doon Sned Rest ↝ @{L7Nmes}
————————×————————
- Email Sent ↝</strong> {rL7N}
<strong>————————×————————
- By ↝ @g_4_q </strong>
            			''',parse_mode='html')
            				else:
            					L7N.send_message(message.chat.id,'*• اليوزر غير صحيح او تم ارسال ريست له من قبل.!*',parse_mode="Markdown")

# What are you doing? I see you steal  
# ترجم كلمة steal

L7N.infinity_polling()           			
