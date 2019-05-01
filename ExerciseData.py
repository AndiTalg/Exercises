
# Exercise dictionary: group, name, factor, unit, image
ex_dict = {
    'barbell_press': {'group':'bench', 'factor':100, 'unit':'kg', 'default':30, 'image':'empty_image'},
    'dumbbell_inclined_press': {'group':'bench', 'factor':100, 'unit':'kg', 'default':10,'image':'empty_image'},
    'dumbbell_alternate_press': {'group':'bench', 'factor':100, 'unit':'kg',  'default':8,'image':'empty_image'}, 
    'dumbbell_one_arm': {'group':'bench', 'factor':100, 'unit':'kg', 'default':10, 'image':'empty_image'}, 
    'dumbbell_overhead': {'group':'bench', 'factor':100, 'unit':'kg', 'default':10, 'image':'empty_image'}, 
    'dumbbell_row': {'group':'bench', 'factor':100, 'unit':'kg', 'default':8, 'image':'empty_image'}, 
    'quad_standing': {'group':'stretch', 'factor':100, 'unit':'sec', 'default':20, 'image':'empty_image'}, 
    'hamstring_standing': {'group':'stretch', 'factor':100, 'unit':'sec', 'default':20, 'image':'empty_image'}, 
    'hamstring_instep': {'group':'stretch', 'factor':100, 'unit':'sec', 'default':20, 'image':'empty_image'}, 
    'calf_footsling': {'group':'stretch', 'factor':100, 'unit':'sec', 'default':20, 'image':'empty_image'}, 
    'calf_standing': {'group':'stretch', 'factor':100, 'unit':'sec', 'default':20, 'image':'empty_image'}, 
    'achillis_standing': {'group':'stretch', 'factor':100, 'unit':'sec', 'default':20, 'image':'empty_image'}, 
    'side_bend': {'group':'stretch', 'factor':100, 'unit':'sec', 'default':20, 'image':'empty_image'}, 
    'lift_body': {'group':'sling', 'factor':100, 'unit':'num', 'default':12, 'image':'empty_image'}, 
    'crunch_body': {'group':'sling', 'factor':100, 'unit':'num', 'default':10, 'image':'empty_image'}, 
    'pull_narrow': {'group':'pullup', 'factor':100, 'unit':'num', 'default':5, 'image':'empty_image'}, 
    'pull_standard': {'group':'pullup', 'factor':100, 'unit':'num', 'default':5, 'image':'empty_image'}, 
    'pull_middle': {'group':'pullup', 'factor':100, 'unit':'num', 'default':5, 'image':'empty_image'}, 
    'pull_wide': {'group':'pullup', 'factor':100, 'unit':'num', 'default':5, 'image':'empty_image'}, 
    'roll_calf_single': {'group':'blackroll', 'factor':100, 'unit':'num', 'default':8, 'image':'empty_image'}, 
    'roll_calf_double': {'group':'blackroll', 'factor':100, 'unit':'num', 'default':8, 'image':'empty_image'}, 
    'roll_hamstring_single': {'group':'blackroll', 'factor':100, 'unit':'num', 'default':8, 'image':'empty_image'}, 
    'roll_hamstring_double': {'group':'blackroll', 'factor':100, 'unit':'num', 'default':8, 'image':'empty_image'}, 
}

# Get list of different groups
def get_groups():
    return set([ex_dict[e]['group'] for e in ex_dict.keys()])

# Get all exercises of specific group
def get_names(group):
    return [e for e in ex_dict.keys() if ex_dict[e]['group'] == group]

# Get factor for specific exercise
def get_factor(ex):
    return ex_dict[ex]['factor']

# Get unit for specific exercise
def get_unit(ex):
    return ex_dict[ex]['unit']    

# Get default value for weight, seconds, repetitions, ... unit for specific exercise
def get_default(ex):
    return ex_dict[ex]['unit']   

# Get image for specific exercise
def get_image(ex):
    return ex_dict[ex]['image']    

#print(get_groups())
#print(get_names('stretch'))
#print(get_factor('hamstring_instep'))
#print(get_unit('hamstring_instep'))
#print(get_image('hamstring_instep'))