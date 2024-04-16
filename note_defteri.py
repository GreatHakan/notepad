import tkinter as tk

def save_file():
    with open("note.txt", "a") as file:
        content = text_area.get("1.0", tk.END)
        file.write(content)


# pythonda temelde 3 mod ile dosya açılabilir:
# 1. "r" (read): Dosyayı sadece okuma modunda açar.
# 2. "w" (write): Dosyayı yazma modunda açar. 
# 3. "a" (append): Dosyanın sonuna ekler. 

pencere = tk.Tk()
pencere.title("Not Defteri")

text_area = tk.Text(pencere)
text_area.pack()                              

save_button = tk.Button(pencere, text="Save", command=save_file)
save_button.pack(side=tk.LEFT)

exit_button = tk.Button(pencere, text="Exit", command=pencere.destroy)
exit_button.pack(side=tk.RIGHT)

pencere.mainloop()