# 1. Ryan Harwick
# 2. 2022-01-18
# 3. Week 1 - Variable and Datatype Exercises

ans = 2**256

#Question 1&2
print("Question 1&2")

print(ans)
print(f"The answer to 2^256 is {ans}")

#Question 3
print("Question 3")

ans2 = 1+2*3
print(ans2)
ans3 = (1+2)*3
print(ans3)
#This order of operation follows math order of operation (PEMDAS)

#Question 4
print("Question 4")

a = 9
b = a
a = 1
print(b)
#b is equal to 9 still because you do not update its value after assigning it the value the first time.

#Question 5
print("Question 5")

fp1 = 5.678
fp2 = 3.827

ans1 = fp1 + fp2
ans2 = fp2 + fp1
ans3 = fp1 - fp2
ans4 = fp2 - fp1
ans5 = fp1 // fp2
ans6 = fp2 // fp1
ans7 = fp1 / fp2
ans8 = fp2 / fp1
ans9 = fp1 ** fp2
ans10 = fp2 ** fp1
ans11 = fp1 % fp2
ans12 = fp2 % fp1

print(f"+ {ans1}\n+ {ans2}\n- {ans3}\n- {ans4}\n// {ans5}\n// {ans6}\n/ {ans7}\n/ {ans8}\n** {ans9}\n** {ans10}\n% {ans11}\n% {ans12}")

#The order mattered in all of the operations besides the addition operation. No errors occured within python.w