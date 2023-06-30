from tkinter import Tk, PhotoImage, Label
from tkinter import StringVar, Button
from tkinter import Entry, filedialog
import os
import pywhatkit

# Principal

Windows = Tk()
NumberPhone = StringVar()
NumberHours = StringVar()
NumberMinutes = StringVar()
Message = ''

# Functions


def SendMessage():
    Phone = "+52"+NumberPhone.get()
    Hours = int(
        NumberHours.get()
    )
    Minutes = int(
        NumberMinutes.get()
    )

    pywhatkit.sendwhatmsg(
        Phone,
        Message,
        Hours,
        Minutes
    )


def OpenFilesForMessage(Entry):
    global Message
    Entry.config(
        state='normal'
    )
    Entry.delete(
        '0',
        'end'
    )
    FileName = filedialog.askopenfilename(
        filetypes=[
            (
                'Archivos de texto', '*.txt'
            )
        ]
    )
    NameTheFile = os.path.basename(
        FileName
    )

    Entry.insert(
        'end',
        NameTheFile
    )
    Entry.config(
        state='disabled'
    )
    with open(FileName, 'r') as file:
        Message = file.read()

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

# Entry Number Phone | App

EntryNumberPhone = Entry(
    Windows,
    textvariable=NumberPhone,
    background='#148d73',
    foreground='white',
    font=(
        'Fredoka One',
        20
    ),
    justify='center',
    border=0
)

EntryNumberPhone.place(
    width=326,
    x=31,
    y=241
)

# Entry Select Message | App

EntrySelectMessage = Entry(
    Windows,
    background='#148d73',
    foreground='white',
    font=(
        'Fredoka One',
        20
    ),
    justify='center',
    border=0,
    state='disabled',
    disabledbackground='#148d73',
    disabledforeground='white'
)

EntrySelectMessage.place(
    width=260,
    x=31,
    y=347
)

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
    cursor='hand2',
    command=lambda: [
        {
            OpenFilesForMessage(
                Entry=EntrySelectMessage
            )
        }
    ]
)
ButtonFile.place(
    x=315,
    y=346
)

# Entry Number Hours | App

EntryNumberHours = Entry(
    Windows,
    background='#148d73',
    textvariable=NumberHours,
    foreground='white',
    font=(
        'Fredoka One',
        20
    ),
    justify='center',
    border=0
)

EntryNumberHours.place(
    width=326,
    x=31,
    y=453
)

# Entry Number Minutes | App

EntryNumberMinutes = Entry(
    Windows,
    background='#148d73',
    textvariable=NumberMinutes,
    foreground='white',
    font=(
        'Fredoka One',
        20
    ),
    justify='center',
    border=0
)

EntryNumberMinutes.place(
    width=326,
    x=31,
    y=563
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
    activeforeground='white',
    command=lambda: [
        {
            SendMessage()
        }
    ]
)
ButtonSend.place(
    x=75,
    y=730
)


Windows.mainloop()
