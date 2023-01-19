#Functions with Outputs

#def format_name(f_name, l_name): 
#  full_name = (f_name + " " + l_name).title()
#  return full_name

#formated_string = format_name("mika", "TURNER")
#print(formated_string)

def format_name(f_name, l_name):
  """Take a first and last name and format it to return the title case of the version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  full_name = (f_name + " " + l_name).title()
  return full_name

print(format_name(input("What is your first name?"), input("What is your last name?")))

