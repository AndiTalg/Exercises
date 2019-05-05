import sqlite3

# DB information
#
# Table name: exercises
#   timestamp TEXT PRIMARY KEY (consists of date and time when logging)
#   name TEXT (name of the exercise)
#   value FLOAT (value depending on exercise, e.g. 12 kg if wheight exercise)
#   set1 INTEGER (number of repetitions in first set)
#   set2 INTEGER (number of repetitions in second set - defaults to 0 if no other value supplied)
#   set3 INTEGER (number of repetitions in third set - defaults to 0 if no other value supplied)
#
# Unique index not necessary


class DBExercise:
    # Connect to exercises database
    def __init__(self, db_path):
        try:
            self.con = sqlite3.connect(db_path)
            self.cur = self.con.cursor()
        except:
            print("Error ocurred opening database")

    # Close connection
    def __del__(self):
        self.con.close()

    # Update record in exercise table
    def update_data(self, timestamp, name, value, set1, set2=0, set3=0):
        self.cur.execute(
            "UPDATE exercises SET name = ?, value = ?, set1 = ?, set2 = ?, set3 = ? WHERE timestamp = ?",
            (name, value, set1, set2, set3),
        )
        self.con.commit()

    # Insert new record into exercises table
    def insert_data(self, timestamp, name, value, set1, set2=0, set3=0):
        self.cur.execute(
            "INSERT OR REPLACE INTO exercises (timestamp, name, value, set1, set2, set3) VALUES(?,?,?,?,?,?)",
            (timestamp, name, value, set1, set2, set3),
        )
        self.con.commit()

    # Delete record from exercises table based on key (timestamp)
    def delete_data(self, timestamp):
        self.cur.execute("DELETE FROM exercises WHERE timestamp=?", (timestamp,))
        self.con.commit()

    # Create database including table, only used for setup and testing purposes
    def create_db(self):
        self.cur.execute(
            f"CREATE TABLE IF NOT EXISTS exercises"
            f"(timestamp TEXT PTRIMARY KEY, name TEXT, value REAL, set1 INTEGER , set2 INTEGER, set3 INTEGER)"
        )

    # Delete exercise table, only used for setup and testing purposes
    def delete_table(self):
        self.cur.execute("DROP TABLE IF EXISTS exercises")

    # Delete all records from exercise table, only used for setup and testing purposes
    def clear_table(self):
        self.cur.execute("DELETE FROM exercises")

    # Dump all records to console, only used for testing purposes
    def dump_data(self):
        self.cur.execute("SELECT * FROM exercises")
        for ex in self.cur.fetchall():
            print(ex)


# myDB = DBExercise("mytest.sqlite3")
# myDB.clear_table()
# myDB.delete_table()
# myDB.create_db()
# myDB.insert_data("2019-05-05 18:33:41", "quad_standing", 0, 12)
# myDB.dump_data()
