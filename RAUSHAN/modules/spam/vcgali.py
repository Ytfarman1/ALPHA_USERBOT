import random
from pyrogram import Client, filters
from pyrogram.types import Message

# Abuse list (VC Gali)
VC_GALI = [
    "Jaa na Bsdk, gaand mara jaake.",
    "Tu paidaishi chutiya hai ki koi course kiya hai?",
    "randi chod ke 1/- me apni gand bech le",
    "lode pe lagi hai haldi chuss mere jaldi",
    "And the truth is, you're a fucking cunt",
    "Bohot Sari RANDI dekhi lakin teri chut sabse aalag",
    "Jaa na Gandu",
    "Aand ka na Gaand ka, Gyaan jhaare pure Brahmand ka",
    "Dhaat teri maa ki chut",
    "Gaand se tatti nikalke jaadugar samajhta hai apne aap ko?",
    "kitne me bechaga?",
    "izzat karo humari warna maa chod denge tumari",
    "Tu aise nhi maanega - Mat maan, maa chuda",
    "Tujhse zada sundar teri jali hui gaand hai",
]


# Main command
@Client.on_message(filters.command(["vcgali", "vc_abuse"], ".") & filters.me)
async def vcgali_cmd(client: Client, message: Message):
    await message.edit(random.choice(VC_GALI))
