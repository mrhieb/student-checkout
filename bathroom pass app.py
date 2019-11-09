from guizero import *
import csv
import time
'''
Next steps....

Limit the number of students leaving.
Properly clear the screen 3 seconds after they choose a location or report
back to class.  If a student returns back to class, take their name off the gui.


'''
class_number = 0
disk_number = 0
combo = ''
temp_out_of_class = []
out_of_class1=[]
out_of_class2 = []
out_of_class3 = []
out_of_class4 = []
out_of_class5 = []
current_name = ''
current_place = ''
current_start_time = 0
aoc1_text = ''
aoc2_text = ''
aoc3_text = ''
aoc4_text = ''
aoc5_text = ''

def reset_screen():
    combo.visible = False
    disk_number_text.value =''
    name_space.value =''
    checkout_button.visible = False
    checkin_button.visible = False
    welcome_text.value = ''
    bathroom.visible = False
    drink.visible = False
    nurse.visible = False
    other.visible = False
    hour1.bg = 'white'
    hour2.bg = 'white'
    hour3.bg = 'white'
    hour4.bg = 'white'
    hour5.bg = 'white'
    hour6.bg = 'white'

def record_data(student_list):
    with open('StudentsOut.csv', 'a') as csv_file:
        csv_appender = csv.writer(csv_file)
        csv_appender.writerow(student_list)
        
