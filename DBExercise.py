import sqlite3

# DB information
#
# Table name: exercises
#   timestamp TEXT PRIMARY KEY
#   name TEXT
#   value FLOAT
#   set1 INTEGER
#   set2 INTEGER
#   set3 INTEGER
#
# Unique index not necessary


class DBExercise:
    def __init__(self, db_path):
        try:
            self.con = sqlite3.connect(db_path)
            self.cur = self.con.cursor()
        except:
            print("Error ocurred opening database")

    def __del__(self):
        self.con.close()

    def update_data(self, timestamp, name, value, set1, set2=0, set3=0):
        self.cur.execute(
            "UPDATE exercises SET name = ?, value = ?, set1 = ?, set2 = ?, set3 = ? WHERE timestamp = ?",
            (name, value, set1, set2, set3),
        )
        self.con.commit()

    def insert_data(self, timestamp, name, value, set1, set2=0, set3=0):
        self.cur.execute(
            "INSERT OR REPLACE INTO exercises (timestamp, name, value, set1, set2, set3) VALUES(?,?,?,?,?,?)",
            (timestamp, name, value, set1, set2, set3),
        )
        self.con.commit()

    def delete_data(self, timestamp):
        self.cur.execute("DELETE FROM exercises WHERE timestamp=?", (timestamp,))
        self.con.commit()

    def create_db(self):
        # Create DB with table
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS exercises
	(timestamp TEXT PTRIMARY KEY, name TEXT, value REAL, set1 INTEGER , set2 INTEGER, set3 INTEGER)"""
        )

    def delete_table(self):
        self.cur.execute("DROP TABLE IF EXISTS exercises")

    # cur.execute('CREATE UNIQUE INDEX daily_date ON dailydata ( date)')

    def dump_data(self):
        self.cur.execute("SELECT * FROM exercises")
        for ex in self.cur.fetchall():
            print(ex)

