import pickle

from tkinter import *

from tkinter import filedialog

root = Tk()


class TodoList(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Todo")
        self.master.geometry("800x600")

        self.my_Font = ("Arial", 20, "bold")

        # Create frame
        self.my_frame = Frame(self.master)
        self.my_frame.pack(pady=10)

        # Listbox
        self.my_list = Listbox(self.my_frame, font=self.my_Font, width=50,
                               height=5, bg="white", bd=0, fg="#464646",
                               highlightthickness=0, selectbackground="#a6a6a6",
                               activestyle="none")
        self.my_list.pack()

        '''
        my_list = ["Poop", "Fart", "Pee"]
        for item in my_list:
            self.my_list.insert(END, item)
        '''

        self.my_scrollbar = Scrollbar(self.my_frame)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_list.config(yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_list.yview)

        # Add items
        self.my_entry = Entry(self.master, font=(self.my_Font, 20), width = 24)
        self.my_entry.pack(pady=20)


        #top bar
        my_menu = Menu(self.master)
        self.master.config(menu=my_menu)

        # Add items
        file_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="File", menu=file_menu)

        # Dropdown
        file_menu.add_command(label="Save List", command=self.save_list)
        file_menu.add_command(label="Open List", command=self.open_list)
        file_menu.add_separator()
        file_menu.add_command(label="Void List", command=self.void_list)



        # Buttons
        button_frame = Frame(self.master)
        button_frame.pack(pady=20)

        delete_button = Button(button_frame, text="Delete Item", command=self.delete_item)
        add_button = Button(button_frame, text="Add Item", command=self.add_item)
        cross_button = Button(button_frame, text="Cross Off Item", command=self.cross_item)
        uncross_button = Button(button_frame, text="Un-Cross Off Item", command=self.uncross_item)
        clear_all_button = Button(button_frame, text="Clear", command=self.clear)

        delete_button.grid(row=0, column=0)
        add_button.grid(row=0, column=1, padx=15)
        cross_button.grid(row=0, column=2)
        uncross_button.grid(row=0, column=3, padx=15)
        clear_all_button.grid(row=0, column=4)



    def delete_item(self):
        self.my_list.delete(ANCHOR)

    def add_item(self):
        self.my_list.insert(END, self.my_entry.get())
        self.my_entry.delete(0, END)

    def cross_item(self):
        #Cross Off
        self.my_list.itemconfig(
            self.my_list.curselection(),
            fg="#ff0000"
        )
        #Get rid of select bar
        self.my_list.selection_clear(0, END)

    def uncross_item(self):
        #Cross Off
        self.my_list.itemconfig(
            self.my_list.curselection(),
            fg="#464646"
        )
        #Get rid of select bar
        self.my_list.selection_clear(0, END)

    def clear(self):
        count = 0
        while count < self.my_list.size():
            if self.my_list.itemcget(count, "fg") == "#ff0000":
                self.my_list.delete(self.my_list.index(count))
            else:
                count +=1


    def save_list(self):
        file_name = filedialog.asksaveasfilename(
            initialdir="C:\\Users\\<NAME>\\Desktop\\",
            title="Save",
            filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
        )
        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f'{file_name}.dat'

        #Delete crossed off before saving
        count = 0
        while count < self.my_list.size():
            if self.my_list.itemcget(count, "fg") == "#ff0000":
                self.my_list.delete(self.my_list.index(count))
            else:
                count +=1

        #Grab elements
        stuff = self.my_list.get(0,END)

        #Open file
        output_file = open(file_name, "wb")

        #Add data to file
        pickle.dump(stuff, output_file)


    def open_list(self):
        file_name = filedialog.askopenfilename(
            initialdir="C:\\Users\\<NAME>\\Desktop\\",
            title="Save",
            filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
        )

        if file_name:
            #Delete currently open
            self.my_list.delete(0, END)

            #Open
            input_file = open(file_name, "rb")

            #Load
            stuff = pickle.load(input_file)

            for item in stuff:
                self.my_list.insert(END, item)
    def void_list(self):
        self.my_list.delete(0, END)










