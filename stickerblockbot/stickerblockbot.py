import sys

from telegram import TelegramError
from telegram.ext import MessageHandler, Filters

from telegramapi import TelegramEndpoint


def delete_message_handler(bot, context):
    try:
        bot.deleteMessage(chat_id=context.message.chat.id, message_id=context.message.message_id)
        print('Deleted message from ' + str(context.message.from_user.id))
    except TelegramError:
        bot.send_message(chat_id=context.message.chat.id, text=sys.exc_info()[1].message)


def main():
    telegram_api = TelegramEndpoint()

    sticker_handler = MessageHandler(Filters.sticker, delete_message_handler)
    telegram_api.register_command_handler(sticker_handler)

    gif_handler = MessageHandler(Filters.animation, delete_message_handler)
    telegram_api.register_command_handler(gif_handler)

    print('Started Sticker-block-bot')

    telegram_api.start()


if __name__ == '__main__':
    main()
