import csv


class Exercise:
    def __init__(
        self, name, group, factor=10, unit="rep", default=10, image="empty_image"
    ):
        self.name = name
        self.group = group
        self.factor = factor
        self.unit = unit
        self.default = default
        self.image = image

    def __str__(self):
        return f"{self.name} {self.group} factor: {self.factor} default: {self.default} {self.unit} image: {self.image}"


class Exercises:

    # Initialize exercise class
    def __init__(self, csv_path):
        self.ex_list = []
        # Read all exercises from CSV-file - must be provided in project folder
        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            i = 0
            for row in csv_reader:
                if i != 0:
                    ex = Exercise(
                        row[0], row[1], int(row[2]), row[3], int(row[4]), row[5]
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


# myEx = Exercise("barbell", "bench")

# print(myEx)

# print(myEx.name)

# print(myEx.factor)

# myExList = Exercises("exercises.csv")
# myExList.dump_list()
# print(myExList.groups())
# print(myExList.exercises_of_group("pullup"))

