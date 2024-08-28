from tkinter import *
from tkinter import messagebox
import bankconnection as c
balance = 0


def create():
    def shift1():
        x1, y1, x2, y2 = canvas.bbox("marquee")
        if(x2 < 0 or y1 < 0):
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height()//2
            canvas.coords("marquee", x1, y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(100//fps, shift1)

    def submit():
        username = Name.get()
        user_id = Pancard_no.get()
        print(user_id)
        money = Amount.get()
        a_c = Account_no.get()
        user_phoneno = Mobile_no.get()
        c.Insert(username, user_id, money, a_c, user_phoneno)
        root1.destroy()

    root1 = Tk()
    root1.geometry("900x600")
    root1.config(bg="light blue")
    root1.title('Create Account')
    Label(root1, text="Welcome to our bank!!!!", bg="light blue", fg="dark blue",
          font=("Times Roman New", 30, "underline")).grid(row=1, column=2)
    Label(root1, text="Enter Your Name :-", bg="light blue", fg="black",
          font=("Times Roman New", 17, "underline")).grid(row=3, column=1)
    Name = Entry(root1)
    Name.grid(row=3, column=2)
    Label(root1, text="Enter Your Pancard-no :-", bg="light blue", fg="black",
          font=("Times Roman New", 17, "underline")).grid(row=4, column=1, pady=25)
    Pancard_no = Entry(root1)
    Pancard_no.grid(row=4, column=2)
    Label(root1, text="Enter your Amount", bg="light blue", fg="black",
          font=("Times Roman New", 17, "underline")).grid(row=5, column=1)
    Amount = Entry(root1)
    Amount.grid(row=5, column=2)
    Label(root1, text="Enter your Account-no", bg="light blue", fg="black",
          font=("Times Roman New", 17, "underline")).grid(row=6, column=1, pady=25)
    Account_no = Entry(root1)
    Account_no.grid(row=6, column=2)
    Label(root1, text="Enter your Mobile-no", bg="light blue", fg="black",
          font=("Times Roman New", 17, "underline")).grid(row=7, column=1, pady=25)
    Mobile_no = Entry(root1)
    Mobile_no.grid(row=7, column=2)
    canvas = Canvas(root1, bg='light green')
    canvas.grid(row=2, column=2, pady=50)
    text_var = "Hello!!!Please Fill Up the Following Details!!!"
    text = canvas.create_text(0, -10000, text=text_var, font=(
        'Times New Roman', 18, 'bold'), tags=("marquee",), anchor='w')
    x1, y1, x2, y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width'] = width
    canvas['height'] = height
    fps = 17
    shift1()
    # Button(root, text="Quit", command=root.destroy).pack()
    Button(root1, text="Submit", command=submit).grid(row=8, column=2)


def credit_amount():
    global balance

    def shift2():
        x1, y1, x2, y2 = canvas.bbox("marquee")
        if(x2 < 0 or y1 < 0):
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height()//2
            canvas.coords("marquee", x1, y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(100//fps, shift2)

    def Update():
        global balance
        a_c1 = Account_no.get()
        money = credit_amount.get()
        data = c.Credit(a_c1, money)
        if(data):
            messagebox.showinfo("info", "Data updated successfully")
        root2.destroy()
    root2 = Tk()
    root2.geometry("800x550")
    root2.config(bg="light blue")
    root2.title('Credit Amount')
    Label(root2, text="Welcome to our bank!!!!", bg="light blue", fg="dark blue",
          font=("Times Roman New", 30, "underline")).grid(row=1, column=2)
    Label(root2, text="Enter Your Account-no :-", bg="light blue", fg="black",
          font=("Times Roman New", 17, "underline")).grid(row=3, column=1)
    Account_no = Entry(root2)
    Account_no.grid(row=3, column=2)
    Label(root2, text="Enter your Amount", bg="light blue", fg="black", font=(
        "Times Roman New", 17, "underline")).grid(row=5, column=1, pady=50)
    credit_amount = Entry(root2)
    credit_amount.grid(row=5, column=2)
    canvas = Canvas(root2, bg='light green')
    canvas.grid(row=2, column=2, pady=50)
    text_var = "Hello!!!Please Fill Up the Following Details!!!"
    text = canvas.create_text(0, -10000, text=text_var, font=(
        'Times New Roman', 18, 'bold'), tags=("marquee",), anchor='w')
    x1, y1, x2, y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width'] = width
    canvas['height'] = height
    fps = 17
    shift2()
    Button(root2, text="update", bg="dark orange", fg="blue", font=(
        "Bodoni MT", 15), command=Update).grid(row=7, column=1)


def debit_amount():
    global balance

    def shift3():
        x1, y1, x2, y2 = canvas.bbox("marquee")
        if(x2 < 0 or y1 < 0):
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height()//2
            canvas.coords("marquee", x1, y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(100//fps, shift3)

    def update():
        global balance
        a_c2 = Account_no.get()
        money1 = debit_amount.get()
        data1 = c.Debit(a_c2, money1)
        if(data1):
            messagebox.showinfo("info", "Data updated successfully")
        root3.destroy()
    root3 = Tk()
    root3.geometry("800x550")
    root3.config(bg="light blue")
    root3.title('Debit Amount')
    Label(root3, text="Welcome to our bank!!!!", bg="light blue", fg="dark blue",
          font=("Times Roman New", 30, "underline")).grid(row=1, column=2)
    Label(root3, text="Enter Your Account-no :-", bg="light blue", fg="black",
          font=("Times Roman New", 17, "underline")).grid(row=3, column=1)
    Account_no = Entry(root3)
    Account_no.grid(row=3, column=2)
    Label(root3, text="Enter your Amount", bg="light blue", fg="black", font=(
        "Times Roman New", 17, "underline")).grid(row=5, column=1, pady=50)
    debit_amount = Entry(root3)
    debit_amount.grid(row=5, column=2)
    canvas = Canvas(root3, bg='light green')
    canvas.grid(row=2, column=2, pady=50)
    text_var = "Hello!!!Please Fill Up the Following Details!!!"
    text = canvas.create_text(0, -10000, text=text_var, font=(
        'Times New Roman', 18, 'bold'), tags=("marquee",), anchor='w')
    x1, y1, x2, y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width'] = width
    canvas['height'] = height
    fps = 17
    shift3()
    Button(root3, text="update", bg="dark orange", fg="blue", font=(
        "Bodoni MT", 15), command=update).grid(row=7, column=1)


def bank_info():
    def shift4():
        x1, y1, x2, y2 = canvas.bbox("marquee")
        if(x2 < 0 or y1 < 0):
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height()//2
            canvas.coords("marquee", x1, y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(100//fps, shift4)

    def show_data():
        a_c = Account_no.get()
        database = c.Show(a_c)  # database hold record of ac no in list
        # print("="*100)
        # print(type(database))
        # print("="*100)
        bi = Tk()
        bi.geometry("520x200")
        bi.config(bg="light blue")
        bi.title('Your Account Information')
        i = 2
        Label(bi, text="Account-No", bg="light blue", fg="black",
              font=("Times Roman New", 17, "bold")).grid(row=1, column=1)
        Label(bi, text="Name", bg="light blue", fg="black", font=(
            "Times Roman New", 17, "bold")).grid(row=1, column=2, padx=100)
        Label(bi, text="Balance", bg="light blue", fg="black", font=(
            "Times Roman New", 17, "bold")).grid(row=1, column=3)

        # Showing bank info.
        for x in database:
            Label(bi, text=x[3], bg="light blue", font=(
                "Times New Roman", 10, "bold")).grid(row=i, column=1)
            Label(bi, text=x[0], bg="light blue", font=(
                "Times New Roman", 10, "bold")).grid(row=i, column=2)
            Label(bi, text=x[2], bg="light blue", font=(
                "Times New Roman", 10, "bold")).grid(row=i, column=3)
    root4 = Tk()
    root4.geometry("900x600")
    root4.config(bg="light blue")
    root4.title('bank_info')
    Label(root4, text="Welcome to our bank!!!!", bg="light blue", fg="dark blue",
          font=("Times Roman New", 30, "underline")).grid(row=1, column=2)
    Label(root4, text="Enter your Account-no", bg="light blue", fg="black",
          font=("Times Roman New", 17, "underline")).grid(row=6, column=1, pady=25)
    Account_no = Entry(root4)
    Account_no.grid(row=6, column=2)
    canvas = Canvas(root4, bg='light green')
    canvas.grid(row=2, column=2, pady=50)
    text_var = "Hello!!!Please Fill Up the Following Details!!!"
    text = canvas.create_text(0, -10000, text=text_var, font=(
        'Times New Roman', 18, 'bold'), tags=("marquee",), anchor='w')
    x1, y1, x2, y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width'] = width
    canvas['height'] = height
    fps = 17
    shift4()
    Button(root4, text="show_data", bg="dark orange", fg="blue", font=(
        "Bodoni MT", 15), command=show_data).grid(row=7, column=1)


def exit():
    root.destroy()


def shift():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    if(x2 < 0 or y1 < 0):
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee", x1, y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(110//fps, shift)


# ===============================================================================================
# main program of Bank Project
root = Tk()
root.geometry("900x500")
root.config(bg="light blue")
root.title('Bank Home Page')
Label(root, text="STATE BANK OF INDIA ", bg="light blue",
      fg="dark blue", font=("Latin", 32)).grid(row=1, column=2, padx=55)
canvas = Canvas(root, bg='light blue')
canvas.grid(row=3, column=2, pady=50)
text_var = "Hello!!!Kindly Choose Your Operation."
text = canvas.create_text(0, -10000, text=text_var,
                          font=('Times New Roman', 18, 'bold'), tags=("marquee",), anchor='w')
x1, y1, x2, y2 = canvas.bbox("marquee")
width = x2-x1
height = y2-y1
canvas['width'] = width
canvas['height'] = height
fps = 17
shift()
Button(root, text="Create Account", bg="dark blue", fg="white", font=(
    "Bodoni MT", 15), height=5, width=12, command=create).grid(row=4, column=1, padx=20)
Button(root, text="Credit Amount", bg="dark blue", fg="white", font=("Bodoni MT",
       15), height=5, width=12, command=credit_amount).grid(row=4, column=2, padx=20)
Button(root, text="Debit Amount", bg="dark blue", fg="white", font=("Bodoni MT",
       15), height=5, width=12, command=debit_amount).grid(row=4, column=3, padx=23)
Button(root, text="Bank Information", bg="dark blue", fg="white", font=("Bodoni MT", 15),
       height=5, width=12, command=bank_info).grid(row=5, column=1, pady=15, padx=20)
Button(root, text="Exit", height=5, bg="dark blue", fg="white", font=(
    "Bodoni MT", 15), width=12, command=exit).grid(row=5, column=3, padx=26)
root.mainloop()
