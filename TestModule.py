from ExerciseData import Exercises
from DBExercise import DBExercise
from datetime import datetime

myclass = Exercises()
lst = myclass.groups()
# print(lst)

# print(myclass.exercises("stretch"))

# print(myclass.factor("hamstring_instep"))
# print(myclass.unit("hamstring_instep"))
# print(myclass.image("hamstring_instep"))
# print(myclass.default("hamstring_instep"))
mydb = DBExercise("mytest.sqlite3")

# mydb.delete_table()

# mydb.create_db()

mydb.delete_data("2019-05-01 18:14:20.046117")

mydb.insert_data(str(datetime.now()), "hamstring_instep", 0.0, 10, 8, 10)

mydb.dump_data()

