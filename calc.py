def compute(string):
    """Psimple calculator all basic operators and both integers and decimals.
	example: '5+7 -> 12'
    """
    values = string.split('')
    num0 = float(values[0])
    num1 = float(values[1])
    operator = values[1]
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    else:
        msg = f'Unknown operator: "{operator}"\n'
	msg += 'Choose from "+" and "-".'
	raise ValueError(msg)
