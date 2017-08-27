#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from telebot import types
import time
import os

TOKEN = "441277063:AAFQ43s2DF1MgFVPNCf7xkJWI_nMKZg450c"                  #TOKEN Obtenido
userStep = {}                    #Diccionario para ID y num menú
knownUsers = []                  #Usuarios conectados

#Color Texto en Consola
class color:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[32m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    
#función verificar ususario como nuevo o existente
def get_user_step (uid):
    if uid in userStep:
        return userStep [uid]
    else
        knownUsers.append (uid)
        userStep [uid] = 0

        print (color.RED + "[i] ¡Nuevo Usuario!" + color.ENDC)

#listener
    def listener (messages):
        for m in messages
            if m.content_type == 'text'
                print ("[" + str (m.chat.id) + "]" + str (m. chat.first_name) + ": " + m.text)

bot = telebot.Telebot (TOKEN)
bot.set_update_listener (listener)

#diccionario con comandos bot
commands = {
    'start' : 'Arranca el bot'
    'ayuda' : 'Comandos disponibles'
    'exec' : 'Ejecuta un comando'
            }

#ayuda
@bot.message_handler (commands = ['ayuda'])
def.command_help (m):
    cid = m.chat.id
    help_text = "Comandos disponibles: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += comands [key] + "\n"
    bot.send_message (cid, help_text)
    
