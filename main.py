exit_program = True

# "If True" statement, without reference to above 'exit_program' variable will be **True**

if True:
    print("True. Exit Program")
else:
    print("False. Don't exit")
    
    
exit_program_2 = False

# "If True" statement, without reference to above 'exit_program_2' variable will be **True**

if True:
    print("True_2. Exit Program")
else:
    print("False_2. Don't exit")
    

exit_program_3 = True

# "If True" statement, referencing above 'exit_program_3' variable will be **True**

if exit_program_3:
    print("True_3. Exit Program")
else:
    print("False_3. Don't exit")
    
    
exit_program_4 = False

# "If True" statement, referencing above 'exit_program_4' variable will be **False**

if exit_program_4:
    print("True_4. Exit Program")
else:
    print("False_4. Don't exit")


exit_program_5 = False

# "If not" statement, referencing above 'exit_program_5' variable will be **True**

if not exit_program_5:
    print("True_5. Exit Program")
else:
    print("False_5. Don't exit")