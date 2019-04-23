import argparse
from pprint import pprint
import pdb

result = 1

def recursive_function(value):
    
    pdb.set_trace()
    if value == 1:
        return value
    else:
        return value * recursive_function(value - 1)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int, help="enter number to cal factorial")

    data = parser.parse_args()

    value = recursive_function(data.number)

    print("\nFactorial of {} is {} \n".format(data.number, value))
