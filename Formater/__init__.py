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
import importlib

def open_send_formater(name, args):
    '''
        Open a send formater.
    '''

    path = os.path.dirname(__file__)
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)) and f not in (".", ".."):
            if f == name:
                m_name = "Formater.%s"%(name)
                m = importlib.import_module(m_name)
                return m.SendFormater(args)

    else:
        raise FileNotFoundError("Formater \"%s\" not found."%name)

    return None

def open_recv_formater(name, args):
    '''
        Open a receive formater.
    '''

    path = os.path.dirname(__file__)
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)) and f not in (".", ".."):
            if f == name:
                m_name = "Formater.%s"%(name)
                m = importlib.import_module(m_name)
                return m.RecvFormater(args)

    else:
        raise FileNotFoundError("Formater \"%s\" not found."%name)

    return None

class SendFormater:
    '''
        Class which is used to get data to send. It should be implemented by 
        formaters.
    '''
    def __init__(self, args):
        '''
            SendFormater(args) -> formater
        '''
        raise NotImplementedError
    
    def get_data(self):
        '''
            formater.get_data() -> bytes

            Get data to send.
        '''
        raise NotImplementedError

    def close(self):
        '''
            formater.close()

            Close send formater.
        '''
        raise NotImplementedError

class RecvFormater:
    '''
        Class which is used to format received data and display them. It should
        be implemented by formaters.
    '''
    def __init__(self, args):
        '''
            RecvFormater(args) -> formater
        '''
        raise NotImplementedError
    
    def on_data(self, data):
        '''
            formater.on_data(data)
            
            Display bytes received.
        '''
        raise NotImplementedError

    def close(self):
        '''
            formater.close()

            Close receive formater.
        '''
        raise NotImplementedError
