# -*- coding:utf-8 -*-
"""

语法分析

"""
__date__ = "14/12/2017"
__author__ = "zhaojm"

import codecs

from scanner.scanner import Scanner
from token import token


class Parser(object):
    def __init__(self):
        pass

    def parse(self, filename):
        with codecs.open(filename, encoding='utf-8') as f:

            s = Scanner(f.read())

            i = 100
            while True:
                i -= 1
                pos, tok, lit = s.scan()
                print('--------------------', pos, tok, lit)
                if tok == token.EOF or i < 0:
                    break
