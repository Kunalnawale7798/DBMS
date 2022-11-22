from tkinter import *
window=Tk()
window['bg'] = 'blue'
lbl=Label(window, text="Name: Sahil Bhawat ", fg='olive')
lbl.place(x=60, y=50)
btn=Button(window, text="Roll No: 4", fg='purple')
btn.place(x=150, y=100)
window.title('Welcome to PVG')
window.geometry("300x200+10+10")
window.mainloop()
