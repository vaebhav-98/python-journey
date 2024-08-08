# Python code
# To reverse words in a given string

str = "Hello World"
print(" ".join(str.split()[::-1]))

""" Time Complexity: O(n)
Auxiliary Space: O(n) """


#    using two pointer approach
def reverseWords(s):
    strng = s.split()
    start = 0
    end = len(strng) - 1
    while start < end:
        strng[start], strng[end] = strng[end], strng[start]
        start += 1
        end -= 1
    return " ".join(strng)

print(reverseWords(str))