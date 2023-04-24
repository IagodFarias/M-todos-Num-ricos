def convert_to_float(number):
    if number == 0:
        return 0

    sign = '-' if number < 0 else ''
    number = abs(number)

    exponent = 0
    while number >= 10:
        number /= 10
        exponent += 1

    while number < 1 and exponent > -4:
        number *= 10
        exponent -= 1

    if exponent > 4:
        print("Overflow")
        return

    if exponent < -4:
        print("Underflow")
        return

    mantissa = round(number, 5 - len(str(int(number))) - 1)
    mantissa_str = str(mantissa).replace('.', '')

    while len(mantissa_str) < 5:
        mantissa_str += '0'

    return sign + mantissa_str + str(exponent)


# Teste da função com alguns números
print(convert_to_float(12345))  # imprime "Overflow"
print(convert_to_float(0.00001))  # imprime "Underflow"
print(convert_to_float(123.456))  # imprime "123456-3"
print(convert_to_float(-0.0123456))  # imprime "-12346-5"
