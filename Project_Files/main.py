from tkinter import *
from information import Information

text = Information()

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
Apkudo = '#B20600'
FONT_NAME = "Courier"
font_2 = 'Rage Italic'


def reset(reset_text,header):
    info.config(state='normal')
    info.delete('1.0', END)
    info.insert(END, reset_text)
    label_text['text'] = header
    description['text'] = 'General'
    add_message()
    info.config(state='disabled')


def charge1(text_version,desc):
    info.config(state='normal')
    info.delete('1.0', END)
    info.insert(END, text_version)
    info['wrap'] = WORD
    info.config(fg='black')
    info.get("1.0", END)
    info.config(state='disabled')
    description['text'] = desc



def choice(*args):
    if clicked.get() == 'USB-C':
        reset(text.usb_1,'USB-C')
        add_message()
        for i in window.winfo_children()[5:]:
            i.forget()

        Button(text="Overview", highlightbackground=YELLOW, highlightthickness=0, width=8, command= lambda: charge1(text.usb_2,'overview')).pack(
            side=LEFT,
            padx=50)
        Button(text="PD", highlightbackground=YELLOW, highlightthickness=0, width=8, command = lambda: charge1(text.power_delivery,'Power Delivery')).pack(
            side=LEFT,
            padx=60)

        Button(text="Reset", fg=Apkudo, width=5, height=3, highlightbackground=YELLOW, command = lambda: reset(text.usb_1,'USB-C')).pack(
            side=LEFT,
            padx=60)

        Button(text="VO", highlightbackground=YELLOW, highlightthickness=0, width=8, command= lambda: charge1(text.video_output,'Video Output')).pack(
            side=LEFT,
            padx=60)

        Button(text="Downsides", highlightbackground=YELLOW, highlightthickness=0, width=8, command=  lambda: charge1(text.downsides,'Downsides')).pack(
            side=LEFT,
            padx=50)

    else:
        if clicked.get() == 'Charging':
            reset(text.summary,'Charging Standards')
            for i in window.winfo_children()[5:]:
                i.forget()

            Button(window, text="QC 1.0", highlightbackground=YELLOW, highlightthickness=0, width=7,
                   command= lambda: charge1(text.charge_1,'Quick Charge 1.0')).pack(
                side=LEFT,
                padx=30)
            Button(text="QC 2.0", highlightbackground=YELLOW, highlightthickness=0, width=7, command=lambda: charge1(text.charge_2,'Quick Charge 2.0')).pack(
                side=LEFT,
                padx=30)

            Button(text="QC 3.0", highlightbackground=YELLOW, highlightthickness=0, width=7, command= lambda: charge1(text.charge_3,'Quick Charge 3.0')).pack(
                side=LEFT,
                padx=30)
            Button(text="Reset", fg=Apkudo, width=5, height=3, highlightbackground=YELLOW, command=lambda: reset(text.summary,'Charging Standards')).pack(
                side=LEFT,
                padx=30)

            Button(text="QC 4.0", highlightbackground=YELLOW, highlightthickness=0, width=7, command=lambda: charge1(text.charge_4,'Quick Charge 4.0')).pack(
                side=LEFT,
                padx=30)

            Button(text="QC 4.0+", highlightbackground=YELLOW, highlightthickness=0, width=7,
                   command=lambda: charge1(text.charge_4_1,'Quick Charge 4.0+')).pack(
                side=LEFT,
                padx=30)

            Button(text="QC 5.0", highlightbackground=YELLOW, highlightthickness=0, width=7, command=lambda: charge1(text.charge_5,'Quick Charge 5.0')).pack(
                side=LEFT,
                padx=30)


window = Tk()
window.title('NR Project')
window.config(padx=10, pady=5, bg=YELLOW)
window.geometry('1100x600')

apkudo = Label(text='Apkudo - NR Team', font=(FONT_NAME, 18), fg=Apkudo, bg=YELLOW, pady=10)
apkudo.pack()

options = ['Charging', 'USB-C']
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(window, clicked, *options, command=choice)
drop.config(width=7, bg='white', fg='grey', font=(FONT_NAME, 15, 'bold'), pady=10)
drop.pack(side='top')

label_text = Label(text='Charging Standards', font=(FONT_NAME, 60, 'bold'), fg='grey', bg=YELLOW)
label_text.pack(side='top')

description = Label(text='General', font=(FONT_NAME, 40, 'bold'), fg='gray', bg=YELLOW, pady=10)
description.pack()

info = Text(window, height=12, width=150, bg=YELLOW, highlightthickness=0, fg='black', font=(FONT_NAME, 18))
info.pack()
info.insert(END, text.summary)
info.tag_config('color', foreground=Apkudo)
info['wrap'] = WORD
info.get("1.0", END)


def add_message():
    info.insert(END, '\n\n\n\t\t\t\tHit any button for more information','color')


add_message()

choice(clicked)

window.mainloop()
