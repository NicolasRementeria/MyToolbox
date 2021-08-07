def isDigitPresent(x, d):
    # Breal loop if d is present as digit
    if "6" in str(x):
        return 1
    else: 
        return 0

def checkDigit(n, d):
    count = 0
    for i in range(0, n+1):
        # checking for digit
        if (i == d or isDigitPresent(i, d)):
            count+=1
    return count

# Driver code
n = 1200
d = 6
print("The number of values are")
#printNumbers(n, d)
print(checkDigit(n, d))