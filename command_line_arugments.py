"""
This program implements calculator function using command line args.
@author: Tushar Nitave
"""

import argparse

if __name__ == '__main__':

    operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']

    parser = argparse.ArgumentParser()


    #optional arguments
    parser.add_argument('-a', action='store_true', help = 'perform addition')
    parser.add_argument('-s', action='store_true', help = 'perform subtraction')
    parser.add_argument('-m', action='store_true', help = 'perform multiplication')
    parser.add_argument('-d', action='store_true', help = 'perform division')
    
    #positional arguments
    parser.add_argument('first_number', type=float, help="enter first number")
    parser.add_argument('second_number', type=float, help="enter second number")

    data = parser.parse_args()

    #perform addition 
    if data.a:
        print("\nOperation performed: {}".format(operations[0]))
        print("\nResult: {}\n".format(data.first_number + data.second_number))

    #perfom subtraction
    elif data.s:
        print("\nOperation performed: {}".format(operations[1]))
        print("\nResult: {}\n".format(data.first_number - data.second_number))

    #perform multiplication
    elif data.m:
        print("\nOperation performed: {}".format(operations[2]))
        print("\nResult: {}\n".format(data.first_number * data.second_number))

    #perform division
    elif data.d:
        print("\nOperation performed: {}".format(operations[3]))
        print("\nResult: {}\n".format(data.first_number / data.second_number))
