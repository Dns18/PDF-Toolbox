"""PDF Toolbox – belépési pont.  Indítás:  python main.py"""

import customtkinter as ctk

from gui.pages import (CompressPage, ExtractTextPage, ImagesToPdfPage, MergePage,
                       PagesPage, RotatePage, SecurityPage, SplitPage, WatermarkPage)

ctk.set_appearance_mode("dark")          # "dark", "light" vagy "system"
ctk.set_default_color_theme("blue")      # "blue", "green" vagy "dark-blue"

# Ez a lista adja az oldalsáv menüpontjait.
# Lépésről lépésre haladhatsz: kezdd csak az első sorral, és a többit
# kommentből kivéve add hozzá egyesével, ahogy elkészülsz velük.
PAGES = [
    ("Összefűzés", MergePage),
    ("Szétvágás", SplitPage),
    ("Forgatás", RotatePage),
    ("Törlés / átrendezés", PagesPage),
    ("Szövegkinyerés", ExtractTextPage),
    ("Képek → PDF", ImagesToPdfPage),
    ("Vízjel", WatermarkPage),
    ("Jelszó", SecurityPage),
    ("Tömörítés", CompressPage),
]


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PDF Toolbox")
        self.geometry("1000x700")
        self.minsize(880, 620)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Bal oldali menü
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.pack_propagate(False)
        ctk.CTkLabel(self.sidebar, text="PDF Toolbox",
                     font=ctk.CTkFont(size=22, weight="bold")).pack(padx=20, pady=(26, 22))

        # Jobb oldali tartalom
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=0, column=1, sticky="nsew", padx=28, pady=24)

        self.pages = {}
        self.nav_buttons = {}
        for name, page_class in PAGES:
            button = ctk.CTkButton(
                self.sidebar, text=name, anchor="w", height=38,
                fg_color="transparent", text_color=("gray10", "gray90"),
                hover_color=("gray75", "gray30"),
                command=lambda name=name: self.show_page(name))
            button.pack(fill="x", padx=12, pady=2)
            self.nav_buttons[name] = button
            self.pages[name] = page_class(self.content)

        self.show_page(PAGES[0][0])

    def show_page(self, name):
        """Csak a kiválasztott oldal látszik, a menüpont kiemelve."""
        for page in self.pages.values():
            page.pack_forget()
        self.pages[name].pack(fill="both", expand=True)

        for button_name, button in self.nav_buttons.items():
            active = button_name == name
            button.configure(fg_color=("gray75", "gray25") if active else "transparent")


if __name__ == "__main__":
    App().mainloop()
