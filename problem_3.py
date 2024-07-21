def display_right_angle_triangle(n):
    for i in range(1, n + 1):
        print('1 ' * i)

##################################################

def display_palindromic_triangle(n):
    for i in range(1, n + 1):
#####################################################
        left_part = ''.join(str(x) for x in range(1, i + 1))
        right_part = left_part[-2::-1]  
        row = left_part + right_part
        print(row)

def help_menu():
    print("\nHelp:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1")
    print("121")
    print("12321")
    print("1234321")
    print("123454321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
       ##############################################
        if choice == '1':
            try:
                rows = int(input("Enter the number of lines: "))
                display_right_angle_triangle(rows)
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == '2':
        ##########################################
            try:
                rows = int(input("Enter the number of lines: "))
                display_palindromic_triangle(rows)
            except ValueError:
                print("Please enter a valid integer.")

        ############################################
        elif choice == '3':
            help_menu()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid! kindly enter a number between 1 & 4.")

if __name__ == "__main__":
    main()