def specific_names():
    global class_number
    global disk_number
    global combo
    global current_name
    disk_number = int(combo.value)
    with open('StudentNames.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count == class_number:
                name_space.value =row[disk_number]
                print(row[disk_number])
                
                
                temp_out_of_class.append(row[disk_number])
                current_name = row[disk_number]
                '''
                if len(out_of_class1)==0:
                    out_of_class1.append(row[disk_number])
                
                elif len(out_of_class2) == 0:
                    out_of_class2.append(row[disk_number])
                elif len(out_of_class3) == 0:
                    out_of_class3.append(row[disk_number])
                elif len(out_of_class4) == 0:
                    out_of_class4.append(row[disk_number])
                elif len(out_of_class2) == 0:
                    out_of_class5.append(row[disk_number])
                '''
                checkout_button.visible = True
                checkin_button.visible = True
            line_count+=1
        
def first_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    hour1.bg = 'white'
    hour2.bg = 'white'
    hour3.bg = 'white'
    hour4.bg = 'white'
    hour5.bg = 'white'
    hour6.bg = 'white'
    class_number = 0
    hour1.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True
    


def second_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    class_number = 1
    hour1.bg = 'white'
    hour2.bg = 'white'
    hour3.bg = 'white'
    hour4.bg = 'white'
    hour5.bg = 'white'
    hour6.bg = 'white'
    hour2.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True
def third_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    class_number = 2
    hour1.bg = 'white'
    hour2.bg = 'white'
    hour3.bg = 'white'
    hour4.bg = 'white'
    hour5.bg = 'white'
    hour6.bg = 'white'
    hour3.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True
def fourth_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    class_number = 3
    hour1.bg = 'white'
    hour2.bg = 'white'
    hour3.bg = 'white'
    hour4.bg = 'white'
    hour5.bg = 'white'
    hour6.bg = 'white'
    hour4.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True
def fifth_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    class_number = 4
    hour1.bg = 'white'
    hour2.bg = 'white'
    hour3.bg = 'white'
    hour4.bg = 'white'
    hour5.bg = 'white'
    hour6.bg = 'white'
    hour5.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True
def sixth_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    class_number = 5
    hour1.bg = 'white'
    hour2.bg = 'white'
    hour3.bg = 'white'
    hour4.bg = 'white'
    hour5.bg = 'white'
    hour6.bg = 'white'
    hour6.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True

def checkout_options():
    bathroom.visible = True
    drink.visible = True
    nurse.visible = True
    other.visible = True

def welcome_back():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text
    end_time = time.time()
    total_time = end_time-out_of_class1[1]
    if current_name == out_of_class1[0]:
        print('yes1')
        out_of_class1.append(total_time)
        record_data(out_of_class1)
        aoc1_text.destroy()
        
    elif current_name == out_of_class2[0]:
        print('yes2')
        out_of_class2.append(total_time)
        record_data(out_of_class2)
    elif current_name == out_of_class3[0]:
        print('yes3')
        out_of_class3.append(total_time)
        record_data(out_of_class3)
    elif current_name == out_of_class4[0]:
        print('yes4')
        out_of_class4.append(total_time)
        record_data(out_of_class4)
    elif current_name == out_of_class5[0]:
        print('yes5')
        out_of_class5.append(total_time)
        record_data(out_of_class5)
    out_of_class1.append(total_time)
    welcome_text.value = 'Welcome back to class!!!'
    welcome_text.text_size = 40
    welcome_text.text_color = 'white'
    #reset_screen()
    
    
    
def going_bathroom():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text
    start_time = time.time()
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('bathroom')
        aoc1_text = Text(student_out_box_left, current_name+ '----   bathroom')
    elif len(out_of_class2) == 0:
        out_of_class2.append(current_name)
        out_of_class2.append(start_time)
        out_of_class2.append('bathroom')
        aoc2_text = Text(student_out_box_left, current_name+ '----   bathroom')
    elif len(out_of_class3) == 0:
        out_of_class3.append(current_name)
        out_of_class3.append(start_time)
        out_of_class3.append('bathroom')
        aoc3_text = Text(student_out_box_left, current_name+ '----   bathroom')
    elif len(out_of_class4) == 0:
        out_of_class4.append(current_name)
        out_of_class4.append(start_time)
        out_of_class4.append('bathroom')
        aoc4_text = Text(student_out_box_left, current_name+ '----   bathroom')
    elif len(out_of_class5) == 0:
        out_of_class5.append(current_name)
        out_of_class5.append(start_time)
        out_of_clas5.append('bathroom')
        aoc5_text = Text(student_out_box_left, current_name+ '----   bathroom')
    
    reset_screen()


def going_drink():
    start_time = time.time()
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('drink')
    elif len(out_of_class2) == 0:
        out_of_class2.append(current_name)
        out_of_class2.append(start_time)
        out_of_class2.append('drink')
    elif len(out_of_class3) == 0:
        out_of_class3.append(current_name)
        out_of_class3.append(start_time)
        out_of_class3.append('drink')
    elif len(out_of_class4) == 0:
        out_of_class4.append(current_name)
        out_of_class4.append(start_time)
        out_of_class4.append('drink')
    elif len(out_of_class5) == 0:
        out_of_class5.append(current_name)
        out_of_class5.append(start_time)
        out_of_clas5.append('drink')
    Text(student_out_box_left, current_name+'----   drink')
    reset_screen()

def going_nurse():
    start_time = time.time()
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('nurse')
    elif len(out_of_class2) == 0:
        out_of_class2.append(current_name)
        out_of_class2.append(start_time)
        out_of_class2.append('nurse')
    elif len(out_of_class3) == 0:
        out_of_class3.append(current_name)
        out_of_class3.append(start_time)
        out_of_class3.append('nurse')
    elif len(out_of_class4) == 0:
        out_of_class4.append(current_name)
        out_of_class4.append(start_time)
        out_of_class4.append('nurse')
    elif len(out_of_class5) == 0:
        out_of_class5.append(current_name)
        out_of_class5.append(start_time)
        out_of_clas5.append('nurse')
    Text(student_out_box_left, current_name+'Go to----   nurse')
    reset_screen()

def going_other():
    start_time = time.time()
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('other')
    elif len(out_of_class2) == 0:
        out_of_class2.append(current_name)
        out_of_class2.append(start_time)
        out_of_class2.append('other')
    elif len(out_of_class3) == 0:
        out_of_class3.append(current_name)
        out_of_class3.append(start_time)
        out_of_class3.append('other')
    elif len(out_of_class4) == 0:
        out_of_class4.append(current_name)
        out_of_class4.append(start_time)
        out_of_class4.append('other')
    elif len(out_of_class5) == 0:
        out_of_class5.append(current_name)
        out_of_class5.append(start_time)
        out_of_clas5.append('other')
    Text(student_out_box_left, current_name+'----   other')
    reset_screen()
    

app = App(title = 'Pass collector', bg = (200, 30, 30))
app.full_screen = True
hour_text = Text(app, text = 'Click on your hour')
hour_text.text_size = 80
box = Box(app, layout = 'grid')
hour1 = PushButton(box, text = 'Hour 1', grid = [0,0], command = first_hour)
hour2 = PushButton(box, text = 'Hour 2', grid = [1,0], command = second_hour)
hour3 = PushButton(box, text = 'Hour 3', grid = [2,0], command = third_hour)
hour4 = PushButton(box, text = 'Hour 4', grid = [0,1], command = fourth_hour)
hour5 = PushButton(box, text = 'Hour 5', grid = [1,1], command = fifth_hour)
hour6 = PushButton(box, text = 'Hour 6', grid = [2,1], command = sixth_hour)
hour1.bg = 'white'
hour2.bg = 'white'
hour3.bg = 'white'
hour4.bg = 'white'
hour5.bg = 'white'
hour6.bg = 'white'

combo=Combo(app, options =[0,1,2, 3, 4,5, 6, 7, 8, 9,
                               10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                               20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                               30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                               40], command = specific_names)
combo.visible = False
disk_number_text = Text(app, '')
disk_number_text.text_size = 18
name_space = Text(app, '')
name_space.text_size = 30
checkout_checkin_box = Box(app, layout = 'grid')
checkout_button = PushButton(checkout_checkin_box, text = "Checkout", grid = [1,1], command = checkout_options)
checkin_button = PushButton(checkout_checkin_box, text = "Checkin", grid = [2,1], command = welcome_back)

checkout_button.bg = 'white'
checkin_button.bg = 'white'
checkout_button.visible = False
checkin_button.visible = False
welcome_text = Text(app, text = '')
checkout_options_box = Box(app, layout = 'grid')
bathroom = PushButton(checkout_options_box, text = 'Bathroom', grid = [1,1], command = going_bathroom)
drink = PushButton(checkout_options_box, text= 'Drink', grid = [2,1], command = going_drink)
nurse = PushButton(checkout_options_box, text = 'Nurse', grid = [3,1], command = going_nurse)
other = PushButton(checkout_options_box, text = 'Other', grid = [4,1], command = going_other)
bathroom.bg = 'white'
drink.bg = 'white'
nurse.bg = 'white'
other.bg = 'white'
bathroom.visible = False
drink.visible = False
nurse.visible = False
other.visible = False
students_out_box = Box(app, layout = 'grid', border = 1, width = 800, height = 400)
students_out_box.bg = 'white'
student_out_box_left = Box(students_out_box, border = 2, grid = [1,1], height = 400,width = 400 )
student_out_box_right = Box(students_out_box, border = 2, grid = [2,1], height = 400,width = 400 )
student_out_list = Text(student_out_box_left, 'Students Out of Classroom', width = 45)
student_waiting_list = Text(student_out_box_right, 'Students Waiting', width = 45)
app.display()
