#!/usr/bin/python
import sqlite3

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE users (
                username INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL,
                maxTimeAllowed TEXT NOT NULL,
                isPaused Boolean NOT NULL,
                playedTime TEXT NOT NULL
            );
        ''')

        conn.execute('''
                    CREATE TABLE games (
                        username TEXT NOT NULL,
                        game_name TEXT NOT NULL,
                        game_description,
                        icon TEXT NOT NULL,
                        FOREIGN KEY(username) REFERENCES users(username) 
                    );
                ''')

        conn.commit()
        print("Games table created successfully")
    except:
        print("Games table creation failed")
    finally:
        conn.close()