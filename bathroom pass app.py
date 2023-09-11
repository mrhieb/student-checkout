from guizero import *
import csv
import time
import datetime
import pandas as pd
'''
Next steps....

If a student is out of the classroom, they can not go out again.
If they return and they didn't check-out, ask if they are tardy.  Tell them to share their pass
with the teacher if they are not tardy.


'''
starting = 0
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
students_out_counter = 0
student_out_time_counter = 0

def reset_screen():
    combo.visible = True
    disk_number_text.value =''
    name_space.value =''
    checkout_button.visible = False
    checkin_button.visible = False
    welcome_text.value = ''
    bathroom.visible = False
    drink.visible = False
    nurse.visible = False
    other.visible = False
    dean.visible = False
    locker.visible = False


def record_data(student_list):
    #We want to record the information on our csv file so we can look at the data later.  
    with open('StudentsOut.csv', 'a') as csv_file:
        csv_appender = csv.writer(csv_file)
        csv_appender.writerow(student_list)
        
def specific_names():
    #Check times to determine class period
    check_times()
    global class_number
    global disk_number
    global combo
    global current_name
    disk_number = int(combo.value)
    

    SHEET_ID = '1vi5lbXkMNC73IXJ-XXqcBwa88NDXdL9dQwtZIAEb-oQ'
    #SHEET_NAME is the name of the tab
    SHEET_NAME = 'Names'
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    df = pd.read_csv(url)
    #Transposes the data
    df = df.T
    name_space.value = df._get_value(class_number, disk_number-1)
    temp_out_of_class.append(df._get_value(class_number, disk_number-1))
    current_name = df._get_value(class_number, disk_number-1)
    checkout_button.visible = True
    checkin_button.visible = True


def check_times():
    global class_number
    global disk_number
    global combo
    if datetime.time(7, 30, 0)<datetime.datetime.now().time()<datetime.time(8, 39, 0):
        class_number = "Period 1"
    elif datetime.time(8, 39, 0)<datetime.datetime.now().time()<datetime.time(9, 30, 0):
        class_number = "Period 2"
    elif datetime.time(9, 30, 0)<datetime.datetime.now().time()<datetime.time(10, 23, 0):
        class_number = "Period 3"
    elif datetime.time(10, 23, 0)<datetime.datetime.now().time()<datetime.time(11, 16, 0):
        class_number = "Period 4"
    elif datetime.time(11, 50, 0)<datetime.datetime.now().time()<datetime.time(12, 39, 0):
        class_number = "Period 5"
    elif datetime.time(12, 39, 0)<datetime.datetime.now().time()<datetime.time(13, 32, 0):
        class_number = "Period 6"
    elif datetime.time(13,32,0)<datetime.datetime.now().time():
        class_number = "Period 7"
    
    disk_number_text.value = 'Is this you?'
    combo.visible = True
    print(class_number)
    
def checkout_options():
    bathroom.visible = True
    drink.visible = True
    nurse.visible = True
    other.visible = True
    locker.visible = True
    dean.visible = True

