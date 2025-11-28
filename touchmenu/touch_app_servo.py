#!/usr/bin/env python3
import tkinter as tk
from servo_test_b1 import run_servo_test1
from servo_test_b1 import run_servo_test2
from time import sleep
from adafruit_servokit import ServoKit


# -------------------------------------------------------------
# App Framework
# -------------------------------------------------------------
class TouchApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Touchscreen App")
        self.attributes("-fullscreen", True)
        self.configure(bg="black")

        # Escape key exits fullscreen (only for debugging)
        self.bind("<Escape>", lambda e: self.destroy())

        # Container for pages
        self.container = tk.Frame(self, bg="black")
        self.container.pack(fill="both", expand=True)

        # Dictionary of pages
        self.pages = {}

        # Add your pages here
        for Page in (HomePage, SettingsPage, InfoPage):
            page = Page(parent=self.container, controller=self)
            self.pages[Page] = page
            page.place(relwidth=1, relheight=1)

        self.show_page(HomePage)

    def show_page(self, page_class):
        """Bring a page to the top."""
        page = self.pages[page_class]
        page.tkraise()


# -------------------------------------------------------------
# Component: Touch Button (bigger, friendlier)
# -------------------------------------------------------------
class TouchButton(tk.Button):
    def __init__(self, parent, text, command):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=("Arial", 24),
            height=2,
            width=12,
            bg="#444",
            fg="white",
            activebackground="#666",
            bd=0,
            relief="flat"
        )


# -------------------------------------------------------------
# PAGE 1: Home Page
# -------------------------------------------------------------
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        tk.Label(
            self, text="Home Page", font=("Arial", 36),
            bg="black", fg="white"
        ).pack(pady=40)

        TouchButton(self, "Servo 1",
                    lambda: run_servo_test1()).pack(pady=20)

        TouchButton(self, "Servo 2",
                    lambda: run_servo_test2()).pack(pady=20)

        TouchButton(self, "Exit",
                    lambda: controller.destroy()).pack(pady=60)


# -------------------------------------------------------------
# PAGE 2: Settings Page
# -------------------------------------------------------------
class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        tk.Label(
            self, text="Settings", font=("Arial", 36),
            bg="black", fg="white"
        ).pack(pady=40)

        TouchButton(self, "Back to Home",
                    lambda: controller.show_page(HomePage)).pack(pady=20)


# -------------------------------------------------------------
# PAGE 3: Info Page
# -------------------------------------------------------------
class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        tk.Label(
            self, text="Information Screen", font=("Arial", 36),
            bg="black", fg="white"
        ).pack(pady=40)

        tk.Label(
            self, text="This is an example of a multi-page\n"
                       "touchscreen interface.",
            font=("Arial", 22), bg="black", fg="white",
            justify="center"
        ).pack(pady=40)

        TouchButton(self, "Back",
                    lambda: controller.show_page(HomePage)).pack(pady=20)


# -------------------------------------------------------------
# Run App
# -------------------------------------------------------------
if __name__ == "__main__":
    app = TouchApp()
    app.mainloop()
