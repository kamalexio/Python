#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculator():
    # This function performs arithmetic operations
    while True:
        print("\nEnter 'quit' to end the program")
        num1 = input("Enter a number (or a letter to quit): ")
        if num1 == 'quit':
            break
        num2 = input("Enter another number: ")
        operation = input("Enter an operation (+, -, *, /): ")

        try:
            num1 = float(num1)
            num2 = float(num2)
            if operation == '+':
                print("\nResult: ", num1 + num2)
            elif operation == '-':
                print("\nResult: ", num1 - num2)
            elif operation == '*':
                print("\nResult: ", num1 * num2)
            elif operation == '/':
                print("\nResult: ", num1 / num2)
            else:
                print("\nInvalid operator! Try again.")
        except ValueError:
            print("\nInvalid input! Try again.")


# In[ ]:


calculator()

