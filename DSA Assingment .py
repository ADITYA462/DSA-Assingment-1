#!/usr/bin/env python
# coding: utf-8

# 1.Write a program to find all pairs of an integer array whose sum is equal to a given number?

# In[1]:


def pairs(array,target):
    pairs=[]
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] + array[j] == target:
                pairs.append((array[i], array[j]))
    return pairs
        
array = [0,2,4,6,8,10,11]
target = 8
result = pairs(array,target)
print(result)


# 2.Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

# In[2]:


def reverse(array):
    i = 0
    j = len(array) - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

array = [2, 5, 7, 10, 4]
reverse(array)
print(array)


# 3.Write a program to check if two strings are a rotation of each other?

# In[3]:


def rotate(x, y):
    if len(x) != len(y):
        return False
    z = x + x
    if y in z:
        return True
    else:
        return False

# Example usage
x = "alone king"
y = "gnik enola"
result = rotate(x, y)
print(result)


# 4.Write a program to print the first non-repeated character from a string?

# In[4]:


def char(str):
    counts = {}
    for c in str:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    for c in str:
        if counts[c] == 1:
            return c
    return None

str = "Adhi"
result = char(str)
print(result)


# 5.Read about the Tower of Hanoi algorithm. Write a program to implement it

# In[10]:


def Tower_Hanoi(n, source, destination, aux):
    if n == 0:
        return
    Tower_Hanoi(n-1, source, aux, destination)
    print("Move disk", n, "source", source, "destination", destination)
    Tower_Hanoi(n-1, aux, destination, source)
  

N = 3

Tower_Hanoi(N, 'i', 'k', 'B')


# 6.Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# In[12]:


def operator(x):
    if x == "+":
        return True
    if x == "-":
        return True
    if x == "*":
        return True
    if x == "/":
        return True

def postfixtoprefix(postfix_exp):
    stack = []
    length = len(postfix_exp)
    for i in range(length):
        if (operator(postfix_exp[i])):
            operand_1 = stack[-1]
            stack.pop()
            operand_2 = stack[-1]
            stack.pop()
            temp = postfix_exp[i] + operand_2 + operand_1
            stack.append(temp)
        else:
            stack.append(postfix_exp[i])
            
    ans = " "
    for i in stack:
        ans = ans + i
    return ans

postfix_exp = "xy+wz+*"
print("PostFix Expression is:",postfix_exp)
print("PreFix Expression is:",postfixtoprefix(postfix_exp))


# 7.Write a program to convert prefix expression to infix expression.

# In[13]:


def prefixToInfix(prefix):
    if len(prefix) == 0:
        return ""
    elif prefix[0].isnumeric():
        return prefix[0]
    else:
        operator = prefix[0]
        left_operand = prefixToInfix(prefix[1:])
        right_operand = prefixToInfix(prefix[len(left_operand)+1:])
        return "(" + left_operand + operator + right_operand + ")"

prefix = input("Enter a prefix expression: ")
infix = prefixToInfix(prefix)
print("The infix expression is:", infix)


# 8.Write a program to check if all the brackets are closed in a given code snippet

# In[14]:


def is_balanced(code):
    stack = []
    for char in code:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            open_char = stack.pop()
            if (open_char == '(' and char != ')') or                (open_char == '[' and char != ']') or                (open_char == '{' and char != '}'):
                return False
    return not stack


code1 = "def func(x): return x * (x + 1)"  
code2 = "for i in range(10): print(i"      

print(is_balanced(code1)) 
print(is_balanced(code2))


# 9.Write a program to reverse a stack.

# In[15]:


def reverse(stack):
    if not stack:
        return
    top = stack.pop()
    reverse(stack)
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)


stack = [2, 4, 6, 8, 10]
reverse(stack)
print(stack)


# 10.Write a program to find the smallest number using a stack.

# In[16]:


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.stack:
            return None
        item = self.stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        return item

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


stack = MinStack()
stack.push(1)
stack.push(3)
stack.push(5)
stack.push(7)
stack.push(2)
print(stack.get_min()) 
stack.pop()
stack.pop()
print(stack.get_min())


# In[ ]:




