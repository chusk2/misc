def main():

    def num_into_words(num_str):

        # Define the words for the ciphers

        units = {0: 'zero', 1: 'one', 2: 'two', 3: 'three',
                 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                 8: 'eight', 9: 'nine'}

        tens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                18: 'eighteen', 19: 'nineteen',
                20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
                60: 'sisty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

        num = int(num_str)

        units_w = ''  # word for the units
        tens_w = ''  # word for the tens
        hundreds_w = ''  # word for the hundreds

        units_f = ''  # cipher for the units
        tens_f = ''  # cipher for the tens
        hundreds_f = ''  # cipher for the hundreds

        # ONE-FIGURE NUMBER
        # example: 1,2,3...,9
        if len(num_str) == 1:
            units_f = num  # num is one-figure number
            units_w = units[units_f]
            word = units_w

        # TWO-FIGURE numbers
        elif len(num_str) == 2:

            # example: 10,11,12,...,20,30,...,90
            if num in tens.keys():

                tens_w = tens[num]
                word = tens_w

            # example: 21,22,45,67,...
            else:
                units_f = int(num_str[1])
                tens_f = int(num_str[0]) * 10
                units_w = units[units_f]
                tens_w = tens[tens_f]

                word = tens_w + '-' + units_w

        # three-figure numbers
        else:

            # example: 100, 200, 300 or 350,140,860
            if num_str[1] == '0':

                # example: 100, 200, 300
                if num_str[1:] == '00':
                    hundreds_f = int(num_str[0])

                    hundreds_w = units[hundreds_f]

                    word = hundreds_w + ' hundred'

                # example 101, 102, 103, 250
                else:
                    hundreds_f = int(num_str[0])
                    units_f = int(num_str[2])

                    hundreds_w = units[hundreds_f]
                    units_w = units[units_f]

                    word = hundreds_w + ' hundred and ' + units_w

            # example: 310, 420, 530, 670
            elif num_str[-1] == '0':
                hundreds_f = int(num_str[0])
                # redefine the tens to be multiple of 10
                tens_f = int(num_str[1]) * 10

                hundreds_w = units[hundreds_f]
                tens_w = tens[tens_f]

                word = hundreds_w + ' hundred and ' + tens_w

            # example: 346, 785, 284
            else:
                hundreds_f = int(num_str[0])
                tens_f = int(num_str[1]) * 10
                units_f = int(num_str[2])

                hundreds_w = units[hundreds_f]
                tens_w = tens[tens_f]
                units_w = units[units_f]

                word = hundreds_w + ' hundred and ' + tens_w + '-' + units_w

        return word
    # end of function num_into_word ###

    while True:
        num_str = input('\nGive me a number from 0 to 999: ')

        if num_str == '':
            break

        elif not num_str.isnumeric():  # check if it is a number

            # check if it is a float number
            # decimal numbers include only numbers and decimal point
            allowed_char = [str(i) for i in range(10)] + ['.', ',', "'"]
            for i in num_str:
                if i not in allowed_char:
                    print('\nInvalid number. Please, try again.')
                    break

                elif i in ['.', "'", ',']:
                    print('\nGiven number must be integer. Please, try again.')
                    break
            continue

        elif len(num_str) >= 4:
            print('\nInvalid number. Only 3 digit numbers. Please, try again.')
            continue

        else:
            print(num_into_words(num_str))


if __name__ == '__main__':
    main()
