import ui,console
import math
from ExerciseData import Exercises, Exercise
from DBExercise import DBExercise

MARGIN = 10
V_SPACING = 5
H_SPACING = 5
SET_BTN_W = 0.06
SET_BTN_Y = 0.7
VAL_BTN_W = 0.05
VAL_BTN_Y = 0.8
DATEPICKER_W = 0.6
DATEPICKER_H = 0.25
DATEPICKER_Y = 0.02
INFOLBL_W = 0.6
INFOLBL_H = 0.05
INFOLBL_Y = 0.45
TEXT_W = 0.2
TEXT_H = 0.05
TEXT_Y = 0.55
CMDBTN_W = 0.1
CMDBTN_H = 0.05
CMDBTN_Y = 0.9

TOP_LEVEL = 0
EX_LEVEL = 1

class tvDelegate(object):
    
    def __init__(self, mview):   
        self.ex = Exercises('exercises.csv')
        self.mview = mview
        self.currentTitle = None
        self.currentRow = None
        self.items = list(self.ex.groups())
        self.level = 0
        self.currentNumLines = len(self.items)
        
    def tableview_did_select(self, tableview, section, row):
        
        # Selection on top level -> reload table view with corresponding exercises
        if self.level == TOP_LEVEL:
            self.items = self.ex.exercises_of_group(self.items[row])
            self.level = EX_LEVEL
        # Selection on exercise level -> start save exercise dialogue
        else:
            # Get corresponding exercise object of user selection
            ex_obj = self.ex.get_exercise(self.items[row])
            # Reset list items of table vie to top level
            self.items = list(self.ex.groups())
            self.level = TOP_LEVEL
            # Present dialogue to log exercise
            s = SaveView(self.mview, ex_obj)
            s.background_color = '#dcf1ff'
            s.present('')
     
        self.currentNumLines = len(self.items)
        tableview.reload_data() # forces changes into the displayed list

    def tableview_number_of_rows(self, tableview, section):
        # Return the number of rows in the section
        return self.currentNumLines #needed to be in sync with displayed version, 

    def tableview_cell_for_row(self, tableview, section, row):
        # Create and return a cell for the given section/row
        cell = ui.TableViewCell()
        cell.text_label.text =  self.items[row]
        cell.accessory_type = 'disclosure_indicator'
        return cell
    


