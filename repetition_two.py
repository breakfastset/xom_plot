
count = 0     # priming the loop -> prepare to enter the loop
while count < 5:   # as long as count is less than 5, execute the statements
    print(count)
    count = count + 1     # increment count by 1, ensure condition becomes False to exit the loop

#  prime the loop
#  while condition is True:
#       statement 1
#       statement 2
#       ....
#       statement n
#
#       modify variable to eventually make the condition False (to exit loop)
#
print()
#
user_input = input("Say something or Q to quit: ").upper()    # prime the loop
while user_input != "Q":                              # condition
    print(user_input)     # Echo what the user says in uppercase (statement)
    user_input = input("Say something or Q to quit: ").upper()    # modify user_input to eventually stop the loop

print("End of program.")