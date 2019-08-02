TAX_RATE_2018_19 = .6
TAX_RATE_2019_20 = .75

# 2018-19 tax rate taken from
# https://ww.web.pk/2018/updated-fbr-income-tax-rates-2018-19-for-salaried-persons-in-pakistan/
def get_2018_19_tax(annual_salary):
    if annual_salary < 1.2e6: # case 1
        return 0
    if annual_salary <= 2.4e6: # case 2
        return 0.05 * annual_salary
    if annual_salary <= 4.8e6: # case 3
        return 0.1 * annual_salary
    return 0.15 * annual_salary # case 4

# 2019-20 tax rate taken from
# http://taxcalculator.pk
def get_2019_20_tax(annual_salary):
    if annual_salary <= 6e5: # case 1
        return 0
    if annual_salary <= 1.2e6: # case 2
        return 0.05 * (annual_salary - 6e5)
    if annual_salary <= 1.8e6: # case 3
        return 3e4 + 0.1 * (annual_salary - 1.2e6)
    if annual_salary <= 2.5e6: # case 4
        return 9e4 + 0.15 * (annual_salary - 1.8e6)
    if annual_salary <= 3.5e6: # case 5
        return 1.95e5 + 0.175 * (annual_salary - 2.5e6)
    if annual_salary <= 5e6: # case 6
        return 3.7e5 + 0.2 * (annual_salary - 3.5e6)
    if annual_salary <= 8e6: # case 7
        return 6.7e5 + 0.225 * (annual_salary - 5e6)
    if annual_salary <= 12e6: # case 8
        return 1.345e6 + 0.25 * (annual_salary - 8e6)
    if annual_salary <= 30e6: # case 9
        return 2.345e6 + 0.275 * (annual_salary - 12e6)
    if annual_salary <= 50e6: # case 10
        return 7.295e6 + 0.3 * (annual_salary - 30e6)
    if annual_salary <= 75e6: # case 11
        return 13.295e6 + 0.325 * (annual_salary - 50e6)
    return 21.42e6 + 0.35 * (annual_salary - 75e6) # case 12

def get_monthly_take_home(monthly_salary, fiscal_year):
    assert(fiscal_year in ["2018-19", "2019-20"])
    if fiscal_year == "2018-19":
        academic_tax_rate = 0.6
        get_annual_tax = get_2018_19_tax
    else: # fiscal_year == "2019-20":
        academic_tax_rate = 0.75
        get_annual_tax = get_2019_20_tax
    annual_tax = academic_tax_rate * get_annual_tax(monthly_salary * 12)
    return monthly_salary - (annual_tax / 12)
    
def main():
    monthly_salaries = [20000] + list(range(50000, 1000000, 50000))
    for salary in monthly_salaries:
        print(f'Take home salary for monthly salary of {salary}:')
        year = '2018-19'
        print(f'\t In {year}:', get_monthly_take_home(salary, year))
        year, increment = '2019-20', 0.05
        for increment in [0, 0.05, 0.06]:
            print(f'\t In {year} with increment of {increment}:',
                  get_monthly_take_home(salary * (1+increment), year))
        
if __name__ == '__main__':
    main()
