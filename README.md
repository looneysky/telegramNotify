pip3 install -r requirements.txt # Установка зависимостей
python -m PyInstaller bot.spec # Билд EXE
signtool sign /a /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 bot.exe # Подпись EXE

Через Inno Setup билдим установщик (файл setup.iss), получаем TelegramNotifyInstaller.exe