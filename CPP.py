class CPP_deductions:
    def __init__(self, value_1):
        self.__income = float(value_1)
        self.__maximum_pensionable_earnings = 61600.00
        self.__n = 0.0545
        self.__cpp_cuts = self.__income * self.__n

    def cpp_deduct(self):
        cpp = 0
        if self.__income <= self.__maximum_pensionable_earnings:
            cpp = self.__cpp_cuts
        elif self.__income > self.__maximum_pensionable_earnings:
            cpp = self.__maximum_pensionable_earnings * self.__n
        return cpp
