import tkinter as tk
import os

import model


icon_path = r'files\icon.png'

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Calculator')
    root.geometry('290x300+570+250')
    root.resizable(False, False)
    root.focus_force()

    if os.path.exists(icon_path):
        root.iconphoto(True, tk.PhotoImage(file=icon_path))

    app = model.App(root)

    root.mainloop()
