from pyscript import document, display

club_members = ["Rachel Balasico","Adrianna Averilla","Ciara De Guzman","Zyrene Nieto"]

def check_member(e):
    #gets the info from index.html
    first_name = Element("firstName").element.value
    last_name = Element("lastName").element.value

    #for the message
    full_name = first_name + " " + last_name

    #checks if what is inputed part for the list
    is_member = full_name in club_members

    messages = {True: f"Congratulations {full_name}! You are now part of the ICT club.", False: f"Sorry {full_name}, your name is not on the list.}

    #displays the message
    display(messages[is_member], target="result")
