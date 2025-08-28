def highest(**kwargs):
    high_key = ""
    high_value = 0

    for key, value in kwargs.items():
        if value > high_value:
            high_value = value
            high_key = key
    return high_key, high_value


print(highest(apple=100, banana=40, milk=60))
