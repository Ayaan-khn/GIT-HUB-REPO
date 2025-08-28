def greet(**kwargs):
    name = kwargs["name"]
    age = kwargs["age"]
    print(f"Hello {name}, you are {age} years old!")
greet(name="Ayaan", age=21)