#railway management system
from tkinter import *
import mysql.connector
import tkinter.messagebox
import tkinter.ttk as ttk
from PIL import ImageTk, Image

#connecting to mysql database
con = mysql.connector.connect(host="localhost",user="root", passwd="root",database="railway")
cur = con.cursor()

#creating the tables
cur.execute("CREATE TABLE IF NOT EXISTS train (train_no BIGINT PRIMARY KEY, train_name VARCHAR(50), source VARCHAR(50), destination VARCHAR(50), arrival_time TIME, departure_time TIME, distance INT(5), fare INT(5))")
cur.execute("CREATE TABLE IF NOT EXISTS passenger (passenger_id MEDIUMINT NOT NULL AUTO_INCREMENT,passenger_name CHAR(30) NOT NULL,age INT,gender VARCHAR(50),train_no INT(5),train_name VARCHAR(50),PRIMARY KEY (passenger_id),FOREIGN KEY (train_no) REFERENCES train(train_no))")
cur.execute("CREATE TABLE IF NOT EXISTS admin (name VARCHAR(50), id BIGINT PRIMARY KEY)")


def add_train():
    def submit():
        if train_no == "" or train_name == "" or source == "" or destination == "" or arrival_time == "" or departure_time == "" or distance == "" or fare == "":
            tkinter.messagebox.showinfo("Railway Management System", "Please fill all the entries")
        else:
            train_no = train_no_entry.get()
            train_name = train_name_entry.get()
            source = source_entry.get()
            destination = destination_entry.get()
            arrival_time = arrival_time_entry.get()
            departure_time = departure_time_entry.get()
            distance = distance_entry.get()
            fare = fare_entry.get()
            sql = "INSERT INTO train (train_no, train_name, source, destination, arrival_time, departure_time, distance, fare) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (train_no, train_name, source, destination, arrival_time, departure_time, distance, fare)
            cur.execute(sql, val)
            con.commit()
            tkinter.messagebox.showinfo("Railway Management System", "Train added successfully")
            train_no_entry.delete(0, END)
            train_name_entry.delete(0, END)
            source_entry.delete(0, END)
            destination_entry.delete(0, END)
            arrival_time_entry.delete(0, END)
            departure_time_entry.delete(0, END)
            distance_entry.delete(0, END)
            fare_entry.delete(0, END)
    tk = Tk()
    tk.title("Railway Management System")
    tk.geometry("400x400")
    tk.configure(background="light blue")
    train_no = Label(tk, text="Train No:",bg="light blue",fg='black' ,font=("arial", 16, "bold"))
    train_no.place(x=0, y=0)
    train_no_entry = Entry(tk, width=30)
    train_no_entry.place(x=150, y=0)
    train_name = Label(tk, text="Train Name:",bg="light blue",fg='black', font=("arial", 16, "bold"))
    train_name.place(x=0, y=50)
    train_name_entry = Entry(tk, width=30)
    train_name_entry.place(x=150, y=50)
    source = Label(tk, text="Source:", bg="light blue",fg='black',font=("arial", 16, "bold"))
    source.place(x=0, y=100)
    source_entry = Entry(tk, width=30)
    source_entry.place(x=150, y=100)
    destination = Label(tk, text="Destination:",bg="light blue",fg='black', font=("arial", 16, "bold"))
    destination.place(x=0, y=150)
    destination_entry = Entry(tk, width=30)
    destination_entry.place(x=150, y=150)
    arrival_time = Label(tk, text="Arrival Time:",bg="light blue",fg='black', font=("arial", 16, "bold"))
    arrival_time.place(x=0, y=200)
    arrival_time_entry = Entry(tk, width=30)
    arrival_time_entry.place(x=150, y=200)
    departure_time = Label(tk, text="Departure Time:",bg="light blue",fg='black', font=("arial", 16, "bold"))
    departure_time.place(x=0, y=250)
    departure_time_entry = Entry(tk, width=30)
    departure_time_entry.place(x=150, y=250)
    distance = Label(tk, text="Distance:",bg="light blue",fg='black', font=("arial", 16, "bold"))
    distance.place(x=0, y=300)
    distance_entry = Entry(tk, width=30)
    distance_entry.place(x=150, y=300)
    fare = Label(tk, text="Fare:", font=("arial", 16, "bold"), bg="light blue")
    fare.place(x=0, y=350)
    fare_entry = Entry(tk, width=30)
    fare_entry.place(x=150, y=350)
    submit = Button(tk, text="Submit", width=20, bg="light green", command=submit)
    submit.place(x=100, y=400)
    tk.mainloop()


