'''
TASK:
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.
'''
phonebook = {}
entries = int(input())

for n in range(entries):
    name, num = input().strip().split(' ')
    name, num = [str(name), int(num)]
    phonebook[name] = num

while True:
    try:  
        search = str(input())

        if search in phonebook:
            output = ''.join('%s=%r' % (search, phonebook[search]))
            print(output)
        else:
            print("Not found")
    except EOFError:
        break
    
