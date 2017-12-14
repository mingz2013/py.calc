# -*- coding:utf-8 -*-
"""
"""
__date__ = "14/12/2017"
__author__ = "zhaojm"

import codecs

from scanner.scanner import Scanner


class Parser(object):
    def __init__(self):
        pass

    def parse(self, filename):
        with codecs.open(filename, encoding='utf-8') as f:
            Scanner(f.read()).scan()
