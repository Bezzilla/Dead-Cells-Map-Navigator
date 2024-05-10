import customtkinter as ctk
from CTkListbox import *

DATA_INDEX = {
    'company': '0',
    'product': '1',
    'typeName': '2',
    'inches': '3',
    'screenresolution': '4',
    'cpu': '5',
    'ram': '6',
    'memory': '7',
    'gpu': '8',
    'opsys': '9',
    'weight': '10',
    'price': '11'
}


class LaptopUI(ctk.CTk):

    def __init__(self, csv_data):
        super().__init__()
        self.data = csv_data
        # set up

        ctk.set_appearance_mode('dark')
        self.geometry('1000x500')
        self.minsize(900, 500)

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        self.menu = Menu(self, data=self.data)
        self.menu.grid(row=0, column=0)

    def start(self):
        self.mainloop()


class Menu(ctk.CTkTabview):

    def __init__(self, parent, data):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew')
        self.data = data

        # taps
        self.add('Data comparison')
        self.add('Story telling')

        Data_Comparison(self.tab('Data comparison'), data=self.data)
        Story_Telling(self.tab('Story telling'))


class Data_Comparison(ctk.CTkFrame):

    def __init__(self, parent, data):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')
        self.data = data
        Search_Panel(self, data=self.data)


class Story_Telling(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')


class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='#4a4a4a')
        self.pack(fill='x', pady=4, padx=4)


class Search_Panel(Panel):

    def __init__(self, parent, data):
        super().__init__(parent=parent)
        self.data = data
        self.selected_data = []

        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)

        self.search_label = ctk.CTkLabel(self, text="Search by")
        self.search_label.grid(row=0, column=0, sticky='W', padx=5, pady=5)

        self.filter_search = ctk.CTkComboBox(self, values=data[0])
        self.filter_search.grid(row=0, column=1, sticky='E', padx=5, pady=5,
                                columnspan=2)

        self.search_panel = ctk.CTkEntry(self)
        self.search_panel.grid(row=1, column=0, sticky='EW', padx=5, pady=5,
                               columnspan=3)
        self.search_panel.bind("<Return>", self.Search_list_box)

        self.search_list_box = CTkListbox(self, width=250)
        self.search_list_box.grid(row=2, column=0, sticky='EW', padx=5,
                                  pady=5, columnspan=3)

        self.add_button = ctk.CTkButton(self, text="Add to Compare List",
                                        command=self.add_to_compare_list)
        self.add_button.grid(row=3, column=0, sticky='EW', padx=5, pady=5,
                             columnspan=3)

        self.selected_label = ctk.CTkLabel(self, text="Selected List")
        self.selected_label.grid(row=4, column=0, sticky='N', padx=5, pady=5,
                                 columnspan=3)

        self.compare_list_box = CTkListbox(self, width=250)
        self.compare_list_box.grid(row=5, column=0, sticky='EW', padx=5,
                                   pady=5, columnspan=3)

        self.del_button = ctk.CTkButton(self, text="Delete",
                                        command=self.del_button)
        self.del_button.grid(row=6, column=0, sticky='N', padx=5,
                             pady=5)

        self.compare_button = ctk.CTkButton(self, text="Compare")
        self.compare_button.grid(row=6, column=1, padx=5,
                                 pady=5)

        self.clear_button = ctk.CTkButton(self, text="Clear",
                                          command=self.clear_button)
        self.clear_button.grid(row=6, column=2, padx=5,
                               pady=5)

    def Search_list_box(self, event):
        index = int(DATA_INDEX[self.filter_search.get()])
        count = 0
        try:
            self.search_list_box.delete(0, 'end')
            search_text = self.search_panel.get().lower()
            if search_text != "":
                for row in self.data:
                    if search_text.lower() in row[index].lower():
                        self.search_list_box.insert('end',
                                                    f"{row[-1]}:{row[index]}")
                        count += 1
        except Exception as e:
            pass

    def add_to_compare_list(self):
        index = self.search_list_box.curselection()
        selected_value = self.search_list_box.get(index).split(':')
        index = selected_value[0]  # index in self.data
        self.compare_list_box.insert('end', selected_value)

    def clear_button(self):
        self.compare_list_box.delete(0, 'end')

    def del_button(self):
        selected_index = self.compare_list_box.curselection()
        if selected_index:
            self.compare_list_box.delete(selected_index)
