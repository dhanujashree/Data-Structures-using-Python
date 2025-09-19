from collections import deque

def is_palindrome(word):
   
    n = len(word)

    
    dq = deque()

    
    for ch in word:
        dq.append(ch)

    while len(dq) > 1:  
        front = dq.popleft()   
        rear = dq.pop()        

        if front != rear:      
            return False

    return True



word = input("Enter a string: ")

if is_palindrome(word):
    print(f" '{word}' is a Palindrome")
else:
    print(f" '{word}' is NOT a Palindrome")
