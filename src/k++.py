#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8
#
# https://codeshare.io/ppLOE
#
#

from __future__ import print_function

import sys
import ast
import re

# These are the regular expressions that define the language. As of now,
# they include multi-line regexes, which might require hacking newlines.
k = {
    "boilerplate"   :   r"^#DJKHALED\n#WETHEBEST",
    "import"        :   r"fanluv (?P<libname>\w+?)\b",
    "def"           :   r"they don't want you to (?P<func_name>\w*?) (?P<args>[\w ]*)\n (?P<body>.*?)🙏",
    # "func_open"     :   r"they don't want you to (?P<func_name>\w*) (?P<args>[\w ]*)",
    # "func_end"      :   r"🙏",
    "="             :   r"🔑 (?P<left>\w*) (?P<right>.*)",
    "loops"         :   r"ride wit me(?P<loop>.*?)another one",
    "break"         :   r"you played yourself",
    "return"        :   r"major 🔑 (?P<return>\w*?)",
    "print"         :   r"🔥 (?P<print>.+)",
    "true"          :   r"(?P<true>👍)",
    "false"         :   r"(?P<false>👎)",
    "struct"        :   r"(?P<struct>\w*?) talk(?P<fields>.*)you smart",
    "fields"        :   r"(🔑 [\w_]*$)+",
}
combined = "(" + ")|(".join(k.values()) + ")"

f = open('/Users/razi/git/🔑++/inspiration.liooooon', 'r')
program = f.read()

def line_to_ast(line):

    l = line.strip()

    # fanluv
    if re.search(k["import"], l):
        libname = re.match(k["import"], l).group('libname')
        return ast.Import(
            names=[ast.alias(name=libname, asname=None)])

    # major 🔑 x
    if re.search(k["return"], l):
        var = re.search(k["return"], l).group('return')
        return ast.Return(
            value=ast.parse(var, mode='eval').body, decorator_list=[])

    # you played yourself
    if re.search(k["break"], l):
        return ast.Break()

    # 🔑 x y 
    if re.search(k["="], l):
        left, right = re.search(k["="], l).groups()

        left_eval  = ast.parse(left, mode='eval').body
        right_eval = ast.parse(right, mode='eval').body

        return ast.Assign(targets=[left_eval], value=right_eval)

    # print
    if re.search(k["print"], l):
        val = re.search(k["print"], l).group('print')
        val_eval = ast.parse(val, mode='eval').body
        return ast.Print(dest=None, values=[val_eval], nl=True)



    print("Could not match {}".format(l))
    # return False


    # if not re.search(k["boilerplate"], ''.join(lines[:2])):
    #     raise SyntaxError("You played yourself")


def parse(program):
    ''' Read and tokenize 🔑++ source, return a Python AST '''

    lines = program.strip().splitlines(True)

    context = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # comments
        if line[0] == "#":
            i += 1
            continue

        # functions
        if re.search(k["func_open"], line):
            func_name, args = re.search(k["func_open"], line).groups()
            
            start_index = i
            while not re.search(k["func_end"], lines[i]):
                print(lines[i])
                i += 1
                if i == len(lines) :
                    raise SyntaxError("You played yourself. 🙏")
            
            # parse the body of the function
            print(start_index, i)

            # TODO
            # Some weird funky shit is happening with this recursive step
            body_parsed = parse(''.join(lines[start_index:i]))
            args_parsed = map(lambda x: ast.parse(x), args.split())

            context.append(ast.FunctionDef(name=func_name, 
                args=arguments(args=args_parsed, vararg=None, kwarg=None, defaults=[],
                decorator_list=[],
                body=body_parsed)))


        i += 1

    body = ast.Module(body=context)
    ast.fix_missing_locations(body)
    return body


def substitute(p):
    #   Substitute Python for 🔑++

    subs = [
        (k["true"],     r"True"),
        (k["false"],    r"False"),
        (k["import"],   r"import \g<libname>"),
        (k["return"],   r"return \g<return>"),
        (k["="],        r"\g<left> = \g<right>"),
        (k["print"],    r"print(\g<print>)"),
        (k["break"],    r"break"),
    ]

    for pattern, replacement in subs:
        p = re.sub(pattern, replacement, p)

    p = re.sub(k["loops"],  r"while True:\n \g<loop>", p, 
            flags=re.DOTALL)
    p = re.sub(k["def"],    r"def \g<func_name>(\g<args>):\n \g<body>", p, 
            flags=re.DOTALL)
    
    return p

def parse_v2(program):

    # check for boilerplate
    if not re.match(k["boilerplate"], program):
        raise SyntaxError("You played yourself. #DJKHALED #WETHEBEST")

    return ast.parse(substitute(program))


exec(compile(parse_v2(program), filename="<ast>", mode="exec")) 

try:
    pass
except:
    print("Your code could not compile. You played yourself.")

# import ast

# node = ast.Expression(ast.BinOp(
#                 ast.Str('xy'),
#                 ast.Mult(),
#                 ast.Num(3)))

# fixed = ast.fix_missing_locations(node)

# codeobj = compile(fixed, '<string>', 'eval')
# print eval(codeobj)