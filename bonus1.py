todo_list = ["shower", "brush teeth", "mow lawn", "eat brains" ]

# loop over thing
for thing in todo_list:
    print(thing)
    
# Python:
# With enumerate() it's a breeze
for index, thing in enumerate(todo_list):
    print(f"{index}: {thing}")