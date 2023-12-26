import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Meu programa')
        self.geometry("750x350")
        self.grid_columnconfigure((0, 1), weight=0)

        self.button = customtkinter.CTkButton(self, text='Login', command=self.hello)
        self.button.grid(row=3, column=0, pady=20, padx=20, sticky='ew', columnspan=2)



    def hello(self):
        print('Button pressed!')


class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = customtkinter.CTkCheckBox(text='Option 1', padx=20, pady=(0, 20))

app = App()
app.mainloop()
