"""
What is Loop.

* Loop to perform certain operation repeatedly for finite number of times until condition become false.
========================================================================================================
Types of loop.

* While loop
* For loop
* Nested loop

While loops
==========:- The while loop statement check for a condition at the beginning and till the condition is fulfiled,
             it will execute the body of the loop.

             syntax
             =======:- while condition :
                        statements

             Ex
             ===:- Display number from 1 to 10.
               x = 1
               while x <= 10:
                    print(x)
                    x+ = 1
               print("End")
==========================================================================================
For loops
========:- The for loop is useful to iterate over the element of a sequence.

           Syntax
           =======:-for var in sequence:
                        statements

           Ex:-1
           ===:- Display  number from 1 to 10.
               for i in range(1,11):
                   print(i)

           Ex:- 2
           ====:- Display  even no. from 1 to 10.
                 for i in range (1,11):
                     if i%2==0:
                     print(i)
 ============================================================================================
Nested loops
===========:- It is possible to write one loop to another loop.
             Ex:- 1
             ====:- row=5
             #outer loop
             for i in range(1,row+1):
             #inner loop
             for j in range(1,i+1):
                print("*",end" ")
            print(" ")

"""