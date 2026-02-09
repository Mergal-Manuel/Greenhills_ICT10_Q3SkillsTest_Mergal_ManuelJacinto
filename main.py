from pyscript import document, display

def signUp(e):

    document.getElementById('output').innerHTML = "   "
    
    username = document.getElementById('inputuser').value
    password = document.getElementById('inputpass').value


    if len(username) >= 7 and len(password) >=10 and password.isdigit() == False and password.isalpha() == False:
        
        display(f'successfully signed up.', target='output')

    else:
    
        if len(username) < 7:
            display(f'your username must have more than or equal to 7 characters.', target='output')

        elif len(password) < 10:
            display(f'your password must contain more than or equal to 10 characters', target='output')

        elif password.isdigit() == True:
            display(f'your password must contain at least 1 letter.', target='output')

        elif password.isalpha() == True:
            display(f'your password must contain at least 1 number.', target='output')

        else:
            pass