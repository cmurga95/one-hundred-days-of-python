from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = -1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer")
    check_marks.config(text = "")
    global reps
    reps = -1
    ##timer_text 00:00
    ##title_label "Timer"
    ##checkmarks
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 20
    #if its 1,3,5,7 rep
    # if reps in (1,3,5,7):
    if reps % 8 ==0:
        count_down(work_sec)
        label_ch(title = "Work", bcolor = GREEN)
    #if its the 8 rep
    elif reps % 2 == 0:
        count_down(long_break_sec)
        label_ch(title = "Break", bcolor = PINK)
    #if its 2,4,6
    else:
        count_down(short_break_sec)
        label_ch(title = "Long break", bcolor = RED)

def label_ch(title, bcolor):
    title_label.config(text = title, fg = bcolor)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    # if len(str(count_sec)) == 1:
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"
    
    canvas.itemconfig(timer_text, text = (f"{count_min}:{count_sec}"))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_marks.config(text = math.floor(reps/2)*"✓")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 100, bg = YELLOW)


#title label
title_label = Label(text = "Timer", 
                    fg = GREEN, 
                    bg = YELLOW, 
                    font = (FONT_NAME, 50, "bold"))
title_label.grid(column = 1, row = 0)

#canvas (image)
canvas = Canvas(width=220, 
                height=220, 
                bg = YELLOW, 
                highlightthickness=0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(105,105, image = tomato_image)
timer_text = canvas.create_text(105,120, text = "00:00", 
                   fill = "white", 
                   font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

#button
#start
start_button = Button(text = "Start", highlightthickness=0, command = start_timer)
start_button.grid(column = 0, row = 2)
#reset
reset_button = Button(text = "Reset", highlightthickness=0, command = reset_timer)
reset_button.grid(column = 2, row = 2)

#checkmarks
check_marks = Label(fg = GREEN, 
                    bg = YELLOW,
                    font = (FONT_NAME, 20, "bold"))
check_marks.grid(column = 1, row = 3)


window.mainloop()