from tkinter import Tk, PhotoImage, Label, StringVar, Button

Windows = Tk()
NumberPhone = StringVar()
NumberHours = StringVar()
NumberMinutes = StringVar()


# View Windows

Windows.geometry(
    '390x844+200+100'
)
Windows.title(
    'WhatsApp || Message Automatic'
)
Windows.iconbitmap(
    'images/icon-app.ico'
)
Windows.resizable(
    False,
    False
)

# Background | App

BackgroundAppImg = PhotoImage(
    file='images/background.png'
)

BackgroundApp = Label(
    Windows,
    image=BackgroundAppImg
)
BackgroundApp.pack()

# Button File | App

ButtonFileImg = PhotoImage(
    file='images/file.png'
)

ButtonFile = Button(
    Windows,
    image=ButtonFileImg,
    border=0,
    activebackground='#00a884',
    background='#00a884',
    cursor='hand2'
)
ButtonFile.place(
    x=315,
    y=346
)


# Button Send | App

ButtonSend = Button(
    Windows,
    text='E N V I A R',
    font=(
        'Fredoka One',
        30
    ),
    background='#359b85',
    foreground='white',
    border='0',
    cursor='hand2',
    activebackground='#359b85',
    activeforeground='white'
)
ButtonSend.place(
    x=75,
    y=730
)


Windows.mainloop()
