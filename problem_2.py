def decimal_to_binary(n):
    return bin(n)[2:]  

###################################
while True:
    try:
        number = int(input("Enter a positive decimal number: "))
        
        if number < 0:
            print("Invalid input! please enter a positive number")
        else:
 ####################################
            
            binary_equivalent = decimal_to_binary(number)
            print(f"The binary equivalent is {binary_equivalent}")
            break  

    except ValueError:
        print("Invalid input. kindly enter a valid positive decimal number.")
