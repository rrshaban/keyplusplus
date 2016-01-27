#DJKHALED
#WETHEBEST
#
# https://codeshare.io/sYZ1d
# 
# fibonacci_in_python_w_ast.py
#
# This is some 🔥 Fibonacci: an imperative implementation
# in Python and its ast representation.
#


#
# Python syntax
#

def fibonacci(n):
    acc1 = 0
    acc2 = 1

    while True:
        temp = acc2
        acc2 = acc2 + acc1
        acc1 = temp
        n = n - 1

    if n < 1:
        break

    return acc1


# 
# Python's ast representation of the above code. This is what 
# we're trying to generate by parsing the 🔑++. 
#

Module(
    body=[FunctionDef(name='fibonacci', args=arguments(
                                        args=[Name(id='n', ctx=Param())], 
                                        vararg=None, 
                                        kwarg=None, 
                                        defaults=[]), 
                    body=[
                        Assign(targets=[Name(id='acc1', ctx=Store())], value=Num(n=0)), 
                        Assign(targets=[Name(id='acc2', ctx=Store())], value=Num(n=1)), 
                        While(
                            test=Name(id='True', ctx=Load()), 
                            body=[
                                Assign(targets=[Name(id='temp', ctx=Store())], value=Name(id='acc2', ctx=Load())), 
                                Assign(targets=[Name(id='acc2', ctx=Store())], value=BinOp(left=Name(id='acc2', ctx=Load()), op=Add(), right=Name(id='acc1', ctx=Load()))), 
                                Assign(targets=[Name(id='acc1', ctx=Store())], value=Name(id='temp', ctx=Load())), 
                                Assign(targets=[Name(id='n', ctx=Store())], value=BinOp(left=Name(id='n', ctx=Load()), op=Sub(), right=Num(n=1)))
                                ], orelse=[]), 
                        If(test=Compare(left=Name(id='n', ctx=Load()), ops=[Lt()], comparators=[Num(n=1)]), 
                            body=[Break()], orelse=[]), 
                        Return(value=Name(id='acc1', ctx=Load()))], decorator_list=[])])
