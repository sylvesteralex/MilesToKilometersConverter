from tkinter import Label, Button, Entry
from setup import LABEL_BG, LABEL_FONT, BUTTON_BG, BUTTON_FONT
from setup import window


def main_window():

    def miles_to_km():
        miles = float(miles_input.get())
        km_value["text"] = round(miles * 1.609, 2)

    miles_input = Entry()
    miles_input.grid(column=1, row=0, padx=10, pady=10)
    miles_input.config(width=15, border=2)

    miles_label = Label(text="Miles")
    miles_label.grid(column=2, row=0, padx=10, pady=10)
    miles_label.config(background=LABEL_BG, font=LABEL_FONT)

    equal_label = Label(text="is equal to")
    equal_label.grid(column=0, row=1, padx=10, pady=10)
    equal_label.config(background=LABEL_BG, font=LABEL_FONT)

    km_value = Label(text="0")
    km_value.grid(column=1, row=1, padx=10, pady=10)
    km_value.config(background=LABEL_BG, font=LABEL_FONT)

    km_label = Label(text="Km")
    km_label.grid(column=2, row=1, padx=10, pady=10)
    km_label.config(background=LABEL_BG, font=LABEL_FONT)

    calc_button = Button(text="Calculate", command=miles_to_km)
    calc_button.grid(column=1, row=2, padx=10, pady=10)
    calc_button.config(background=BUTTON_BG, font=BUTTON_FONT, border=1)

    return window


if __name__ == '__main__':
    app = main_window()
    app.mainloop()
