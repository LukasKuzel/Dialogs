import tkinter as tk
from typing import Dict


class ParameterUpdater:
    def __init__(self, parameters: Dict[str, int], master):
        self.parameters = parameters
        self.create_widgets(master)
        self.load_parameters()  # Load parameters on initialization

    def create_widgets(self, master):
        master.grid_rowconfigure(0, minsize=120)

        self.parameter_entries = []
        for i, key in enumerate(self.parameters):
            label = tk.Label(master, text=key, padx=5)
            label.grid(row=i + 1, column=0, padx=10, pady=5, sticky='e')
            entry = tk.Entry(master, validate="key")
            entry.insert(0, str(self.parameters[key]))
            entry.config(validatecommand=(entry.register(self.validate_entry), '%P'))
            entry.grid(row=i + 1, column=1, padx=10, pady=5, sticky='w')
            self.parameter_entries.append(entry)
        button_frame = tk.Frame(master)
        button_frame.grid(row=len(self.parameters) + 1, column=0, columnspan=2, padx=10, pady=10)
        update_button = tk.Button(button_frame, text="Update Parameters", command=self.update_parameters)
        update_button.pack(side='left', padx=5)
        save_button = tk.Button(button_frame, text="Save Parameters", command=self.save_parameters)
        save_button.pack(side='right', padx=5)
        load_button = tk.Button(button_frame, text="Load Parameters", command=self.load_parameters)
        load_button.pack(side='right', padx=5)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)

    def validate_entry(self, new_text):
        try:
            if new_text:
                new_value = int(new_text)
                return new_value >= 0
            else:
                return True
        except ValueError:
            return False

    def update_parameters(self):
        for i, key in enumerate(self.parameters):
            value = self.parameter_entries[i].get()
            if value:
                self.parameters[key] = int(value)

    def save_parameters(self):
        with open('parameters.txt', 'w') as f:
            for key, value in self.parameters.items():
                f.write(f'{key}={value}\n')

    def load_parameters(self):
        try:
            with open('parameters.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    key, value = line.strip().split('=')
                    if key in self.parameters:
                        self.parameters[key] = int(value)
        except FileNotFoundError:
            pass
        self.update_ui()

    def update_ui(self):
        for i, key in enumerate(self.parameters):
            self.parameter_entries[i].delete(0, tk.END)
            self.parameter_entries[i].insert(0, str(self.parameters[key]))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Parameter Updater")
    width = 800
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.resizable(width=False, height=False)
    parameters = {'Parameter 1': 10, 'Parameter 2': 20, 'Parameter 3': 30}
    app = ParameterUpdater(parameters, root)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(len(parameters)+1, weight=1)
    root.mainloop()