# Q1

def my_funk(x1, x2, x3):
    arr = [x1, x2, x3]
    for x in arr:
        if type(x) is str:
            return 'None'
        elif type(x) is bool:
            return 'None'

        elif type(x) is int:
            return "Error: parameters should be float"

    sumX = x1 + x2 + x3
    if sumX == 0:
        return "Not a number – denominator equals zero"
    else:
        return (sumX * (x2 + x3) * x3) / sumX

# print(my_funk(1.0, 2.0, 3.0))
