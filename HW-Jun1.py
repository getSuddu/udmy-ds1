'''
You are given an array of integers that represents the scores of students in a class. However, some of the scores are missing, 
and they are represented by -1. Your task is to complete the missing scores by assigning a unique score to each missing element
in such a way that the overall class average is maximized. Once the missing scores are completed, sort the array in ascending order 
using the bubble sort algorithm. Finally, your program should print the sorted array, the highest and lowest scores, and the maximum class 
average achieved.

Write a Python program to solve this task. Your program should include a function named complete_scores that takes the original array as
input and returns the completed array.

Example:
Input:
scores = [85, -1, 78, 90, -1, 95, 80]
Output:
Sorted array: [74, 78, 80, 85, 90, 92, 95]
Highest score: 95
Lowest score: 74
Maximum class average: 84.71428571428571
'''
scores = [85, -1, 78, 90, -1, 95, 80]
#avg= sum(scores)/len(scores)
def complete_scores(scores):
    high_score=max(scores)
    class_avg=0
    print('current class_avg', class_avg)
    missing_count=0
    j=1 #var to update missing number=high-j
    for i,score in enumerate(scores):
        if score==-1:
            missing_count+=1  #To know how many were missing
            temp_score=high_score-j
            while temp_score in scores:
                temp_score-=1
            scores[i]=temp_score
            j+=1
        #calculate avg at each iteration
        avg=sum(scores[:i+1])/(i+1)
        print(scores[:i+1], avg,85.6)
    print('final scores', scores, 'final avg', avg)


#Prompt user to Enter Score    
#scores=[int(score) for score in input('Enter scores of students in a class ').split()]
#Comlete missing score              #print(scores)
complete_scores(scores)

#Bubble sort

def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(len(list1)-i-1):
            if list1[j]>list1[j+1]:
                #swap 
                list1[j+1],list1[j] = list1[j],list1[j+1]
    print('Sorted Array: ',list1)

bubble_sort(scores)
print('Highest Score: ', scores[-1])
print('Lowest Score: ', scores[-1])
print('Maximum Class Average: {:.2f}'.format(sum(scores)/len(scores)))
#print(f'Maximum Class Average: {sum(scores)/len(scores):.2f}' )



'''
You are given an array of integers representing the heights of a group of people. Each height is unique. Your task is to sort the array in ascending order using the selection sort algorithm. Once the array is sorted, you need to implement a stack data structure using an array. After implementing the stack, you need to perform a binary search on the sorted array to find the index of a specific target height. Finally, your program should print the sorted array, the target height, the index of the target height, and the elements in the stack after performing a series of push and pop operations.

Write a Python program to solve this task. Your program should include the implementation of the selection sort algorithm, the stack data structure, and the binary search algorithm.


Example:


Input:

heights = [175, 160, 180, 165, 170, 185]

target_height = 170


Output:

Sorted array: [160, 165, 170, 175, 180, 185]

Target height: 170

Index of target height: 2

Stack elements (top to bottom): [180, 175, 165, 160]


You are given an unordered linked list of integers. Your task is to sort the linked list in ascending order using the insertion sort algorithm. You need to implement a function that takes the head of the linked list as input and returns the sorted linked list. Your program should also print the original linked list and the sorted linked list.

Write a Python program to solve this task. Your program should include the implementation of a singly linked list and the insertion sort algorithm.


Example:


Input:

Linked list: 5 -> 2 -> 8 -> 1 -> 9


Output:

Original linked list: 5 -> 2 -> 8 -> 1 -> 9

Sorted linked list: 1 -> 2 -> 5 -> 8 -> 9


You are given an array of integers representing the heights of a group of people. Your task is to determine if there exists a pair of heights in the array such that their sum is equal to a given target value. You need to write a function that takes the array of heights and the target value as input and returns True if such a pair exists and False otherwise.

Write a Python program to solve this task. Your program should include a function named check_heights that takes the array of heights and the target value as input and returns True or False.


Example:


Input:

heights = [175, 160, 180, 165, 170]

target = 335


Output:

Result: True


Explanation:

In this example, the pair (175, 160) has a sum of 335, which matches the target value. Therefore, the function returns True.









You are given an unordered queue of positive integers. Your task is to perform the following operations:

Transfer the elements from the queue to a stack.
Sort the elements in the stack in ascending order using the selection sort algorithm.
Transfer the sorted elements back to a new queue.
Implement a singly linked list to store the elements of the new queue.
Perform a binary search on the linked list to find the index of a specific target value.

Write a Python program to solve this task. Your program should include the implementation of a queue, stack, singly linked list, selection sort algorithm, and binary search algorithm.


Example:

Input:

Queue: 8 -> 3 -> 5 -> 2 -> 7

Target value: 5


Output:

Sorted queue: 2 -> 3 -> 5 -> 7 -> 8

Linked list: 2 -> 3 -> 5 -> 7 -> 8

Index of the target value (5): 2
'''


