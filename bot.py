from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "မင်္ဂလာပါ ခင်ဗျာ။ 👍\nဝယ်ယူထားတဲ့ ငွေလွှဲစလစ် (Wave Pay Slip) ပုံကို ဒီချတ်ထဲသို့ ပို့ပေးပါ။"
    )

def main():
    token = "8693443035:AAGWqmRM2WQP6vVXhJCA_bfbsBt4DMSVztU"
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot is running on cloud...")
    application.run_polling()

if __name__ == "__main__":
    main()
                
