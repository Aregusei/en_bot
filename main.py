import telebot
from telebot import types

bot = telebot.TeleBot('6134461162:AAGxvm1YTjWe0Cl4K2iYIF1pJKquf0BRgwM')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello!, {message.from_user.first_name}!\nYou can find answers to your questions by using the commands listed in the dropdown menu to the left of the input message field.',disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['website'])
def website(message):
    bot.send_message(message.chat.id, '⛓ <b>C-Patex Ecosystems</b> <a href="https://c-patex.com/">Website</a>\nFor more information, please see the <a href="https://t.me/cpatexen/11089"><b>F.A.Q</b></a>  👈',disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['withdrawal'])
def withdrawal(message):
    bot.send_message(message.chat.id, '💰 <b>All withdrawals</b> are processed within 3 hours. If your withdrawal is delayed, please contact support (<i>details on command </i> <b>/contact</b>)\nFor more information, please see the <a href="https://t.me/cpatexen/11089"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['fees'])
def fees(message):
    bot.send_message(message.chat.id, '💲 A detailed <b>list of commissions</b> can be found <a href="https://c-patex.com/fees/">here</a>.\n For more information, please see the <a href="https://t.me/cpatexen/11089"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['kyc'])
def kyc(message):
    bot.send_message(message.chat.id, '👤 <b> The maximum time limit</b>  for verifications is ~24 hours. Usually though, applications are processed much faster.\nFor more information, please see the <a href="https://t.me/cpatexen/11089/"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['deposit'])
def deposit(message):  bot.send_message(message.chat.id, '🪙 If your deposit has <b>not been credited</b>, please provide us with detailed transaction details <b> (AMOUNT, VALUE, HASH) </b> to email: 📬 support@c-patex.com\nFor more information, please see the <a href="https://t.me/cpatexen/11089"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['contact'])
def contact(message):   bot.send_message(message.chat.id, 'You can contact us by email — 📬 support@c-patex.com\n🌐 Create a support ticket at <a href="https://c-patex.com/support">website</a>\n📱 Or contact a support agent on <a href="http://t.me/cpatexsupport">Telegram</a>', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['two_factor_auth'])
def  two_factor_auth(message):   bot.send_message(message.chat.id, '👤To disable <b>2FA</b> please provide <b>both sides of your document (passport or ID card or drivers license ),  and  🤳a selfie of you holding the document and a piece of paper with the following handwritten text "C-PATEX.COM", current date and your signature.</b>\nPlease send all photos to us at support@c-patex.com.\n For more information, please see the <a href="https://t.me/cpatexen/11089"><b>F.A.Q</b></a> 👈\n', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['docs'])
def docs(message):   bot.send_message(message.chat.id, '📝 Link to <a href="https://c-patex.com/files/en/wp.pdf?v=1.2"><b>whitepaper</b></a>\n🔩 Link to <a href="https://patex.io/docs/Patex%20Tokenomics.pdf"><b>tokenomics</b></a>', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['socials'])
def socials(message):   bot.send_message(message.chat.id, '📜 <a href="https://linktr.ee/patex_ecosystem"><b>Linktr.ee</b></a>\n \
— <a href="https://www.facebook.com/patexecosystem"><b>Facebook</b></a>\n \
— <a href="https://www.instagram.com/patex_ecosystem/"><b>Instagram</b></a> \n \
— <a href="https://www.youtube.com/channel/UCLmHyM6kZ5bViyh7my6ZkpA"><b>YouTube</b></a> \n \
— <a href="https://medium.com/@patex_ecosystem"><b>Medium</b></a> \n \
— <a href="https://twitter.com/patex_ecosystem"><b>Twitter</b></a> \n \
       \n \
📝<a href="https://linktr.ee/patex_ecosystem"><b>Patex Chats</b></a>\n \
— <a href="https://t.me/cpatexeng"><b>TG Channel (English)</b></a> \n \
— <a href="https://t.me/cpatexexchange"><b>TG Channel (Español / Portuguese)</b></a> \n \
— <a href="https://t.me/cpatexespanol"><b>TG Chat (Español)</b></a> \n \
— <a href="https://t.me/cpatexportuguese"><b>TG Chat (Portuguese)</b></a> \n \
— <a href="https://t.me/+HmW0DJAYl1YzMjAy"><b>TG Chat (English)</b></a> \n \
— <a href="https://t.me/cpatexcis"><b>TG Chat (CIS)</b></a>', disable_web_page_preview=True, parse_mode='HTML')

bot.polling(none_stop=True, interval=1)