def isPrime(n): 
      
    # Corner case 
    if (n <= 1): 
        return False
  
    # Check from 2 to n-1 
    for i in range(2, n): 
        if (n % i == 0): 
            return False
  
    return True   

def power(x, y) : 
      
    if (y == 0) : 
        return 1
    elif (y % 2 == 0) : 
        return(power(x, y // 2) *
               power(x, y // 2)) 
    else : 
        return(x * power(x, y // 2) *
                power(x, y // 2))

def rightTruPrime(n) :

    while (n != 0) : 
        if (isPrime(n)) : 
            n = n // 10     
        else : 
            return False 
      
    return True

def leftTruPrime(n) : 

    temp = n 
    cnt = 0
  
    while (temp != 0) : 
           
        cnt=cnt + 1 
          
        temp1 = temp % 10  
        if (temp1 == 0) : 
            return False 
          
        temp = temp // 10
        
     
    for i in range(cnt, 0, -1) : 
        
        mod = power(10, i)  
        if (isPrime(n % mod) != True) :  
            return False 
              
    return True 