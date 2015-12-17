import crypt

def mktripcode(pw):
    pw = pw[:8]
    salt = (pw + "H.")[1:3]
    trip = crypt.crypt(pw, salt)
    print("="*20)
    print(name, "!" + trip[-10:])

print("="*20)
name = input("What's your name?\n> ")
pazz = input("What's your tripkey?\n> #")
mktripcode(pazz)
