# s="demoi looups"
# for index in range(len(s)):
#     if s[index]== 'i' :
#         print('we found the i at ',index)

###OR for above code###

# for char in s:
#     if char =='d' :
#         print('we found i at ',char[0])

##############
##Just normal Cheer Leaders code

# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))
#
# i = 0
# while i < len(word):
#    char = word[i]
#    if char in an_letters:
#        print("Give me an " + char + "! " + char)
#    else:
#        print("Give me a  " + char + "! " + char)
#    i += 1
# print("What does that spell?")
# for i in range(times):
#    print(word, "!!!")

#############
##To find cube root of given no.

# cube=8120601
# increment=0.01
# guess=0.0
# num_guesses=0
# epsilon=1
#
# while abs(guess**3- cube)>= epsilon and guess <=cube:
#     guess+=increment
#     num_guesses+=1
# print(guess)
# print(num_guesses)
