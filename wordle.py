import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def clear(*v):
    vars[0].set('*****')
    vars[1].set('')
    vars[2].set('')

def refresh(*v):
    s1 = vars[0].get().lower()
    s2 = vars[1].get().lower()
    s3 = vars[2].get().lower()

    for c in ' _*?':
        s1 = s1.replace(c, '[a-z]')
    patt = re.compile(s1, re.I)

    results = [w for w in words
               if  all(c     in w.lower() for c in s2)
               and all(c not in w.lower() for c in s3)
               and patt.fullmatch(w)]

    txt.delete('1.0', 'end')
    txt.insert('1.0', '\n'.join(results))


with open('words.txt') as f:
    words = f.read().strip().split('\n')

top = tk.Tk()
top.title('Wordle Assistant')
top.resizable(0, 0)

vars = []
for i, name in enumerate(['Pattern', 'Include', 'Exclude']):
    var = tk.StringVar()
    var.trace('w', refresh)
    vars.append(var)
    tk.Label(top, text=name+':').grid(row=0, column=i*2)
    tk.Entry(top, textvariable=var).grid(row=0, column=i*2+1)

txt = ScrolledText(top)
txt.grid(row=3, column=0, columnspan=6)
top.bind('<Escape>', clear)

vars[0].set('*****')

top.mainloop()
