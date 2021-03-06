
from pathlib import PureWindowsPath,Path
import os
import readline
from colours import *

##############################################################

path_to_ROMS       = "/media/E_USB/ROMs"
path_to_emulators  = '/mnt/c/Users/LaunchBox/Emulators'

#needed to launch windows shortcut
win_exe = "/mnt/c/Windows/explorer.exe"

win_path_to_ROMS       = "E:\\ROMs"
win_path_to_emulators  = "C:\\Users\\benja\\LaunchBox\\Emulators"

##############################################################

def set_tab_complete_options(options):
    """
    allows user to tab complete inputs
    """

    readline.parse_and_bind("tab: complete")

    def complete(text,state):
        if text:
            results = [s for s in options if s and s.startswith(text)]
        else: 
            results = results[:]

        return results[state]

    readline.set_completer(complete)

def find_rom_in_dir(path_to_dir):
    """
    prints & returns the roms within the supplied directory
    """
    repo_list = []
    rom_exts = ['.nds','.gba','.wbfs','.iso','.ISO','.wux','.bin']
    for d in os.listdir(path_to_dir) :
        for rom_ext in rom_exts:
            if rom_ext in d:
                print(' - '+green+str(d)+white)
                repo_list.append(d)

    return repo_list

def print_dirs_in_dir(path_to_dir):
    """
    prints & returns the directories within the supplied directory
    """
    repo_list = []
    for d in os.listdir(path_to_dir) :
        if '.' not in d:
            print(' - '+green+str(d)+white)
            repo_list.append(d)

    return repo_list

def select_emulator(console):
    """
    returns the associated emulator path for  given console
    """
    if console == 'Nintendo DS':
        pass
    if console == 'Nintendo GBA':
        pass
    if console == 'Nintendo Wii':
        emulator =  win_path_to_emulators+"\\Wii\\Dolphin-x64\\Dolphin.exe"
        flags = "-e"
        return emulator,flags
    if console == 'Nintendo Wii U':
        emulator =  win_path_to_emulators+"\\Wii U\\cemu_1.17.4\\Cemu.exe"
        flags = "-g"
        return emulator,flags
    if console == 'Playstation':
        pass
    if console == 'Playstation 2':
        emulator = win_path_to_emulators+"\\PS2\\PCSX2 1.6.0\\pcsx2.exe"
        flags = ""
        return emulator,flags
    if console == 'Playstation 3':
        emulator = win_path_to_emulators+"\\PS3\\rpcs3.exe"
        flags = ""
        return emulator,flags
    if console == 'Playstation Portable':
        pass
    print('emulator not configured yet.')
    exit(0)

def choose_console():
    """
    allows user to pick a console/ dir name
    """
    print('\nConsoles in your library:')
    choice_list = print_dirs_in_dir(path_to_ROMS)
    set_tab_complete_options(choice_list)
    choice = input('\nInput Console you want to play:\n'+input_colour)
    print(''+white)
  
    if choice == 'exit':
        exit(0)

    if choice in choice_list:
        console = choice
        return console
    else:
        print('not a valid input')
        choose_console()

def choose_game(console):
    """
    ask user to choose the game a preivoulst chosen console
    ,will return path to that rom
    """
    print('\nGames in your {} library:'.format(console))
    choice_list = print_dirs_in_dir(path_to_ROMS+"/"+console)
    set_tab_complete_options(choice_list)
    choice = input('\nInput the game you want to play:\n'+input_colour)
    print(''+white)
  
    if choice == 'exit':
        exit(0)

    if choice in choice_list:
        game_name = choice.split('.')[0]
        if console == "Playstation 3":
            rom = "PS3_GAME\\USRDIR\\EBOOT.BIN"
        else:
            rom = find_rom_in_dir(path_to_ROMS+"/"+console+"/"+choice)[0]
        game = win_path_to_ROMS+"\\"+console+"\\"+choice + "\\" +rom
        return game,game_name
    else:
        print('not a valid input')
        choose_game()

def make_shortcut(emulator,flags,rom,shortcut_name):
    """
    will generate a windows batch file containing the paths for the emulator
    and rom with the correct emulator flags
    """

    emulator = PureWindowsPath(Path(emulator))
    rom = PureWindowsPath(Path(rom.replace("'","`")))

  #  command  = '"{}" {} "{}"'.format(emulator,flags,game)
    desktop  = win_path_to_desktops + '\\' + shortcut_name+'.lnk'

    ico_check = path_to_ICOS +'/'+ shortcut_name+'.ico'

    if not os.path.exists(ico_check):
        ico_name = win_path_to_ICOS +'\\es_not_found.ico'
    else:
        ico_name = win_path_to_ICOS +'\\'+ shortcut_name +'.ico'

    ico_name = PureWindowsPath(Path(ico_name))

    fcontents = '$WScriptShell = New-Object -ComObject WScript.Shell;$Shortcut = $WScriptShell.CreateShortcut("{}");$Shortcut.TargetPath = \'"{}"\';$ShortCut.Arguments=\'{} "{}"\';$shortcut.IconLocation=\"{}\";$Shortcut.Save()'.format(desktop,emulator,flags,rom,ico_name)
    print(fcontents)
    f = open("make_shortcut.ps1".format(shortcut_name), "w")
    f.write(fcontents)
    f.close()

    ostr = "powershell.exe -ExecutionPolicy Bypass -File make_shortcut.ps1".format(win_exe)
    print(ostr)
    os.system(ostr)

def main_menu():
    """
    main function of this file which acts as an interactive menu call other functions
    """
    print('\nEmulation Station options:')

    console        = choose_console()
    game,game_name = choose_game(console)
    emulator,flags = select_emulator(console)

    make_shortcut(emulator,flags,game,game_name)
    exit(0)
    
main_menu()

def make_shortcuts_from_list():
    """
    """
    shortcuts = [
                {'emulator':'',
                 'rom' : '',
                 'ico' : ''}]

    for shortcut in shortcuts:
        console  = shortcut['console']
        rom      = shortcut['rom']
        ico      = shortcut['ico']

        make_shortcut(emulator,flags,game,game_name)