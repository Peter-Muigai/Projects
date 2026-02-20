import pywhatkit as kit
import datetime

class WhatsAppBot:
    def __init__(self, group_id):
        self.__group_id = group_id  # private attribute
        self.__log = []             # private message log

    def send_message(self, message, hour=None, minute=None):
        if hour is None or minute is None:
            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute + 2  # default: send 2 minutes later

        try:
            formatted_msg = f"_*{message}*_"  # WhatsApp formatting
            kit.sendwhatmsg_to_group(self.__group_id, formatted_msg, hour, minute)
            self.__log.append(f"Message sent at {hour}:{minute} -> {message}")
            print("✅ Message scheduled.")
        except Exception as e:
            print("❌ Error sending message:", e)

    def get_log(self):
        return self.__log.copy()
