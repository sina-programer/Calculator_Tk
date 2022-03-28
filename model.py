import tkinter as tk

import dialogs


class App:
    error_txt = 'ERROR: '
    characters = {
        'x': '*', '÷': '/', '^': '**', '²√': 'sqrt'
    }

    def __init__(self, master):
        master.config(menu=self.init_menu(master))

        # set shortcuts -----------------------------------------
        master.bind('0', lambda _: self.update('0'))
        master.bind('1', lambda _: self.update('1'))
        master.bind('2', lambda _: self.update('2'))
        master.bind('3', lambda _: self.update('3'))
        master.bind('4', lambda _: self.update('4'))
        master.bind('5', lambda _: self.update('5'))
        master.bind('6', lambda _: self.update('6'))
        master.bind('7', lambda _: self.update('7'))
        master.bind('8', lambda _: self.update('8'))
        master.bind('9', lambda _: self.update('9'))
        master.bind('+', lambda _: self.update('+'))
        master.bind('-', lambda _: self.update('-'))
        master.bind('*', lambda _: self.update('x'))
        master.bind('/', lambda _: self.update('÷'))
        master.bind('^', lambda _: self.update('^('))
        master.bind('.', lambda _: self.update('.'))
        master.bind('(', lambda _: self.update('('))
        master.bind(')', lambda _: self.update(')'))
        master.bind('r', lambda _: self.round_number())
        master.bind('c', lambda _: self.clear())
        master.bind('<Delete>', lambda _: self.backspace())
        master.bind('<BackSpace>', lambda _: self.backspace())
        master.bind('<Return>', lambda _: self.calculate())
        # -------------------------------------------------------

        # create elements ---------------------------------------
        self.result = tk.StringVar()
        tk.Entry(master, width=24, textvariable=self.result, justify=tk.RIGHT, 
                 state='readonly', font=('consolas', 13, 'bold')).pack(pady=15)

        buttons_frame = tk.Frame(master)
        buttons_frame.pack(pady=5)
        padding = {'pady': 6, 'padx': 7}

        row = 1
        tk.Button(buttons_frame, text='(', width=6, command=lambda: self.update('(')).grid(row=row, column=1, **padding)
        tk.Button(buttons_frame, text=')', width=6, command=lambda: self.update(')')).grid(row=row, column=2, **padding)
        tk.Button(buttons_frame, text='C', width=6, command=self.clear).grid(row=row, column=3, **padding)
        tk.Button(buttons_frame, text='←', width=6, command=self.backspace).grid(row=row, column=4, **padding)

        row = 2
        tk.Button(buttons_frame, text='R', width=6, command=self.round_number).grid(row=row, column=1, **padding)
        tk.Button(buttons_frame, text='xʸ', width=6, command=lambda: self.update('^(')).grid(row=row, column=2, **padding)
        tk.Button(buttons_frame, text='x²', width=6, command=lambda: self.update('^(2)')).grid(row=row, column=3, **padding)
        tk.Button(buttons_frame, text='²√', width=6, command=lambda: self.update('²√(')).grid(row=row, column=4, **padding)

        row = 3
        tk.Button(buttons_frame, text='7', width=6, command=lambda: self.update('7')).grid(row=row, column=1, **padding)
        tk.Button(buttons_frame, text='8', width=6, command=lambda: self.update('8')).grid(row=row, column=2, **padding)
        tk.Button(buttons_frame, text='9', width=6, command=lambda: self.update('9')).grid(row=row, column=3, **padding)
        tk.Button(buttons_frame, text='x', width=6, command=lambda: self.update('x')).grid(row=row, column=4, **padding)

        row = 4
        tk.Button(buttons_frame, text='4', width=6, command=lambda: self.update('4')).grid(row=row, column=1, **padding)
        tk.Button(buttons_frame, text='5', width=6, command=lambda: self.update('5')).grid(row=row, column=2, **padding)
        tk.Button(buttons_frame, text='6', width=6, command=lambda: self.update('6')).grid(row=row, column=3, **padding)
        tk.Button(buttons_frame, text='÷', width=6, command=lambda: self.update('÷')).grid(row=row, column=4, **padding)

        row = 5
        tk.Button(buttons_frame, text='1', width=6, command=lambda: self.update('1')).grid(row=row, column=1, **padding)
        tk.Button(buttons_frame, text='2', width=6, command=lambda: self.update('2')).grid(row=row, column=2, **padding)
        tk.Button(buttons_frame, text='3', width=6, command=lambda: self.update('3')).grid(row=row, column=3, **padding)
        tk.Button(buttons_frame, text='+', width=6, command=lambda: self.update('+')).grid(row=row, column=4, **padding)

        row = 6
        tk.Button(buttons_frame, text='=', width=6, command=self.calculate).grid(row=row, column=1, **padding)
        tk.Button(buttons_frame, text='0', width=6, command=lambda: self.update('0')).grid(row=row, column=2, **padding)
        tk.Button(buttons_frame, text='.', width=6, command=lambda: self.update('.')).grid(row=row, column=3, **padding)
        tk.Button(buttons_frame, text='-', width=6, command=lambda: self.update('-')).grid(row=row, column=4, **padding)
        # -------------------------------------------------------

    def calculate(self):
        try:
            result = self.result.get().lstrip(App.error_txt)
            for key, value in App.characters.items():
                result = result.replace(key, value)

            self.result.set(str(eval(result)))

        except Exception:
            result = self.result.get()
            if not result.startswith(App.error_txt):
                self.result.set(App.error_txt + result)

    def backspace(self):
        result = self.result.get()
        if result:
            self.result.set(result[:-1])

        if result.startswith(App.error_txt):
            try:
                result = self.result.get().lstrip(App.error_txt)
                final = result
                for key, value in App.characters.items():
                    result = result.replace(key, value)

                eval(result)
                self.result.set(final)

            except Exception:
                pass

    def round_number(self):
        result = self.result.get()
        if result:
            self.result.set(str(round(eval(result.lstrip(App.error_txt)))))

    def update(self, text):
        self.result.set(self.result.get() + text)

    def clear(self):
        self.result.set('')

    @staticmethod
    def init_menu(master):
        menu = tk.Menu(master)
        menu.add_command(label='About us', command=lambda: dialogs.AboutDialog(master))

        return menu
