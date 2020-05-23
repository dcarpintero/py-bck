## PY-BCK
A naive blockchain implementation in Python. Consensus is based on proof-of-work as in the 
[Bitcoin](https://nakamotoinstitute.org/static/docs/bitcoin.pdf "Bitcoin: A Peer-to-Peer Electronic Cash System; S. Nakamoto; October 31, 2008") and 
[Hashcash](http://www.hashcash.org/hashcash.pdf "Hashcash - A Denial of Service Counter-Measure; A. Back; 2002") implementations.

Each block contains the following metadata:
* its position in the blockchain
* a reference to the hash of the previous (parent) block in the chain
* a cryptographic hash of the root of the Merkle-Tree of transactions
* the approximate creation time of the block (seconds from Unix Epoch)
* a unique answer to a difficult-to-solve mathematical puzzle
* a cryptographic hash of the block metadata

(https://travis-ci.com/dcarpintero/py-bck.svg?branch=master)


## Jupyter Notebook
```
bck_demo.ipynb
```

## Create and Activate a virtual environment
```
virtualenv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (OS X and Ubuntu)
```

## Install dependencies
```
pip install -r requirements.txt
```

## Run tests
```
python -m pytest
```

## Run Demo
```
python bck_demo.py
```