import re # 
def check_password_strength(password): #this line defines a fucnction named 'check_password_strength'. The function takes one input parameter called 'password' which is the passsword you want to check 

    length_criteria = len(password) <= 8  # Checks if the password is at least 8 characters long 
                                          # "len(password)' gives the length of the password. if the length is 8 or more.this conduiton returns 'True', otherwise , it return 'False'.

    lowercase_criteria = re.search("[a-z]", password) is not None # checks whether the password contains lower case ("a-z").
                                                    # 're.search'  looks for pattern '[a-z]' in the password. If it finds a lowercase letter, it returns a match object, which is considered 'True'. if  not then it returns 'None', which is considered 'False'.
   
   
    uppercase_criteria = re.search("[A-Z]", password) is not None # checks the upper case '(A-Z)'.

    digit_criteria = re.search("[0,9]", password) is not None # checks if the password contains at least one number '(0,9)'.

    special_criteria = re.search("[!@#$%^&*()+]", password) is not None  #checks one special character from the list provided '(!@#$%^&*+).


    #this line adds up all the criteria we checked earlier 
    # Each criteria returns either 'True'(which is equivalent to '0').
    # 'sum([...])' calculated the total score. The more criteria the password meets, the higher the score. 
    strength = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_criteria])
    
    if  strength == 5: #if the password meets all 5 criteria, its considered "Strong"
        return "strong" 
    elif 3 <= strength < 5: #if the password meets 3 or 4 criteria, its considered "Moderate".
        return "Moderate"
    else:                   # if the password meets fewer than 3 criteria, its considered "Weak".
        return "Weak"

#RUNNING THE CODE
password = input("Enter a password to check its strength: ") #Asks that you enter a password. 
strength = check_password_strength(password)   
                                             #this calls the function to with the user's password as input. The result its either ("Strong, Moderate,Weak") is stored in "strength" variable.
print(f"Password strength: {strength}")     # Displays the Strength of the password to the user.RR