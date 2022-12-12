
def create_complex_number(real_part, imaginary_part):
    return {"real": real_part, "imaginary": imaginary_part}
#def create_complex_number(real_part, imaginary_part):
    #return [real_part,imaginary_part]


def get_real_part(complex_number):
    if isinstance(complex_number, dict):
        return complex_number["real"]
    else:
        return complex_number[0]

def get_imaginary_part(complex_number):
    if isinstance(complex_number, dict):
        return complex_number["imaginary"]
    else:
        return complex_number[1]


def set_real_part(complex_number, real_part):
    if isinstance(complex_number, dict):
        complex_number["real"] = real_part
    else:
        complex_number[0]=real_part
    return complex_number


def set_imaginary_part(complex_number, imaginary_part):
    if isinstance(complex_number, dict):
        complex_number["imaginary"] = imaginary_part
    else:
        complex_number[1]=imaginary_part
    return imaginary_part


def is_digit(character):
    for digit in range(0, 10):
        if str(digit) == character:
            return True
    return False


def is_sign(character):
    return character == "+" or character == "-"


def create_integer_part(part_string, part_sign):
    part = int(part_string)
    if part_sign == "-":
        part = -part
    return part


def parse_number_string(number_string):
    real_part_string, real_sign, imaginary_part_string, imaginary_sign = get_number_parts(number_string)
    real_part = create_integer_part(real_part_string, real_sign)
    imaginary_part = create_integer_part(imaginary_part_string, imaginary_sign)
    number = create_complex_number(real_part, imaginary_part)
    return number


def get_number_parts(number_string):
    real_part_string = ""
    real_part_sign = ""
    imaginary_part_string = ""
    imaginary_part_sign = ""
    for i in range(len(number_string)):
        if is_digit(number_string[i]):
            if imaginary_part_sign == "":
                real_part_string += number_string[i]
            else:
                imaginary_part_string += number_string[i]
        elif is_sign(number_string[i]):
            if real_part_string == "":
                real_part_sign = number_string[i]
            else:
                imaginary_part_sign = number_string[i]
    return real_part_string, real_part_sign, imaginary_part_string, imaginary_part_sign





def is_real(complex_number):
    """
    This function tells if a complex number is real or not
    :param complex_number: a complex number
    :return: True if the number is real
             False otherwise
    """
    if get_imaginary_part(complex_number) == 0:
        return True
    else:
        return False

def create_list(complex_numbers):
    arr=[]
    for i in range(len(complex_numbers)):
        arr.insert(i, get_real_part(complex_numbers[i]))
    return arr



def get_longest_sequence(complex_numbers):
    sequence=SubarrayWithMaxSum(complex_numbers)
    return sequence

def get_longest_sequence_mountain(complex_numbers):
    best_sequence = []
    for i in range(len(complex_numbers)):
        for j in range(i, len(complex_numbers)):
            sequence = complex_numbers[i:j + 1]
            if isMountainArray(sequence):
                if len(sequence) > len(best_sequence):
                    best_sequence = sequence[:]
    return best_sequence

def isMountainArray(arr):

    if (len(arr) < 3):
        return False
    i = 0
    for i in range(1, len(arr)):
        if get_real_part(arr[i]) <= get_real_part(arr[i-1]):
            break

    if (i == len(arr) or i == 1):
        return False

    while i < len(arr):
        if get_real_part(arr[i]) >= get_real_part(arr[i-1]):
            break
        i += 1
    return i == len(arr)


def SubarrayWithMaxSum(nums):
    # Initialize currMax and globalMax
    # with first value of nums
    currMax = get_real_part(nums[0])
    globalMax = get_real_part(nums[0])
    # Initialize endIndex startIndex,globalStartIndex
    endIndex = 0
    startIndex = 0
    globalMaxStartIndex = 0

    # Iterate for all the elements of the array
    for i in range(1, len(nums)):

        # Update currMax and startIndex
        if get_real_part(nums[i]) > get_real_part(nums[i]) + currMax:
            currMax = get_real_part(nums[i])
            startIndex = i  # update the new startIndex

        # Update currMax
        elif get_real_part(nums[i]) < get_real_part(nums[i]) + currMax:
            currMax += get_real_part(nums[i])

        # Update globalMax and globalMaxStartIndex
        if (currMax > globalMax):
            globalMax = currMax
            endIndex = i
            globalMaxStartIndex = startIndex
    x=[]
    # Printing the elements of subarray with max sum
    for i in range(globalMaxStartIndex, endIndex + 1):
        x.append(nums[i])
    return x

