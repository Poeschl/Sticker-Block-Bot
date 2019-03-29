from telegram.ext import Updater

from secret import Secrets


class TelegramEndpoint:
    __BOT_NAME = 'Sticker-Block-Bot'
    __API_TOKEN = Secrets().telegram_token()

    def __init__(self):
        self.updater = Updater(self.__API_TOKEN)

    def register_command_handler(self, handler):
        self.updater.dispatcher.add_handler(handler)

    def start(self):
        self.updater.start_polling()

    def shutdown(self):
        self.updater.stop()