def welcome_back():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text
    global out_of_class1, out_of_class2, out_of_class3, out_of_class4, out_of_class5
    global students_out_counter, app
    end_time = time.time()
    total_time = 0
    if len(out_of_class1) != 0:
        if current_name == out_of_class1[0]:
            total_time = end_time-out_of_class1[1]

            out_of_class1.append(total_time)
            record_data(out_of_class1)
            aoc1_text.destroy()
            out_of_class1 = []
            


    min_total_time = total_time//60
    total_time = total_time % 60
    total_time = round(total_time, 1)
    

    if students_out_counter%12==0:
        s1_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1
    elif students_out_counter%12==1:
        s2_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1
    elif students_out_counter%12==2:
        s3_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1 
    elif students_out_counter%12==3:
        s4_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1
    elif students_out_counter%12==4:
        s5_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1 
    elif students_out_counter%12==5:
        s6_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1 
                        
    elif students_out_counter%12==6:
        s7_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1
    elif students_out_counter%12==7:
        s8_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1
    elif students_out_counter%12==8:
        s9_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1
    elif students_out_counter%12==9:
        s10_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1
    elif students_out_counter%12==10:
        s11_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1 
    elif students_out_counter%12==11:
        s12_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
        students_out_counter += 1 



    info(text = 'Welcome back to Class.  You were gone for ...  '+str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds', title = 'Returning Student')
    welcome_text.value = 'Welcome back to class!!!'
    welcome_text.text_size = 40
    welcome_text.text_color = 'white'
    app.bg = (30, 200, 30)
    app.after(1000, reset_screen)
    
    
    
def going_bathroom():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text, app
    global starting
    global student_out_time_counter
    start_time = time.time()
    app.bg = (200, 30, 30)
    starting = time.strftime('%H:%M')
    if len(out_of_class1) != 0:# and len(out_of_class2) != 0 and len(out_of_class3) != 0  and len(out_of_class4) != 0  and len(out_of_class5) != 0 :
        app.warn(title = 'Student Checkout Exeeded Limit', text = 'Wait until students return before leaving the classroom')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('bathroom')
        aoc1_text = Text(student_out_box_left, current_name+ '----   bathroom')
        
    check_students_out_time()
    reset_screen()
def check_students_out_time():
    global starting
    global current_name
    global student_out_time_counter
    print(student_out_time_counter)
    if student_out_time_counter%12 == 0:
        s1_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter +=1
    elif student_out_time_counter%12 == 1:
        s2_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter +=1
    elif student_out_time_counter%12 == 2:
        s3_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter +=1
    elif student_out_time_counter%12 == 3:
        s4_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter += 1
    elif student_out_time_counter%12 == 4:
        s5_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter +=1
    elif student_out_time_counter%12 == 5:
        s6_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter +=1
    elif student_out_time_counter%12 == 6:
        s7_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter +=1
    elif student_out_time_counter%12 == 7:
        s8_time_text.value =  current_name + '   ' + str(starting)
        student_out_time_counter +=1
    elif student_out_time_counter%12 == 8:
        s9_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter +=1
    elif student_out_time_counter%12 == 9:
        s10_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter +=1
    elif student_out_time_counter%12 == 10:
        s11_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter += 1
    elif student_out_time_counter%12 == 11:
        s12_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter += 1
    else:
        clear_students_out()
        s1_time_text.value = current_name + '   ' + str(starting)
        student_out_time_counter += 1
        

def going_drink():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text, app
    start_time = time.time()
    app.bg = (200, 30, 30)
    starting = time.strftime('%H:%M')
    if len(out_of_class1) != 0:# and len(out_of_class2) != 0 and len(out_of_class3) != 0  and len(out_of_class4) != 0  and len(out_of_class5) != 0 :
        app.warn(title = 'Student Checkout Exeeded Limit', text = 'Wait until students return before leaving the classroom')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('drink')
        aoc1_text = Text(student_out_box_left, current_name+ '----   drink')

    check_students_out_time()
    reset_screen()

def going_nurse():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text, app
    start_time = time.time()
    app.bg = (200, 30, 30)
    starting = time.strftime('%H:%M')
    if len(out_of_class1) != 0:
        app.warn(title = 'Student Checkout Exeeded Limit', text = 'Wait until students return before leaving the classroom')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('nurse')
        aoc1_text = Text(student_out_box_left, current_name+ '----   nurse')

    check_students_out_time()
    reset_screen()
def going_locker():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text, app
    start_time = time.time()
    app.bg = (200, 30, 30)
    starting = time.strftime('%H:%M')
    if len(out_of_class1) != 0:
        app.warn(title = 'Student Checkout Exeeded Limit', text = 'Wait until students return before leaving the classroom')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('locker')
        aoc1_text = Text(student_out_box_left, current_name+ '----   locker')

    check_students_out_time()
    reset_screen()
def going_dean():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text, app
    app.bg = (200, 30, 30)
    start_time = time.time()
    starting = time.strftime('%H:%M')
    if len(out_of_class1) != 0: 
        app.warn(title = 'Student Checkout Exeeded Limit', text = 'Wait until students return before leaving the classroom')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('dean')
        aoc1_text = Text(student_out_box_left, current_name+ '----   dean')

    check_students_out_time()
    reset_screen()
def going_other():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text, app
    app.bg = (200, 30, 30)
    start_time = time.time()
    starting = time.strftime('%H:%M')
    if len(out_of_class1) != 0:
        app.warn(title = 'Student Checkout Exeeded Limit', text = 'Wait until students return before leaving the classroom')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('other')
        aoc1_text = Text(student_out_box_left, current_name+ '----   other')

    check_students_out_time()
    reset_screen()
    
def out_students():
    student_out_box_right.visible = True
def student_reason():
    student_reasons.visible = True
def exit():
    app.destroy()
def clear_students_out():
    s1_text.value = ''
    s2_text.value = ''
    s3_text.value = ''
    s4_text.value = ''
    s5_text.value = ''
    s6_text.value = ''
    s7_text.value = ''
    s8_text.value = ''
    s9_text.value = ''
    s10_text.value = ''
    s11_text.value = ''
    s12_text.value = ''
    s13_text.value = ''
    s14_text.value = ''
app = App(title = 'Pass collector', bg = (30, 200, 30))
MenuBar(app, toplevel = ['Update'], options = [[['Time to Return', out_students], ['Students Leaving Times', student_reason], ['Exit', exit]]])
app.full_screen = True
hour_text = Text(app, text = 'Pick your disk number', color = 'white')
hour_text.text_size = 80
box = Box(app, layout = 'grid')


combo=Combo(app, options =[0,1,2, 3, 4,5, 6, 7, 8, 9,
                               10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                               20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                               30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                               40], command = specific_names)
combo.text_size = 8
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
locker = PushButton(checkout_options_box, text = 'Locker', grid = [4,1], command = going_locker)
dean = PushButton(checkout_options_box, text = 'Dean', grid = [5,1], command = going_dean)
other = PushButton(checkout_options_box, text = 'Other', grid = [6,1], command = going_other)

bathroom.bg = 'white'
drink.bg = 'white'
nurse.bg = 'white'
other.bg = 'white'
dean.bg = 'white'
locker.bg = 'white'
dean.visible = False
locker.visible = False
bathroom.visible = False
drink.visible = False
nurse.visible = False
other.visible = False
students_out_box = Box(app, border = 0, width = 1200, height = 400, layout = 'grid')
students_out_box.bg = (30, 200, 30)
Picture(students_out_box, image = 'charger.png', grid = [1,1])
Text(students_out_box, width = 10, grid = [2,1])
student_out_box_left = Box(students_out_box, border = 2, height = 400,width = 400, grid = [3,1] )
Text(students_out_box, width = 30, grid = [4,1])
student_out_box_left.bg = 'white'
student_out_box_right = Window(app, height = 400,width = 400 )
student_out_list = Text(student_out_box_left, 'Students Out of Classroom', width = 45)
student_waiting_list = Text(student_out_box_right, 'Students Checked-In', width = 45)
s1_text = Text(student_out_box_right)
s2_text = Text(student_out_box_right)
s3_text = Text(student_out_box_right)
s4_text = Text(student_out_box_right)
s5_text = Text(student_out_box_right)
s6_text = Text(student_out_box_right)
s7_text = Text(student_out_box_right)
s8_text = Text(student_out_box_right)
s9_text = Text(student_out_box_right)
s10_text = Text(student_out_box_right)
s11_text = Text(student_out_box_right)
s12_text = Text(student_out_box_right)
s13_text = Text(student_out_box_right)
s14_text = Text(student_out_box_right)

student_out_box_right.visible = False
student_reasons = Window(app, height = 400, width = 400)
student_reasons_out = Text(student_reasons, 'Student Reasons', width = 45)
s1_time_text = Text(student_reasons)
s2_time_text = Text(student_reasons)
s3_time_text = Text(student_reasons)
s4_time_text = Text(student_reasons)
s5_time_text = Text(student_reasons)
s6_time_text = Text(student_reasons)
s7_time_text = Text(student_reasons)
s8_time_text = Text(student_reasons)
s9_time_text = Text(student_reasons)
s10_time_text = Text(student_reasons)
s11_time_text = Text(student_reasons)
s12_time_text = Text(student_reasons)
s13_time_text = Text(student_reasons)
s14_time_text = Text(student_reasons)
student_reasons.visible = False
app.display()