def view_passenger():
    def submit():
        cur.execute("select * from passenger where passenger_name = %s", (passenger_name_entry.get(),))
        passenger = cur.fetchall()
        if passenger:
            tkinter.messagebox.showinfo("Passenger Details","passenger found")
        else:
            tkinter.messagebox.showinfo("Passenger Details", "Passenger not found")
    tk = tkinter.Tk()
    tk.title("Railway Management System")
    tk.geometry("400x400")
    tk.configure(background="light green")
    passenger_name_label = tkinter.Label(tk, text="Passenger name", font=("bold", 10))
    passenger_name_label.place(x=20, y=20)
    passenger_name_entry = tkinter.Entry(tk)
    passenger_name_entry.place(x=150, y=20)
    submit_button = tkinter.Button(tk, text="Submit", width=10, bg="blue", fg="white", command=submit)
    submit_button.place(x=150, y=50)
    tk.mainloop()

def adminSignup():
    def submit(na, Id):
        cur.execute("insert into admin values (%s,%s)", (na, Id))
        con.commit()
        tkinter.messagebox.showinfo('Alert', 'Name added successfully')
        tk.destroy()

    tk = tkinter.Tk()
    tk.configure(background="grey")
    tk.resizable(False, False)
    tk.geometry("360x220")
    tk.title("Train Ticket Reservation - Admin")

    nameLabel = Label(tk, text="Name:",fg='black',bg='pink')
    nameLabel.grid(row=0, column=0, padx=10, pady=20)
    nameEntry = Entry(tk, width=37)
    nameEntry.grid(row=0, column=1, padx=10, pady=20, ipady=2.2)

    Id = Label(tk, text='ID:',fg='black',bg='pink')
    Id.grid(row=1, column=0)
    idEntry = Entry(tk, width=37)
    idEntry.grid(row=1, column=1, padx=10, pady=20, ipady=2.21)

    Button(tk, text='submit',bg="blue", fg="white",command=lambda: submit(nameEntry.get(), idEntry.get())).grid(row=2, column=1, padx=10,  pady=10, ipadx=100)

def adminLogin():
    def submit(na,ID):
        cur.execute("select * from admin where name = %s and id = %s", (na,ID))
        admin = cur.fetchall()
        if admin:
            tkinter.messagebox.showinfo("Admin Login", "Login successful")
            tk.destroy()
            adminMenu()
        else:
            tkinter.messagebox.showinfo("Admin Login", "Login failed")
    tk = tkinter.Tk()
    tk.title("Railway Management System")
    tk.geometry("400x400")
    tk.configure(background="peach puff")
    name_label = tkinter.Label(tk, text="Name",fg='black',bg='peach puff', font=("bold", 10))
    name_label.place(x=20, y=20)
    name_entry = tkinter.Entry(tk)
    name_entry.place(x=150, y=20)
    Id_label = tkinter.Label(tk, text="ID",fg='black',bg='peach puff',font=("bold", 10))
    Id_label.place(x=20, y=50)
    Id_entry = tkinter.Entry(tk)
    Id_entry.place(x=150, y=50)
    submit_button = tkinter.Button(tk, text="Submit", width=10, bg="blue", fg="white", command=lambda:submit(name_entry.get(), Id_entry.get()))
    submit_button.place(x=150, y=80)
    tk.mainloop()

