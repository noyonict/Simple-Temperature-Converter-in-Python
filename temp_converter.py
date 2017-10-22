def first_screen():
    print('1 - Celsius to Fahrenheit.')
    print('2 - Fahrenheit to Celsius.')
    print('3 - Exit')
    try:
        choice = int(input('Enter a choice: '))
        return choice
    except Exception as e:
        print(e)
        print('Please enter 1 or 2 or 3.')
        first_screen()

"""
Made by Md. Mohaymenul Islam (Noyon)
"""

def c_to_f(celsius):
    return int(celsius * 1.8 + 32)


def f_to_c(fahrenheit):
    return int((fahrenheit - 32) / 1.8)


def main():
    value = first_screen()
    while value:
        if value == 1:
            # Convert C To F
            c = eval(input('Enter degrees celsius: '))
            print('{}C = {}F'.format(c, c_to_f(c)))
        elif value == 2:
            # Convert F to C
            f = eval(input('Enter degrees fahrenheit: '))
            print('{}F = {}C'.format(f, f_to_c(f)))
            f_to_c(f)
        elif value == 3:
            print('Thank you! See you soon.')
            exit()
        else:
            print('Invalid input!\a')
        main()

if __name__ == '__main__':
        main()
