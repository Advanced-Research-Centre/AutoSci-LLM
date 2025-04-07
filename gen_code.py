import sys

def gen_code():
    # Check if a command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        return
    
    # Convert the command-line argument to an integer
    number = int(sys.argv[1])
    
    # Calculate factorial of the given number
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    
    # Print the result
    print(f"The factorial of {number} is: {factorial}")

if __name__ == "__main__":
    gen_code()