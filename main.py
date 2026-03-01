import ptbot
import os
import random
from dotenv import load_dotenv
from pytimeparse import parse


load_dotenv()
TG_CHAT_ID = os.environ['TG_CHAT_ID']
TG_TOKEN = os.environ['TG_TOKEN']


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(chat_id, text):
  message_id = bot.send_message(chat_id, "Запускаю таймер...")
  bot.create_countdown(parse(text), notify_progress, message_id=message_id, chat_id=chat_id, message=text, start_seconds=parse(text))
  bot.create_timer(parse(text), notify, chat_id=chat_id, message=text)


def notify_progress(secs_left, chat_id, message, message_id, start_seconds):
	stop_seconds = start_seconds - secs_left
	progressbar = render_progressbar(start_seconds, stop_seconds)
	bot_message = "Осталось секунд: {}.\n".format(secs_left)
	update_message = bot_message + progressbar
	bot.update_message(chat_id, message_id, update_message)


def notify(chat_id, message):
  bot.send_message(chat_id, "Время вышло")


if __name__ == "__main__":
	bot = ptbot.Bot(TG_TOKEN)
	bot.reply_on_message(reply)
	bot.run_bot()