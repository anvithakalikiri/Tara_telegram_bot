import os
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from openai import OpenAI
key1=os.environ.get('key1')
client = OpenAI(api_key=key1)



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm Tara, How can i help you?")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
   response=openai(update.message.text)
   await context.bot.send_message(chat_id=update.effective_chat.id,text=response)
   print(response)
def openai(user):
  completion = client.chat.completions.create(model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": user}])
  print(completion.choices[0].message.content)
  return completion.choices[0].message.content

if __name__ == '__main__':
    key2=os.environ.get('key2')
    application = ApplicationBuilder().token(key2).build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.run_polling()
