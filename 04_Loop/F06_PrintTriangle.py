def print_triangle(h):
    print(("." * (h - 1)) + "*")
    
    for i in range(2, h, 1):
        print(("." * (h - i)) + "*" + ("." * (2 * (i - 1) - 1)) + "*")
    
    print("*" * (2 * h - 1))

exec(input())
