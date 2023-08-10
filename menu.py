# -*- coding: utf-8 -*-
import keyboard as kb
import os
import time

class Menu():
    '''
    Class representing a menu item with a list of items
    items: dict          - dict with items and functions
    __point_list: list   - list with keys of items
    __pointer: int       - pointer to the current menu item

    def update(self):    - clear terminal and print new menu
    def move_up(self):   - move menu point up
    def move_down(self): - move menu point down
    def start(self):     - main menu loop
    '''
    items: dict
    __point_list: list
    __pointer: int

    def __init__(self, title: str, items: dict):
        self.title = title
        self.items = items
        self.__point_list = list(items.keys())
        self.__pointer = 0

    def __str__(self):
        return self.title + "\n" + "\n".join(
            [f"{'->' if self.__point_list[self.__pointer] == key else '--'} {key}" for key in self.items.keys()])

    def update(self):
        '''clear terminal and print new menu'''
        os.system('cls')
        print(self)

    def move_up(self):
        '''move menu point up'''
        self.__pointer -= 1
        if self.__pointer < 0:
            self.__pointer = len(self.__point_list) - 1
        self.update()

    def move_down(self):
        '''move menu point down'''
        self.__pointer += 1
        if self.__pointer > len(self.__point_list) - 1:
            self.__pointer = 0
        self.update()


    def start(self):
        '''main menu loop'''
        self.update()
        running = True
        time.sleep(0.1)

        while running:
            if kb.is_pressed('down'):
                self.move_down()
                time.sleep(0.2)

            if kb.is_pressed('up'):
                self.move_up()
                time.sleep(0.2)

            if kb.is_pressed('space') or kb.is_pressed('enter'):
                item = self.items[self.__point_list[self.__pointer]]()
                if item:
                    self.update()

                time.sleep(0.2)

            if kb.is_pressed('esc'):
                running = False
        return 1
