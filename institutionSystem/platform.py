#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from getpass                          import getpass
from institutionSystem.administrative import admin
from institutionSystem.teacher        import teacher
from institutionSystem.student        import student
from institutionSystem                import utils

class institutionPlatform(object):
    """
    General plataform class where the institution can create its environment attributes
    such as institution name, teacher and student register and so.
    """

    def __init__(self):
        pass

    def menu(self):
        
        print("\nSelect user: \n1. Admin\n2. Teacher\n3. Student\n\n")

        user = input("Enter the selected option: ")

        if user == "Admin" or user == "1":
            self.userAdmin = admin()
        
        elif user == "Teacher" or user == "2":
            self.userTeacher = teacher()
        
        elif user == "Student" or user == "3":
            self.userStudent = student()
        
        else:
            print(utils.colored("\nError: Invalid option Selected. Try again!\n","red"))

            self.menu()

    def login(user, password):
        pass

