#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:29:35 2019

@author: ayushsrivastava
"""
from tkinter import *
import sqlite3
import datetime

class Application:
    def __init__(self, master):
        #------ constants for controlling layout ------
        frame_bg = "midnight blue"
        fg_color = "red"
        bg_color = "peach puff"
        
        font_tuple = ("Courier", 18)
        
        entry_width = 25
        label_width = 15
        
        button_width = 6      ### (1)
		
        button_padx = "2m"    ### (2)
        button_pady = "1m"    ### (2)
        buttons_frame_padx =  "3m"   ### (3)
        buttons_frame_pady =  "2m"   ### (3)		
        buttons_frame_ipadx = "3m"   ### (3)
        buttons_frame_ipady = "1m"   ### (3)
		# -------------- end constants ----------------
		
        #------ global variables ----------
        index = 0
        self.data = StringVar()
        self.name = StringVar()
        self.author = StringVar()
        self.borrow_date = StringVar()
        self.return_date = StringVar()
        #------- end variables ------------
        
        self.data.set("Firstname:\nLastname\nMobile:\nAddress:\nTitle:\nAuthor:\nBorrowDate:\nDueDate:\n" )
        self.name.set(" ")
        self.author.set(" ")
        self.borrow_date.set(" ")
        self.return_date.set(" ")
        
        self.master = master
        master.title("DIGITAL LIBRARY")   
        master.resizable(0, 0)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        
        self.container1 = Frame(master, bg = frame_bg, bd = 5, relief = RAISED)
        self.container1.pack(side = TOP, fill = BOTH)

        self.container2 = Frame(master, bg = frame_bg, bd = 2, relief = RAISED)
        self.container2.pack(fill = BOTH, expand = True)
        
        self.label_frame2 = LabelFrame(self.container2, text = "Library Membership Details", bg = frame_bg)
        self.label_frame2.pack(side = LEFT, fill = BOTH, expand = True)
        
        self.label_frame3 = LabelFrame(self.container2, text = "Book Details", bg = frame_bg)
        self.label_frame3.pack(side = RIGHT, fill = BOTH, expand = True)

        self.container3 = Frame(master, bg = frame_bg, bd = 2, relief = RAISED)
        self.container3.pack(fill = BOTH, expand = True)
        
        self.label_frame4 = LabelFrame(self.container3, text = "Firstname\tLastname\tMobile\tAddress\tTitle\tAuthor\tBorrow_date\tDue_date", bg = frame_bg)
        self.label_frame4.pack(side = BOTTOM, fill = BOTH, expand = True)

        self.container4 = Frame(master, bg = frame_bg, bd = 2, relief = RAISED)
        self.container4.pack(fill = BOTH, expand = True)

                
        self.welcome_label = Label(self.container1, font = ("Courier", 75), text = "LIBRARY MANAGEMENT SYSTEM", 
                                   bg = frame_bg, fg = "black", bd = 5, width = 33, relief = SUNKEN)

        self.firstname_label = Label(self.label_frame2, font = font_tuple, text = "Firstname", 
                                    bg = bg_color, fg = fg_color, bd = 2, width = label_width, relief = RAISED)
        self.firstname_entry = Entry(self.label_frame2, font = font_tuple, 
                                    bg = bg_color, fg = fg_color, bd = 2, width = entry_width, relief = SUNKEN)
        
        self.lastname_label = Label(self.label_frame2, font = font_tuple, text = "Lastname", 
                                    bg = bg_color, fg = fg_color, bd = 2, width = label_width, relief = RAISED)
        self.lastname_entry = Entry(self.label_frame2, font = font_tuple, 
                                    bg = bg_color, fg = fg_color, bd = 2, width = entry_width, relief = SUNKEN)
  
        self.mobile_label = Label(self.label_frame2, font = font_tuple, text = "Mobile", 
                                    bg = bg_color, fg = fg_color, bd = 2, width = label_width, relief = RAISED)
        self.mobile_entry = Entry(self.label_frame2, font = font_tuple, 
                                    bg = bg_color, fg = fg_color, bd = 2, width = entry_width, relief = SUNKEN)
        
        self.address_label = Label(self.label_frame2, font = font_tuple, text = "Address", 
                                    bg = bg_color, fg = fg_color, bd = 2, width = label_width, relief = RAISED)
        self.address_entry = Entry(self.label_frame2, font = font_tuple, 
                                    bg = bg_color, fg = fg_color, bd = 2, width = entry_width, relief = SUNKEN)

        self.title_label = Label(self.label_frame2, font = font_tuple, text = "Title", 
                                    bg = bg_color, fg = fg_color, bd = 2, width = label_width, relief = RAISED)
        self.title_entry = Entry(self.label_frame2, font = font_tuple, 
                                    bg = bg_color, fg = fg_color, bd = 2, width = entry_width, relief = SUNKEN, textvariable = self.name)
        
        self.author_label = Label(self.label_frame2, font = font_tuple, text = "Author", 
                                    bg = bg_color, fg = fg_color, bd = 2, width = label_width, relief = RAISED)
        self.author_entry = Entry(self.label_frame2, font = font_tuple, 
                                    bg = bg_color, fg = fg_color, bd = 2, width = entry_width, relief = SUNKEN, textvariable = self.author)
        
        self.borrow_date_label = Label(self.label_frame2, font = font_tuple, text = "BorrowDate", 
                                    bg = bg_color, fg = fg_color, bd = 2, width = label_width, relief = RAISED)
        self.borrow_date_entry = Entry(self.label_frame2, font = font_tuple, textvariable = self.borrow_date, 
                                    bg = bg_color, fg = fg_color, bd = 2, width = entry_width, relief = SUNKEN)
        
        self.return_date_label = Label(self.label_frame2, font = font_tuple, text = "DueDate", 
                                    bg = bg_color, fg = fg_color, bd = 2, width = label_width, relief = RAISED)
        self.return_date_entry = Entry(self.label_frame2, font = font_tuple, textvariable = self.return_date,  
                                    bg = bg_color, fg = fg_color, bd = 2, width = entry_width, relief = SUNKEN)
        
        self.data_scrollbar = Scrollbar(self.label_frame3, bg = bg_color)                
        self.books_listbox = Listbox(self.label_frame3, font = font_tuple, bg = bg_color, fg = fg_color, yscrollcommand = self.data_scrollbar.set)
        self.books_listbox.pack(side = LEFT, fill = BOTH)
        self.data_scrollbar.pack(side = LEFT, fill = Y)
        self.books_listbox.bind('<Button-1>', self.fetch)
        
        conn = sqlite3.connect("/Users/ayushsrivastava/Downloads/Library/testDB.db")
        cursor = conn.execute("SELECT ISBN, NAME, GENRE, QUANTITY FROM BOOK_DETAILS")
        for row in cursor:
            index += 1
            self.books_listbox.insert(index, row[1])
        
        self.details_label = Label(self.label_frame3, font = font_tuple, textvariable = self.data, 
                                        bg = bg_color, fg = fg_color, bd = 2, width = 35, height = 15, relief = SUNKEN)
        
        self.add_book_button = Button(self.label_frame3, font = font_tuple, text = "Add Book",
                                      bg = bg_color, fg = fg_color, bd = 2, width = 10, relief = RAISED, command = self.add_book)
        
        self.result_listbox = Listbox(self.label_frame4, font = font_tuple, bg = bg_color, fg = fg_color)
        self.result_listbox.pack(expand = True, fill = BOTH)

        self.display_button = Button(self.container4, font = font_tuple, text = "Display", 
                                     bg = bg_color, fg = fg_color, bd = 2, width = 10, relief = RAISED, command = self.display)
        
        self.clear_button = Button(self.container4, font = font_tuple, text = "Clear", 
                                   bg = bg_color, fg = fg_color, bd = 2, width = 10, relief = RAISED, command = self.clear)
        
        self.exit_button = Button(self.container4, font = font_tuple, text = "Exit", 
                                  bg = bg_color, fg = fg_color, bd = 2, width = 10, relief = RAISED, command = self.exit)
        
                
        self.welcome_label.grid(row = 0, column = 0)
        self.firstname_label.grid(row = 2, column = 0)
        self.firstname_entry.grid(row = 2, column = 1)
        self.lastname_label.grid(row = 4, column = 0)
        self.lastname_entry.grid(row = 4, column = 1)
        self.mobile_label.grid(row = 6, column = 0)
        self.mobile_entry.grid(row = 6, column = 1)
        self.address_label.grid(row = 8, column = 0)
        self.address_entry.grid(row = 8, column = 1)
        self.title_label.grid(row = 2, column = 2)
        self.title_entry.grid(row = 2, column = 3)
        self.author_label.grid(row = 4, column = 2)
        self.author_entry.grid(row = 4, column = 3)
        self.borrow_date_label.grid(row = 6, column = 2)
        self.borrow_date_entry.grid(row = 6, column = 3)
        self.return_date_label.grid(row = 8, column = 2)
        self.return_date_entry.grid(row = 8, column = 3)
        self.details_label.pack()
        self.add_book_button.pack(side = BOTTOM)
        self.display_button.grid(row = 0, column = 10)
        self.clear_button.grid(row = 0, column = 12)
        self.exit_button.grid(row = 0, column = 14)
        
    def display(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        mobile = self.mobile_entry.get()
        address = self.address_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        borrow_date = self.borrow_date_entry.get()
        return_date = self.return_date_entry.get()
        
        if firstname and lastname and mobile and address and title and author and borrow_date and return_date:
            self.data.set("Firstname: " + firstname + "\n" +
                          "Lastname: " + lastname + "\n" +
                          "Mobile: " + mobile + "\n" + 
                          "Address: " + address + "\n" +
                          "Title: " + title + "\n" +
                          "Author: " + author + "\n" +
                          "Borrow date: " + borrow_date + "\n" +
                          "Return date: " + return_date + "\n")
            self.result_listbox.insert(0, firstname + "\t" + lastname + "\t" + mobile + "\t" + address + "\t" + title + "\t" + author + "\t" + borrow_date + "\t" + return_date)

    
    def fetch(self, event):
        try:
            index = self.books_listbox.curselection()
            book_name = self.books_listbox.get(index[0])
            
            conn = sqlite3.connect("/Users/ayushsrivastava/Downloads/Library/testDB.db")
            cursor = conn.execute("SELECT ISBN, NAME, GENRE, QUANTITY FROM BOOK_DETAILS")

            for row in cursor:
                if str(book_name) == str(row[1]):
                    self.name.set(row[1])
                    self.author.set(row[2])
            time_struct = time.localtime() 
            print(time_struct[0:3])
            self.borrow_date.set(time_struct[-5:])
            print(datetime.timedelta(days = 10))
            datetime.datetime.strptime(s, '%d/%m/%Y') + datetime.timedelta(days=10)
        except IndexError:
            return
            
    def add_book(self):
        self.master.withdraw()
        top = Toplevel()
        self.master.transient()
        self.name_label = Label(top, font = font_tuple, bg = bg_color, fg = fg_color, text = "TITLE", relief = RAISED, width = label_width)
        self.name_entry = Entry(top, font = font_tuple, bg = bg_color, fg = fg_color, relief = SUNKEN, width = entry_width)
        self.author_label = Label(top, font = font_tuple, bg = bg_color, fg = fg_color, text = "AUTHOR", relief = RAISED, width = label_width)
        self.author_entry = Entry(top, font = font_tuple, bg = bg_color, fg = fg_color, relief = SUNKEN, width = entry_width)
        self.add_button = Button(top, font = font_tuple, text = "Add", relief = RAISED)
        
        self.name_label.grid(row = 1, column = 0)
        self.name_entry.grid(row = 1, column = 3)
        self.author_label.grid(row = 2, column = 0)
        self.author_entry.grid(row = 2, column = 3)
        self.add_button.grid(row = 4, column = 0)
        
    def exit(self):
        self.master.destroy()
        exit()
    
    def clear(self):
        self.result_listbox.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    application = Application(root)
    root.mainloop()
