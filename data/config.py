# from environs import Env
#
# # Теперь используем вместо библиотеки python-dotenv библиотеку environs
# env = Env()
# env.read_env()
#
# BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
# ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
# IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
#
import os

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot token
ADMINS = list(os.environ.get("ADMINS"))  # adminlar ro'yxati
IP = str(os.environ.get("ip"))  # Xosting ip manzili
# PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))