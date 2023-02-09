#!/usr/bin/env python
# coding: utf-8

# In[2]:


#2. Write a python program to convert temperatures to and from Celsius, Fahrenheit.
#[Formula: c/5 = f-32/9]
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")


# In[3]:


#3. Write a python program to find GCD of two numbers 
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = 1
while(i <= num1 and i <= num2):
  if(num1 % i == 0 and num2 % i == 0):
    gcd = i
  i = i + 1
print("GCD is", gcd)


# In[15]:


#4. Write a program that prints all Armstrong numbers between 1 to 1000. 
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)  


# In[17]:


#5. Write a python program that removes duplicated elements in a given list
# input - [23, 2, 67, 89, 5, 90, 67, 2, 67] 
duplicate = [23, 2, 67, 89, 5, 90, 67, 2, 67]
print(list(set(duplicate)))


# In[20]:


#6. Write a python program to check given number is disarium or not .
x=19
s=0
for i in x:
    for i, val in enumerate(str(x)):
        s=s+int(val)**(i+1)
        if s==x:
        print("Given number is a disarium number",x)
        else :
        print("Given number is not a disarium number",x)
            


# In[21]:


#6. Write a python program to check given number is disarium or not .
def digits(n):
    l=0
    while(n>0):
        n=n//10
        l=l+1
    return l
def Disarium(x,n):
    Sum=0
    while(n>0):
        r=n%10
        Sum=Sum+(r**x)
        x=x-1
        n=n//10
    return Sum
n=int(input())
x=digits(n)
m=Disarium(x,n)
if(m==n):
    print("Disarium")
else:
    print("Not Disarium")


# In[22]:


#7. Write a Python program to print all disarium numbers between 1 and 1000
#Output : numbers are 1 2 3 4 5 6 7 8 9 89 135 175 518 598 
def length_calculation(my_val):
   len_val = 0
   while(my_val != 0):
      len_val = len_val + 1
      my_val = my_val//10
   return len_val
def digit_sum(my_num):
   remaining = sum_val = 0
   len_fun = length_calculation(my_num)
   while(my_num > 0):
      remaining = my_num%10
      sum_val = sum_val + (remaining**len_fun)
      my_num = my_num//10
      len_fun = len_fun - 1
   return sum_val
ini_result = 0
print("The disarium numbers between 1 and 100 are : ")
for i in range(1, 101):
   ini_result = digit_sum(i)
   if(ini_result == i):
      print(i)


# In[ ]:


#8. Define list animal=["cow","elephant","tiger","horse"].Write a python program that prints
#list element and its length
#Output: cow 3
#elephant 8
#tiger 5
#horse 5
animal=["cow","elephant","tiger","horse"]
for i in animal:
    print(i,len(i))


# In[ ]:


#1. Read two integers X ,Y from STDIN and print three lines where:
#a) The first line print ,X to the power of Y (store the results into pow)
#b) The second line prints the floor division between pow and product of X and Y (store
#the results into div).
#c) The third line prints the exclusive or (^) between div and sum of X and Y
x=int(input("Enter the value of x :"))
y=int(input("Enter the value of y :"))
pow=x**y
div=pow//(x*y)
print(pow)
print(div)
print(div^(x+y))


# In[25]:


#12.WAPP that compute product of a list of numbers [45, 3, 2, 89, 72, 1, 10, 7]
import math
nums = [45, 3, 2, 89, 72, 1, 10, 7]
print("Original list numbers:")
print(nums)
nums_product = math.prod(nums)
print("\nProduct of the said numbers (without using for loop):",nums_product)




# In[26]:


#11. WAPP take a list of integers as an argument, and converts it into a single integer (return
#the integer).
#Input: [11, 33, 50]
def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return(res)
list = [11, 33, 50]
print(convert(list))


# In[28]:


#10. Write a program that generate a string AAHTX from given list
#name=["Arjun","Ramu","Ashok","Prateek","Lax"]
list=['Arjun','ramu','Ashock','prateek','lax']
print(list[0][0].lower(),end="")
print(list[0][4].upper(),end="")
print(list[1][0].lower(),end="")
print(list[1][8].upper(),end="")
print(list[2][0].lower(),end="")
print(list[2][2].upper(),end="")
print(list[3][0].lower(),end="")
print(list[3][1].upper(),end="")
print(list[4][0].lower(),end="")
print(list[4][5].upper(),end="")


# In[1]:


#8. Define list animal=["cow","elephant","tiger","horse"].Write a python program that prints
#list element and its length
#Output: cow 3
#elephant 8
#tiger 5
#horse 5
animal=["cow","elephant","tiger","horse"]
for i in animal :
    print(i,len(i))


# In[3]:


string="this python program"
print(string.replace("","-"))


# In[4]:



inp="orange,white,red,cyan,green,magenta,cyan,pink,white"
lt=inp.split(",")
print(list(set(lt)))


# In[5]:





# In[ ]:





# In[ ]:




