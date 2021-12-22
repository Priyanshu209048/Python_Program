print("Welcome To My Calculator")
i=1
while(i>0):
    print("Main menu")
    print("1.Calculator")
    print("2.Area Finder")
    print("3.Volume Finder")
    print("4.Exit")
    opt=int(input("select Calculator, Area Finder, Volume Finder, Exit:"))
    if opt==1:
        a=int(input("Enter Number 1: "))
        b=int(input("Enter Number 2: "))
        print("1.Add")
        print("2.Multiple")
        print("3.Divide")
        print("4.Subtract")
        select=int(input("select Add, Multiple, Divide, Subtract:"))
        if select==1:
            add=a+b
            print("Addision of two number is ",add)
        elif select==2:
            multiple=a*b
            print("Multiplication of two number is ",multiple)
        elif select==3:
            divide=a/b
            print("Division of two number is ",divide)
        elif select==4:
            add=a+b
            print("Addision of two number is ",add)
        print("Do you want to return Main menu")
        select=input("yes/no")
        if select=="yes":
            print("Go to Main menu")
            continue
        else:
            break
    elif opt==2:
        print("You select Area finder")
        print("Which shape of area you want: ")
        print("1.Square")
        print("2.Rectangle")
        print("3.Circle")
        print("4.Triangle")
        select=int(input("select Square, Rectangle, Circle, Triangle:"))
        if select==1:
            side=int(input("Enter side of a square:"))
            area=side**2
            print("Area of Square:",area)
        elif select==2:
            l=int(input("Enter number 1: "))
            b=int(input("Enter number 2: "))
            area=l*b
            print("Area of Rectangle: ",area)
        elif select==3:
            r=int(input("Enter radius: "))
            pi=3.14
            area=pi*(r**2)
            print("Area of Circle",area)
        elif select==4:
            b=int(input("Enter base: "))
            h=int(input("Enter height: "))
            area=0.5*b*h
            print("Area of triangle: ",area)
        print("Do you want to return Main menu")
        select=input("yes/no")
        if select=="yes":
            print("Go to Main menu")
            continue
        else:
            break
    elif opt==3:
        print("You Select Volume finder")
        print("Which shape of area you want: ")
        print("1.Sphere")
        print("2.Cylinder")
        print("3.Cone")
        select=int(input("select Sphere, Cylinder, Cone:"))
        if select==1:
            r=int(input("Enter radius: "))
            pi=3.14
            volume=(4/3)*pi*(r**3)
            print("Volume of circle",volume)
        elif select==2:
            r=int(input("Enter radius: "))
            h=int(input("Enter height: "))
            volume=3.14*(r**2)*h
            print("Volume of rectangle: ",volume)
        elif select==3:
            r=int(input("Enter radius: "))
            h=int(input("Enter height 2: "))
            volume=(1/3)*3.14*(r**2)*h
            print("Volume of rectangle: ",volume)
        print("Do you want to return Main menu")
        select=input("yes/no")
        if select=="yes":
            print("Go to Main menu")
            continue
        else:
            break
        i+=1
