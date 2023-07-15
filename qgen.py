#!/usr/bin/env python3

"""question generator for korays homework style"""

# https://stackoverflow.com/a/28777781/15079222
import string
import sys
from collections import OrderedDict


def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)]).lower()
#


help_str = r"""# Here is a sample usage
>>> ./qgen.py 21
\question{1}
\subquestion{1}
\subquestion{2}
\question{2}
\subquestion{1}
>>> ./qgen.py 3.3.3
...
>>> ./qgen.py 12.12.3
...
>>> ./qgen.py -1a 522
...
>>> ./qgen.py -aa 522
..."""

if "--help" in sys.argv or "-h" in sys.argv:
    print(help_str)
    exit()

nums = sys.argv[-1]

questions_alpha = False
subquestions_alpha = False
questions_roman = False
subquestions_roman = False
if "-aa" in sys.argv:
    questions_alpha = True
    subquestions_alpha = True
elif "-1a" in sys.argv:
    questions_alpha = False
    subquestions_alpha = True


def prettier(i: int, is_question=False, is_subquestion=False):
    if is_question:
        if questions_alpha:
            assert i < len(string.ascii_lowercase)
            return string.ascii_lowercase[i - 1]
        if questions_roman:
            return write_roman(i)
        return i

    if is_subquestion:
        if subquestions_alpha:
            assert i < len(string.ascii_lowercase)
            return string.ascii_lowercase[i - 1]
        if subquestions_roman:
            return write_roman(i)
        return i
    return i


if '.' in nums:
    nums = nums.split('.')

nums = list(map(int, nums))

for question_no, subqestion_count in enumerate(nums, start=1):
    print(r"\question{" + str(prettier(question_no, is_question=True)) + "}")

    for subq_no in range(1, subqestion_count + 1):
        print(r"\subquestion{" + str(prettier(subq_no, is_subquestion=True)) + "}")
