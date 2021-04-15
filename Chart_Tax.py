import matplotlib.pyplot as plt
import pandas as pd


class plot_pi_chart:
    def __init__(self, total_tax_input, net_pay_input):
        self.__total_tax_percentage = total_tax_input
        self.__net_pay_percentage = net_pay_input

    def pie_chart(self):
        labels = 'Net pay', 'Total Tax'
        sizes = [self.__net_pay_percentage, self.__total_tax_percentage]
        explode = (0, 0.1)  # only "explode" the 2nd slice
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()


class excel_creation:
    def __init__(self, income_input, fed_input, prov_input, cpp_input, ei_input):
        # This is the order that the main program should take the class args.
        self.__salary = income_input
        self.__Federal = fed_input
        self.__provincial = prov_input
        self.__cpp_deductions = cpp_input
        self.__EI_deductions = ei_input
        # self.__total_deductions = total_tax_input
        # self.__Net_pay = net_pay_input

    def writing_on(self):
        d = {  # Stores the calculated variables in a dict object.
            'Names': ('Salary', 'Federal tax deduction', 'Provincial tax deduction', 'CPP deductions', 'EI deductions'),
            'values': (self.__salary, self.__Federal, self.__provincial, self.__cpp_deductions, self.__EI_deductions)
        }
        df = pd.DataFrame(d)
        return df.to_excel('./Income_Tax_Chart.xlsx', sheet_name="Sheet1", index_label="label", merge_cells=False)
