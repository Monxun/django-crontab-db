def StringChallenge(num):

    nums = list(range(1, num+1))
    for a, b in enumerate(nums):
        if (b % 3 == 0) and (b % 5 == 0):
            nums.pop(a)
            nums.insert(a, "FizzBuzz")
        elif (b % 3 == 0):
            nums.pop(a)
            nums.insert(a, "Fizz")
        elif (b % 5 == 0):
            nums.pop(a)
            nums.insert(a, "Buzz")
        else:
            continue

    s = " ".join([str(x) for x in nums])

    # nums = list(map(str, range(1, num)))
    # s = " ".join(nums)
    return nums


def StringChallenge(strParam):
    x = [char for char in strParam]
    x = [ord(char) - 96 if char.isalpha() else char for char in x]
    x = [str(char) for char in x]
    return ''.join(x)

    
# # keep this function call here 
# print(StringChallenge('af5c a#!'))

def ArrayChallenge(arr):
    x = set(arr)
    count = len(arr) - len(x)
    return count

# keep this function call here 
print(ArrayChallenge([0, -2, -2, 5, 5, 5]))