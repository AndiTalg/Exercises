import csv
import json
from pprint import pprint


class Exercise:
    def __init__(self, ex):
        self.group = ex["group"]
        self.name = ex["name"]
        self.factor = int(ex["factor"])
        self.unit = ex["unit"]
        self.default = int(ex["default"])
        self.min = int(ex["min"])
        self.max = int(ex["max"])
        self.step = int(ex["step"])
        self.image = ex["name"] + ".png"

    def __str__(self):
        return f"{self.group} {self.name} factor: {self.factor} default: {self.default} {self.unit} range: {self.min}-{self.max} step: {self.step} image: {self.image}"


class Exercises:

    # Initialize exercises class
    def __init__(self, json_path):
        # Read json-file with exercise information
        with open(json_path) as f:
            self._ex_dict = json.load(f)
        # Create group list
        self.group_list = [
            {"name": g["name"], "image": g["image"]} for g in self._ex_dict["groups"]
        ]
        # Create exercise list
        self.ex_list = [Exercise(ex) for ex in self._ex_dict["exercises"]]

    # Dump all exercises to console
    def dump_list(self):
        for ex in self.ex_list:
            print(ex)

    # # Get all different group-names for first level navigation
    def group_names(self):
        return [g["name"] for g in self.group_list]

    # Get all exercises of a specific group
    def exercises_of_group(self, group):
        return [ex.name for ex in self.ex_list if ex.group == group]

    # Get exercise object for given exercise name
    def get_exercise(self, name):
        for ex in self.ex_list:
            if ex.name == name:
                return ex


# myEx = Exercise("barbell", "bench")

# print(myEx)

# print(myEx.name)

# print(myEx.factor)

# myExList = Exercises("exercises.json")

# for g in myExList.group_list:
#     print(g["name"], g["image"])

# myExList.dump_list()
# print(myExList.get_exercise("barbell_press"))

# print(myExList.exercises_of_group("bench"))
# print(myExList.group_names())

# print(myExList.get_exercise('barbell_press'))
# myExList.dump_list()
# print(myExList.groups())
# print(myExList.exercises_of_group("pullup"))
