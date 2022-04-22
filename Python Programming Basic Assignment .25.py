#!/usr/bin/env python
# coding: utf-8

# Question1
# Create a function that takes three integer arguments (a, b, c) and returns the amount of
# integers which are of equal value.
# Examples
# equal(3, 4, 3) ➞ 2
# equal(1, 1, 1) ➞ 3
# equal(3, 4, 1) ➞ 0
# Notes
# Your function must return 0, 2 or 3.
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def equal(a,b,c):
    if a==b==c:
        print(f'{a,b,c} ➞ {3}')
    elif a==b or b==c:
        print(f'{a,b,c} ➞ {2}')
    else:
        print(f'{a,b,c} ➞ {0}')

equal(3, 4, 3)
equal(1, 1, 1)
equal(3, 4, 1)


# Question2
# Write a function that converts a dictionary into a list of keys-values tuples.
# Examples
# dict_to_list({
# &quot;D&quot;: 1,
# &quot;B&quot;: 2,
# &quot;C&quot;: 3
# }) ➞ [(&quot;B&quot;, 2), (&quot;C&quot;, 3), (&quot;D&quot;, 1)]
# dict_to_list({
# &quot;likes&quot;: 2,
# &quot;dislikes&quot;: 3,
# &quot;followers&quot;: 10
# }) ➞ [(&quot;dislikes&quot;, 3), (&quot;followers&quot;, 10), (&quot;likes&quot;, 2)]
# Notes
# Return the elements in the list in alphabetical order.
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


def dict_to_list(in_dict):
    out_list = []
    for keys,values in in_dict.items():
        out_list.append((keys,values))
    print(f'{in_dict} ➞ {out_list}')
                   
dict_to_list({"D": 1,"B": 2,"C": 3})
dict_to_list({"likes": 2,"dislikes": 3,"followers": 10})


# Question3
# Write a function that creates a dictionary with each (key, value) pair being the (lower case,
# upper case) versions of a letter, respectively.
# Examples
# mapping([&quot;p&quot;, &quot;s&quot;]) ➞ { &quot;p&quot;: &quot;P&quot;, &quot;s&quot;: &quot;S&quot; }
# 
# mapping([&quot;a&quot;, &quot;b&quot;, &quot;c&quot;]) ➞ { &quot;a&quot;: &quot;A&quot;, &quot;b&quot;: &quot;B&quot;, &quot;c&quot;: &quot;C&quot; }
# mapping([&quot;a&quot;, &quot;v&quot;, &quot;y&quot;, &quot;z&quot;]) ➞ { &quot;a&quot;: &quot;A&quot;, &quot;v&quot;: &quot;V&quot;, &quot;y&quot;: &quot;Y&quot;, &quot;z&quot;: &quot;Z&quot; }
# Notes
# All of the letters in the input list will always be lowercase.
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def mapping(in_list):
    out_dict = {}
    for ele in in_list:
        out_dict[ele] = ele.upper()
    print(f'{in_list} ➞ {out_dict}')
    
mapping(["p", "s"])
mapping(["a", "b", "c"])
mapping(["a", "v", "y", "z"])


# Question4
# Write a function, that replaces all vowels in a string with a specified vowel.
# Examples
# vow_replace(&quot;apples and bananas&quot;, &quot;u&quot;) ➞ &quot;upplus und bununus&quot;
# vow_replace(&quot;cheese casserole&quot;, &quot;o&quot;) ➞ &quot;chooso cossorolo&quot;
# vow_replace(&quot;stuffed jalapeno poppers&quot;, &quot;e&quot;) ➞ &quot;steffed jelepene peppers&quot;
# Notes
# All words will be lowercase. Y is not considered a vowel.
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def vow_replace(in_string,vow_char):
    vowels = ['a','e','i','o','u']
    out_string = ''
    for ele in in_string:
        if ele in vowels:
            out_string += vow_char
        else:
            out_string += ele
    print(f'{in_string} ➞ {out_string}')
        
vow_replace("apples and bananas", "u")
vow_replace("cheese casserole", "o")
vow_replace("stuffed jalapeno poppers", "e")


# Question5
# Create a function that takes a string as input and capitalizes a letter if its ASCII code is even
# and returns its lower case version if its ASCII code is odd.
# Examples
# ascii_capitalize(&quot;to be or not to be!&quot;) ➞ &quot;To Be oR NoT To Be!&quot;
# ascii_capitalize(&quot;THE LITTLE MERMAID&quot;) ➞ &quot;THe LiTTLe meRmaiD&quot;
# ascii_capitalize(&quot;Oh what a beautiful morning.&quot;) ➞ &quot;oH wHaT a BeauTiFuL
# moRNiNg.&quot;
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def ascii_capitalize(in_string):
    out_string = ''
    for ele in in_string.lower():
        if (ord(ele)%2 == 0):
            out_string += ele.upper()
        else:
            out_string += ele
    print(f'{in_string} ➞ {out_string}')
        
ascii_capitalize("to be or not to be!")
ascii_capitalize("THE LITTLE MERMAID")
ascii_capitalize("Oh what a beautiful morning.")

