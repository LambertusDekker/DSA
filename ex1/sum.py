def main():
    n = int(input("give me a number:"))
    r = remainder(n)
    print(f"Remainder: {r}.")
    if r == 0:
        print("even.")
    else:
        print("odd.")

def remainder(n):
    r = n % 2
    return(r)

if __name__ == "__main__":
    main()

#
# https://www.geeksforgeeks.org/dsa/check-whether-given-number-even-odd/