def greet_user(first_name, last_name):  #parameters are the placeholders when we define a function(here name is the parameter)
    print(f"Hello! {first_name} {last_name}")
    print("How are you??")

print("start")
greet_user("Chaitanya", "Kanade") #arguments are actual piece of information we supply in place of parameters
greet_user(last_name="Kanade", first_name="Chaitanya") #keyword arguments
print("finish")