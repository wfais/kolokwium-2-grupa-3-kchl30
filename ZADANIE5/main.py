import tkinter as tk

def create_app():

    root = tk.Tk()
    root.title("Prosta aplikacja Tkinter")

    label_instruct = tk.Label(root, text="Wpisz coś:")
    label_instruct.pack()

    entry_text = tk.Entry(root)
    entry_text.pack()

    label_result = tk.Label(root, text="Tu pojawi się Twój tekst")
    label_result.pack()

    def show_text():
        user_text = entry_text.get()
        label_result.config(text=f"Wpisałeś: {user_text}")

    button_show = tk.Button(root, text="Pokaż", command=show_text)
    button_show.pack()

    return root

if __name__ == '__main__':
    app = create_app()
    app.mainloop()
