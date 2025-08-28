def total(**kwargs):
    totalmrp=0
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        totalmrp= totalmrp+value
    return totalmrp
print(total(apple=100,banana=40,milk=50))