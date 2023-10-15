import tkinter as tk

window = tk.Tk()
window.title('Simple Python GUI Calculator')

root_frame = tk.Frame(window)
window.geometry('650x600')

display_frame = tk.LabelFrame(root_frame, width=400, height=80)
display_frame.grid(row=0, column=0, pady=(10, 10))
display_frame.grid_propagate(0)

keypad_frame = tk.LabelFrame(root_frame, width=400, height=450)
keypad_frame.grid(row=1, column=0, padx=10, pady=(10, 10))
keypad_frame.grid_propagate(0)

numbers_frame = tk.LabelFrame(keypad_frame, width=260, height=400)
numbers_frame.grid(row=0, column=0, padx=(10, 20), pady=(10, 10))
numbers_frame.grid_propagate(0)

signs_frame = tk.LabelFrame(keypad_frame, width=100, height=400)
signs_frame.grid(row=0, column=1, pady=(10, 10))
signs_frame.grid_propagate(0)

root_frame.pack()

window.mainloop()
