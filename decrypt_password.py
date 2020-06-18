import bcrypt as bc

def password_hash(plain_password: str):

    hashed_password = bc.hashpw(plain_password.encode('utf-8'), bc.gensalt())
    return hashed_password.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str):
    return bc.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))