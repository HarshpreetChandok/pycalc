def compute(string)
    values = string.split('')
    num0 = int(values[0])
    num1 = int(values[1])
    operator = values[1]
    if operator == '+'
        return num0 + num1
    else:
        raise ValueError('unknown operator!')
