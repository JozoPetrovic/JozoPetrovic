def parni(br):
    p=0
    n=0
    for i in range(br):
        if i%2==0:
            p+=1
            print("Parni:")
            yield i
        else:
            n+=1
            print("Neparni:")
            yield i




br=int(input("Unesi parametar: "))
for i in parni(br):
    while i<br:
        print(i)
        break