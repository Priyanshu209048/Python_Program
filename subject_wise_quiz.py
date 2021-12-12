print("Do you want to play quiz")
print("Select yes or no")
select=input()
score=0
if select=="yes":
    print("1.Science")
    print("2.Grammer")
    print("3.Maths")
    opt=int(input("Select Science, Grammer, Maths: "))
    if opt==1:
        print("Q1. Which gas will be emitted when metals react with water?")
        print("Options")
        print("1.Nitrogen")
        print("2.Hydrogen")
        print("3.Oxygen")
        print("4.Carbon Dioxide")
        ans1=input()
        if ans1=="4":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q2.What type of reaction is respiration?")
        print("Options")
        print("1.Endotherum")
        print("2.Combination")
        print("3.Oxidation")
        print("4.Reduction")
        ans2=input()
        if ans2=="3":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q3.Compounds formed by the transfer of electrons are called?")
        print("Options")
        print("1.Electrovalent")
        print("2.Organic")
        print("3.Covalent")
        print("4.None")
        ans3=input()
        if ans3=="1":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q4.What is the color of silver chloride?")
        print("Options")
        print("1.Green")
        print("2.White")
        print("3.Yellow")
        print("4.Black")
        ans4=input()
        if ans4=="2":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q5.The process of coating zinc with iron is called?")
        print("Options")
        print("1.Corrosion")
        print("2.Electrolysis")
        print("3.Water Planting")
        print("4.Galvanization")
        ans5=input()
        if ans5=="4":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)
        print("Total score: ",score)
    elif opt==2:
        print("Q1.__________ of the two sisters is married.")
        print("Options")
        print("1.Both")
        print("2.Every")
        print("3.Each")
        print("4.Any")
        ans1=input()
        if ans1=="3":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q2._________ of you should attend the conference.")
        print("Options")
        print("1.Both")
        print("2.Each")
        print("3.Every")
        print("4.Many")
        ans2=input()
        if ans2=="1":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q3.We should inform __________ of them.")
        print("Options")
        print("1.Many")
        print("2.Every")
        print("3.Few")
        print("4.All")
        ans3=input()
        if ans3=="4":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q4.They have spent __________ for their son’s wedding.")
        print("Options")
        print("1.Many")
        print("2.Enough")
        print("3.All")
        print("4.The little")
        ans4=input()
        if ans4=="2":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q5.__________ of the candidates pass this exam.")
        print("Options")
        print("1.Enough")
        print("2.Fewer")
        print("3.Either")
        print("4.Most")
        ans5=input()
        if ans5=="4":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)
        print("Total score: ",score)
    elif opt==3:
        print("Q1.The decimal expansion of √2 is.")
        print("Options")
        print("1.finite decimal")
        print("2.no-finite decimal")
        print("3.non-terminating recurring")
        print("4.non-terminating non recurring")
        ans1=input()
        if ans1=="4":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q2.Find the value of 525² – 475².")
        print("Options")
        print("1.100")
        print("2.10000")
        print("3.50000")
        print("4.100000")
        ans2=input()
        if ans2=="3":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q3.The surface area of a cube whose edge equals to cm is:")
        print("Options")
        print("1.62cm^2")
        print("2.30cm^2")
        print("3.54cm^2")
        print("4.90cm^2")
        ans3=input()
        if ans3=="3":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q4.The graph of the equation 2x + 3y = 6 cuts the x-axis at the point")
        print("Options")
        print("1.(0,3)")
        print("2.(3,0)")
        print("3.(2,0)")
        print("4.(0,2)")
        ans4=input()
        if ans4=="2":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)

        print("Q5.How many linear equation in x and y can be satisfied by x = 1 and y = 2?")
        print("Options")
        print("1.Only one")
        print("2.Two")
        print("3.Infinitely many")
        print("4.Three")
        ans5=input()
        if ans5=="":
            print("correct")
            score=score+10
            print("Score: ",score)
        else:
            print("incorrect")
            print("Score: ",score)
        print("Total score: ",score)
else:
    print("Khatam Tata bye bye gaya")
