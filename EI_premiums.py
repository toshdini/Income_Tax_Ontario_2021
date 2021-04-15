class EI_Deductions:
    def __init__(self, val_1):
        self.__income = float(val_1)
        self.__Maximum_annual_insurable_earnings = 56300.00
        self.__n = 0.0158
        self.ei_premiums = self.__income * self.__n

    def ei_calculation(self):
        ei = 0
        if self.__income <= self.__Maximum_annual_insurable_earnings:
            ei = self.ei_premiums
        elif self.__income > self.__Maximum_annual_insurable_earnings:
            ei = self.__Maximum_annual_insurable_earnings * self.__n
        return ei
