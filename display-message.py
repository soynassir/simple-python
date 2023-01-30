# request user's name
name = input("Enter your name:")


# request the user's email address
email = input("Enter your email address:")

# display the message with the info they provided
print("Hi " + name.replace(name[0], name[0].upper()) + "! " +"We will be contacting you shortly at " + email)
