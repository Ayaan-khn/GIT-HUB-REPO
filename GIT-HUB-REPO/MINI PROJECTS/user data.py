def user_info(**kwargs):
    for key,values in kwargs.items():
        print(key,":",values)
user_info(name="Ayaan",City="Lucknow",Age="21")