def palind(r):
    e = len(r) -1
    s = 0

    while (s < e):
        if(r[s] != r[e]):
            return False
        
        s = s+1
        e = e-1

    return True

r = (1,2,3,3,2,1)
print(r)
print()

result = palind(r)

if(result):
    print("The tuple is Flip-Flop")
else:
    print("The tuple is not Flip-Flop")