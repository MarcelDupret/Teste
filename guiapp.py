import tkinter as tk
win = tk.Tk()
win.title("Aplicação GUI com tkinter")
tk.Label(win,text="Componente Label").grid(column=0,row=0)
win.mainloop()