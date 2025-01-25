# Telegram Notify Bot Installer

This guide will help you build and sign the executable for the Telegram Notify Bot and create an installer using Inno Setup.

## Installation and Build Steps

1. **Install Dependencies**  
   Install the required Python dependencies listed in the `requirements.txt` file:
   ```bash
   
   pip3 install -r requirements.txt
   ```

2. **Assembly of the executable file**
   Assemble the executable file using `PyInstaller`:
  
    ```bash
    python -m PyInstaller bot.spec
     ```

3. **Signature of the executable file**
   Sign the collected file bot.exe using `signtool`:
  
    ```bash
    signtool sign /a /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 bot.exe
    ```

4. **Creating an installer**
   Create an installer using `Inno Setup':

   Open the file ```setup.iss``` in Inno Setup.
   
   Click **Build** to create the installer.
   
   The result is a file ```TelegramNotifyInstaller.exe ```
