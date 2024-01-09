import streamlit as st
import os
import asyncio
from telegram import Bot
from telegram.error import TelegramError

# Replace these with your bot's token and your chat ID
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN","6671561034:AAE-I-eUsf81XsIBup_wVzpn7wbRecEMAnk")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID","729712388")

bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_notification(message, photo=None):
    try:
        # Send the text message
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

        if photo is not None:
            # Assuming 'photo' is a file-like object
            # If it's a file path, you may use open(photo, 'rb') instead
            await bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=photo)

    except TelegramError as e:
        print(f"An error occurred: {e}")

st.set_page_config(page_title="Access Request Midtown", page_icon="🔒")

st.sidebar.title("Access Request Midtown")
choice = st.sidebar.radio("Select an Form", ("אישור זמני", "אישור קבוע"))


if choice == "אישור זמני":
    st.header("טופס אישור כניסה זמני מידטאון")
    with st.form("temp_access_form"):
        floor = st.text_input("קומת יעד")
        date = st.date_input("תאריך כניסה")
        end_date = st.date_input("תאריך סיום")
        full_name = st.text_input("שם מלא")
        id_number = st.text_input("ת.ז.")
        mobile_phone = st.text_input("טלפון נייד")
        job = st.text_input("תפקיד")
        escort = st.text_input("מלווה")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            message = f"אישור כניסה:\nקומת יעד - {floor}\nתאריך כניסה - {date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')} \nשם מלא - {full_name}\nת.ז. - {id_number}\nטלפון נייד - {mobile_phone}\nתפקיד - {job}\nמלווה - {escort}"
            asyncio.run(send_notification(message))

if choice == "אישור קבוע":
    st.header("טופס אישור כניסה קבוע מידטאון")
    with st.form("perm_access_form"):
        floor = st.text_input("קומת יעד")
        date = st.date_input("תאריך כניסה")
        sivog = st.text_input("סיווג")
        first_name = st.text_input("שם פרטי")
        last_name = st.text_input("שם משפחה")
        id_number = st.text_input("ת.ז.")
        mobile_phone = st.text_input("טלפון נייד")
        job = st.text_input("תפקיד")
        escort = st.text_input("מלווה")
        st.write("Upload a photo or take one using your camera.")

        photo_upload = st.file_uploader("Upload Photo", type=["jpg", "png"])
        photo_camera = st.camera_input("Take a photo")

        photo = photo_camera or photo_upload

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            message = f"אישור כניסה קבוע :\nקומת יעד - {floor}\nתאריך כניסה - {date.strftime('%d/%m/%Y')}\nשם פרטי - {first_name}\nשם משפחה - {last_name}\nת.ז. - {id_number}\nטלפון נייד - {mobile_phone}\nתפקיד - {job}\nמלווה - {escort} \nסיווג - {sivog}"
            asyncio.run(send_notification(message, photo))