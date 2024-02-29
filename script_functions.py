def get_environment():
    option = input("Is this for 'test' or 'production'? ")
    if option == "test":
        return option
    if option == "production":
        return production
    else:
        return ""