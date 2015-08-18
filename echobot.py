#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Simple Bot to reply Telegram messages
# Copyright (C) 2015 Leandro Toledo de Souza <leandrotoeldodesouza@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].


import logging
import telegram
import time
import random
import settings


LAST_UPDATE_ID = None


def main():
    global LAST_UPDATE_ID

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Telegram Bot Authorization Token
    bot = telegram.Bot(settings.TOKEN)

    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        echo(bot)
        time.sleep(3)


def echo(bot):
    global LAST_UPDATE_ID

    # Request updates from last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID):
        if LAST_UPDATE_ID < update.update_id:
            # chat_id is required to reply any message
            chat_id = update.message.chat_id
            sender = update.message.from_user #['from']['first_name']
            # message = update.message.text.encode('utf-8')


            messages = (
                'Deja de estar mamando, %s',
                'Sacate por ahi, %s',
                'Come caca, %s',
                'Deja de joder, %s',
                'Que chingados quieres, %s?',
                'Como castras, %s',
                'Alguien aplaudale a %s, por favor',
                'A veces dices cosas chidas, a veces la cagas, %s',
                'Eres culeroon %s',
                'Tu madre no se sentiria muy orgullosa de escuchar esto, %s',
                '%s, eres una pobre persona falta de amor...',
                '%s, puedes irte muy lejos, alla por donde da la vuelta el viento'
            )
       
            message = random.choice(messages) % sender.first_name
            if sender.id == 13872946:
                message = "Sacate por ahi Eder, deja de andar cagando el palo!"
            print('sender: ' + sender.first_name)
            print('sender id: ' + str(sender.id))
            print('incomming message: ' + update.message.text)
            print('outcoming message: ' + message)
            print('-'*80)

            if (message):
                # Reply the message
                bot.sendMessage(chat_id=chat_id,
                                text=message)

                # Updates global offset to get the new updates
                LAST_UPDATE_ID = update.update_id


if __name__ == '__main__':
    main()
