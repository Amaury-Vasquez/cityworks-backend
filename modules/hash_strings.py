def hash_id(string: str, len: int = 11):
    return str(hash(string))[1:len]
