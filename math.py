# -*- coding: UTF-8 -*-
"""
    @Author: Chaos.Zheng
    @Description: My mathmatics library
"""


def full_permutation(choices, scale):
    """
       This function implement the full permutaion with the specified choices and scale value.
       It is implemented as a generator.
       @choices: List. A character set that will be used to permutate.
       @scale: The number of elements.
       Example:
           for sequence in full_permutation('012345', 10):
              print sequence
           
    """

    char_cnt = len(choices)
    total = char_cnt ** scale

    # default element in every position is the last character in choices.
    seq = [choices[char_cnt - 1]] * scale
    for count in range(total):
        index = 0
        quot = count
        while quot != 0:
             quot = count / char_cnt
             remainder = count % char_cnt
             count = quot
             char = choices[remainder]
             seq[index] = char
             index += 1
        yield seq


if __name__ == "__main__":
    for sequence in full_permutation('012345', 4):
        print sequence

