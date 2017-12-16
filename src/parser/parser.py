# -*- coding:utf-8 -*-
"""

语法分析

"""
__date__ = "14/12/2017"
__author__ = "zhaojm"

from scanner.scanner import Scanner
from token import token


class Parser(object):
    def __init__(self, filename, src):
        self.file = token.File(filename)

        self.scanner = Scanner(self.file, src)

        self.pos = None
        self.tok = None
        self.lit = None

        self.next_token()

    def next_token(self):
        self.pos, self.tok, self.lit = self.scanner.scan()
        print('--------------------', self.pos, self.tok, self.lit)
        if self.tok == token.EOF:
            pass
