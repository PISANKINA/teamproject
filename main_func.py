class ToRomanNumber:
    def __init__(self, rom_number):
        self.rom_number = rom_number
        self.int_number = None

    def validation(self):
        ROM_NUMBERS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        valid = 0
        for i in self.rom_number:
            if i in ROM_NUMBERS:
                valid += 1

        if valid == len(self.rom_number):
            return True
        else:
            return False

    def converting(self):
        if self.validation() == True:
            return self.rom_in_int()
        else:
            return 'Not roman number. Try one more time'

    def rom_in_int(self):

        fin_num = 0
        prev_num = 0
        rom_numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        for i in self.rom_number:
            num = rom_numbers[i]

            if num < prev_num:
                fin_num += prev_num
                prev_num = num

            elif num > prev_num:

                if prev_num == 0:
                    prev_num = num
                else:
                    fin_num += num - prev_num
                    prev_num = 0

            elif num == prev_num:
                fin_num += prev_num + num
                prev_num = 0

        fin_num = fin_num + prev_num
        self.int_number = str(fin_num)
        return self.int_number


    def __add__(self, other):
        if type(other) == ToRomanNumber:
            return ToRomanNumber(self.rom_number + other.rom_number)


    def __repr__(self):
        return self.converting()


    def __str__(self):
        return self.__repr__()


print(ToRomanNumber('XVII'))

