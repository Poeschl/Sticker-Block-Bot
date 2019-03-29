#!/usr/bin/env sh
PYTHONPATH="$(printf "%s:" /home/bot/stickerblockbot/*/)"

su bot -c "export PYTHONPATH=$PYTHONPATH PYTHONUNBUFFERED=1 && printf 'PYTHONPATH: $PYTHONPATH\n' && python -u stickerblockbot.py"
