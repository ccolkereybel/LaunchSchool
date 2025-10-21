balance = (1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print(balance) 

balance = 1000
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05

print(balance)

obj = 'ABcd' #reassign
obj.upper()     #neither
obj = obj.lower() #reassign
print(len(obj)) #neither
obj = list(obj) #reassignment
obj.pop() #mutate
obj[2] = 'X' #mutate object
obj.sort() #mutate object
set(obj) #neither
obj = tuple(obj) #reassignment