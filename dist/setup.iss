; Script for Inno Setup to install bot.exe, .env, logs.txt, and the _internal folder with a shortcut in shell:startup
[Setup]
AppName=Telegram Notify
AppVersion=1.0
DefaultDirName={pf}\Telegram Notify
DefaultGroupName=Telegram Notify
DisableProgramGroupPage=yes
OutputDir=.
OutputBaseFilename=TelegramNotifyInstaller
Compression=lzma
SolidCompression=yes

[Files]
; Указываем файлы, которые будут добавлены в папку установки
Source: "bot\bot.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: ".env"; DestDir: "{app}"; Flags: ignoreversion
Source: "bot\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; Shortcut in shell:startup (Startup folder)
Name: {userstartup}\Telegram Notify; Filename: {app}\bot.exe; WorkingDir: {app}; IconFilename: {app}\bot.exe

[Code]
procedure InitializeWizard();
begin
  WizardForm.DirEdit.Text := ExpandConstant('{pf}\Telegram Notify');
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then begin
    MsgBox('Telegram Notify успешно установлен. Приложение будет автоматически запускаться при входе в систему.', mbInformation, MB_OK);
  end;
end;
