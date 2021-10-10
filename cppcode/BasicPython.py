from typing import List
from operator import mul
from functools import reduce
import random


def split(word: str) -> List[str]:  #   Problem 1
    """Return the  list of characters formed by breaking the string Name.

    doctests:
    >>> split("abc")
    ['a', 'b', 'c']
    >>> split("Guwahati")
    ['G', 'u', 'w', 'a', 'h', 'a', 't', 'i']
    """
    charList = list(word)
    return charList


def join(word_list: List[str]) -> str:  # Problem 2
    """Returns a string after joining the character in the string list word_list.

    doctests:
    >>> join (['a', 'b', 'c'])
    'abc'
    >>> join(['G', 'u', 'w', 'a', 'h', 'a', 't', 'i'])
    'Guwahati'
    """
    word = "".join(word_list)
    return word


def randomList(num: int) -> List[int]:  # Problem 3
    """Returns a list of n random numbers where n being the int num.

    doctests:
    >>> randomList(1)
    [1]
    >>> randomList(0)
    []
    """
    number_list = random.sample(range(1, num + 1), num)
    return number_list


def descendingOrder(numList: List[int]) -> List[int]:  # Problem 4
    """Returns a sorted list of descending order from the given list numList.

    doctests:
    >>> descendingOrder([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]

    >>> descendingOrder([3, 2, 1, 5, 4])
    [5, 4, 3, 2, 1]

    """
    new_NumList = sorted(numList, reverse=True)
    return new_NumList


def getFrequency(numList: List[int]) -> dict[int]:  # Problem 5
    """Returns the frequency of each number in the list numList.

    doctests:
    >>> getFrequency([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1: 2, 3: 3, 2: 4}
    >>> getFrequency([1, 4, 5, 2, 5, 3, 2, 4, 6])
    {1: 1, 4: 2, 5: 2, 2: 2, 3: 1, 6: 1}

    """
    frequencyDict = {}
    for i in range(len(numList)):
        key = numList[i]
        value = numList.count(key)
        frequencyDict.update({key: value})
    return frequencyDict


def getUnique(numList: List[int]) -> set():  # Problem 6
    """Returns the unique element from the given list numList.

    doctests:
    >>> getUnique([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1, 2, 3}
    >>> getUnique([1, 4, 4, 2, 3, 7, 2, 1, 6, 7, 9, 3, 9])
    {1, 2, 3, 4, 6, 7, 9}
    """
    uniqueSet = set()
    for i in numList:
        if i not in uniqueSet:
            uniqueSet.add(i)

    return uniqueSet


def getRepeatingElement(numList: List[int]) -> set():  # Problem 7
    """Returns the first repeating element from the given list numList.

    doctests:
    >>> getRepeatingElement([1, 2, 3, 4, 5, 1, 2])
    {1}
    >>> getRepeatingElement([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
    {5}
    """
    min = 10000000
    repeatingSet = set([0])
    for i in range(len(numList)):
        for j in range(i + 1, len(numList)):
            if numList[i] == numList[j]:
                if j - i < min:
                    repeatingSet.pop()
                    min = j - i
                    repeatingSet.add(numList[i])

    return repeatingSet


def getSqAndCube(num: int) -> dict():  # Problem 8
    """Returns a dictionary containing keys from 0 to n with the square and cube mapped.

    doctests:
    >>> getSqAndCube(3)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27]}
    >>> getSqAndCube(5)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64], 5: [25, 125]}
    """
    reqDict = {}
    for i in range(num + 1):
        key = i
        value = [i ** 2, i ** 3]
        reqDict.update({key: value})
    return reqDict


def createTuple(list1: list(), list2: list()) -> tuple():  # Problem 9
    """Returns tuples formed of each consecutive element of same index from two lists.
    >>> createTuple([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
    ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))
    >>> createTuple([7.1, 8.2, 4.0], ['Red', 'Blue', 'Green'])
    ((7.1, 'Red'), (8.2, 'Blue'), (4.0, 'Green'))
    """
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    reqTuple = zip(tuple1, tuple2)
    return tuple(reqTuple)


def generateSqLC(num: int) -> List[int]:  # Problem 10
    """Returns a list of squares from 0 to num using list comprehension.
    >>> generateSqLC(5)
    [0, 1, 4, 9, 16, 25]
    >>> generateSqLC(12)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
    """
    newList = [x ** 2 for x in range(num + 1)]
    return newList


def generateSqDC(num: int) -> List[int]:  # Problem 11
    """Returns a dictionary  mapping squares from 0 to n using dictionary comprehension.
    >>> generateSqDC(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> generateSqDC(12)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
    """
    newDict = {x: x ** 2 for x in range(num + 1)}
    return newDict


class MyClass:  # Problem 12
    """
    >>> a = MyClass([1, 2, 3, 4])
    >>> a.apply(lambda x: x*x)
    [1, 4, 9, 16]
    >>> a = MyClass([1, 2, 3, 4, 5])
    >>> a.apply(lambda x: x + 10)
    [11, 12, 13, 14, 15]
    """

    def __init__(self, variable):
        self.variable = variable

    def apply(self, func):
        try:
            return list(map(func, self.variable))
        except TypeError:
            raise Exception("Custom Error") from TypeError()


def uppercaseWords(wordList: List[str]) -> List[str]:  # Problem 13
    """Returns a list of words that has been uppercased from an existing list wordList using 'functools.map'.
    >>> uppercaseWords(['aa', 'bb', 'cd', 'e'])
    ['AA', 'BB', 'CD', 'E']
    >>> uppercaseWords(['this', 'is', 'an', 'apple', 'tree'])
    ['THIS', 'IS', 'AN', 'APPLE', 'TREE']
    """
    newList = map(getUpper, wordList)
    return list(newList)


def getUpper(word: str) -> str:
    return word.upper()


def productOfList(numList: List[int]) -> int:  # Problem 14
    """Returns the product of all the numbers in the list numList using 'functools.reduce'.
    >>> productOfList([1, 2, 3, 4, 5])
    120
    >>> productOfList([12, 5, 7, 9, 4])
    15120
    """
    result = reduce(mul, numList)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
