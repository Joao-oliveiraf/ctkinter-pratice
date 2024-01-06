import customtkinter

window_size = '620x240'
min_size = '350x200'
max_cols = 2


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure((0, max_cols), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.geometry(window_size)
        self.title('Login Page')
        self._set_appearance_mode('system')
        self.resizable(width=True, height=True)
        self.minsize(width=350, height=270)
        cur_widht = self.winfo_width()

        self.user = customtkinter.CTkEntry(self, placeholder_text='Usuário')
        self.pw = customtkinter.CTkEntry(self, placeholder_text='Senha', show='*')
        self.user.pack(anchor='center', ipadx=10, ipady=10, pady=20)
        self.pw.pack(anchor='center', ipadx=10, ipady=10, pady=20)
        self.button = customtkinter.CTkButton(self, text='Login')
        self.button.pack(anchor='center', ipadx=10, ipady=10, pady=10)
        self.alert = customtkinter.CTkLabel(self, text_color='lightblue', text='Success')
        self.alert.pack(anchor='center')

    def create(self):
        try:
            if int(self.pw.get()) == 1512 and self.user.get() == 'John':
                return 'Success!'
            elif int(self.pw.get()) != 1512:
                return 'Wrong password!'
            elif self.user.get() != 'John':
                return 'Wrong username'
        except ValueError:
            return 'Fill the fields!'

    def authenticate(self):
        if self.create() == 'Success!':
            pass


class AlertMsg(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(master)
        self.alerta = customtkinter.CTkLabel(self, text_color='red', text='Success')


class Entries(customtkinter.CTkEntry):
    def __init__(self, master, placeholder, row, column):
        super().__init__(master)
        self.entry = customtkinter.CTkEntry(self, corner_radius=6, placeholder_text=placeholder)
        self.entry.grid(row=row, column=column, padx=20, pady=(10, 5))


app = App()
app.mainloop()
