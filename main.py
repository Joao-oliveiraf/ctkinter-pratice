import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Meu programa')
        self.geometry("400x220")
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._set_appearance_mode('system')

        # Frames com checkbox
        self.checkbox_frame = CheckboxFrame(self, values=['Value 1', 'Value 2', 'Value 3'], title='Values')
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsew')
        self.checkbox_frame.configure(fg_color='gray10')
        self.checkbox_frame2 = RadiobuttonFrame(self, values=['Option 1', 'Option 2'], title='Options')
        self.checkbox_frame2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky='nsew')
        self.checkbox_frame2.configure(fg_color='gray10')
        self.checkbox_frame3 = CheckboxFrame(self, values=['Value 1', 'Value 2', 'Value 3'], title='Values')
        self.checkbox_frame3.grid(row=0, column=2, padx=10, pady=(10, 0), sticky='nsew')
        self.checkbox_frame3.configure(fg_color='gray10')

        #Frames com radio


        # Buttons
        self.button = customtkinter.CTkButton(self, text='Login', command=self.button_callback)
        self.button.grid(row=3, column=0, pady=10, padx=10, sticky='ew', columnspan=3)

    def button_callback(self):
        print(f'checkbox 1: {self.checkbox_frame.get()}')
        print(f'checkbox 2: {self.checkbox_frame2.get()}')
        print(f'radiobuttons : {self.checkbox_frame3.get()}')


class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, values, title):
        super().__init__(master)
        self.values = values
        self.checkboxes = []
        self.title = title

        self.title = customtkinter.CTkLabel(self, text=self.title, corner_radius=6, fg_color="gray30")
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='we')


        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value, hover_color='darkblue')
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky='w')
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = list()
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class RadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.variable = customtkinter.StringVar(value='')
        self.radiobuttons = list()

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='ew')

        for i, value in enumerate(values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, variable=self.variable, value=value)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky='w')
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        return self.variable.set(value=value)


app = App()
app.mainloop()
