## PY-BCK
A naive blockchain implementation in Python. Consensus is based on proof-of-work as in the 
[Bitcoin](https://nakamotoinstitute.org/static/docs/bitcoin.pdf "Bitcoin: A Peer-to-Peer Electronic Cash System; S. Nakamoto; October 31, 2008") and 
[Hashcash](http://www.hashcash.org/hashcash.pdf "Hashcash - A Denial of Service Counter-Measure; A. Back; 2002") implementations.

Each block is identified by a hash, generated using the SHA256 algorithm on its block header which consists of the following metadata:
* its position in the blockchain (height).
* a reference to the hash of the previous (parent) block in the chain.
* a cryptographic hash of the root of the Merkle-Tree.
* the approximate creation time of the block (seconds from Unix Epoch).
* a unique answer to a difficult-to-solve mathematical puzzle (CPU cost function).

[![Build Status](https://travis-ci.com/dcarpintero/py-bck.svg?branch=master)](https://travis-ci.com/github/dcarpintero/py-bck)
[![codecov](https://codecov.io/gh/dcarpintero/py-bck/branch/master/graph/badge.svg)](https://codecov.io/gh/dcarpintero/py-bck)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/dcarpintero/py-bck)](https://www.codefactor.io/repository/github/dcarpintero/py-bck)
[![Known Vulnerabilities](https://snyk.io/test/github/dcarpintero/py-bck/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/dcarpintero/py-bck?targetFile=requirements.txt)
[![License](https://img.shields.io/github/license/dcarpintero/py-bck)](https://github.com/dcarpintero/py-bck/blob/master/LICENSE)

## Jupyter Notebook
```
bck_demo.ipynb
```
