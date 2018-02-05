def c_to_f(celsius):
    return float(celsius) * 9 / 5 + 32


def f_to_c(fahrenheit):
    return (float(fahrenheit) - 32) * 5 / 9


if __name__ == '__main__':
    run = True
    while run:
        c_or_f = raw_input(
            'Celsius or Fahrenheit (please choose c, f, or q to quit): '
        )

        if c_or_f == 'c':
            temp = raw_input('Temp: ')
            try:
                print('{} Fahrenheit'.format(c_to_f(temp)))
            except ValueError:
                print('Please choose a valid number.')

        elif c_or_f == 'f':
            temp = raw_input('Temp: ')
            try:
                print('{} Celsius'.format(f_to_c(temp)))
            except ValueError:
                print('Please choose a valid number.')

        elif c_or_f == 'q':
            run = False

        else:
            print('That was not c, f, or q! That was {}!'.format(c_or_f))
