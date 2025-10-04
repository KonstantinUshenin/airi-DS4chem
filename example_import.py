

def my_fun2(num, power=2):
    num_square = num**2
    return num_square


class MyPowerAlgorithm:

    def __init__(self, power_of_mul=2):
        self.power_of_mul=power_of_mul

    def process(self, number):
        num_square = number**self.power_of_mul
        return num_square
    