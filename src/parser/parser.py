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
        # if self.tok == token.EOF:
        #     pass
        # else:
        #
        #     # self.next_token()
        #     pass

    def parse_file(self):
        return self.expression()

    def error(self):
        print("error....")
        exit(1)

    def expression(self):
        """表达式"""
        print("expression....")
        ret = self.relational_expression()

        if self.tok != token.EOF:
            self.error()  # 解析完一个完整的表达式后，没有结束
        print("expression...>", ret)
        return ret

    def relational_expression(self):
        """加减类表达式"""
        print("relational_expression....")
        ret = self.multiplicative_expression()
        while self.tok == token.ADD or self.tok == token.SUB:

            tok1 = self.tok

            self.next_token()
            ret2 = self.multiplicative_expression()

            if tok1 == token.ADD:
                tmp_ret = ret
                ret += ret2
                print(tmp_ret, "+", ret2)
            elif tok1 == token.SUB:
                tmp_ret = ret
                ret -= ret2
                print(tmp_ret, "-", ret2)
            else:
                self.error()

        print("relational_expression...>", ret)
        return ret

    def multiplicative_expression(self):
        """乘除类表达式"""
        print("multiplicative_expression....")
        ret = self.unary_expression()

        while self.tok == token.DIV or self.tok == token.MUL:
            tok1 = self.tok

            self.next_token()
            ret2 = self.unary_expression()

            if tok1 == token.DIV:
                tmp_ret = ret
                ret /= ret2
                print(tmp_ret, "/", ret2)
            elif tok1 == token.MUL:
                tmp_ret = ret
                ret *= ret2
                print(tmp_ret, "*", ret2)
            else:
                self.error()

        print("multiplicative_expression...>", ret)
        return ret

    def unary_expression(self):
        """一元表达式"""
        print("unary_expression....")
        ret = self.primary_expression()
        # if self.tok == token.ADD or self.tok == token.SUB or self.tok == token.MUL:
        #
        #     tok1 = self.tok
        #
        #     self.next_token()
        #     ret2 = self.unary_expression()
        #
        #     if tok1 == token.ADD:
        #         ret += ret2
        #         print(ret - ret2, "+", ret2)
        #     elif tok1 == token.SUB:
        #         ret -= ret2
        #         print(ret + ret2, "-", ret2)
        #     elif tok1 == token.MUL:
        #         ret *= ret2
        #         print(ret / ret2, "*", ret2)
        #     else:
        #         self.error()

        print("unary_expression...>", ret)
        return ret

    def primary_expression(self):
        """初值表达式"""
        print("primary_expression....", self.tok, self.lit)
        if self.tok == token.NUMBER:

            ret = int(self.lit)

            self.next_token()

        else:
            self.error()  # 两个符号连续了
        print("primary_expression...>", ret)
        return ret
