# hour of the day
hour = 18

# is the guard there?
guard = False

if ( hour >= 7):
  if ( hour <= 17 ):
    print("You're in!")
  else:
    if ( guard == True):
      print("You're in! Thanks to Guard")
    else:
      print("You're NOT in! No Guard around")
else:
  if ( guard == True):
    print("You're in! Thanks to Guard")
  else:
    print("You're NOT in! No Guard around")
  
 
