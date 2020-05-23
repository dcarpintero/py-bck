from hashlib import sha256
import random as rand
import datetime as date


def compute_hash(data):
    return sha256(data.encode('utf-8')).hexdigest()


def compute_double_hash(data):
    return compute_hash(compute_hash(data))


def compute_hash_merkle(data):
    return compute_hash(data)


def compute_nonce(length=20):
    return ''.join([str(rand.randint(0, 9)) for i in range(length)])


def compute_difficulty_target(difficulty):
    difficulty_str = "0x" + '0' * difficulty + 'F' * (64 - difficulty)
    return(int(difficulty_str, 16))


def block_converter(obj):
    if isinstance(obj, date.datetime):
        return obj.__str__()
