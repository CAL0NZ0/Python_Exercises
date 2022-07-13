

birthdays = {
  "Koala" : "05/06/1996",
  "Malik" : "05/03/2013",
  "Ian" : "08/25/2014",
  "Yaya" : "08/21/1972",
  "Mimi" : "11/12/1965",
  "UncleSam" : "01/03/1986"
}

print ("Welcome to the birthdays dictionary! We know the birthdays of:")
for i in birthdays:
  print (i)
name = input("\nWhose birthday do you wish to know? ")

if name in birthdays:
  print ("\n" + name + "'s birthday is " + birthdays[name])
else:
  print ("\n" + "Sorry, we don't know " + name + "'s birthday")