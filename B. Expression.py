Score: 1
    
CPU: 1s
Memory: 2048MB


Petya studies in a school and he adores Maths. His class has been studying arithmetic expressions. On the last class the teacher wrote three positive integers a, b, c on the blackboard. The task was to insert signs of operations '+' and '*', and probably brackets between the numbers so that the value of the resulting expression is as large as possible. Let's consider an example: assume that the teacher wrote numbers 1, 2 and 3 on the blackboard. Here are some ways of placing signs and brackets:

• 1+2*3=7

• 1*(2+3)=5

• 1* 2 *3=6

• (1+2)*3=9

Note that you can insert operation signs only between a and b, and between b and c, that is, you cannot swap integers. For instance, in the given sample you cannot get expression (1+3)*2.

It's easy to see that the maximum value that you can obtain is 9. Your task is: given a, b and c print the maximum value that you can get.


#Input
The input contains three integers a, b and c, each on a single line (1 ≤ a, b, c ≤ 10).


#Output
Print the maximum value of the expression that you can obtain.


Sample:
Input
1
2
3
Output
9

##################
##   Solution   ##
##################

a = int(input())
b = int(input())
c = int(input())
total = 0
d = [a,b,c]
while (True):
    if(a==0 or b==0 or c==0 or a==1 or b==1 or c==1):
        for x in d:
            if(x==0 or x==1):
                total = total + x
            elif(total==0 or total == 1):
                total = total + x
            else:
                total = total * x
        print(total)
        break

    else:
        print(a*b*c)
        break
