#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from institutionSystem.platform import institutionPlatform
from institutionSystem import utils

def main():

    print("################################################################"                     )
    print("#               ",utils.colored("Welcome to Tata Code College!", "cyan"),"                #")
    print("################################################################\n\n"                 )

    tataCodeCollege = institutionPlatform()

    tataCodeCollege.menu()

    print("\n\nDone!\n\n")

if __name__ == '__main__':
    main()