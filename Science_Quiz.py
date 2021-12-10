print("Do you want to play quiz")
print("Select yes or no")
select=input()
score=0
if select=="yes":
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
else:
    print("Khatam Tata bye bye gaya")
