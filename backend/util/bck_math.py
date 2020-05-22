from hashlib import sha256
import hashlib as hasher
import random as rand
import datetime as date

def hash(data):
    return sha256(data.encode('utf-8')).hexdigest()

def double_hash(data):
    return hash(hash(data))

def compute_hash_merkle(data):
    return hash(data)

def compute_nonce(length=20):
    return ''.join([str(rand.randint(0, 9)) for i in range(length)])

def compute_difficulty_target(difficulty):
    difficulty_str = "0x" + '0' * difficulty + 'F' * (64 - difficulty)
    return(int(difficulty_str, 16))

def block_converter(obj):
    if isinstance(obj, date.datetime):
        return obj.__str__()

