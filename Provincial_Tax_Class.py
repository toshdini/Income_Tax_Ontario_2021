class Provincial_Tax:
    def __init__(self, val_1):
        self.__income = float(val_1)
        self.__n = 0.00
        self.__bracket_1 = self.__income - 45142.00
        self.__bracket_2 = self.__income - 90287.00
        self.__bracket_3 = self.__income - 150000.00
        self.__bracket_4 = self.__income - 220000.00

    def find_provincial_tax_bracket(self):
        pt = 0
        if 0.00 <= self.__income <= 45142.00:
            self.__n = 0.0505
            pt = self.__income * self.__n
        elif 45142.00 < self.__bracket_1 <= 90287.00:
            self.__n = 0.0915
            pt = self.__income * self.__n
        elif 90287.00 < self.__bracket_2 <= 150000.00:
            self.__n = 0.1116
            pt = self.__income * self.__n
        elif 150000.00 < self.__bracket_3 <= 220000.00:
            self.__n = 0.1216
            pt = self.__income * self.__n
        elif 220000.00 < self.__bracket_4:
            self.__n = 0.1316
            pt = self.__income * self.__n
        return pt
