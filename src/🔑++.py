#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8

from __future__ import print_function

import sys
import ast
# import argparse
import re

# parser = argparse.ArgumentParser(description='#WETHEBEST')
# parser.add_argument("source")
# args = parser.parse_args()

# parse(args.source)

khaled = {
    "boilerplate"   :   r"#DJKHALED\n#WETHEBEST",
    "import"        :   r"fanluv (?P<libname>\w*?)",
    "def"           :   r"they don't want you to (?P<func_name>\w*?) (?P<args>[\w ]*?\n) (?P<body>.*?)🙏",
    "="             :   r"🔑 (?P<left>\w+?) (?P<right>\w+?)",
    "loops"         :   r"ride wit me(?P<body>.*?)another one$",
    "break"         :   r"you played yourself",
    "return"        :   r"major 🔑 (?P<return>.*?$)",
    "print"         :   r"🔥 (?P<print>.*?)$",
    "true"          :   r"(?P<true>👍)",
    "false"         :   r"(?P<false>👎)",
    "struct"        :   r"(?P<struct>\w*?) talk(?P<fields>.*)you smart",
    "fields"        :   r"(🔑 [\w_]*$)+",
}


program = 'fanluv Math'

def parse(program):
    ''' Read and tokenize 🔑++ source, return a Python AST
    '''
    return ast_from_tokens(tokenize(program))

def tokenize(string):
    return string.split()

def ast_from_tokens(tokens):
    pass













# import ast

# node = ast.Expression(ast.BinOp(
#                 ast.Str('xy'),
#                 ast.Mult(),
#                 ast.Num(3)))

# fixed = ast.fix_missing_locations(node)

# codeobj = compile(fixed, '<string>', 'eval')
# print eval(codeobj)