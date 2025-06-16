# Import required modules
import sqlite3
from sqlite3 import Error
from tkinter import *
import tkinter.messagebox

# Initialize main window
window = Tk()
window.geometry('600x370')
contacts_list = []
window.title('AddressBook')
contact_name = StringVar()
contact_phone = StringVar()

# Establish a connection to the database and populate names list
def open_connection(db_path):
    connection = None
    try:
        connection = sqlite3.connect(db_path)
        result = connection.execute('SELECT * FROM addresses')
        for entry in result:
            contacts_list.append(entry[1])
        return connection
    except Error as err:
        print(err)
    return connection

# Create a new table if it doesn't exist
def setup_table(connection, table_query):
    try:
        cursor = connection.cursor()
        cursor.execute(table_query)
    except Error as err:
        print(err)

# Show info popup for add/delete actions
def show_added_popup():
    tkinter.messagebox.showinfo("Info", contact_name.get() + " has been added.")

def show_deleted_popup():
    tkinter.messagebox.showinfo("Info", contact_name.get() + " has been deleted.")

# Function to add a new contact, with validation
def add_contact():
    insert_query = ''' INSERT INTO addresses(name, phone)
                       VALUES(?, ?) '''
    if contact_name.get() not in contacts_list:
        if contact_name.get() == '' or contact_phone.get() == '' or len(contact_phone.get()) != 10:
            popup = Toplevel(window)
            popup.geometry('200x100')
            if contact_phone.get() == '' or len(contact_phone.get()) != 10:
                Label(popup, text="Phone must be 10 digits").pack()
            else:
                Label(popup, text="Name cannot be empty").pack()
            Button(popup, text='Back', command=popup.destroy).pack()
            return
        show_added_popup()
        cur = db_conn.cursor()
        cur.execute(insert_query, (contact_name.get(), contact_phone.get()))
        db_conn.commit()
        return cur.lastrowid
    else:
        popup = Toplevel(window)
        popup.geometry('200x100')
        if contact_name.get() == '':
            Label(popup, text="Name cannot be empty").pack()
        elif contact_phone.get() == '' or len(contact_phone.get()) != 10:
            Label(popup, text="Phone must be 10 digits").pack()
        else:
            Label(popup, text=contact_name.get() + " already exists").pack()
        Button(popup, text='Back', command=popup.destroy).pack()

# Search for a contact by name
def search_contact():
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM addresses WHERE name=?", (contact_name.get(),))
    results = cur.fetchall()
    if not results:
        WarningDialog(window)
        window.wait_window()
    else:
        contact_phone.set(results[0][2])

# Update a contact's phone number
def edit_contact():
    update_query = ''' UPDATE addresses
                       SET phone = ?
                       WHERE name = ? '''
    if contact_name.get() not in contacts_list or contact_name.get() == '':
        WarningDialog(window)
        window.wait_window()
        return
    cur = db_conn.cursor()
    cur.execute(update_query, (contact_phone.get(), contact_name.get()))
    db_conn.commit()

# Remove a contact by name
def remove_contact():
    if contact_name.get() not in contacts_list or contact_name.get() == '':
        WarningDialog(window)
        window.wait_window()
        return
    show_deleted_popup()
    delete_query = 'DELETE FROM addresses WHERE name=?'
    cur = db_conn.cursor()
    cur.execute(delete_query, (contact_name.get(),))
    db_conn.commit()

# Display all contacts
def show_all_contacts():
    result = db_conn.execute('SELECT * from addresses')
    row_idx = 0
    col_idx = 0
    popup = Toplevel(window)
    for entry in result:
        contacts_list.append(entry[1])
        for col_idx in range(len(entry)):
            entry_widget = Entry(popup, width=11, fg='Gray20')
            entry_widget.grid(row=row_idx, column=col_idx)
            entry_widget.insert(END, entry[col_idx])
        row_idx += 1
    Button(popup, text='OK', command=popup.destroy).grid(row=row_idx+3, column=max(col_idx, 1)-1)

# Database file path and table definition
db_file = r"./Address-Book/addressbook.db"
create_table_query = """CREATE TABLE IF NOT EXISTS addresses (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            phone integer NOT NULL
                        );"""

# Open connection and create table if needed
db_conn = open_connection(db_file)
if db_conn is not None:
    setup_table(db_conn, create_table_query)
else:
    print("Error: Could not connect to the database.")

# Dialog for warnings/not found
class WarningDialog:
    def __init__(self, parent):
        popup = self.popup = Toplevel(parent)
        Label(popup, text=contact_name.get().upper() + " NOT FOUND!").pack()
        Button(popup, text='Exit', command=self.close).pack()
    def close(self):
        self.popup.destroy()

# Close the application
def close_app():
    window.destroy()

# Reset name and phone fields
def clear_fields():
    contact_name.set('')
    contact_phone.set('')

# Build the UI
Label(window, text='Name', font='Times 15 bold').place(x=130, y=20)
Entry(window, textvariable=contact_name, width=42).place(x=200, y=25)
Label(window, text='Phone Number', font='Times 15 bold').place(x=130, y=70)
Entry(window, textvariable=contact_phone, width=35).place(x=242, y=73)
Button(window, text="Add", font='Times 14 bold', bg='dark gray',
       command=add_contact, width=8).place(x=130, y=110)
Button(window, text="Edit", font='Times 14 bold', bg='dark gray',
       command=edit_contact, width=8).place(x=260, y=108)
Button(window, text="Delete", font='Times 14 bold', bg='dark gray',
       command=remove_contact, width=8).place(x=390, y=107.5)
Button(window, text="Show All", font='Times 14 bold', bg='dark gray',
       command=show_all_contacts, width=12).place(x=160, y=191)
Button(window, text="Search", font='Times 14 bold', bg='dark gray',
       command=search_contact, width=13).place(x=330, y=190)
Button(window, text="Exit", font='Times 14 bold', bg='dark gray',
       command=close_app, width=8).place(x=200, y=280)
Button(window, text="Clear", font='Times 14 bold', bg='dark gray',
       command=clear_fields, width=8).place(x=320, y=280)

window.mainloop()