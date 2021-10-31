from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import os
from PIL import Image
import matplotlib.pyplot as plt


# 1. create a window
window = Tk()
window.title("First Window")

"""
# ------------------------------------------------------------------------
# PART1: BOX

# 2. Add a label
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# 3. Set the size of window
window.geometry("400x300")

# 4. Add a button
lbl_button = Label(window, text="1 Button")
lbl_button.grid(column=0, row=2)
btn = Button(window, text="Clik Here")
btn.grid(column=2, row=2)


# 5. Add function to the button
def clicked():
	lbl_button.configure(text="Button was clicked!")
	# handle user input
	# res = "Welcom to " + txt.get()
	#lbl_button.configure(text=res)
btn = Button(window, text="Click Here", command=clicked)
btn.grid(column=2, row=2)


# 6. Add the entry for user input
txt = Entry(window, width=10)
txt.grid(column=1, row=2)
txt.focus()

# 7. Add combo box
lbl_combobox = Label(window, text="2 Combobox")
lbl_combobox.grid(column=0, row=4)
combo = ttk.Combobox(window, width=6)
combo['values'] = (1,2,3,4,5,"Text")
combo.current(1)
combo.grid(column=1, row=4)

# 8. Add check button
lbl_checkbutton = Label(window, text="3 Checkbutton")
lbl_checkbutton.grid(column=0, row=6)
chk_state1 = BooleanVar()
chk_state1.set(True)
chk1 = ttk.Checkbutton(window, text="Choose1", var=chk_state1)
chk1.grid(column=1, row=6)
chk_state2 = BooleanVar()
chk_state2.set(False)
chk2 = ttk.Checkbutton(window, text="Choose2", var=chk_state2)
chk2.grid(column=2, row=6)


# 9. Add radio button
lbl_radiobutton = Label(window, text="4 Radiobutton")
lbl_radiobutton.grid(column=0, row=8)
rad1 = ttk.Radiobutton(window, text="First", value=1)
rad2 = ttk.Radiobutton(window, text="Second", value=2)
rad3 = ttk.Radiobutton(window, text="Third", value=3)
rad1.grid(column=1, row=8)
rad2.grid(column=2, row=8)
rad3.grid(column=3, row=8)

# 10. Add spin box
lbl_spinbox = Label(window, text="5 Spinbox")
lbl_spinbox.grid(column=0, row=10)
spin = Spinbox(window, from_=0, to=10, width=8)
spin.grid(column=1, row=10)


# 11. Add progress bar
lbl_progressbar = Label(window, text="6 Progressbar")
lbl_progressbar.grid(column=0, row=12)
bar = ttk.Progressbar(window, length=100)
bar['value'] = 70
bar.grid(column=3, row=12)
"""


# ------------------------------------------------------------------------
# PART2: MESSAGE
# 1. Add text box
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=0)

# 2. Add message box
def clicked_messagebox():
	messagebox.showinfo("Message title", "Message content")
btn = Button(window, text="Message", command=clicked_messagebox)
btn.grid(column=0, row=2)

# 3. Add file open button
def clicked_openfile():
	file = filedialog.askopenfilename(initialdir=os.path.dirname(__file__))
	image = Image.open(file)
	plt.imshow(image)
	plt.show()
btn_file = Button(window, text="Open File", command=clicked_openfile)
btn_file.grid(column=0, row=4)



window.mainloop()