print("Welcome to my band name generator, anon!")
#ask user for their name
name = input("What is your first name?\n")
#ask user for name of city they grew up in
city_name = input("Insert name of city you grew up in:\n")
#ask user for name of their pet
pet = input("Do you have a pet? yes/no\n")
if pet == "yes":
  pet_name = input("What pet do you have?\n")
elif pet == "no":
  pet_name = input("What pet would you love to own?\n")
#combine the names of city and pet and display their band name
print("Okay " + name +", your band name is " + city_name + " " + pet_name + ".")