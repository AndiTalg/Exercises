import json

#name;group;factor;unit;default;min;max;step;image
#barbell_press;bench;10;kg;20;6;20;2;image.png
#dumbbell_inclined_press;bench;10;kg;12;6;20;2;image.png
#dumbbell_alternate_press;bench;10;kg;10;6;20;2;image.png
#dumbbell_one_arm;bench;10;kg;8;6;20;2;image.png
#dumbbell_overhead;bench;10;kg;12;6;20;2;image.png
#dumbbell_row;bench;10;kg;9;6;20;2;image.png
#quad_standing;stretch;10;sec;30;1;3;1;image.png
#hamstring_standing;stretch;10;sec;30;20;50;5;image.png
#hamstring_instep;stretch;10;sec;30;20;50;5;image.png
#calf_footsling;stretch;10;sec;30;20;50;5;image.png
#calf_standing;stretch;10;sec;30;20;50;5;image.png
#achillis_standing;stretch;10;sec;30;20;50;5;image.png


# you can also use the open function to read the content of a JSON file to a string
json_data = """ {
    "bench": {
        "image": "bench.png",
        "exercises": {
            "barbell_press": {
            	"factor": "10",
            	"unit": "kg",
            	"default": 20,
            	"min": 20,
            	"max": 50,
            	"step": 2,
            	"image": "barbell_press.png"
            },
            "dumbbell_inclined_press": {
            	"factor": "15",
            	"unit": "kg",
            	"default": 10,
            	"min": 8,
            	"max": 20,
            	"step": 2,
            	"image": "dumbbell_inclined_press.png"
            }
        },
    }
    "stretch": {
        "image": "stretch.png",
        "exercises": {
            "quad_standing": {
            	"factor": "10",
            	"unit": "sec",
            	"default": 0,
            	"min": 20,
            	"max": 60,
            	"step": 5,
            	"image": "quad_standing.png"
            },
            "hamstring_standing": {
            	"factor": "10",
            	"unit": "sec",
            	"default": 0,
            	"min": 20,
            	"max": 60,
            	"step": 5,
            	"image": "hamstring_standing.png"
            }
        }
    }
    "key 1": "value 1",
    "key 2": "value 2",
    "decimal": 10,
    "boolean": true,
    "list": [1, 2, 3],
    "dictionary": {
        "child key 1": "child value",
        "child key 1": "child value"
    }
}"""

my_dict = json.loads(json_data)

print(my_dict["dictionary"]["child key 1"])
print(json.dumps(my_dict, indent=4))
for x in my_dict:
	print(x)
	
level0 = [x for x in my_dict]
print(level0)
