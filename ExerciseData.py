import csv


class Exercise:
    def __init__(
        self, name, group, factor=10, unit="rep", default=10, min=1, max=10, step=1, image="empty_image"
    ):
        self.name = name
        self.group = group
        self.factor = factor
        self.unit = unit
        self.default = default
        self.min = min
        self.max = max
        self.step = step
        self.image = image

    def __str__(self):
        return f"{self.name} {self.group} factor: {self.factor} default: {self.default} {self.unit} range: {self.min}-{self.max} step: {self.step} image: {self.image}"


class Exercises:

    # Initialize exercise class
    def __init__(self, csv_path):
        self.ex_list = []
        # Read all exercises from CSV-file - must be provided in project folder
        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            i = 0
            for row in csv_reader:
                if i != 0:
                    ex = Exercise(
                        row[0], row[1], int(row[2]), row[3], int(row[4]), int(row[5]), int(row[6]), int(row[7]), row[8]
                    )
                    self.ex_list.append(ex)
                i += 1

    # Dump all exercises to console
    def dump_list(self):
        for ex in self.ex_list:
            print(ex)

    # Get all different groups for first level navigation
    def groups(self):
        return set([e.group for e in self.ex_list])

    # Get all exercises of a specific group
    def exercises_of_group(self, group):
        return [e.name for e in self.ex_list if e.group == group]
        
    # Get exercise object for given exercise name
    def get_exercise(self, name):
        print(name)
        for ex in self.ex_list:
            if ex.name == name:
                return ex


# myEx = Exercise("barbell", "bench")

# print(myEx)

# print(myEx.name)

# print(myEx.factor)

#myExList = Exercises("exercises.csv")

#print(myExList.get_exercise('barbell_press'))
# myExList.dump_list()
# print(myExList.groups())
# print(myExList.exercises_of_group("pullup"))
