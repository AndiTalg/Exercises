import json

# from ExerciseData import Exercises
# from DBExercise import DBExercise
# from datetime import datetime
from pprint import pprint

# myExList = Exercises("JSONTest.json")

with open("JSONTest3.json") as f:
    ex_dict = json.load(f)

pprint(ex_dict["exercises"])

for g in ex_dict["groups"]:
    print(g["name"], g["image"])

for e in ex_dict["exercises"]:
    print(e["name"], e["group"])

exs = []


# print(lst)

# print(myclass.exercises("stretch"))

# print(myclass.factor("hamstring_instep"))
# print(myclass.unit("hamstring_instep"))
# print(myclass.image("hamstring_instep"))
# print(myclass.default("hamstring_instep"))
# mydb = DBExercise("mytest.sqlite3")

# mydb.delete_table()

# mydb.create_db()

# mydb.delete_data("2019-05-01 18:14:20.046117")

# mydb.clear_table()

# mydb.insert_data(str(datetime.now()), "hamstring_instep", 0.0, 10, 8, 10)

# mydb.dump_data()

