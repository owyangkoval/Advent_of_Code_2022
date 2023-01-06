# AoC = Counting Calories - for the Top Three Elves

def main():
    file = open('Pset1_AoC_input.txt', 'r')
    read = file.readlines()
    read.append('\n')  # appended onto the end of the file to include the last set of calories

    calories = Calories() # calorie object

    elf_calorie_list = []
    for calorie_line in read:
        if calorie_line != '\n':
            elf_calorie_list.append(int(calorie_line.strip()))

        else:
            elf = Elf(elf_calorie_list)  # elf object
            elf.get_calorie_sum()  # get calorie sum
            calories.add_elf(elf)  # add elf to list
            elf_calorie_list = []  # start over with empty list

    total_calories = (calories.get_max_calories()) + (calories.get_second_max_calories()) + (calories.get_third_max_calories())

    print(f"The elf with the maximum calories has {calories.get_max_calories()} calories.")
    print(f"The elf with the second maximum calories has {calories.get_second_max_calories()} calories.")
    print(f"The elf with the third maximum calories has {calories.get_third_max_calories()} calories.")
    print(f"The total number of calories between the top three elves is {total_calories} calories.")


class Elf:
    """creating elf object"""
    def __init__(self, calories):
        self._calories = calories  # calories is a list of ints per elf object

    def get_calories(self):
        return self._calories

    def get_calorie_sum(self):
        calorie_sum = 0
        for val in self._calories:
            calorie_sum += val
        return calorie_sum


class Calories:
    """calorie class"""
    def __init__(self):
        self._elf_list = []

    def add_elf(self, elf_object):
        if elf_object not in self._elf_list:
            self._elf_list.append(elf_object)

    def get_max_calories(self):
        max_calories = 0
        for elf_object in self._elf_list:
            if elf_object.get_calorie_sum() > max_calories:
                max_calories = elf_object.get_calorie_sum()
        return max_calories

    def get_second_max_calories(self):
        second_max_calories = 0
        for elf_object in self._elf_list:
            if elf_object.get_calorie_sum() > second_max_calories and elf_object.get_calorie_sum() \
            < self.get_max_calories():
                second_max_calories = elf_object.get_calorie_sum()
        return second_max_calories

    def get_third_max_calories(self):
        third_max_calories = 0
        for elf_object in self._elf_list:
            if elf_object.get_calorie_sum() > third_max_calories and elf_object.get_calorie_sum() < \
            self.get_max_calories() and elf_object.get_calorie_sum() < self.get_second_max_calories():
                third_max_calories = elf_object.get_calorie_sum()
        return third_max_calories

if __name__ == '__main__':
    main()