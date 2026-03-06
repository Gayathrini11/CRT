'''
Optimization: process of modifying the code to reduce the time compexity
Brute Force --. trying of all possible combinations
optimal solution --. needs thinking,low complexity
Optimization Basics : Making the sution 
'''
a=[10,20,30,40,52]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i]+a[j])  #O(n^2)

a=[10,20,30,40,52]
for num in a:
    print(num+num)#O(n)

'''why it is importimprove code speedreduce memory usage'''