def add_train():
    def submit():
            cur.execute("insert into train values (%s,%s,%s,%s,%s,%s,%s,%s)", (int(train_no_entry.get()), train_name_entry.get(), source_entry.get(), destination_entry.get(), arrival_time_entry.get(), departure_time_entry.get(), int(distance_entry.get()), int(fare_entry.get())))
            con.commit()
            tkinter.messagebox.showinfo('Alert', 'Train added successfully')
            tk.destroy()
    tk = tkinter.Tk()
    tk.title("Railway Management System")
    tk.geometry("400x400")
    tk.configure(background="biscuit")
    train_no_label = tkinter.Label(tk, text="Train Number",bg="light blue",fg='black', font=("bold", 10))
    train_no_label.place(x=20, y=20)
    train_no_entry = tkinter.Entry(tk)
    train_no_entry.place(x=150, y=20)
    train_name_label = tkinter.Label(tk, text="Train Name",bg="light blue",fg='black', font=("bold", 10))
    train_name_label.place(x=20, y=50)
    train_name_entry = tkinter.Entry(tk)
    train_name_entry.place(x=150, y=50)
    source_label = tkinter.Label(tk, text="Source",bg="light blue",fg='black', font=("bold", 10))
    source_label.place(x=20, y=80)
    source_entry = tkinter.Entry(tk)
    source_entry.place(x=150, y=80)
    destination_label = tkinter.Label(tk, text="Destination",bg="light blue",fg='black', font=("bold", 10))
    destination_label.place(x=20, y=110)
    destination_entry = tkinter.Entry(tk)
    destination_entry.place(x=150, y=110)
    arrival_time_label = tkinter.Label(tk, text="Arrival Time",bg="light blue",fg='black', font=("bold", 10))
    arrival_time_label.place(x=20, y=140)
    arrival_time_entry = tkinter.Entry(tk)
    arrival_time_entry.place(x=150, y=140)
    departure_time_label = tkinter.Label(tk, text="Departure Time",bg="light blue",fg='black', font=("bold", 10))
    departure_time_label.place(x=20, y=170)
    departure_time_entry = tkinter.Entry(tk)
    departure_time_entry.place(x=150, y=170)
    distance_label = tkinter.Label(tk, text="Distance",bg="light blue",fg='black', font=("bold", 10))
    distance_label.place(x=20, y=200)
    distance_entry = tkinter.Entry(tk)
    distance_entry.place(x=150, y=200)
    fare_label = tkinter.Label(tk, text="Fare",bg="light blue",fg='black', font=("bold", 10))
    fare_label.place(x=20, y=230)
    fare_entry = tkinter.Entry(tk)
    fare_entry.place(x=150, y=230)
    submit_button = tkinter.Button(tk, text="Submit", width=10, bg="blue", fg="white", command=submit)
    submit_button.place(x=150, y=260)
    tk.mainloop()

def delete_train():
    def submit():
        cur.execute("delete from train where train_no = %s", (int(train_no_entry.get()),))
        con.commit()
        tkinter.messagebox.showinfo('Alert', 'Train deleted successfully')
        tk.destroy()
    tk = tkinter.Tk()
    tk.title("Railway Management System")
    tk.geometry("400x400")
    tk.configure(background="peach puff")
    train_no_label = tkinter.Label(tk, text="Train Number",bg="peach puff",fg='black', font=("bold", 10))
    train_no_label.place(x=20, y=20)
    train_no_entry = tkinter.Entry(tk)
    train_no_entry.place(x=150, y=20)
    submit_button = tkinter.Button(tk, text="Submit", width=10, bg="blue", fg="white", command=submit)
    submit_button.place(x=150, y=50)
    tk.mainloop()

def search_train():
    def submit(tr):
        cur.execute("select * from train where train_no = %s", (tr,))
        train = cur.fetchone()
        if train:
            tkinter.messagebox.showinfo("Train Details", "Train Number: " + str(train[0]) + "\nTrain Name: " + str(train[1]) + "\nSource: " + str(train[2]) + "\nDestination: " + str(train[3]) + "\nArrival Time: " + str(train[4]) + "\nDeparture Time: " + str(train[5]) + "\nDistance: " + str(train[6]) + "\nFare: " + str(train[7]))
        else:
            print(train,tr)
    tk = tkinter.Tk()
    tk.title("Railway Management System")
    tk.geometry("400x400")
    tk.configure(background="grey")
    train_no_label = tkinter.Label(tk, text="Train Number",bg="grey",fg='black', font=("bold", 10))
    train_no_label.place(x=20, y=20)
    train_no_entry = tkinter.Entry(tk)
    train_no_entry.place(x=150, y=20)
    submit_button = tkinter.Button(tk, text="Submit", width=10, bg="blue", fg="white", command=lambda:submit(int(train_no_entry.get())))
    submit_button.place(x=150, y=50)
    tk.mainloop()


