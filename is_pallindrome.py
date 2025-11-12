T=int(input())
for _ in range(T):
    S=input()
    if S==S[::-1]:
        print(1)
    else:
        print(0)
    print()
