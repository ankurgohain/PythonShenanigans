def c(s,e):
    if s<0 and e<0:
        print("Starting and ending numbers must be greater than or equal to zero")
        exit(0)
    if s>e:
        print("Invalid input!! Ending number should be greater than starting number")
        exit(0)

print("Enter the starting and ending numbers:")
start,end=map(int,input().split())
c(start,end)

print(f"Armstrong numbers between {start} and {end} are:")
for num in range(max(start, 100), min(end, 999) + 1):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    if sum(d ** power for d in digits) == num:
        print(num, "\n")