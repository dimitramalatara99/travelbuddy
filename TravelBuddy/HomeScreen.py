import tkinter as tk
from tkinter import ttk


class HomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Business Directory")

        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