class SaveView (ui.View):
	
	def __init__(self, mview, ex_obj, *args, **kwargs):
		
		super().__init__(self, frame=(0, 0, mview.width * 0.8, mview.height * 0.8), *args, **kwargs)
		
		self.val_btns = [] # Store value button field
		self.set_btns = [] # Store set button field
		self.set = 0 # Store index of current set button 
		self.ex_obj = ex_obj # Store reference to selected exercise
		
		# Datepicker to modify timestamp
		self.datepicker = ui.DatePicker()
		self.datepicker.background_color = "white"
		self.datepicker.action = self.datepicker_action
		self.add_subview(self.datepicker)
		
		# Show infolabel label
		self.lbl = ui.Label()
		self.lbl.background_color = "white"
		self.lbl.text = f"{self.ex_obj.group}: {self.ex_obj.name}  {self.datepicker.date:%Y-%m-%d %H:%M:%S}"
		self.lbl.alignment = ui.ALIGN_CENTER
		self.lbl.font = ('arial', 24)
		self.add_subview(self.lbl)
		
		# Textfield for value if applicable
		self.tf = ui.TextField()
		self.tf.background_color = "white"
		self.tf.text = str(ex_obj.default)
		self.tf.alignment = ui.ALIGN_CENTER
		self.tf.font = ('arial', 24)
		self.add_subview(self.tf)
		
		# Create set buttons (max. 3 sets per ecercise)
		for i in range(0,3):
			btn = ui.Button()
			btn.name = str(i)
			btn.background_color = "#fdffd8"
			btn.border_color = "black"
			btn.border_width = 2
			btn.title = "0"
			btn.action = self.btn_set_action
			self.set_btns.append(btn)
			self.add_subview(btn)
		# Highlight first set button (as selected)
		self.set_btns[0].background_color = "#faff8d"
		
		# Create value buttons
		for i in range(ex_obj.min, ex_obj.max + 1, ex_obj.step):
				btn = ui.Button(title = str(i))
				btn.background_color = "white"
				btn.corner_radius = 6
				btn.action = self.set_val
				self.val_btns.append(btn)
				self.add_subview(btn)
		
		# Abort logging
		self.btn_cancel = ui.Button()
		self.btn_cancel.background_color = "white"
		self.btn_cancel.corner_radius = 9
		self.btn_cancel.title = 'Cancel'
		self.btn_cancel.action = self.button_cancel_action
		self.add_subview(self.btn_cancel)
		
		# Save log to database
		self.btn_save = ui.Button()
		self.btn_save.background_color = "white"
		self.btn_save.corner_radius = 9
		self.btn_save.title = 'Save'
		self.btn_save.action = self.button_save_action
		self.add_subview(self.btn_save)
		
	def layout(self):
		
		# Get width and height of view to place subviews correctly
		w = self.width
		h = self.height
		
		# Calculate width and height of single set button
		set_btn_w_h = w * SET_BTN_W 
		# Calculate width of set button field (3 buttons, 2 spaces)
		s_btn_field_w = 3 * set_btn_w_h + 2 * H_SPACING
		# Calculate x position to center set button field in view
		x = w / 2 - s_btn_field_w / 2
		# Place set buttons in a row centered on screen
		for btn in self.set_btns:
				btn.frame = (x, h * SET_BTN_Y, set_btn_w_h, set_btn_w_h)
				x += (set_btn_w_h + H_SPACING)
		
		# Calculate width and height of single value button#
		val_btn_w_h = w * VAL_BTN_W
		# Calculate width of value button field
		n = len(self.val_btns)
		v_btn_field_w = n * val_btn_w_h + (n - 1) * H_SPACING
		# Calculate x position to center value button field in view
		x = w / 2 - v_btn_field_w / 2
		# Place value buttons in a row centered on screen below set buttons
		for btn in self.val_btns:
				btn.frame = (x, h * VAL_BTN_Y, val_btn_w_h, val_btn_w_h)
				x += (val_btn_w_h + H_SPACING)
		
		# Datepicker for selecting timestamp
		dpw = w * DATEPICKER_W
		dph = h * DATEPICKER_H
		self.datepicker.frame = ((w - dpw) / 2, h * DATEPICKER_Y, dpw, dph)
		
		# Textfield for value
		tfw = w * TEXT_W
		tfh = h * TEXT_H
		self.tf.frame = ((w - tfw) / 2, h * TEXT_Y, tfw, tfh)
		
		# Label for displaying selected exercise and timestamp
		lblw = w * INFOLBL_W
		lblh = h * INFOLBL_H
		self.lbl.frame = ((w - lblw) / 2, h * INFOLBL_Y, lblw, lblh)
		
		# Buttons Cancel and Save
		bw = w * CMDBTN_W
		bh = h * CMDBTN_H
		self.btn_cancel.frame = (MARGIN, h * CMDBTN_Y,  bw, bh)
		self.btn_save.frame = (w - bw - MARGIN, h * CMDBTN_Y, bw, bh)
	
	# Datepicker changed -> update info label
	def datepicker_action(self, sender):
		self.lbl.text = f"{self.ex_obj.group}: {self.ex_obj.name}  {self.datepicker.date:%Y-%m-%d %H:%M:%S}"
	
	# Value button clicked -> set value of corresponding set button
	def set_val(self, sender):
		self.set_btns[self.set].title = sender.title
	
	# Set button clicked -> Change focus
	def btn_set_action(self, sender):
		# Reset highlighting
		for btn in self.set_btns:
			btn.background_color = "#fdffd8"
		# Higlight newly selected button
		sender.background_color = "#faff8d"
		self.set = int(sender.name)
		
	# Save selected exercise with timesramp and data from SaveView
	def button_save_action(self, sender):
		db = DBExercise("mytest.sqlite3")
		timestamp = f"{self.datepicker.date:%Y-%m-%d %H:%M:%S}"
		set1 = self.set_btns[0].title
		set2 = self.set_btns[1].title
		set3 = self.set_btns[2].title
		val = int(self.tf.text)
		db.insert_data(timestamp, self.ex_obj.name, val, int(set1), int(set2),int(set3))
		db.dump_data()
		self.close()
		pass
	
	# Abort logging and go back to top level of table view
	def button_cancel_action(self, sender):
		self.close()
		print(sender.title)
		pass


w, h = ui.get_screen_size()
v = ui.View(name = 'Log exercise', bg_color = 'lightyellow', frame = (0,0,w,h))

#def back_action(sender):
		#print("Clicked on back button")
		
# Create back button
#lb = ui.ButtonItem()
#lb.tint_color = (1.0, .52, .0, 1.0)
#lb.title = 'Back'
#lb.enabled = True
#lb.action = back_action


#left_button_items = [lb]

vdel = tvDelegate(v)

# Create table view for displaying groups and exercises
tv = ui.TableView()
tv.name = 'tv_ex'
tv.flex = "wb"
tv.bg_color = "lightblue"
tv.frame = v.frame
tv.delegate = tv.data_source = vdel
v.add_subview(tv)

#v.left_button_items = [lb]
v.present('full screen')
