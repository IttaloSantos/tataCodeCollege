#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

class institutionPlatform(object):
    """
    General plataform class where the institution can create its environment attributes
    such as institution name, teacher and student register and so.
    """

    def __init__(self, login, password):
        self.admLogin = login
        self.admPass  = password