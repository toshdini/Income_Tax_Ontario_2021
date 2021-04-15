class Federal_tax:
    def __init__(self, val1):
        self.__value_1 = float(val1)
        self.__n = 0.00
        self.__bracket_1 = self.__value_1 - 49020.00
        self.__bracket_2 = self.__value_1 - 98040.00
        self.__bracket_3 = self.__value_1 - 151978.00
        self.__bracket_4 = self.__value_1 - 216511.00

    def find_federal_tax_bracket(self):
        fd = 0
        if 0.00 <= self.__value_1 <= 49020.00:
            self.__n = 0.25
            fd = self.__value_1 * self.__n
        elif 49020.00 < self.__bracket_1 <= 98040.00:
            self.__n = 0.205
            fd = self.__value_1 * self.__n
        elif 98040.00 < self.__bracket_2 <= 151978.00:
            self.__n = 0.26
            fd = self.__value_1 * self.__n
        elif 151978.00 < self.__bracket_3 <= 216511.00:
            self.__n = 0.29
            fd = self.__value_1 * self.__n
        elif 216511.00 < self.__bracket_4:
            self.__n = 0.33
            fd = self.__value_1 * self.__n
        return fd
