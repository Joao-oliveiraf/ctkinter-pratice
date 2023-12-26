import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Meu programa')
        self.geometry("400x180")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = CheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsw')

        self.button = customtkinter.CTkButton(self, text='Login', command=self.hello)
        self.button.grid(row=1, column=0, pady=20, padx=20, sticky='ew', columnspan=2)

    def hello(self):
        print('Button pressed!')


class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value, hover_color='green')
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky='w')
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = list()
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

        #self.checkbox_1 = customtkinter.CTkCheckBox(master=self, text='Option 1', hover_color='green')
        #self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self, text='Option 2', hover_color='green')
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky='w')
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self, text='Option 3', hover_color='green')
        self.checkbox_3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')


app = App()
app.mainloop()
