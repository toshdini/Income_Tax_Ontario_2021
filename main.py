import Federal_tax_Class
import Provincial_Tax_Class
import CPP
import EI_premiums
import Chart_Tax


def main():
    user_input = float(input('Enter your 2021 annual income: '))

    fed_deductions = Federal_tax_Class.Federal_tax(user_input)
    fed_deductions.find_federal_tax_bracket()

    provincial_deductions = Provincial_Tax_Class.Provincial_Tax(user_input)
    provincial_deductions.find_provincial_tax_bracket()

    cpp_deductions = CPP.CPP_deductions(user_input)
    cpp_deductions.cpp_deduct()

    ei_deductions = EI_premiums.EI_Deductions(user_input)
    ei_deductions.ei_calculation()

    total_tax_input = float(fed_deductions.find_federal_tax_bracket()) + float(provincial_deductions.find_provincial_tax_bracket()) + float(cpp_deductions.cpp_deduct()) + float(ei_deductions.ei_calculation())
    net_pay_input = user_input - total_tax_input

    print('The Total tax for 2021 is: ', format(total_tax_input, '.2f'))
    print('Net pay equals: ', format(net_pay_input, '.2f'))

    chart_creation = Chart_Tax.excel_creation(user_input, fed_deductions.find_federal_tax_bracket(),
                                              provincial_deductions.find_provincial_tax_bracket(),
                                              cpp_deductions.cpp_deduct(), ei_deductions.ei_calculation())
    chart_creation.writing_on()

    plot_creation = Chart_Tax.plot_pi_chart(total_tax_input, net_pay_input)
    plot_creation.pie_chart()

    return chart_creation, plot_creation


if __name__ == '__main__':
    main()
