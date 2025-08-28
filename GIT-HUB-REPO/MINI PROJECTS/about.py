def describe_me(**kwargs):
    for key,values in kwargs.items():
        print(key,":",values)
describe_me(name="Ayaan", age=21, city="Lucknow", hobby="Coding")