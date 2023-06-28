def key():
    with open("secret_key.txt", "r") as f:
        SECRET_KEY = f.readline()
    return SECRET_KEY
