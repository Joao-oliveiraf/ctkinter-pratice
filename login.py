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

        self.user = customtkinter.CTkEntry(self, placeholder_text='teste')
        self.user.grid(row=0, column=0, sticky='center')

        self.button = customtkinter.CTkButton(self, text='Login')
        self.button.grid(row=1, column=0, padx=20, pady=15, columnspan=max_cols+1, sticky='ew')


class Entries(customtkinter.CTkEntry):
    def __init__(self, master, placeholder, row, column):
        super().__init__(master)
        self.entry = customtkinter.CTkEntry(self, corner_radius=6, placeholder_text=placeholder)
        self.entry.grid(row=row, column=column, padx=20, pady=(10, 5))

app = App()
app.mainloop()