# Problem 7 - Palindrome
words = ["wooo","racecar","madam","test"]
checkPalin = None

def palindrome(text):
    i1 = 0
    i2 = len(text)-1

    for t in text:
        if text[i1] != text[i2]:
            return False
        i1+=1
        i2-=1
    return True

def printResults(result, str):
    if result == True:
        print(" %s is a palindrome" % str)
    elif result == False:
        print(" %s is not palindrome" % str)

checkPalin = palindrome(words[0])
printResults(checkPalin, words[0])

checkPalin = palindrome(words[1])
printResults(checkPalin, words[1])

checkPalin = palindrome(words[2])
printResults(checkPalin, words[2])

checkPalin = palindrome(words[3])
printResults(checkPalin, words[3])