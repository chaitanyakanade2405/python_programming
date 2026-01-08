def prime():
    number = int(input("enter no.: "))
    if number <= 1:
        print("not prime")
        return
    for i in range(2, number):
        if(number % i==0):
            print("not prime")
            return
        
    print("prime")

prime()
        