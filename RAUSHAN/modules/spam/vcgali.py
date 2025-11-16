import random
import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
from gtts import gTTS
import os

from config import API_ID, API_HASH, STRING_SESSION1

client = Client("vcgali", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1)
call = PyTgCalls(client)

GALI = [
    "Jaa na bhosdike, gaand mara jaake.",
    "Teri maa ki chut me dynamite phod dunga.",
    "Randi ke bacche chup baith.",
    "Aand ka na gaand ka, gyaan jhaarr raha hai.",
    "Madarchod teri shakal dekh ke mirchi bhi ro diye."
]

@client.on_message(filters.command("vcgali", ".") & filters.me)
async def vc_gali(client, message):
    chat_id = message.chat.id

    await message.edit("🎤 **Voice Chat Join Ho Raha Hai...**")

    try:
        await call.join_group_call(
            chat_id,
            InputAudioStream("silent.mp3")
        )
    except:
        pass

    abuse = random.choice(GALI)

    tts = gTTS(abuse, lang="hi")
    tts.save("gali.mp3")

    await message.edit(f"🎧 **VC Gali:**\n`{abuse}`")

    await call.change_stream(
        chat_id,
        InputAudioStream("gali.mp3")
    )

    await asyncio.sleep(5)

    await call.leave_group_call(chat_id)
    os.remove("gali.mp3")
