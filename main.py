from tkinter import *
import time


def on_enter_pressed():
    text.insert(END, "\n")


def update_text_width(event):
    text.config(width=event.width//10)


def typing(event):
    if event.char.isalnum():
        app.after_cancel(after_id)


def not_typing(event):
    global after_id
    after_id = app.after(4000, disappear_text)


def disappear_text():
    if text.get("1.0", "end-1c") == "Start Typing":
        text.delete("1.0", "end-1c")
        text.config(fg="black")
    else:
        text.delete("1.0", "end")


def on_focus_in(event):
    if text.get("1.0", "end-1c") == "Start Typing":
        text.delete("1.0", "end-1c")
        text.config(fg="black")


def on_focus_out(event):
    if not text.get("1.0", "end-1c"):
        text.insert("1.0", "Start Typing")
        text.config(fg="gray")


app = Tk()
app.geometry("500x400")
app.title("Message Disappearing app")
app.config(bg="cyan")

text = Text(wrap="word", bg="cyan",  borderwidth=0, fg="gray")
text.insert("1.0", "Start Typing")
text.pack(fill="both", expand=True, padx=5, pady=5)

text.bind('<Return>', on_enter_pressed)
app.bind('<Configure>', update_text_width)

text.bind("<Key>", typing)
text.bind("<KeyRelease>", not_typing)

text.bind("<FocusIn>", on_focus_in)
text.bind("<FocusOut>", on_focus_out)

after_id = None

app.mainloop()

