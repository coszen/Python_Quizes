'''
Python Problem #7
* Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.
*  
* Consider the following dictionary
* { i, like, sam, sung, samsung, mobile, ice,
*  cream, icecream, man, go, mango}
*  
* Input:  ilike
* Output: Yes
* The string can be segmented as "i like".
*  
* Input:  ilikesamsung
* Output: Yes
* The string can be segmented as "i like samsung"
* or "i like sam sung".
'''
'''
Input :-
1]
***************************
Enter a string1
icecreamcreamice
_creamice
__ice
___
Yes
***************************
2]
***************************
Enter a string
___________________________
No
***************************
'''
import re

count = 0
input_list = []
input_list = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"]
input_list_2 = tuple(sorted(input_list, key = len, reverse = True))

print input_list_2 
print "Enter a string using above words combination and spaces"
input_string = raw_input()
input_string_2 = input_string

flag = False
out = False
strr = input_string_2.find("_")
#print input_list_2
if (re.sub("_ *","",input_string_2) == "" or re.sub(" _*","",input_string_2) == "" or input_string_2 == "" or re.sub(" *", "",input_string_2) == "" or re.sub("_*", "",input_string_2) == "" or strr != -1):
    out = True

while(count <= len(input_list_2)and out == False):
    for strings in input_list_2 :
        
        sample = input_string_2.find(strings)
        #print sample
        
        if sample != -1:
            result = input_string_2
            result = re.sub(strings, "_", result)
            
            print result            
            input_string_2 = result
            
            if (input_string_2 == "" or re.sub(" ", "",input_string_2) == "" or re.sub("_", "",input_string_2) == "" or re.sub("_ *","",input_string_2) == "" or re.sub(" _*","",input_string_2) == ""):
                flag = True
                break

        else:

            count = count + 1
            #print count

    if flag == True :
        break
    
if flag == True:
    print "Yes"
else:
    print "No"
