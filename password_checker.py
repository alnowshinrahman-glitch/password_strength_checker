#objective: evaluate how strong a password is and gives clear feedgack to the user on how to improve it
# take user project
#analyze strings character by character
#use conditionals and loops correctly
#write clear functions
#return meaningful results (not just print)

password = input("Enter a password: ")

def check_password_strength(password):
  has_upper = False
  has_lower = False
  has_digit = False
  has_special = False
  strength = 0

  has_length = len(password) >= 8 #checks for each character to know the length

  #loop to check character to meet requirements
  for char in password:
    if char.isupper():
      has_upper = True
    elif char.islower():
      has_lower = True
    elif char.isdigit():
      has_digit = True
    elif char in "!@#$%&":
      has_special = True

    #for each check that fails to meet requirements
  if not has_upper:
    strength += 1 #counts the mistakes
    print("Missing uppercase letter")
  if not has_lower:
    strength += 1
    print("Missing lowercase letter")
  if not has_digit:
     strength += 1
     print("Missing digits")
  if not has_special:
    strength += 1
    print("Missing special characters")
  if not has_length:
    strength += 1
    print("Password too short!")

  if strength == 0:
    return("Password: STRONG!")
  elif strength == 1 or strength == 2:
    return("Password: MEDIUM!")
  elif strength >= 3:
    return("Password: WEAK")

result = check_password_strength(password)
print(result)

#to remember: return sends data back to the caller n print only shows the data on screen





