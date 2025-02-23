# To all the below given questions make sure to use the structure and algorithm that you believe would be highly accurate if not already provided. (well nothing is accurate in life, but for here let's consider accurate as a close trad-off b/w time and space complexities)

# WAP to ask the user to enter 10 numbers(could be float or int), once entered; provide a choice if the user wants that to be saved 
#in a LinkedList or in an array. After the user made the choice; respond with a success message and ask to provide the user with the options 
#of searching any element, deleting any element or swapping any element with a new element. These choices should appear until the user selects 
#to exit the program; once chosen exit, print the final structure and its length.

num_list=[int(x) for x in input('Enter 10 int numbers... ').split()]
    

print(num_list)
# WAP to ask the user to input elements in a queue which is fixed in size as 5. After the 5th element if the user continues to input, keep on dequeuing the element from the queue and push it to a stack named backup. The condition here is such that the user can only input maximum up-to elements twice the length of the initial queue. At the end print both the structures and their length.
# WAP to implement the binary search to a stack applied over singly linked list [1,2,5,8,19,23,34,109]
