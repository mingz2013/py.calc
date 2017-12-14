# -*- coding:utf-8 -*-
"""

词法分析

"""
__date__ = "14/12/2017"
__author__ = "zhaojm"

from token import token


def is_letter(ch):
    return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or ch == '_'


def is_digit(ch):
    return '0' <= ch <= '9'


class Scanner(object):
    def __init__(self, src):
        self.tokens = []
        self.src = src

        self.ch = ' '
        self.offset = -1

        print(self.src)
        print("=========")

    def next_ch(self):
        print("next_ch", self.offset, self.ch)
        self.offset += 1

        if self.offset < len(self.src):
            self.ch = self.src[self.offset]
        else:
            self.offset = len(self.src)
            self.ch = -1  # eof

    def skip_white_space(self):
        """
        跳过空白部分
        :return:
        """
        # self.next_ch()
        while self.ch in (' ', '\t', '\n', '\r'):
            self.next_ch()

    def scan_identifier(self):
        """
        id
        :return:
        """
        offs = self.offset

        self.next_ch()
        while is_letter(self.ch) or is_digit(self.ch):
            self.next_ch()
        self.next_ch()
        return self.src[offs:self.offset]

    def scan_number(self):
        offs = self.offset
        self.next_ch()
        while is_digit(self.ch):
            self.next_ch()
        self.next_ch()
        return self.src[offs: self.offset]

    def scan(self):
        self.skip_white_space()
        pos = self.offset
        ch = self.ch

        if is_letter(ch):
            tok = token.IDENT
            lit = self.scan_identifier()
        elif is_digit(ch):
            tok = token.NUMBER
            lit = self.scan_number()
        else:
            lit = ch
            self.next_ch()
            if ch == -1:
                tok = token.EOF
            elif ch == '+':
                tok = token.ADD
            elif ch == '-':
                tok = token.SUB
            elif ch == '*':
                tok = token.MUL
            elif ch == '/':
                tok = token.DIV
            else:
                raise Exception("Unknown char", ch)

        return pos, tok, lit
