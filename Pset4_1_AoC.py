# Camp Cleanup

def main():
    file = open('Pset4_AoC_input.txt', 'r')
    read = file.readlines()

    counter = 0
    for string in read:
        section_id = SectionIDs()
        check = section_id.check_overlap(string)
        if check == True:
            counter += 1
    print(f"Sum of Subset Pairs = {counter}")


class SectionIDs:

    def __init__(self):
        self._sect_1 = []
        self._sect_2 = []

    def check_overlap(self, string):
        # Split string
        split_string = string.split(",")
        section_1 = split_string[0]
        section_2 = split_string[1]

        # SECTION ONE
        # Split section_1 string
        section_1_split = section_1.split("-")
        str_first_num = section_1_split[0]
        str_second_num = section_1_split[1]

        # Convert to int
        first_num = int(str_first_num)
        second_num = int(str_second_num)

        # Append Section 1 list
        number_range = range(first_num, second_num+1, 1)
        for num in number_range:
            self._sect_1.append(num)

        # SECTION TWO
        # Split section_1 string
        section_2_split = section_2.split("-")
        str_first_num = section_2_split[0]
        str_second_num = section_2_split[1]

        # Convert to int
        first_num = int(str_first_num)
        second_num = int(str_second_num)

        # Append Section 1 list
        number_range = range(first_num, second_num + 1, 1)
        for num in number_range:
            self._sect_2.append(num)

        # OVERLAP CHECK
        counter = 0
        if set(self._sect_1).issubset(self._sect_2) or set(self._sect_2).issubset(self._sect_1) or \
                set(self._sect_2) == set(self._sect_1):
            return True


if __name__ == '__main__':
    main()