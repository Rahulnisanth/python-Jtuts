# NUMBER GUESSING GAME :
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guessNumber(n: int) -> int:
    left, right = 0, n
    while left < right:
        flag = (left & right) + ((left ^ right) >> 1)
        if guess(flag) == 0: # type: ignore
            return flag
        elif guess(flag) == 1: # type: ignore
            left = flag + 1
        else:
            right = flag - 1
    return left