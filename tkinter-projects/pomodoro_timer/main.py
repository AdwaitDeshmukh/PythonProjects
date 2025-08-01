import tkinter as tk
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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(status_text, text="IDLE", fill="white", font=(FONT_NAME, 40, "bold"))
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, timer
    if timer:
        window.after_cancel(timer)
    reps += 1
    if reps % 8 == 0:
        canvas.itemconfig(status_text, text="LONG BREAK", fill=RED, font=(FONT_NAME, 20, "bold"))
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        canvas.itemconfig(status_text, text="SHORT BREAK", fill=PINK, font=(FONT_NAME, 20, "bold"))
        countdown(SHORT_BREAK_MIN * 60)
    else:
        canvas.itemconfig(status_text, text="WORK", fill=GREEN)
        countdown(WORK_MIN * 60)          
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    time_min = math.floor(count / 60)
    time_sec = count % 60
    if time_sec < 10:
        time_sec = f"0{time_sec}"
    else:
        time_sec = str(time_sec)

    canvas.itemconfig(timer_text, text=f"{time_min}:{time_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
    
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file=r"E:\100 days python\day 28 pomodoro\pomodoro_timer\tomato.png")
canvas.create_image(102, 112, image=tomato)
timer_text = canvas.create_text(102, 113, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
status_text = canvas.create_text(102, 180, text="IDLE", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

timer = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer.grid(column=1, row=0)

start = tk.Button(text="start", command=start_timer)
start.grid(column=0, row=2)

reset = tk.Button(text="reset", command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()


