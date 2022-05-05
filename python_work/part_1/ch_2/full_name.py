first_name = "ada"
last_name = "lovelace"
#This is a f-string (f means format). Python formats the strings by replacing the name of any variable in braces with its value
#{first name} & {last name} are replaced by their values ada & lovelace
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)