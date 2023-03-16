people = [
    {"name":"arman","house":"bolari"},
    {"name":"geeky","house":"pantami"},
    {"name":"bash","house":"dawaki"}
]

# def f(person):
#     return person["name"]

# people.sort(key=f)
# print(people)

people.sort(key=lambda person:person["name"])
print(people)