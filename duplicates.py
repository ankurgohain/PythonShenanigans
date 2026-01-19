# Return the duplicate value in an array using Floyd's Tortoise and Hare algorithm

def duplicate(arr):
    slow = arr[0]
    fast = arr[1]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    p1 = arr[0]
    p2 = slow
    while p1 != p2:
        p1 = arr[p1]
        p2 = arr[p2]
    return p1

if __name__=="__main__":
    arr = [1,4,1,3,2] 
    print(duplicate(arr))