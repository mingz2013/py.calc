# -*- coding:utf-8 -*-
"""

词法分析

"""
__date__ = "14/12/2017"
__author__ = "zhaojm"


class Scanner(object):
    def __init__(self, src):
        self.tokens = []
        self.src = src
        self.current_line = None

        print(self.src)

    def scan(self):
        pass

