import telegram
import gsheet
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
		text="Treasurer Bot for Adaptive Network Laboratory Telkom University\n")

def kas(update, context):
    text = update.message.text.split()
    worksheet_list = gsheet.get_worksheet()

    year = text[-1]

    if year in worksheet_list:
      data = gsheet.getKas(year)
      user=[users['NAMA'].lower() for users in data]
      month=['januari','febuari','maret','april','mei','juni','juli','agustus','september','oktober','november','desember']
      if text[1].lower() in user:
        print(text[1].lower())
        ENV = Environment(loader=FileSystemLoader('.'))
        TEMPLATE_PATH = './templates/user.j2'
        baseline = ENV.get_template(TEMPLATE_PATH)
        for user in data:
          if user['NAMA'].lower() == text[1].lower():
             new_data = user
        print(new_data)
        message = baseline.render(data=new_data)
        print(message)
        context.bot.send_message(chat_id=update.effective_chat.id,text=message,parse_mode=telegram.ParseMode.MARKDOWN)
      elif text[1].lower() in month:
        ENV = Environment(loader=FileSystemLoader('.'))
        TEMPLATE_PATH = './templates/month.j2'
        baseline = ENV.get_template(TEMPLATE_PATH)
        new_data=[[user['NAMA'],user[text[1].upper()]] for user in data]
        message = baseline.render(data=new_data,month=text[1])
        context.bot.send_message(chat_id=update.effective_chat.id,text=message,parse_mode=telegram.ParseMode.MARKDOWN)
      else:

        context.bot.send_message(chat_id=update.effective_chat.id,text="Format salah!")

    else:
      context.bot.send_message(chat_id=update.effective_chat.id,text="Tahun pelajaran tidak ditemukan!")