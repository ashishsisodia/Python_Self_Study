
# coding: utf-8

# ##### Chapter 2 Variables, expressions and statements

# In[ ]:


#Exercise 2
name = input("Enter your name: ")
print ("Hello", name)


# In[ ]:


#Exercise 3
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hrs) * float(rate)
print (pay)


# In[ ]:


#Exercise 4
width = 17
height = 13.0
print(width//2)
print(width//2.0)
print(width/2)
print(width/2.0)
print(width%2.0)
print(width%2)
print(height//2)
print(height//2.0)
print(height/2)
print(height/2.0)
print(height%2)
print(height%2.0)


# In[ ]:


#celcius to fahrenheit
#Exercise 5
temp_c = input("Temp in Celsius: ")
temp_f = float(temp_c) * 1.8 + 32
print ("Temp in Fahrenheit is", temp_f)


# ##### Chapter 3 Conditional Execution

# In[ ]:


#Exercise 1, 2
try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if hrs <= 40:
        pay = hrs * rate
    else:
        pay = ((hrs -40) * rate * 1.5) + (40 * rate)
    print (pay)
except:
    print("Please enter numeric input")
    


# In[ ]:


#Exercise 3
try:
    score = float(input("Enter a score between 0.0 and 1.0: "))
    if score > 1.0 or score < 0.0:
        print("Bad Score")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print ("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except:
    print("Bad Score")


# ##### Chapter 4 Functions

# In[ ]:


#Exercise 6
def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    return pay
try:
    hrs = float(input("Enter Hours worked: "))
    rate = float(input("Enter Rate: "))
    pay = computepay(hrs, rate)
    print (pay)
except:
    print("Enter Numeric Values")


# In[ ]:


#Exercise 7
def computegrade(score):
    if score > 1.0 or score < 0.0:
        return("Bad Score")
    elif score >= 0.9:
        return("A")
    elif score >= 0.8:
        return ("B")
    elif score >= 0.7:
        return("C")
    elif score >= 0.6:
        return("D")
    else:
        return("F")
try:
    score = float(input("Enter a score between 0.0 and 1.0: "))
    grade = computegrade(score)
    print(grade)
except:
    print("Bad Score")


# ##### Chapter 5 Iterations

# In[ ]:


#Exercise 1
num = input("Enter a number: ")
total = 0.0
count = 0
avg = 0.0
while num != 'done':
    try:
        num1 = float(num)
    except:
        print("Invalid Input")
        num = input("Enter another number or Enter done if finished: ")
        continue
    total += num1
    count += 1
    num = input("Enter another number or Enter done if finished: ")
avg = total / count
print("Total is", total, "\nCount is", count, "\nAverage is", avg )
    


# In[ ]:


#Exercise 2
num = input("Enter a number: ")
maximum = 0.0
minimum = 0
while num != 'done':
    try:
        num1 = float(num)
    except:
        print("Invalid Input")
        num = input("Enter another number or Enter done if finished: ")
        continue
    if num1 > maximum:
        maximum = num1
    elif num1 < minimum:
        minimum = num1
    num = input("Enter another number or Enter done if finished: ")
print("Maximum is", maximum, "\nMinimum is", minimum)


# ##### Chapter 6 Strings

# In[ ]:


#Exercise 5
str = "X-DSPAM-Confidence:0.8475"
colpos = str.find(':')
num = float(str[colpos + 1:])
print ("The Number in the string is %g" % num)
print (colpos)


# ##### Chapter 7 Files

# In[ ]:


#Exercise 1
file = open("mbox-short.txt")
for line in file:
    print (line.upper())
#print(file)
file.close()


# In[ ]:


#Exercise 1
file = open("C:\\Users\\ashish.sisodia\\Desktop\\Python\\Files\\mbox-short.txt")
fileread = file.read()
print(fileread.upper())
#print(file)
file.close()


# In[ ]:


#Exercise 1
file = open(r"C:\Users\ashish.sisodia\Desktop\Python\Files\mbox-short.txt")
fileread = file.read()
print(fileread.upper())
#print(file)
file.close()


# In[ ]:


#Exercise 2
filename = input("Enter a Filename: ")
while 1:
    try:
        #print("Test")
        file = open(filename)
        break
    except:
        print ("Not a Valid File name/ File not found")
        filename = input("Enter a Filename: ")
        
'''Not Working
        else:
            print("Exiting Program")
            exit()
            
'''
count = 0
avg = 0.0
num = 0.0
for line in file:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence"):  
        colpos = line.find(':')
        #print (colpos)
        #print (line)
        num += float(line[colpos + 2:])
        count += 1
       # num = round(num,10)
avg = round((num / count),10)
print ("The Total of Confidence is %g, Count is %d, and Average Confidence is %g" % (num, count, avg))
file.close()       

