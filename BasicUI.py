import tkinter as tk
import ttkbootstrap as ttk
import time
import random

# Start
window = ttk.Window(themename="darkly")
window.geometry("500x350")
window.title("Sticks N Slippers")
# Frames
shop_frame = ttk.Frame()
name_frame = ttk.Frame()
main_frame = ttk.Frame()
fight_frame = ttk.Frame()
name_frame.pack()

# Definitions
def name_set():
    name_button.pack(pady=5)
    name = name_entry.get()
    main_frame.pack()
    label.pack()
    name_frame.destroy()
    shop_button.pack()
    fight_button.pack()

    label_value.set(f"{name} the unbeatable.")
    print(name)

attack_button = ttk.Button(master=fight_frame, text="Attack")
heal_button = tk.Button(master=fight_frame, text="Heal")

def Shop():
    pass

def Fight():
    main_frame.destroy()
    shop_button.destroy()
    fight_button.destroy()
    fight_frame.pack()
    attack_button.pack()
    heal_button.pack()

# Setting Name
name_value = tk.StringVar()
name_entry = tk.Entry(master=name_frame, textvariable=name_value, justify="center")
name_label = tk.Label(master=name_frame, text= "Enter Nickname")
name_button = tk.Button(master=name_frame, text="Set Name", command=name_set)
name_label.pack()
name_entry.pack()
name_button.pack(pady=5)


# Main Menu
label_value = tk.StringVar()
label = ttk.Label(master=main_frame, textvariable=label_value)
shop_button = ttk.Button(master=main_frame, text="Shop", command=Shop())
fight_button = ttk.Button(master=main_frame, text="Fight", command=Fight)
# Shop Menu

# In-Game Menu

# Definitions


# Run
window.mainloop()
