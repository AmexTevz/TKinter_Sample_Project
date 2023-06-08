from tkinter import *
from information import Information

text = Information()

YELLOW = "#f7f5dd"
back_color = '#B20600'
FONT_NAME = "Courier"

def add_message():
    info.insert(END, '\n\n\n\t\t\t\tHit any button for more information', 'color')

def reset(text_version, header):
    info.config(state='normal')
    info.delete('1.0', END)
    info.insert(END, text_version)
    description['text'] = header
    info.config(state='disabled')


def unlock(desc=None):
    info.config(state='normal')
    label_text['text'] = desc
    add_message()
    description['text'] = 'General'
    info.config(state='disabled')


def button(title, chapter, head, w=None, h=None, background=None):
    Button(text=title, highlightbackground=YELLOW, width=w, height=h, fg=background, highlightthickness=0,
           command=lambda: reset(chapter, head)).pack(side=LEFT, padx=50)


def choice(*args):
    if clicked.get() == 'USB-C':
        reset(text.usb_1, '')
        unlock('USB Standards')
        for i in window.winfo_children()[5:]:
            i.forget()

        button('Overview', text.usb_2, 'Overview', 8)

        button('PD', text.power_delivery, 'Power Delivery', 8)

        button('Reset', text.usb_1, 'General', 5, 3, back_color)

        button('VO', text.video_output, 'Video Output', 8)

        button('Downsides', text.downsides, 'Downsides', 8)

    else:
        if clicked.get() == 'Charging':
            reset(text.summary, '')
            unlock('Charging Standards')
            for i in window.winfo_children()[5:]:
                i.forget()

            button('QC 1.0', text.charge_1, 'Quick Charge 1.0', 8)

            button('QC 3.0', text.charge_3, 'Quick Charge 3.0', 8)

            button('Reset', text.summary, 'General', 5, 3, back_color)

            button('QC 4.0', text.charge_4, 'Quick Charge 4.0', 8)

            button('QC 4.0+', text.charge_4_1, 'Quick Charge 4.0+', 8)

            button('QC 5.0', text.charge_5, 'Quick Charge 5.0', 8)


window = Tk()
window.title('NR Project')
window.config(padx=10, pady=5, bg=YELLOW)
window.geometry('1100x600')

apkudo = Label(text='Apkudo - NR Team', font=(FONT_NAME, 18), fg=back_color, bg=YELLOW, pady=10)
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
info.tag_config('color', foreground=back_color)
info['wrap'] = WORD
info.get("1.0", END)

choice(clicked)

window.mainloop()
