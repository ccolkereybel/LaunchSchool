#function takes 2 arguments --> string and num
#print string as many times as int says

def repeat(string, repeats):
    for _ in range(0, repeats):
        print(string)

repeat('Hello', 3)