# import library 
import tkinter as tk# library tkinter

# Kita akan membuat window/jendela
window = tk.Tk()
# membuat judul dari window
window.title("My Application")
# atur ukuran dari window
window.geometry("300x250") # ini dalam bentuk px

# membuat label
label = tk.Label(window, text="Kelas Python Coding Studio", font=("Calibry", 15))
label.pack(pady=10) # tumpuk
# pady = jarak y-axis; padx = jarak x-axis

label2 = tk.Label(window, text="Ini Sesi Pembelajaran GUI")
label2.pack(pady=10)

label3 = tk.Label(window, text="Ini Sesi Pembelajaran GUI2")
label3.pack(pady=10)
# jalankan App


window.mainloop()