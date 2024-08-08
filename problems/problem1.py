# Hackerrank solution
""" 
Consider a list (list = []). You can perform the following commands:

insert i, e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list. """

""" Example
N = 4

append 1

append 2

insert 3 1

print

append 1: Append 1 to the list, arr = [1].
append 2: Append 2 to the list, arr = [1, 2].
insert 3 1: Insert 3 at index 1,arr = [1, 3, 2].
print: Print the array. """

if __name__ == "__main__":
    N = int(input())
    list = []

    for i in range(N):
        command = input().split()

        if command[0] == "append":
            list.append(int(command[1]))
        elif command[0] == "insert":
            list.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
            list.remove(int(command[1]))
        elif command[0] == "sort":
            list.sort()
        elif command[0] == "pop":
            list.pop()
        elif command[0] == "print":
            print(list)
        else:
            list.reverse()