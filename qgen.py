#!/usr/bin/env python3

"""question generator for korays homework style"""

import sys

help_str = r""">>> qgen.py 21
\question{1}
\subquestion{1}
\subquestion{2}
\question{2}
\subquestion{1}

>>> qgen.py 3.3.3

>>> qgen.py 12.12.3
"""

if "--help" in sys.argv or "-h" in sys.argv:
    print(help_str)
    exit()

nums = sys.argv[-1]

if '.' in nums:
    nums = nums.split('.')

nums = list(map(int, nums))

for question_no, subqestion_count in enumerate(nums, start=1):
    print(r"\question{" + str(question_no) + "}")

    for subq_no in range(1, subqestion_count + 1):
        print(r"\subquestion{" + str(subq_no) + "}")
