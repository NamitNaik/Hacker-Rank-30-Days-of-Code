class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def __init__(self):
        total = 0
        self.total = 0

    def divisorSum(self, n):
        for i in range(n):
            if n % (i+1) == 0:
                self.total = self.total + (i+1)
        return self.total


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
