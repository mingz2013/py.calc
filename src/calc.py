# -*- coding:utf-8 -*-
"""
"""
__date__ = "14/12/2017"
__author__ = "zhaojm"

import os
import sys

sys.path.append(os.path.dirname("."))

from parser.parser import Parser


def calc():
    Parser().parse("test/0.1.calc")


if __name__ == "__main__":
    calc()