def book_ticket():
    def submit():
        cur.execute("select * from train where train_no = %s", (train_no_entry.get(),))
        train = cur.fetchone()
        if train:
            cur.execute("insert into passenger (passenger_name,age,gender,train_no,train_name) values (%s,%s,%s,%s,%s)", (passenger_name_entry.get(), age_entry.get(), gender_entry.get(), train_no_entry.get(), train_name_entry.get()))
            con.commit()
            tkinter.messagebox.showinfo("Alert", "Ticket booked successfully")
        else:
            tkinter.messagebox.showinfo("Alert", "Train not found")
    
    tk = tkinter.Tk()
    tk.title("Railway Management System")
    tk.geometry("400x400")
    tk.configure(background="turquoise")
    passenger_name_label = tkinter.Label(tk, text="Passenger Name",bg="turquoise",fg='black', font=("bold", 10))
    passenger_name_label.place(x=20, y=20)
    passenger_name_entry = tkinter.Entry(tk)
    passenger_name_entry.place(x=150, y=20)
    age_label = tkinter.Label(tk, text="Age",bg="turquoise",fg='black', font=("bold", 10))
    age_label.place(x=20, y=50)
    age_entry = tkinter.Entry(tk)
    age_entry.place(x=150, y=50)
    gender_label = tkinter.Label(tk,text="Gender",bg="turquoise",fg='black', font=("bold", 10))
    gender_label.place(x=20, y=80)
    gender_entry = tkinter.Entry(tk)
    gender_entry.place(x=150, y=80)
    train_no_label = tkinter.Label(tk, text="Train Number",bg="turquoise",fg='black', font=("bold", 10))
    train_no_label.place(x=20, y=110)
    train_no_entry = tkinter.Entry(tk)
    train_no_entry.place(x=150, y=110)
    train_name_label = tkinter.Label(tk, text="Train Name",bg="turquoise",fg='black', font=("bold", 10))
    train_name_label.place(x=20, y=140)
    train_name_entry = tkinter.Entry(tk)
    train_name_entry.place(x=150, y=140)
    Button(tk,text="Submit",bg="blue", fg="white",command=submit).place(x=150,y=170)
    tk.mainloop()

def cancel_ticket():
    def submit():
        cur.execute("delete from passenger where passenger_name = %s", (passenger_name.get(),))
        con.commit()
        tkinter.messagebox.showinfo("Alert", "Ticket cancelled successfully")
    tk = tkinter.Tk()
    tk.title("Railway Management System")
    tk.geometry("400x400")
    tk.configure(background="light green")
    passenger_name = tkinter.StringVar()
    passenger_name_label = tkinter.Label(tk, text="Passenger Name",bg="light green",fg='black', font=("bold", 10))
    passenger_name_label.place(x=20, y=20)
    passenger_name_entry = tkinter.Entry(tk, textvariable=passenger_name)
    passenger_name_entry.place(x=150, y=20)
    submit_button = tkinter.Button(tk, text="Submit", width=10, bg="blue", fg="white", command=submit)
    submit_button.place(x=150, y=50)
    tk.mainloop()


    
def search_ticket():
    def submit():
        cur.execute("select * from passenger where passenger_name = %s", (passenger_name_entry.get(),))
        result = cur.fetchall()
        if result:
            for i in result:
                tkinter.messagebox.showinfo("Ticket Details", "Passenger Name: " + str(i[1]) + "\nAge: " + str(i[2]) + "\nGender: " + str(i[3]) + "\nTrain Number: " + str(i[4]) + "\nTrain Name: " + str(i[5]))
        else:
            tkinter.messagebox.showinfo("Alert", "No record found")
    tk = tkinter.Tk()

    tk.title("Railway Management System")
    tk.geometry("400x400")
    tk.configure(background="lavender")

    passenger_name_label = tkinter.Label(tk, text="Passenger Name",bg="lavender",fg='black', font=("bold", 10))
    passenger_name_label.place(x=20, y=20)
    passenger_name_entry = tkinter.Entry(tk)
    passenger_name_entry.place(x=150, y=20)


    submit_button = tkinter.Button(tk, text="Submit", width=10, bg="blue", fg="white", command=submit)
    submit_button.place(x=150, y=60)
    tk.mainloop()

