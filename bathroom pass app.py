from guizero import *
import csv
import time
import datetime
'''
Next steps....
Limit the number of students leaving.
If a student is out of the classroom, they can not go out again.
If they return and they didn't check-out, ask if they are tardy.  Tell them to share their pass
with the teacher if they are not tardy.
Create a drop down menu to see the times of the last 10 students.
Figure out what to do with kids that do not sign back in .  Maybe a teacher adjustment with password.



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
    with open('StudentsOut.csv', 'a') as csv_file:
        csv_appender = csv.writer(csv_file)
        csv_appender.writerow(student_list)
        
def specific_names():
    check_times()
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
                temp_out_of_class.append(row[disk_number])
                current_name = row[disk_number]
                checkout_button.visible = True
                checkin_button.visible = True
            line_count+=1

def check_times():
    global class_number
    global disk_number
    global combo
    '''
    if int(time.strftime('%H'))>=7:
        if int(time.strftime('%M'))>30:
            class_number == 0
    elif int(time.strftime('%H'))<=8:
        if int(time.strftime('%M'))<37:
            class_number == 0
    elif int(time.strftime('%H'))>=8:
        if int(time.strftime('%M'))>37:
            class_number == 1
    elif int(time.strftime('%H'))<=9:
        if int(time.strftime('%M'))>30:
            class_number == 1
    elif int(time.strftime('%H'))>=9:
        if int(time.strftime('%M'))>30:
            class_number == 2
    elif int(time.strftime('%H'))<=10:
        if int(time.strftime('%M'))<23:
            class_number == 2
    if int(time.strftime('%H'))>=10:
        if int(time.strftime('%M'))>23:
            class_number == 3
    elif int(time.strftime('%H'))<=11:
        if int(time.strftime('%M'))<16:
            class_number == 3
    if int(time.strftime('%H'))>=11:
        if int(time.strftime('%M'))>45:
            class_number == 4
    elif int(time.strftime('%H'))<=12:
        if int(time.strftime('%M'))<39:
            class_number == 4
    if int(time.strftime('%H'))>=12:
        if int(time.strftime('%M'))>39:
            class_number == 5
    elif int(time.strftime('%H'))<=1:
        if int(time.strftime('%M'))>32:
            class_number == 5
    if int(time.strftime('%H'))>=1:
        if int(time.strftime('%M'))>32:
            class_number == 6
    elif int(time.strftime('%H'))<=19:
        if int(time.strftime('%M'))<25:
            class_number == 6
    '''
    if datetime.time(7, 30, 0)<datetime.datetime.now().time()<datetime.time(8, 39, 0):
        class_number = 0
    elif datetime.time(8, 39, 0)<datetime.datetime.now().time()<datetime.time(9, 30, 0):
        class_number = 1
    elif datetime.time(9, 30, 0)<datetime.datetime.now().time()<datetime.time(10, 23, 0):
        class_number = 2
    elif datetime.time(10, 23, 0)<datetime.datetime.now().time()<datetime.time(11, 16, 0):
        class_number = 3
    elif datetime.time(11, 50, 0)<datetime.datetime.now().time()<datetime.time(12, 39, 0):
        class_number = 4
    elif datetime.time(12, 39, 0)<datetime.datetime.now().time()<datetime.time(13, 32, 0):
        class_number = 5
    elif datetime.time(13,32,0)<datetime.datetime.now().time()<datetime.time(2,25,0):
        class_number = 6
    print(class_number)
    disk_number_text.value = 'Is this you?'
    combo.visible = True
def first_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
##    hour1.bg = 'white'
##    hour2.bg = 'white'
##    hour3.bg = 'white'
##    hour4.bg = 'white'
##    hour5.bg = 'white'
##    hour6.bg = 'white'
    class_number = 0
##    hour1.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True
    


def second_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    class_number = 1
##    hour1.bg = 'white'
##    hour2.bg = 'white'
##    hour3.bg = 'white'
##    hour4.bg = 'white'
##    hour5.bg = 'white'
##    hour6.bg = 'white'
##    hour2.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True
def third_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    class_number = 2
##    hour1.bg = 'white'
##    hour2.bg = 'white'
##    hour3.bg = 'white'
##    hour4.bg = 'white'
##    hour5.bg = 'white'
##    hour6.bg = 'white'
##    hour3.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True
def fourth_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    class_number = 3
##    hour1.bg = 'white'
##    hour2.bg = 'white'
##    hour3.bg = 'white'
##    hour4.bg = 'white'
##    hour5.bg = 'white'
##    hour6.bg = 'white'
##    hour4.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True
def fifth_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    class_number = 4
##    hour1.bg = 'white'
##    hour2.bg = 'white'
##    hour3.bg = 'white'
##    hour4.bg = 'white'
##    hour5.bg = 'white'
##    hour6.bg = 'white'
##    hour5.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True
def sixth_hour():
    global class_number
    global disk_number
    global combo
    temp_out_of_class = []
    class_number = 5
##    hour1.bg = 'white'
##    hour2.bg = 'white'
##    hour3.bg = 'white'
##    hour4.bg = 'white'
##    hour5.bg = 'white'
##    hour6.bg = 'white'
##    hour6.bg = 'green'
    disk_number_text.value = 'What is your disk number?'
    combo.visible = True

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
    end_time = time.time()
    total_time = 0
    if len(out_of_class1) != 0:
        if current_name == out_of_class1[0]:
            total_time = end_time-out_of_class1[1]

            out_of_class1.append(total_time)
##            Text(student_out_box_right, text = current_name + '   ' + str(total_time))
            record_data(out_of_class1)
            aoc1_text.destroy()
            out_of_class1 = []
    if len(out_of_class2)!=0:
        if current_name == out_of_class2[0]:
            total_time = end_time-out_of_class2[1]
            out_of_class2.append(total_time)
##            Text(student_out_box_right, text = current_name + '   ' + str(total_time))
            record_data(out_of_class2)
            aoc2_text.destroy()
            out_of_class2 = []
    if len(out_of_class3)!=0:
        if current_name == out_of_class3[0]:
            total_time = end_time-out_of_class3[1]
            
            out_of_class3.append(total_time)
            record_data(out_of_class3)
##            Text(student_out_box_right, text = current_name + '   ' + str(total_time))
            aoc3_text.destroy()
            out_of_class3 = []
    if len(out_of_class4)!=0:
        if current_name == out_of_class4[0]:
            total_time = end_time-out_of_class4[1]
            
            out_of_class4.append(total_time)
##            Text(student_out_box_right, text = current_name + '   ' + str(total_time))
            record_data(out_of_class4)
            aoc4_text.destroy()
            out_of_class4 = []
    if len(out_of_class5)!=0:
        if current_name == out_of_class5[0]:
            total_time = end_time-out_of_class5[1]
            
            out_of_class5.append(total_time)
            record_data(out_of_class5)
##            Text(student_out_box_right, text = current_name + '   ' + str(total_time))
            aoc5_text.destroy()
            out_of_class5 = []
##    else:
##        not_checked_out = app.yesno('Not checked out', 'Are you tardy?')
##        if not_checked_out:
##            print('You are tardy by 5 minutes')
##        else:
##            print('Tell your teacher why you are checking in without checking out.')
    min_total_time = total_time//60
    total_time = total_time % 60
    total_time = round(total_time, 1)
    if len(s1_text.value) == 0:
        s1_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s2_text.value) == 0:
        s2_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s3_text.value) == 0:
        s3_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s4_text.value) == 0:
        s4_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s5_text.value) == 0:
        s5_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s6_text.value) == 0:
        s6_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s7_text.value) == 0:
        s7_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s8_text.value) == 0:
        s8_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s9_text.value) == 0:
        s9_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s10_text.value) == 0:
        s10_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s11_text.value) == 0:
        s11_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    elif len(s12_text.value) == 0:
        s12_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'
    else:
        clear_students_out()
        s1_text.value = current_name + '   ' + str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds'


    info(text = 'Welcome back to Class.  You were gone for ...  '+str(min_total_time)+ 'minutes and ' + str(total_time) + ' seconds', title = 'Returning Student')
    welcome_text.value = 'Welcome back to class!!!'
    welcome_text.text_size = 40
    welcome_text.text_color = 'white'
    app.after(1000, reset_screen)
    
    
    
def going_bathroom():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text
    global starting
    start_time = time.time()
    starting = time.strftime('%H:%M')

    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('bathroom')
        aoc1_text = Text(student_out_box_left, current_name+ '----   bathroom')
        Text(student_reasons, current_name + ' ' + starting)
    elif len(out_of_class2) == 0:
        out_of_class2.append(current_name)
        out_of_class2.append(start_time)
        out_of_class2.append('bathroom')
        aoc2_text = Text(student_out_box_left, current_name+ '----   bathroom')
        Text(student_reasons, current_name + ' ' + starting)
    elif len(out_of_class3) == 0:
        out_of_class3.append(current_name)
        out_of_class3.append(start_time)
        out_of_class3.append('bathroom')
        aoc3_text = Text(student_out_box_left, current_name+ '----   bathroom')
        Text(student_reasons, current_name + ' ' + starting)
    elif len(out_of_class4) == 0:
        out_of_class4.append(current_name)
        out_of_class4.append(start_time)
        out_of_class4.append('bathroom')
        aoc4_text = Text(student_out_box_left, current_name+ '----   bathroom')
    elif len(out_of_class5) == 0:
        out_of_class5.append(current_name)
        out_of_class5.append(start_time)
        out_of_class5.append('bathroom')
        aoc5_text = Text(student_out_box_left, current_name+ '----   bathroom')
        Text(student_reasons, current_name + ' ' + starting)
    check_students_out_time()
    reset_screen()
def check_students_out_time():
    global starting
    global current_name
    if len(s1_time_text.value) == 0:
        s1_time_text.value = current_name + '   ' + starting
    elif len(s2_time_text.value) == 0:
        s2_time_text.value = current_name + '   ' + starting
    elif len(s3_text.value) == 0:
        s3_time_text.value = current_name + '   ' + starting
    elif len(s4_text.value) == 0:
        s4_time_text.value = current_name + '   ' + starting
    elif len(s5_text.value) == 0:
        s5_time_text.value = current_name + '   ' + starting
    elif len(s6_text.value) == 0:
        s6_time_text.value = current_name + '   ' + starting
    elif len(s7_text.value) == 0:
        s7_time_text.value = current_name + '   ' + starting
    elif len(s8_text.value) == 0:
        s8_time_text.value =  current_name + '   ' + starting
    elif len(s9_text.value) == 0:
        s9_time_text.value = current_name + '   ' + starting
    elif len(s10_text.value) == 0:
        s10_time_text.value = current_name + '   ' + starting
    elif len(s11_text.value) == 0:
        s11_time_text.value = current_name + '   ' + starting
    elif len(s12_text.value) == 0:
        s12_time_text.value = current_name + '   ' + starting
    else:
        clear_students_out()
        s1_time_text.value = current_name + '   ' + starting

def going_drink():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text
    start_time = time.time()
    starting = time.strftime('%H:%M')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('drink')
        aoc1_text = Text(student_out_box_left, current_name+ '----   drink')
    elif len(out_of_class2) == 0:
        out_of_class2.append(current_name)
        out_of_class2.append(start_time)
        out_of_class2.append('drink')
        aoc2_text = Text(student_out_box_left, current_name+ '----   drink')
    elif len(out_of_class3) == 0:
        out_of_class3.append(current_name)
        out_of_class3.append(start_time)
        out_of_class3.append('drink')
        aoc3_text = Text(student_out_box_left, current_name+ '----   drink')
    elif len(out_of_class4) == 0:
        out_of_class4.append(current_name)
        out_of_class4.append(start_time)
        out_of_class4.append('drink')
        aoc4_text = Text(student_out_box_left, current_name+ '----   drink')
    elif len(out_of_class5) == 0:
        out_of_class5.append(current_name)
        out_of_class5.append(start_time)
        out_of_clas5.append('drink')
        aoc5_text = Text(student_out_box_left, current_name+ '----   drink')
    
    reset_screen()

def going_nurse():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text
    start_time = time.time()
    starting = time.strftime('%H:%M')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('nurse')
        aoc1_text = Text(student_out_box_left, current_name+ '----   nurse')
    elif len(out_of_class2) == 0:
        out_of_class2.append(current_name)
        out_of_class2.append(start_time)
        out_of_class2.append('nurse')
        aoc2_text = Text(student_out_box_left, current_name+ '----   nurse')
    elif len(out_of_class3) == 0:
        out_of_class3.append(current_name)
        out_of_class3.append(start_time)
        out_of_class3.append('nurse')
        aoc2_text = Text(student_out_box_left, current_name+ '----   nurse')
    elif len(out_of_class4) == 0:
        out_of_class4.append(current_name)
        out_of_class4.append(start_time)
        out_of_class4.append('nurse')
        aoc4_text = Text(student_out_box_left, current_name+ '----   nurse')
    elif len(out_of_class5) == 0:
        out_of_class5.append(current_name)
        out_of_class5.append(start_time)
        out_of_clas5.append('nurse')
        aoc5_text = Text(student_out_box_left, current_name+ '----   nurse')
    
    reset_screen()
def going_locker():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text
    start_time = time.time()
    starting = time.strftime('%H:%M')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('locker')
        aoc1_text = Text(student_out_box_left, current_name+ '----   locker')
    elif len(out_of_class2) == 0:
        out_of_class2.append(current_name)
        out_of_class2.append(start_time)
        out_of_class2.append('locker')
        aoc2_text = Text(student_out_box_left, current_name+ '----   locker')
    elif len(out_of_class3) == 0:
        out_of_class3.append(current_name)
        out_of_class3.append(start_time)
        out_of_class3.append('locker')
        aoc2_text = Text(student_out_box_left, current_name+ '----   locker')
    elif len(out_of_class4) == 0:
        out_of_class4.append(current_name)
        out_of_class4.append(start_time)
        out_of_class4.append('locker')
        aoc4_text = Text(student_out_box_left, current_name+ '----   locker')
    elif len(out_of_class5) == 0:
        out_of_class5.append(current_name)
        out_of_class5.append(start_time)
        out_of_clas5.append('locker')
        aoc5_text = Text(student_out_box_left, current_name+ '----   locker')
    
    reset_screen()
def going_dean():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text
    start_time = time.time()
    starting = time.strftime('%H:%M')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('dean')
        aoc1_text = Text(student_out_box_left, current_name+ '----   dean')
    elif len(out_of_class2) == 0:
        out_of_class2.append(current_name)
        out_of_class2.append(start_time)
        out_of_class2.append('dean')
        aoc2_text = Text(student_out_box_left, current_name+ '----   dean')
    elif len(out_of_class3) == 0:
        out_of_class3.append(current_name)
        out_of_class3.append(start_time)
        out_of_class3.append('dean')
        aoc2_text = Text(student_out_box_left, current_name+ '----   dean')
    elif len(out_of_class4) == 0:
        out_of_class4.append(current_name)
        out_of_class4.append(start_time)
        out_of_class4.append('dean')
        aoc4_text = Text(student_out_box_left, current_name+ '----   dean')
    elif len(out_of_class5) == 0:
        out_of_class5.append(current_name)
        out_of_class5.append(start_time)
        out_of_clas5.append('dean')
        aoc5_text = Text(student_out_box_left, current_name+ '----   dean')
    
    reset_screen()
def going_other():
    global aoc1_text, aoc2_text, aoc3_text, aoc4_text, aoc5_text
    start_time = time.time()
    starting = time.strftime('%H:%M')
    if len(out_of_class1) == 0:
        out_of_class1.append(current_name)
        out_of_class1.append(start_time)
        out_of_class1.append('other')
        aoc1_text = Text(student_out_box_left, current_name+ '----   other')
    elif len(out_of_class2) == 0:
        out_of_class2.append(current_name)
        out_of_class2.append(start_time)
        out_of_class2.append('other')
        aoc2_text = Text(student_out_box_left, current_name+ '----   other')
    elif len(out_of_class3) == 0:
        out_of_class3.append(current_name)
        out_of_class3.append(start_time)
        out_of_class3.append('other')
        aoc3_text = Text(student_out_box_left, current_name+ '----   other')
    elif len(out_of_class4) == 0:
        out_of_class4.append(current_name)
        out_of_class4.append(start_time)
        out_of_class4.append('other')
        aoc4_text = Text(student_out_box_left, current_name+ '----   other')
    elif len(out_of_class5) == 0:
        out_of_class5.append(current_name)
        out_of_class5.append(start_time)
        out_of_clas5.append('other')
        aoc5_text = Text(student_out_box_left, current_name+ '----   other')
    
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
app = App(title = 'Pass collector', bg = (200, 30, 30))
MenuBar(app, toplevel = ['Update'], options = [[['Students Out Times', out_students], ['Students Out Reasons', student_reason], ['Exit', exit]]])
app.full_screen = True
hour_text = Text(app, text = 'Pick your disk number', color = 'white')
hour_text.text_size = 80
box = Box(app, layout = 'grid')
##hour1 = PushButton(box, text = 'Hour 1', grid = [0,0], command = first_hour)
##hour2 = PushButton(box, text = 'Hour 2', grid = [1,0], command = second_hour)
##hour3 = PushButton(box, text = 'Hour 3', grid = [2,0], command = third_hour)
##hour4 = PushButton(box, text = 'Hour 4', grid = [0,1], command = fourth_hour)
##hour5 = PushButton(box, text = 'Hour 5', grid = [1,1], command = fifth_hour)
##hour6 = PushButton(box, text = 'Hour 6', grid = [2,1], command = sixth_hour)
##hour1.bg = 'white'
##hour2.bg = 'white'
##hour3.bg = 'white'
##hour4.bg = 'white'
##hour5.bg = 'white'

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
students_out_box = Box(app, border = 1, width = 400, height = 400)
students_out_box.bg = 'white'
student_out_box_left = Box(students_out_box, border = 2, height = 400,width = 400 )
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
