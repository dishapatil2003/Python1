# WAP to print the lements of a list in a single line(list is the parameter)


cities =["pune","mumbai","gurgoan","chennai"]
heroes = ["chotabhem","thor",'batman',"spydermnan","ironman"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)