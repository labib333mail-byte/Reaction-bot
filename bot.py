import os
import random
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

REACTIONS = ["❤️", "👍", "🔥", "😘", "😍", "🎉", "👀"]

async def react_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if not message:
        return

    reaction = random.choice(REACTIONS)

    try:
        await message.set_reaction(
            reaction=[{"type": "emoji", "emoji": reaction}]
        )
    except Exception as e:
        print(f"Reaction error: {e}")


def main():
    token = os.getenv("8606081959:AAEoKsVPHD72ZiP3OXbxchcYUWHc4hqmHCo

    if not token:
        raise ValueError("BOT_TOKEN is missing!")

    app = Application.builder().token(token).build()

    app.add_handler(
        MessageHandler(
            filters.ALL & ~filters.COMMAND,
            react_to_message
        )
    )

    print("🤖 Random Reaction Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
