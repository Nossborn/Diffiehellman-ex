# Diffie-Hellman key exchange
This is a simple python script that implements a basic version of the Diffie-Hellman key exchange. The algorithm used is taken from two videos on YouTube, found [here](https://www.youtube.com/watch?v=ESPT_36pUFc) and [here](https://www.youtube.com/watch?v=Yjrfm_oRO0w).

## Requirements
- Python 3.7

## Usage
The program can both compute keys, as well as build a precomputed database for faster computations of keys.

### Generating keys
To use the generate keys, type in the command below with an integer seed, like 2053.
```
$ python Diffiehellman.py -N [seed]
```
The program will then execute and generate two private/public key pair for the Diffie-Hellman key exchange.

### The generator database
Beacuse finding the generators for the coprimes of *N* is very slow, the script is using a database of precomputed generators. If you choose an *N* which doesn't exist in the the database, and is larger than 1000, then it may take a *very* long time to compute. The new *N* will then be added to the database. If other N:s are needed, the precomputed database can be expanded by running the [db_handler.py](/db_handler.py), like
```
$ python db_handler.py [start of range] [end of range]
```
Where all generating seeds in the range are added to the database (Note: for adding a single seed, make the *start of range* and *end of range* the same number).

## Disclaimer
This is project is purely for educational purposes and is not intended, or suited, to be used in a real environment.