def update_ticket():
    def submit():
        cur.execute("update passenger set passenger_name = %s", (passenger_name_entry.get(),))
        cur.execute("update passenger set age = %s", (age_entry.get(),))
        cur.execute("update passenger set gender = %s", (gender_entry.get(),))
        cur.execute("update passenger set train_no = %s", (train_no_entry.get(),))
        cur.execute("update passenger set train_name = %s", (train_name_entry.get(),))
        con.commit()
        tkinter.messagebox.showinfo("Alert", "Record updated successfully")
    tk = tkinter.Tk()
    tk.title("Railway Management System")
    tk.geometry("400x400")
    passenger_name_label = tkinter.Label(tk, text="Passenger Name", font=("bold", 10))
    passenger_name_label.place(x=20, y=20)
    passenger_name_entry = tkinter.Entry(tk)
    passenger_name_entry.place(x=150, y=20)
    age_label = tkinter.Label(tk, text="Age", font=("bold", 10))
    age_label.place(x=20, y=50)
    age_entry = tkinter.Entry(tk)
    age_entry.place(x=150, y=50)
    gender_label = tkinter.Label(tk, text="Passenger Gender", font=("bold", 10))
    gender_label.place(x=20, y=80)
    gender_entry = tkinter.Entry(tk)
    gender_entry.place(x=150, y=80)
    train_no_label = tkinter.Label(tk, text="Train No", font=("bold", 10))
    train_no_label.place(x=20, y=110)
    train_no_entry = tkinter.Entry(tk)
    train_no_entry.place(x=150, y=110)
    train_name_label = tkinter.Label(tk, text="Train Name", font=("bold", 10))
    train_name_label.place(x=20, y=140)
    train_name_entry = tkinter.Entry(tk)
    train_name_entry.place(x=150, y=140)
    submit_button = tkinter.Button(tk, text="Submit", width=10, bg="blue", fg="white", command=submit)
    submit_button.place(x=150, y=350)
    tk.mainloop()

def mainWin():
    tk = tkinter.Tk()
    tk.title("Railway Management System")
    tk.geometry("400x400")
    tk.configure(background="light blue")
    Label(tk, text="Railway Management\n System", bg="light blue", fg="black", font=("Fira Code", 20,"bold")).place(x=50, y=20)
    admin_button = tkinter.Button(tk, text="Admin", width=20, bg="blue", fg="white", command=adminLogin)
    admin_button.place(x=120, y=120)
    admin_signup_button = tkinter.Button(tk, text="Admin Signup", width=20, bg="blue", fg="white", command=adminSignup)
    admin_signup_button.place(x=120, y=170)
    passenger_button = tkinter.Button(tk, text="Passenger", width=20, bg="blue", fg="white", command=passWin)
    passenger_button.place(x=120, y=220)
    tk.mainloop()

def passWin():
    tk = Tk()
    tk.title("Railway Management System-Passenger")
    tk.geometry("400x400")
    tk.configure(background="turquoise")
    Button(tk, text="Book Ticket", width=20, bg="blue", fg="white", command=book_ticket).place(x=100, y=100)
    Button(tk, text="Cancel Ticket", width=20, bg="blue", fg="white", command=cancel_ticket).place(x=100, y=150)
    Button(tk, text="View Ticket", width=20, bg="blue", fg="white", command=search_ticket).place(x=100, y=200)
    Button(tk, text="Search Train", width=20, bg="blue", fg="white", command=search_train).place(x=100, y=250)
    Button(tk, text="Update ticket", width=20, bg="blue", fg="white", command=update_ticket).place(x=100, y=300)
    tk.mainloop()

def adminMenu():
    tk = tkinter.Tk()
    tk.title("Railway Management System")
    tk.configure(background="light blue")
    tk.geometry("400x400")
    add_train_button = tkinter.Button(tk, text="Add Train", width=20, bg="blue", fg="white", command=add_train)
    add_train_button.place(x=150, y=20)
    delete_train_button=tkinter.Button(tk,text="Delete train",width=20,bg='blue',fg='white',command=delete_train)
    delete_train_button.place(x=150,y=50)
    view_train_button = tkinter.Button(tk, text="View Train", width=20, bg="blue", fg="white", command=search_train)
    view_train_button.place(x=150, y=80)
    view_train_route_button = tkinter.Button(tk, text="Check Passenger", width=20, bg="blue", fg="white", command=view_passenger)
    view_train_route_button.place(x=150, y=120)
    tk.mainloop()

mainWin()

