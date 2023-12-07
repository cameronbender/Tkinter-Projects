import tkinter as tk

root = tk.Tk()

root.geometry("1920x1080")
root.title("Tkinter Hub")

def home_page():
    home_frame = tk.Frame(main_frame)
    lb = tk.Label(home_frame, text="Academify\n\nHi there!", font=("Bold",30), bg="white", fg="black")
    lb.pack()
    home_frame.pack(pady=20)

def menu_page():
    menu_frame = tk.Frame(main_frame)
    lb = tk.Label(menu_frame, text="Menu\n\nHi there!", font=("Bold",30), bg="white", fg="black")
    lb.pack()
    menu_frame.pack(pady=20)

def contact_page():
    contact_frame = tk.Frame(main_frame)
    lb = tk.Label(contact_frame, text="Contact\n\nHi there!", font=("Bold",30), bg="white", fg="black")
    lb.pack()
    contact_frame.pack(pady=20)

def settings_page():
    settings_frame = tk.Frame(main_frame)
    lb = tk.Label(settings_frame, text="Settings\n\nHi there!", font=("Bold",30), bg="white", fg="black")
    lb.pack()
    settings_frame.pack(pady=20)

def hide_indicators():
    home_indicate.config(bg="#c3c3ce")
    menu_indicate.config(bg="#c3c3ce")
    contact_indicate.config(bg="#c3c3ce")
    settings_indicate.config(bg="#c3c3ce")

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg="#158aff")
    delete_pages()
    page()


options_frame = tk.Frame(root,bg="#c3c3c3")

home_button = tk.Button(options_frame,text="Home", font=("Bold",15),
                        fg = "#158aff", bd=0, bg="#c3c3c3", width=12, height=1,
                        command=lambda: indicate(home_indicate, home_page)
                        )

home_button.place(x=10,y=50)

home_indicate = tk.Label(options_frame,text="", bg = "#c3c3c3")
home_indicate.place(x=3,y=50,width=5,height=27)

menu_button = tk.Button(options_frame,text="Menu", font=("Bold",15),
                        fg = "#158aff", bd=0, bg="#c3c3c3", width=12, height=1,
                        command=lambda: indicate(menu_indicate, menu_page))

menu_button.place(x=10,y=100)

menu_indicate = tk.Label(options_frame,text="", bg = "#c3c3c3")
menu_indicate.place(x=3,y=100,width=5,height=27)

contact_button = tk.Button(options_frame,text="Contact", font=("Bold",15),
                        fg = "#158aff", bd=0, bg="#c3c3c3", width=12, height=1,
                        command=lambda: indicate(contact_indicate, contact_page))

contact_button.place(x=10,y=150)

contact_indicate = tk.Label(options_frame,text="", bg = "#c3c3c3")
contact_indicate.place(x=3,y=150,width=5,height=27)

settings_button = tk.Button(options_frame,text="Settings", font=("Bold",15),
                        fg = "#158aff", bd=0, bg="#c3c3c3", width=12, height=1,
                        command=lambda: indicate(settings_indicate, settings_page))

settings_button.place(x=10,y=200)

settings_indicate = tk.Label(options_frame,text="", bg = "#c3c3c3")
settings_indicate.place(x=3,y=200,width=5,height=27)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=250, height=1080)

main_frame = tk.Frame(root, highlightbackground='black',
                      highlightthickness=3)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1080, width=1920)

root.mainloop()