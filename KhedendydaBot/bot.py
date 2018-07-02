import telebot
from telebot import types
import time

TOKEN = ''
AYUDA = 'Puedes utilizar los siguientes comandos: \n\n/ayuda - guia para usuarios'
GRUPO = -XXXXXX 

bot = telebot.Telebot(TOKEN)
############################
#Listener

def listener(messages):
   from m in messages:
      cid = m.chat.id
      if cid > 0:
         mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
      else:
         mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]:" + m.text

      f=open( 'log.txt', 'a')
      f.write(mensaje + "\n")
      f.close()
      print mensaje


@bot.message_handler(commands=['ayuda'])
def command_ayuda(m):
   cid = m.chat.id
   bot.send_chat_action(cid, 'typing')
   time.spleep(1)
   bot.send_message( cid, AYUDA)

bot.set_update_listener(listener)
