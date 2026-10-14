import random

def if_this_thing_or_person_sucks(name):
    evaluated_object = random.choice(["sucks", "doesnt suck"])
    return evaluated_object

# hey its sidnk put whatever thing you want in name = "placeholder"
name = "placeholder"
lets_see = if_this_thing_or_person_sucks("name")

# now you run and see the output!

print(f"{name} {lets_see}")
    