# text = input("enter text: ")
#
# text_leet = text.replace("d", "|)")
#
# print(text_leet)
#
# text_leet = text_leet.replace("a", "@")
#
# print(text_leet)
#
# text_leet = text_leet.replace("e", "3")
#
# print(text_leet)
#
# print(text.replace("d", "|)").replace("a", "@").replace("e", "3"))

# 5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

text1 = "abcsfgh"
text2 = "xyzhgfshhgsh"

text1a = text2[:2] + text1[2:]
text2a = text1[:2] + text2[2:]

print(text1a + " " + text2a)
