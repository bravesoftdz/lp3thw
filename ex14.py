from sys import argv

script, user_name, lives = argv
prompt = '>'

print("Hi {}, I'm the {} script.".format(user_name, script))
print("I'd like to ask you a few question.")
print(f"Do you like me {user_name}?")
likes = input(prompt)


print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me,
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
print(" ")
