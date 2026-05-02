
def print_name(name, count = 0):
    if count == 5: 
        return
    print(name)
    print_name(name, count + 1)
    
print_name("Kamran")