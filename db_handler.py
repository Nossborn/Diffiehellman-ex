import sqlite3
import os.path
from sys import argv
from sqlite3 import Error

from base import getCoprimeList
from base import findGenerators

def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		print(f"Connection to '{db_file}' successful")
		return conn
	except Error as e:
		print("Error:", e)

def create_tables(conn):
	c = conn.cursor()
	c.execute('CREATE TABLE if not exists generators (N integer, Generators text)')
	conn.commit()

def build_table(conn, startN, endN):
	c = conn.cursor()
	
	n = startN
	while n <= endN:
		c.execute('SELECT N FROM generators WHERE N = ?', (n,))
		if len(c.fetchall()) != 0:
			n += 1
			continue

		coprimeList = getCoprimeList(n)
		gs = findGenerators(n, coprimeList) # This is very slow
		if len(gs) == 0:
			n += 1
			continue
		generators_str = ','.join([str(i) for i in gs])
		c.execute('INSERT INTO generators(N, Generators) VALUES(?,?)', (n, generators_str))
		conn.commit()
		print("Added ", n)
		n += 1

def retrieve_generators(N):
	conn = create_connection("generators.db")
	c = conn.cursor()
	build_table(conn, N, N)
	c.execute('SELECT Generators FROM generators WHERE N = ?', (N,))
	try:
		generators = ((c.fetchall())[0])[0].split(',')
	except:
		generators = []
	conn.close()
	generators = list(map(int, generators))
	return generators

def main():
	conn = create_connection("generators.db")
	create_tables(conn)
	build_table(conn, int(argv[1]), int(argv[2]))
	conn.close()

if __name__ == '__main__':
	main()