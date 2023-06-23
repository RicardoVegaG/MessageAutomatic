from tkinter import Tk, Entry, Label, filedialog, Button, StringVar, PhotoImage
import os
import pywhatkit

windows = Tk()
FileName = StringVar()
mensaje = ''


def SendMessage(NumPhone, NumHor, NumMin):
    phone = "+52"+NumPhone.get()
    hour = int(NumHor.get())
    minutes = int(NumMin.get())

    pywhatkit.sendwhatmsg(
        phone,
        mensaje,
        hour,
        minutes
    )


def OpenFileForMessage(EntryInfo):
    global mensaje
    EntryInfo.config(
        state='normal'
    )
    EntryInfo.delete(
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

    EntryInfo.insert(
        'end',
        NameTheFile
    )
    EntryInfo.config(
        state='disabled'
    )
    with open(FileName, 'r') as file:
        mensaje = file.read()


windows.geometry(
    '350x500+780+280'
)
windows.title(
    'WhatsApp || Messages Automatic'
)
windows.iconbitmap(
    'images/icon-app.ico'
)
windows.resizable(
    False,
    False
)
windows.config(
    background='#00a884'
)

# TEXT - ENTRY | INGRESE EL NUMERO DE TELÉFONO

TextNumeroTeléfono = Label(
    windows,
    text='INGRESE EL NUMERO DE TELÉFONO',
    foreground='white',
    background='#00a884',
    font=(
        'Arial Black',
        12
    )
).place(
    x=12,
    y=20
)

EntryNumeroTeléfono = Entry(
    windows,
    background='#005b47',
    foreground='white',
    font=(
        'Arial',
        14
    ),
    justify='center',
    border=0
)
EntryNumeroTeléfono.place(
    width=326,
    x=12,
    y=63
)

# TEXT - ENTRY - BUTTON | SELECCIONA EL MENSAJE

TextSelecciónMensaje = Label(
    windows,
    text='SELECCIONA EL MENSAJE',
    foreground='white',
    background='#00a884',
    font=(
        'Arial Black',
        12
    )
).place(
    x=50,
    y=100
)

EntrySelecciónMensaje = Entry(
    windows,
    background='#005b47',
    foreground='white',
    font=(
        'Arial',
        14
    ),
    justify='center',
    border=0,
    state='disabled',
    disabledbackground='#005b47',
    disabledforeground='white'
)
EntrySelecciónMensaje.place(
    width=290,
    x=12,
    y=143
)

ButtonSelecciónMensajeImg = PhotoImage(
    file=r'images/file.png'
)

ButtonSelecciónMensaje = Button(
    windows,
    # text='F I L E',
    image=ButtonSelecciónMensajeImg,
    bg='#00a884',
    fg='white',
    activebackground='#00a884',
    border=0,
    font=(
        'Bauhaus 93',
        12
    ),
    cursor='hand2',
    command=lambda: [
        {
            OpenFileForMessage(
                EntryInfo=EntrySelecciónMensaje
            )
        }
    ]
).place(
    x=305,
    y=137
)

# TEXT - ENTRY | INGRESE LA HORA

TextIngreseHora = Label(
    windows,
    text='INGRESE LA HORA',
    foreground='white',
    background='#00a884',
    font=(
        'Arial Black',
        12
    )
).place(
    x=80,
    y=184
)

EntryIngreseHora = Entry(
    windows,
    background='#005b47',
    foreground='white',
    font=(
        'Arial',
        14
    ),
    justify='center',
    border=0
)
EntryIngreseHora.place(
    width=326,
    x=12,
    y=227
)

# TEXT - ENTRY | INGRESE LOS MINUTOS

TextIngreseMinutos = Label(
    windows,
    text='INGRESE LOS MINUTOS',
    foreground='white',
    background='#00a884',
    font=(
        'Arial Black',
        12
    )
).place(
    x=65,
    y=264
)

EntryIngreseMinutos = Entry(
    windows,
    background='#005b47',
    foreground='white',
    font=(
        'Arial',
        14
    ),
    justify='center',
    border=0
)
EntryIngreseMinutos.place(
    width=326,
    x=12,
    y=307
)

# BUTTON | ENVIAR

ButtonEnviar = Button(
    windows,
    text='E N V I A R',
    bg='#00a884',
    fg='white',
    activebackground='#00755b',
    activeforeground='grey',
    border=0,
    font=(
        'Bauhaus 93',
        12
    ),
    cursor='hand2',
    command=lambda: [
        {
            SendMessage(
                NumPhone=EntryNumeroTeléfono,
                NumHor=EntryIngreseHora,
                NumMin=EntryIngreseMinutos
            )
        }
    ]
).place(
    x=260,
    y=460
)

windows.mainloop()
