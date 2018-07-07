# -*- coding:utf-8 -*-
"""

语法分析，生成抽象语法树



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
        """获取下一个token"""
        print("next_token...")
        self.pos, self.tok, self.lit = self.scanner.scan()
        print('--------------------', self.pos, self.tok, self.lit)
        if self.tok == token.EOF:
            pass
        else:

            # self.next_token()
            pass

    def parse_file(self):
        self.expression()

    def error(self):
        print("error....")
        exit(1)

    def expression(self):
        """表达式"""
        print("expression....")
        self.relational_expression()

        if self.tok != token.EOF:
            self.error()  # 解析完一个完整的表达式后，没有结束

    def relational_expression(self):
        """加减类表达式"""
        print("relational_expression....")
        self.multiplicative_expression()
        while self.tok == token.ADD or self.tok == token.SUB:
            self.next_token()
            self.multiplicative_expression()

    def multiplicative_expression(self):
        """乘除类表达式"""
        print("multiplicative_expression....")
        self.unary_expression()
        while self.tok == token.DIV or self.tok == token.MUL:
            self.next_token()
            self.unary_expression()

    def unary_expression(self):
        """一元表达式"""
        print("unary_expression....")
        self.primary_expression()
        if self.tok == token.ADD or self.tok == token.SUB or self.tok == token.MUL:
            self.next_token()
            self.unary_expression()

    def primary_expression(self):
        """初值表达式"""
        print("primary_expression....", self.tok, self.lit)
        if self.tok == token.NUMBER:
            self.next_token()

        else:
            self.error()  # 两个符号连续了
