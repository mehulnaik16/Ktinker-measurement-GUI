import tkinter as tk

def centi():
    cm = float(centi.get())
    res = cm * 0.0328
    A.config(text=str(res))

def feet():
    feet = float(feet.get())
    res = feet * 12
    B.config(text=str(res))

def sqft():
    sqft = float(sqft.get())
    res = sqft * 0.0929
    C.config(text=str(res))

def sq():
    sqft = float(sq.get())
    res = sqft / 43560
    D.config(text=str(res))

window = tk.Tk()
window.title("converter")
window.geometry("600x300")

frame1 = tk.Frame(window)
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = tk.Frame(window)
frame2.grid(row=0, column=1, padx=10, pady=10)

frame3 = tk.Frame(window)
frame3.grid(row=1, column=0, padx=10, pady=10)

frame4 = tk.Frame(window)
frame4.grid(row=1, column=1, padx=10, pady=10)

a = tk.Label(frame1, text="Centimeter to Feet", height=2, width=17, borderwidth=3, relief="solid", bg="blue", fg="white", font=("Arial Black", 10))
a.grid(row=0, column=0, columnspan=2, pady=5)

centi = tk.Entry(frame1, width=20, relief="solid")
centi.grid(row=1, column=0, padx=5, pady=5)

button_centi = tk.Button(frame1, text="Click me!", borderwidth=3, relief="solid", bg="blue", fg="white", command=centi)
button_centi.grid(row=1, column=1, padx=5, pady=5)

one = tk.Label(frame1, text="Solution:", bg="blue", fg="white")
one.grid(row=2, column=0, padx=5, pady=5)

A = tk.Label(frame1, text="", borderwidth=1, width=18, relief="solid")
A.grid(row=2, column=1, padx=5, pady=5)

b = tk.Label(frame2, text="Feet to Inches", height=2, width=17, borderwidth=3, relief="solid", bg="blue", fg="white", font=("Arial Black", 10))
b.grid(row=0, column=0, columnspan=2, pady=5)

feet = tk.Entry(frame2, width=20, relief="solid")
feet.grid(row=1, column=0, padx=5, pady=5)

button_feet = tk.Button(frame2, text="Click me!", borderwidth=3, relief="solid", bg="blue", fg="white", command=feet)
button_feet.grid(row=1, column=1, padx=5, pady=5)

two = tk.Label(frame2, text="Solution:", bg="blue", fg="white")
two.grid(row=2, column=0, padx=5, pady=5)

B = tk.Label(frame2, text="", borderwidth=1, width=18, relief="solid")
B.grid(row=2, column=1, padx=5, pady=5)

c = tk.Label(frame3, text="Sqft to Sqmtrs", height=2, width=17, borderwidth=3, relief="solid", bg="blue", fg="white", font=("Arial Black", 10))
c.grid(row=0, column=0, columnspan=2, pady=5)

sqft = tk.Entry(frame3, width=20, relief="solid")
sqft.grid(row=1, column=0, padx=5, pady=5)

button_sqft = tk.Button(frame3, text="Click me!", borderwidth=3, relief="solid", bg="blue", fg="white", command=sqft)
button_sqft.grid(row=1, column=1, padx=5, pady=5)

three = tk.Label(frame3, text="Solution:", bg="blue", fg="white")
three.grid(row=2, column=0, padx=5, pady=5)

C = tk.Label(frame3, text="", borderwidth=1, width=18, relief="solid")
C.grid(row=2, column=1, padx=5, pady=5)

d = tk.Label(frame4, text="Sqft to Acres", height=2, width=17, borderwidth=3, relief="solid",bg="blue", fg="white", font=("Arial Black", 10))
d.grid(row=0, column=0, columnspan=2, pady=5)

sq = tk.Entry(frame4, width=20, relief="solid")
sq.grid(row=1, column=0, padx=5, pady=5)

button_sq = tk.Button(frame4, text="Click me!", borderwidth=3, relief="solid", bg="blue", fg="white", command=sq)
button_sq.grid(row=1, column=1, padx=5, pady=5)

four = tk.Label(frame4, text="Solution:",bg="blue", fg="white")
four.grid(row=2, column=0, padx=5, pady=5)

D = tk.Label(frame4, text="", borderwidth=1, width=18, relief="solid")
D.grid(row=2, column=1, padx=5, pady=5)

window.mainloop()
