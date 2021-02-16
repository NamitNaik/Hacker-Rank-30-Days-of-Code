import sys


class Solution:

    def __init__(self):
        stack = list()
        queue = list()
        m = 0
        n = 0
        self.stack = stack
        self.queue = queue
        self.m = m
        self.n = n

    def pushCharacter(self, ch):
        self.stack.insert(0, ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack[self.m]
        self.m = self.m + 1

    def dequeueCharacter(self):
        return self.queue[self.n]
        self.n = self.n + 1


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
