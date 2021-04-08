#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from institutionSystem.platform import institutionPlatform
from getpass import getpass

def main():

    print("################################################################"    )
    print("#               Welcome to Tata Code College!                  #"    )
    print("################################################################\n\n")

    admLogin        = input("Input adm login: "     )
    admPass         = getpass("Input adm password: ")

    tataCodeCollege = institutionPlatform(admLogin, admPass)

    print("\n\nDone!\n\n")

if __name__ == '__main__':
    main()