

nums = list(map(int, input().split()))

summation = 0


def findAverage(nums: list[int]) -> float:
    global summation
    for i in range(len(nums)):
        summation += nums[i]

    return summation/len(nums)


print(findAverage(nums))


# The reason why the code knows what nums is but doesn't recognize summation
# without global is due to Python's variable scoping rules. Let's break this down:
# Global vs Local Variables:

# Global variables: Variables that are declared outside of any function and are accessible
# from anywhere in the code, including inside functions.
# Local variables: Variables that are declared inside a function and are only accessible
# within that function.

# 1. Why does the code recognize nums?

#   nums is a global variable because it's declared outside the findAverage() function.
#   In Python, if you access a global variable inside a function without trying to assign
#   a new value to it, Python will allow it because you're just reading it.
#   So, when you loop through nums inside the findAverage() function, you're only reading from
#   the global nums list, and Python knows to look for it in the global scope.

# 2. Why do you need to declare global summation?

#   When you try to modify a global variable inside a function,
# Python assumes by default that you're trying to create a local variable
# (if you don't explicitly declare it as global). So, when you use summation += nums[i],
# Python tries to update a local version of summation, which doesn't exist yet, causing an issue.
