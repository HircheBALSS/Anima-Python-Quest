def square_digits(num):
    # Your code here
    
    concatenate = ""
    
    for i in str(num):
        k = int(i)**2
        concatenate += str(k)
        
    return int(concatenate)