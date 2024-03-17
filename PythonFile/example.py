""" def findMissingNumbers(n):
    numbers = set(n)
    output = []
    print(n[-1])
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    
listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 17]
print(findMissingNumbers(listOfNumbers)) """

word = "Artificial Intelligence"
text = word.split()
print(text)