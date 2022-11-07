name = input("enter your  name\n")
cointype = float(input("enter type of coin\n"))
weight = float(input("enter the weight of the bag\n"))
accuracy = 1
total_bag = 0
 
#user input
 
 
CoinCountFile = open("coincount.txt","a")
CoinCountFile.write("#" + " " +name + "\n")
# CoinCountFile.write("£")
# CoinCountFile.write(str(cointype))
# CoinCountFile.write("\n")
# CoinCountFile.write(str(weight))
# CoinCountFile.write("g")
# CoinCountFile.write("\n")
# CoinCountFile.close()
# writes the variables to the file
 
# def coincalculator(cointype):
#     match cointype:
#         case 2:
#             return 120
#         case 1:
#             return 175
#         case 0.5:
#             return 160
#         case 0.2:
#           return 250
#         case 0.1:
#           return 325
#         case 0.05:
#           return 23.5
#         case 0.02:
#           return 35.6
#         case 0.01:
#           return 36.5
 
if cointype == 2:
  if weight != 120:
    coin_needed =  weight / 120
    accuracy = accuracy - 1
    print(coin_needed)
    CoinCountFile.write("The amount of coins is wrong" + " " + str(weight) )
  else :
    CoinCountFile.write("£")
    CoinCountFile.write(str(cointype))
    CoinCountFile.write("\n")
    CoinCountFile.write(str(weight))
    CoinCountFile.write("g")
    CoinCountFile.write("\n")
    CoinCountFile.close()
    accuracy = accuracy + 1
    print("Thank you for donating")
    total_bag = total_bag + 1
 
if cointype == 1:
  if weight != 175:
    coin_needed =  weight / 175
    accuracy = accuracy - 1
    print(coin_needed)
    CoinCountFile.write("The amount of coins is wrong" + " " + str(weight) )
  else :
    CoinCountFile.write("£")
    CoinCountFile.write(str(cointype))
    CoinCountFile.write("\n")
    CoinCountFile.write(str(weight))
    CoinCountFile.write("g")
    CoinCountFile.write("\n")
    CoinCountFile.close()
    accuracy = accuracy + 1
    print("Thank you for donating")
    total_bag = total_bag + 1
 
if cointype == 0.5:
  if weight != 160:
    coin_needed =  weight / 160
    accuracy = accuracy - 1
    print(coin_needed)
    CoinCountFile.write("The amount of coins is wrong" + " " + str(weight) )
  else :
    CoinCountFile.write("£")
    CoinCountFile.write(str(cointype))
    CoinCountFile.write("\n")
    CoinCountFile.write(str(weight))
    CoinCountFile.write("g")
    CoinCountFile.write("\n")
    CoinCountFile.close()
    accuracy = accuracy + 1
    print("Thank you for donating")
    total_bag = total_bag + 1
 
if cointype == 0.2:
  if weight != 250:
    coin_needed =  weight / 250
    accuracy = accuracy - 1
    print(coin_needed)
    CoinCountFile.write("The amount of coins is wrong" + " " + str(weight) )
  else :
    CoinCountFile.write("£")
    CoinCountFile.write(str(cointype))
    CoinCountFile.write("\n")
    CoinCountFile.write(str(weight))
    CoinCountFile.write("g")
    CoinCountFile.write("\n")
    CoinCountFile.close()
    accuracy = accuracy + 1
    print("Thank you for donating")
    total_bag = total_bag + 1
 
if cointype == 0.05:
  if weight != 23.5:
    coin_needed =  weight / 23.5
    accuracy = accuracy - 1
    print(coin_needed)
    CoinCountFile.write("The amount of coins is wrong" + " " + str(weight) )
  else :
    CoinCountFile.write("£")
    CoinCountFile.write(str(cointype))
    CoinCountFile.write("\n")
    CoinCountFile.write(str(weight))
    CoinCountFile.write("g")
    CoinCountFile.write("\n")
    CoinCountFile.close()
    accuracy = accuracy + 1
    print("Thank you for donating")
    total_bag = total_bag + 1
 
if cointype == 0.02:
  if weight != 35.6:
    coin_needed =  weight / 35.6
    accuracy = accuracy - 1
    print(coin_needed)
    CoinCountFile.write("The amount of coins is wrong" + " " + str(weight) )
  else :
    CoinCountFile.write("£")
    CoinCountFile.write(str(cointype))
    CoinCountFile.write("\n")
    CoinCountFile.write(str(weight))
    CoinCountFile.write("g")
    CoinCountFile.write("\n")
    CoinCountFile.close()
    accuracy = accuracy + 1
    print("Thank you for donating")
    total_bag = total_bag + 1
 
if cointype == 0.01:
  if weight != 36.5:
    coin_needed =  weight / 36.5
    accuracy = accuracy - 1
    print(coin_needed)
    CoinCountFile.write("The amount of coins is wrong" + " " + str(weight) )
  else :
    CoinCountFile.write("£")
    CoinCountFile.write(str(cointype))
    CoinCountFile.write("\n")
    CoinCountFile.write(str(weight))
    CoinCountFile.write("g")
    CoinCountFile.write("\n")
    CoinCountFile.close()
    accuracy = accuracy + 1
    total_bag = total_bag + 1
 
show = input("Show the txt file ? Y/N\n")
 
if show == "Y":
  CoinCountFile = open("coincount.txt","r")
  print(CoinCountFile.read())
elif show == "N" :
  print("thank you for your service")
else :
  print("Not avaible")
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
# Bag value / coin value = how many coins are in the bag
# Number of coins in bag*weight = total weight
 
