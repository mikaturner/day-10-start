#Functions with Outputs

def format_name(f_name, l_name): 
  full_name = (f_name + " " + l_name).title()
  return full_name

formated_string = format_name("mika", "TURNER")
print(formated_string)