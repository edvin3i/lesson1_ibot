def get_vat(price, vat_rate):
    vat = price / 100 * vat_rate
    price_no_vat = price - vat
    print(price_no_vat)

def get_summ(one, two, delimiter='&'):
    str1 = str(one) + str(delimiter) + str(two)
    return str1.upper()


sum_string = get_summ('Learn', 'Python')
print(sum_string)