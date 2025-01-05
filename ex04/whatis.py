import sys

def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
            
        if len(sys.argv) == 1:
            return
            
        num = int(sys.argv[1])
        
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
            
    except ValueError:
        raise AssertionError("argument is not an integer")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
