#Hope Crisafi
#Lab wk 5
#4/27/21
#Charles Klein

#NJW 10/10

#Joke (copy and paste link): https://www.youtube.com/watch?v=dQw4w9WgXcQ

#NJW I CANNOT BELIEVE I DID THAT. Ok Crisafi. It's on.

#Hope is 72 111 112 101

#Part 2

word = input('Enter a word:')
end = len(word)-1

print('the first letter is:',word[0])
print('the last letter is:',word[end])


# #Part 3

word = input('enter a word:')
end = len(word)-1
index = end

while index >= 0:
    print('letter is:',word[index])
    index -= 1

# #Part 4


name = input('enter a name:')
end = len(name)-1
index = 0

while index <= end:
    print(name[index],'is:',ord(name[index]))
    index += 1

#Part 5

# lowerCase = input('enter a word in all lowercase:')
# upperCase = lowerCase.upper()
# end = len(lowerCase)-1
# index = 0

# while index <= end:
#     print(ord(upperCase[index]))
#     index += 1

##but this is probably the way you wanted me to do it:

lower = input('enter a word in all lowercase:')
length = len(lower)
index = 0

while index <= length and index +1 <= length:
    num = ord(lower[index +0])
    upper = num - 32
    index +=1
    print(chr(upper))


#Part 6


word = input('enter a word: ')
wordLength = len(word)
index = 0
vowels = 0


#NJW Why use ord here? Instead of comparing to letters?

a = ord('a')
e = ord('e')
i = ord('i')
o = ord('o')
u = ord('u')

while index < wordLength:
    num = ord(word[index])
    index += 1

    if num == a or num == e or num == i or num == o or num == u:
        vowels += 1
     
print('vowels:',vowels)


# Part 7

wordInput = input('enter a word: ')
letterInput = input('enter a letter: ')
index = 0
length = len(wordInput)
letterAmt = wordInput[index]

#NJW good.

while letterAmt != letterInput and index +1 <= length:
    index += 1
    letterAmt = wordInput[index -1]

if letterAmt == letterInput:
    print('found at index',index)

else:
    print('not found')

    # if letterInput != letterAmt:
    #     print('not found')
