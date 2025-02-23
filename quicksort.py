# function to swap ith and swap index
def swap_list(list1, i, swap): 
    list1[i], list1[swap] = list1[swap], list1[i]

#function to select pivot element
def select_pivot(list1, l, r):
    mid=(r-l)//2
    a=list1[l]
    b=list1[mid]
    c=list1[r]
    if a<=b<=c or c<=b<=a:
        return mid, b
    elif b<=a<=c or c<=a<=b:
        return l, a
    else:
        return r, c
    #temp=[list1[l]]
    #temp.extend((list1[(r-l)//2], list1[r]))
    #temp=sorted(temp)
    #return temp[len(temp)//2]  #return mid element

# Main function to implement pivot - returns 
def pivot_fn(list1,l,r):
    print('in pivot fn',list1)
    pivot_idx, pivot=select_pivot(list1,l,r)
    swap_list(list1,l,pivot_idx)  #move pivot element to beg
    #print('Initial swap',list1)
    swap_idx=pivot_idx=l #start from 2nd; as first is pivot
    for i in range(l+1,r+1): #r+1 is bcoz last elem is excluded        
        if list1[i] < pivot: #move smaller element to left 
            swap_idx+=1 # increment i all time and swap only when condition match
            swap_list(list1,i, swap_idx)
            #print('later Swap',list1, i , pivot_idx, swap_idx)
    swap_list(list1,swap_idx, pivot_idx) #now move pivot to middle
    #print(list1,swap_idx)
    return swap_idx

def quick_sort_helper(list1, l, r):
    if l<r:
        pivot=pivot_fn(list1, l,r)
        quick_sort_helper(list1, l, pivot-1) #skip sorted pivot b/w -1 and + 1
        quick_sort_helper(list1, pivot+1, r)
    return list1

def quick_sort(list1):
    return quick_sort_helper(list1, 0, len(list1)-1)

    
list1=[1,5,3,2,4]
#print(select_pivot(list1, 0, len(list1)-1))
#pivot_fn(list1, 0, 4) #r=len -1 ; ret
print(quick_sort(list1))
