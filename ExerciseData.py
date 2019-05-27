import json

class Group:
    def __init__(self, g):
        self.name = g["name"]
        self.image = g["name"] + ".png"

    def __str__(self):
        return f"Group name: {self.name}, group image: {self.image}"
        
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
        self.group_list = [Group(g) for g in self._ex_dict["groups"]]
        # Create exercise list
        self.ex_list = [Exercise(ex) for ex in self._ex_dict["exercises"]]

    # Dump all exercises to console, only for testing purposes
    def _dump_exercises(self):
        for ex in self.ex_list:
            print(ex)
            
    # Dump all groups to console, only for testing purposes
    def _dump_groups(self):
        for g in self.group_list:
            print(g)

    # Get all different group names for first level navigation
    def group_names(self):
        return [g.name for g in self.group_list]
        
    # Get all exercises of a specific group for second level navigation
    def exercises_of_group(self, group):
        return [ex.name for ex in self.ex_list if ex.group == group]
    
    # Get name of group image
    def group_image(self, name):
        for g in self.group_list:
            if g.name == name:
                return g.image
                
    # Get name of exercise image
    def exercise_image(self, name):
        for e in self.ex_list:
            if e.name == name:
                return e.image
                
    # Get group object with given name
    def get_group(self, name):
        for g in self.group_list:
            if g.name == name:
                return g.image

    # Get exercise object with given name
    def get_exercise(self, name):
        for ex in self.ex_list:
            if ex.name == name:
                return ex
