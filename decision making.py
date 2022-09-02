"""
Decision making
================:- Dicision making is  anticipation of condition while execution of program and specific action
                   were taken according to the condition.
Types
======:-
if   --> python,if statement is used for decision making operations

       Syntax:- if exepression:
       =======     statement

       Ex
       ===:- num = 1
             if num == 1:
                print("one")
=============================================================================================================

elif --> use the elif condition is used include multiple conditional expressions after
        the if condition or b/w if and else conditions.
        Ex
        ===:-num = -5
             if num==0:
                print(num,"is zero")
             elif num>0:
                print(num," is positive")
             else:
                print(num," is negative")

else --> An if else Python statement evaluates whether an expression is true or false.
          If a condition is true, the “if” statement executes. Otherwise,
          the “else” statement executes.

          Ex
          ===:- x= int(input("enter the number:"))
                if x%2==0:
                   print(x," even number")
                else:
                   print(x,"odd number")
=========================================================================================================
Nested if --> There may be a situation when you want to check for another condition after a
          condition resolves to true.
          Ex
          ===:- num = 15
                if num >= 0:
                    if num == 0:
                       print("Zero")
                    else:
                print("Positive number")
                     else:
                print("Negative number")
===========================================================================================================
"""