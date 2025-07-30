weight = int(input("Please enter weight: "))
unite = 0


unite = input("Please enter the unite Kg(k) or Pound (p): ")

if unite.lower() == "k" :
    weight_1 = weight * 2.205
    print(f"{weight}kg = {round(weight_1,2)}lbs")
elif unite.lower() == "p" :
    weight_1 = weight * 0.454
    print(f"{weight}lbs = {round(weight_1,2)}kg")
































