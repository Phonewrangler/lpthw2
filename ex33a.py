def wloop(z, ad):
    i = 0
    ad = int(input("increment by?"))
    numbers = []

    while i < z:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + ad
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")


    print ("The numbers:")

    for num in numbers:
        print(num)

wloop(int(input("How high?>")),int(input("increment by?>")))
