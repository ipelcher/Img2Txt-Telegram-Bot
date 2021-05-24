import bottoken
import imgscan

import telebot
import os

# Creating bot
bot = telebot.TeleBot(bottoken.bottoken)

# Start command
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.from_user.id, "Welcome to TelegramImageReader!\nFor command list send me /help!")

# Help command
@bot.message_handler(commands=['help'])
def start(message):
	bot.send_message(message.from_user.id, "Command list: \n/start - Start work with bot.\n/help - send this message.\n/img2txt - Read text form image.")

# Img2txt command
@bot.message_handler(commands=['img2txt'])
def start(message):
	bot.send_message(message.from_user.id, "Send image to read text from: ")

# Reciving image
@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    bot.reply_to(message, "Processing... Result will appear soon!")

    chat_id = message.chat.id

    # Downloading image
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    f = open('img1.png', 'wb')
    f.write(downloaded_file)
    f.close()
    
    # Reading text from image
    txtFromImg = imgscan.textFromImg('img1.png')

    # Deleting image
    os.remove('img1.png')

    # Sending result to user
    bot.send_message(message.from_user.id, 'Text from image: \n\n' + txtFromImg)

# Launching bot
bot.polling()