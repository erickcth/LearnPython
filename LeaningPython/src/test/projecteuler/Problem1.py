'''
Created on 10 Nov 2016

@author: Erick
'''

from builtins import sum
def main(num):
    answer = []
    i=0
    while i< num:
        if(i % 3 ==0 or i % 5 == 0):
            answer.append(i)
        i = i + 1
        
    print("List of multiple" + str(answer))
    
    total = sum(answer)
    print("Sum of list:" + str(total))



if __name__ == '__main__':
    main(1000)