class Integer:
    def __init__(self, value):
        self.value = value
    def add(self, adder):
        self.value += adder
    def subtract(self, subtractor):
        if subtractor == self.value:
            self.value == 0
        elif subtractor < self.value:
            window = list(range(subtractor
            
            while window[-1] < self.value
        
    def multiply(self, multiplier):

    def divide(self, divisor):


def test_case(num1, num2, solution, test_func):

    output = test_func(num1, num2)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case(1, 3, 3, number_max)
test_case(4, 5, 5, number_max)
test_case(0, -1, 0, number_max)
test_case(1, 1, "same", number_max)

