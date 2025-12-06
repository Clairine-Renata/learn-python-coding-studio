import tkinter as tk

window = tk.Tk()
window.title("My Application")
window.geometry("300x250")

def sapa():
    hasil_nama = entry.get()
    label_output.config(text=f"Halo {hasil_nama}!")
    label_output.pack(pady=20)

    #print(f"Halo {hasil_nama}")
# label
label = tk.Label(window, text="Masukkan Namamu:", font=("Helvetica", 20))
label.pack(pady=5)

# entry
entry = tk.Entry(window, width=20)
entry.pack(pady=5)

# button
button = tk.Button(window, text="Sapa Aku!", command=sapa)
button.pack()

label_output = tk.Label(window, text="", font=("Times New Roman", 15))
label_output.pack()
# jalankan GUI
window.mainloop()