# store the quote into a string variable
quote = "You can have data without information, but you cannot have information without data."

# convert the quote to lowercase
quote = quote.lower()

# list containing all the English alphabet in lowercase
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for letter in alphabet:
  freq = 0
  for aletter in quote:
    if ( aletter == letter ):
      freq += 1
  if ( freq != 0 ):
    print(letter + " : " + str(freq))
