# Emulation Station

Got fed up with various ROM execution methods for different console emulators. So I wrote a work around that uses WSL to nicely generate and run a windows shortcut for a chosen ROM and emulator. The program uses the python3 package `readline` to allow user ease for WSL terminal selection of console and game. To use you will need WSL and to change all the paths to be for your machine.
## Example of use:
```bash
Foo@Bar:Emulation_Station$ python3 emulation_station.py

Emulation Station options:

Consoles in your library:
 - Playstation
 - Playstation 2
 - Playstation 3

Input the console you want to play:
Playstation 2


Games in your Playstation 2 library:

 - Tony Hawk's American Wasteland
 - Tony Hawk's Pro Skater 3
 - Tony Hawk's Pro Skater 4
 - Tony Hawk's Project 8
 - Tony Hawk's Underground

Input the game you want to play:
Tony Hawk's American Wasteland

 - Tony Hawk's American Wasteland.ISO
 ```

The program will make and execute a file called `rom_execution.bat` which contains the following:

```bash
"path to...\PS2\PCSX2 1.6.0\pcsx2.exe"  "path to...\ROM's\Playstation 2\Tony Hawk's American Wasteland\Tony Hawk's American Wasteland.ISO"
```


### make desktop shortcuts
```bash
Foo@Bar:Emulation_Station$ python3 make_desktop_shortcut.py

Emulation Station options:

Consoles in your library:
 - Nintendo DS
 - Nintendo GBA
 - Nintendo Wii
 - Nintendo Wii U
 - Playstation
 - Playstation 2
 - Playstation 3

Input Console you want to play:
Playstation 3


Games in your Playstation 3 library:
 - Call_of_Duty_World_at_War
 - DLCs and Extras
 - Call of Duty Modern Warfare 3
 - MotorStorm
 - Call of Duty Black Ops
 - Far Cry 2
 - Skate
 - Skate 2
 - Skate 3

Input the game you want to play:
Skate 3

$WScriptShell = New-Object -ComObject WScript.Shell;$Shortcut = $WScriptShell.CreateShortcut("C:\Users\benja\Desktop\Skate 3.lnk");$Shortcut.TargetPath = '"C:\Users\benja\Documents\Entertainment\Gaming\Launchers\PS3\rpcs3.exe"';$ShortCut.Arguments=' "E:\ROMs\Playstation 3\Skate 3\PS3_GAME\USRDIR\EBOOT.BIN"';$shortcut.IconLocation="E:\ROM_ICOs\Skate 3.ico";$Shortcut.Save()
powershell.exe -ExecutionPolicy Bypass -File make_shortcut.ps1
```


The program will make and execute a file called `make_shortcut.ps1` which contains the following:

```bash
$WScriptShell = New-Object -ComObject WScript.Shell;$Shortcut = $WScriptShell.CreateShortcut("C:\Users\benja\Desktop\Skate 3.lnk");$Shortcut.TargetPath = '"C:\Users\benja\Documents\Entertainment\Gaming\Launchers\PS3\rpcs3.exe"';$ShortCut.Arguments=' "E:\ROMs\Playstation 3\Skate 3\PS3_GAME\USRDIR\EBOOT.BIN"';$shortcut.IconLocation="E:\ROM_ICOs\Skate 3.ico";$Shortcut.Save()```
```

### Future goals
 - gui xmb interface with controller interaction
