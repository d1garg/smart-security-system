import cv2
import time
import os
import tkinter as tk

def check_password():
    # 📸 STEP 1: Photo capture
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()

    if ret:
        filename = f"photo_{int(time.time())}.png"
        cv2.imwrite(filename, frame)
    else:
        filename = None

    cam.release()

    # 🔐 STEP 2: Password check
    password = entry.get()

    if password == "1234":
        result_label.config(text="Access Granted ✅", fg="green")

        # 🗑️ delete photo if correct
        if filename and os.path.exists(filename):
            os.remove(filename)

    else:
        result_label.config(text="Wrong Password ❌", fg="red")
        # photo will remain saved 😈


# 🎨 GUI setup
root = tk.Tk()
root.title("Secure Login System")
root.geometry("300x200")

label = tk.Label(root, text="Enter Password")
label.pack(pady=10)

entry = tk.Entry(root, show="*")
entry.pack(pady=5)

button = tk.Button(root, text="Login", command=check_password)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
