from tkinter import Tk
from todo import TodoList

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main App")
        self.root.geometry("800x600")

        # Create an instance of TodoList
        self.todo_list_frame = TodoList(self.root)
        self.todo_list_frame.pack()

    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()

if __name__ == "__main__":
    # Create an instance of the Main class and run the application
    main_app = Main()
    main_app.run()
