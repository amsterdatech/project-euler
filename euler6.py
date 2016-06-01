from functools import partial

def power(b,e):
    return b ** e

square = partial(power, e=2)

def ssd(numbers):
    square_sum = square(reduce(lambda x,y: x+y, numbers))
    sum_squares = reduce(lambda x,y:x+y, map(square, numbers))

    return square_sum - sum_squares
    


