'''
Subject :- Paranthesis check

Author :- Kasturi Hanjagi

Status :- Completed

Date Modified :- 05/07/18

'''

'''﻿
Python Problem #1
* Given a string expression s, write a program to test whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in s.
*    
* Sample Input:
* s = “[()]{}{[()(){}[]]()}”
* Output:
* True
*   
* Sample Input:
* s = “[(])”
* Output:
* False
*  
*  
* Assume that the user input string is not allowed to contain any charater other than the following:
* []{}()
'''

'''
Output_1 :
Enter an expression containing '[', '{', '(', ')', '}', ']'
[()]{}{[()(){}[]]()}
True
'''

'''
Output_2 :
Enter an expression containing '[', '{', '(', ')', '}', ']'
[(])
False
'''

'''
Use to check if the parenthesis are valid or not 
'''

def DetectPairs(inputs_2):

    para_check = Check(list(inputs_2))
        
    if para_check == True and FlowCheck(list(inputs_2)) == True:

        print True
                
    else:

        print False


'''
Function used in DetectPairs to check whether types of opening_brackets = closing_brackets
'''

def Check(brackets):

    result = False

    #( = 1
    op_1 = 0

    #[ = 2
    op_2 = 0

    #{ = 2
    op_3 = 0

    #) = 1
    cl_1 = 0
    
    #] = 2
    cl_2 = 0

    #} = 3
    cl_3 = 0

    for x in brackets:
            
        if x == '(':

            op_1 = op_1 + 1
            
            # opening_brackets.append(op_1)
            
            
        if x == '[':

            op_2 = op_2 + 1

            # opening_brackets.append(op_2)
            
            
        if x == '{':

            op_3 = op_3 + 1

            # opening_brackets.append(op_3)
            
            
        if x == ')':

            cl_1 = cl_1 + 1

            # closing_brackets.append(cl_1)
            
        if x == ']':

            cl_2 = cl_2 + 1

            # closing_brackets.append(cl_2)
            
            
        if x == '}':

            cl_3 = cl_3 + 1

            # closing_brackets.append(cl_3)

    '''
    print op_1, op_2, op_3

    print cl_1, cl_2, cl_3
    '''

    # print opening_brackets

    # print closing_brackets
    
    if op_1 == cl_1 and op_2 == cl_2 and op_3 == cl_3:
        
        result = True

        return result


'''
Use to check and return the type of paranthesis
'''

def FindBracket(sample):

    if sample == opb_1:

        return 'opb_1'
    
    if sample == opb_2:

        return 'opb_2'

    if sample == opb_3:

        return 'opb_3'

    if sample == clb_1:

        return 'clb_1'

    if sample == clb_2:

        return 'clb_2'

    if sample == clb_3:

        return 'clb_3'



'''
Use to check the sequence of bracket that is whether one type of opening bracket should lead to another type of closing bracket
'''
        
def FlowCheck(inputs_2):

    y = inputs_2[0]

    result = False

    for x in range(0, len(inputs_2)):

        br_type = FindBracket(inputs_2[x])

        # print inputs_2[x], x

        # print ''.join(str(list(br_type)[0:2]))

        cmp_1 = str(br_type).find('cl')

        # print cmp_1

        cmp_2 = str(FindBracket(y)).find('op')

        # print cmp_2

        if x == 0:

            # print 'Executing' 
            
            continue
        
        elif cmp_1 != -1 and cmp_2 != -1 :

            # print 'Executing'

            if list(br_type)[4] == list(FindBracket(y))[4]:

                y = inputs_2[x]

                continue
                    
            else:

                result = False

                break;

        else:

            y = inputs_2[x]

            result = True
                        
    return result
            

    
# Specify the code for parenthesis

opb_1 = '('

opb_2 = '['

opb_3 = '{'

clb_1 = ')'

clb_2 = ']'

clb_3 = '}'

inputs_2 = ''

print "Enter an expression containing '[', '{', '(', ')', '}', ']'"

# Enter a raw input of parenthesis

inputs = str(raw_input())

inputs_2 = inputs

DetectPairs(inputs_2)
