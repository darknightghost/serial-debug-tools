#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
      Copyright 2017, 王思远 <darknightghost.cn@gmail.com>
      This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
      You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import Formater

class SendFormater(Formater.SendFormater):
    '''
        Class which is used to get data to send. It should be implemented by 
        formaters.
    '''
    def __init__(self, args):
        '''
            SendFormater(args) -> formater
        '''
        return
    
    def get_data(self):
        '''
            formater.get_data() -> bytes

            Get data to send.
        '''
        while True:
            text = input("Input hex to send : ")
            data = []
            text = text.split()
            try:
                for t in text:
                    data.append(int(t, base = 0x10))
                data = bytes(data)
                break

            except ValueError:
                print("Illefal input!")
                continue

        return data

    def close(self):
        '''
            formater.close()

            Close send formater.
        '''
        return

class RecvFormater(Formater.RecvFormater):
    '''
        Class which is used to format received data and display them. It should
        be implemented by formaters.
    '''
    def __init__(self, args):
        '''
            RecvFormater(args) -> formater
        '''
        return

    def on_data(self, data):
        '''
            formater.on_data(data)
            
            Display bytes received.
        '''
        for i in range(0, len(data)):
            if i % 0x10 == 0:
                print("\n0x%.8X : "%(i), end = "")

            print("%.2x "%(i), end = "")

        print("")
        return

    def close(self):
        '''
            formater.close()

            Close receive formater.
        '''
        return
