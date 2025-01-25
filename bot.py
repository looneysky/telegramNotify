import socket
from datetime import datetime
import telebot
import wmi
import requests
from dotenv import load_dotenv
import os

# Загрузка переменных из .env
load_dotenv()

# Переменные из .env
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_IDS = os.getenv('TELEGRAM_CHAT_IDS').split(',')

def send_message(bot, chat_ids, message):
    """Отправляем сообщение в бот на каждый ID из массива."""
    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id=chat_id, text=message)
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {chat_id}: {e}")

def get_computer_name():
    """Возвращаем имя компьютера."""
    return socket.gethostname()

def get_last_reboot_time():
    """Определяет время последней перезагрузки на основе системных журналов."""
    try:
        conn = wmi.WMI()
        query = conn.query("SELECT * FROM Win32_OperatingSystem")
        for os_info in query:
            boot_time = os_info.LastBootUpTime.split('.')[0]
            return datetime.strptime(boot_time, '%Y%m%d%H%M%S')
    except Exception as e:
        print(f'Ошибка вида: {e}')
        exit(1)

def monitor_reboot():
    """Мониторинг перезагрузок и отправка уведомлений."""
    bot = telebot.TeleBot(TELEGRAM_TOKEN)
    computer_name = get_computer_name()
    last_reboot_time = get_last_reboot_time()
    
    if last_reboot_time is None:
        send_message(bot, TELEGRAM_CHAT_IDS, f"Ошибка при получении времени последней перезагрузки на компьютере {computer_name}.")
        return

    send_message(bot, TELEGRAM_CHAT_IDS, f"Компьютер {computer_name} был перезагружен.\n"
                                         f"Время перезагрузки: {last_reboot_time.strftime('%Y-%m-%d %H:%M:%S')}.")
if __name__ == '__main__':
    monitor_reboot()
