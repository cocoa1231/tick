#!/usr/bin/env python

import os, platform, sys

def get_platform():
    if not '--platform' in sys.argv:
        try:
            pform = platform.dist()[0].lower()
            return pform
        except SyntaxError:
            print("Fatal! Could not get platform, please pass it in by the --platform flag")
            raise Exception("Could not get platform")

    pform = sys.argv[ sys.argv.index('--platform') + 1 ].lower() # Get the next item to the platform flag

    return pform


def install_ubuntu():
    
    print("Installing for Ubuntu Linux...")

    apt_packages = 'colordiff python3-pip'
    if os.system('sudo apt install {}'.format(apt_packages)):
        raise Exception("Failed to install dependencies")
    
    if os.system('sudo pip install -r requirements.txt'):
        raise Exception("Failed to install dependencies")

    if os.system('chmod +x init.py'):
        raise Exception("Failed to mark init.py as executable. Check permissions")

    return True 


def install_arch():
    
    print("Installing for Arch Linux...")

    pacman_packages = 'colordiff python-pip'
    if os.system('sudo pacman -S {}'.format(pacman_packages)):
        raise Exception("Failed to install dependencies")
    
    if os.system('sudo pip install -r requirements.txt'):
        raise Exception("Failed to install dependencies")

    if os.system('chmod +x init.py'):
        raise Exception("Failed to mark init.py as executable. Check permissions")

    return True 


if __name__ == '__main__':
    pform = get_platform()

    # Python's version to a switch-case
    install_type = { 'ubuntu' : install_ubuntu,
                     'arch'   : install_arch     }

    # Run the installation
    install_type[pform]()
