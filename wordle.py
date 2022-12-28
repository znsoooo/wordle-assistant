import re
import tkinter as tk

def refresh(*v):
    s1 = vars[0].get()
    s2 = vars[1].get()
    s3 = vars[2].get()

    for c in ' _*?':
        s1 = s1.replace(c, '.')
    patt = re.compile(s1)

    results = [w for w in words
               if  all(c     in w for c in s2)
               and all(c not in w for c in s3)
               and patt.fullmatch(w)]

    txt.delete('1.0', 'end')
    txt.insert('1.0', '\n'.join(results))


with open('words.txt') as f:
    words = f.read().strip().split('\n')

top = tk.Tk()
top.title('Wordle Assistant')

vars = []
for i, name in enumerate(['Green', 'Yellow', 'Gray']):
    var = tk.StringVar()
    var.trace('w', refresh)
    vars.append(var)
    tk.Label(top, text=name+':').grid(row=0, column=i*2)
    tk.Entry(top, textvariable=var).grid(row=0, column=i*2+1)

txt = tk.Text(top)
txt.grid(row=3, column=0, columnspan=6)

vars[0].set('*****')

top.mainloop()
