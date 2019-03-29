# Sticker-Block-Bot

This telegram bot removes all stickers and animations from group conversations.

_Note:_

To start the bot correctly a file named `secret.py` must be created inside `stickerblockbot` with the following content:

```python
class Secrets:

    def telegram_token(self):
        return '<your telegram bot token>'
```

_Note2:_

The bot needs to have the rights to delete messages in a group :sweat: and the bot privacy mode needs to be disabled to recieve group messages.
