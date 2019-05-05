import csv

# Exercise dictionary: group, name, factor, unit, image
ex_dict = {
    "barbell_press": {
        "group": "bench",
        "factor": 100,
        "unit": "kg",
        "default": 30,
        "image": "empty_image",
    },
    "dumbbell_inclined_press": {
        "group": "bench",
        "factor": 100,
        "unit": "kg",
        "default": 10,
        "image": "empty_image",
    },
    "dumbbell_alternate_press": {
        "group": "bench",
        "factor": 100,
        "unit": "kg",
        "default": 8,
        "image": "empty_image",
    },
    "dumbbell_one_arm": {
        "group": "bench",
        "factor": 100,
        "unit": "kg",
        "default": 10,
        "image": "empty_image",
    },
    "dumbbell_overhead": {
        "group": "bench",
        "factor": 100,
        "unit": "kg",
        "default": 10,
        "image": "empty_image",
    },
    "dumbbell_row": {
        "group": "bench",
        "factor": 100,
        "unit": "kg",
        "default": 8,
        "image": "empty_image",
    },
    "quad_standing": {
        "group": "stretch",
        "factor": 100,
        "unit": "sec",
        "default": 20,
        "image": "empty_image",
    },
    "hamstring_standing": {
        "group": "stretch",
        "factor": 100,
        "unit": "sec",
        "default": 20,
        "image": "empty_image",
    },
    "hamstring_instep": {
        "group": "stretch",
        "factor": 100,
        "unit": "sec",
        "default": 20,
        "image": "empty_image",
    },
    "calf_footsling": {
        "group": "stretch",
        "factor": 100,
        "unit": "sec",
        "default": 20,
        "image": "empty_image",
    },
    "calf_standing": {
        "group": "stretch",
        "factor": 100,
        "unit": "sec",
        "default": 20,
        "image": "empty_image",
    },
    "achillis_standing": {
        "group": "stretch",
        "factor": 100,
        "unit": "sec",
        "default": 20,
        "image": "empty_image",
    },
    "side_bend": {
        "group": "stretch",
        "factor": 100,
        "unit": "sec",
        "default": 20,
        "image": "empty_image",
    },
    "lift_body": {
        "group": "sling",
        "factor": 100,
        "unit": "num",
        "default": 12,
        "image": "empty_image",
    },
    "crunch_body": {
        "group": "sling",
        "factor": 100,
        "unit": "num",
        "default": 10,
        "image": "empty_image",
    },
    "pull_narrow": {
        "group": "pullup",
        "factor": 100,
        "unit": "num",
        "default": 5,
        "image": "empty_image",
    },
    "pull_standard": {
        "group": "pullup",
        "factor": 100,
        "unit": "num",
        "default": 5,
        "image": "empty_image",
    },
    "pull_middle": {
        "group": "pullup",
        "factor": 100,
        "unit": "num",
        "default": 5,
        "image": "empty_image",
    },
    "pull_wide": {
        "group": "pullup",
        "factor": 100,
        "unit": "num",
        "default": 5,
        "image": "empty_image",
    },
    "roll_calf_single": {
        "group": "blackroll",
        "factor": 100,
        "unit": "num",
        "default": 8,
        "image": "empty_image",
    },
    "roll_calf_double": {
        "group": "blackroll",
        "factor": 100,
        "unit": "num",
        "default": 8,
        "image": "empty_image",
    },
    "roll_hamstring_single": {
        "group": "blackroll",
        "factor": 100,
        "unit": "num",
        "default": 8,
        "image": "empty_image",
    },
    "roll_hamstring_double": {
        "group": "blackroll",
        "factor": 100,
        "unit": "num",
        "default": 8,
        "image": "empty_image",
    },
}


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

    def dump_list(self):
        for ex in self.ex_list:
            print(ex)

    def groups(self):
        # return list(set([ex_dict[e]["group"] for e in ex_dict.keys()]))
        return set([e.group for e in self.ex_list])

    # Get all exercises of specific group
    def exercises_of_group(self, group):
        return [e for e in ex_dict.keys() if ex_dict[e]["group"] == group]

    # Get factor for specific exercise
    def factor(self, exercise):
        return ex_dict[exercise]["factor"]

    # Get unit for specific exercise
    def unit(self, exercise):
        return ex_dict[exercise]["unit"]

    # Get default value for weight, seconds, repetitions, ... unit for specific exercise
    def default(self, exercise):
        return ex_dict[exercise]["default"]

    # Get image for specific exercise
    def image(self, exercise):
        return ex_dict[exercise]["image"]


myEx = Exercise("barbell", "bench")

print(myEx)

print(myEx.name)

print(myEx.factor)

myExList = Exercises("exercises.csv")
myExList.dump_list()
print(myExList.groups())

