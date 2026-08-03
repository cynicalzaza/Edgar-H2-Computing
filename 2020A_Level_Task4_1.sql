import sqlite3
conn=sqlite3.connect("school.db")
conn.execute(""" CREATE TABLE IF NOT EXISTS "People" (
	"PersonID"	INTEGER,
	"Fullname"	TEXT,
	"DateOfBirth"	TEXT,
	"ScreenName"	TEXT,
	"IsAdult"	INTEGER,
	PRIMARY KEY("PersonID" AUTOINCREMENT))"""
)