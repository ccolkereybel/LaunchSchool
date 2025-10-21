def greetings (names, profession):
    greeting = (
        f'Hello, {" ".join(names)}! ' 
        f'Nice to have a {profession["title"]} {profession['occupation']} around.'
    )
    
    return greeting
