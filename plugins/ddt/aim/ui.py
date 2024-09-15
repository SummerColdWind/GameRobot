import tkinter as tk
from tkinter import ttk

from plugins.ddt.aim.core import AimCore

class AimUI(tk.Tk):
    def __init__(self, handle):
        super().__init__()

        self.core = AimCore(handle)

        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.configure(bg='#ADD8E6')  # 淡蓝色
        self.attributes("-alpha", 0.95)  # 设置透明度，范围0.0到1.0
        self.geometry('200x100')  # 稍微增大窗口以适应现代化设计

        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>', self.click_win)
        self.bind('<B1-Motion>', self.drag_win)

        self.label = None
        self.force = 0

        self.create_widgets()
        self.mainloop()


    def click_win(self, event):
        """记录鼠标点击时的偏移量"""
        self._offsetx = event.x
        self._offsety = event.y

    def drag_win(self, event):
        """拖动窗口"""
        x = event.x_root - self._offsetx
        y = event.y_root - self._offsety
        self.geometry(f'+{x}+{y}')

    def get_position(self):
        """
        获取窗口左上角的位置坐标。

        Returns:
            tuple: (x, y) 窗口左上角的 x 和 y 坐标。
        """
        self.update_idletasks()  # 确保获取到最新的位置
        x = self.winfo_x()
        y = self.winfo_y()
        return x, y

    def update_force(self):
        self.label.config(text=f"预测力度: {round(self.force, 1)}")

    def shot(self):
        self.core.shot(self.force)

    def aim(self):
        self.force = self.core.predict(self.get_position())
        self.update_force()

    def create_widgets(self):
        style = ttk.Style(self)
        style.theme_use('clam')  # 使用 'clam' 主题

        # 自定义按钮样式
        style.configure('TButton',
                        background='#4A90E2',
                        foreground='white',
                        font=('Segoe UI', 10, 'bold'),
                        borderwidth=0)
        style.map('TButton',
                  background=[('active', '#357ABD')])

        # 自定义标签样式
        style.configure('TLabel',
                        background='#ADD8E6',
                        foreground='#333333',
                        font=('Segoe UI', 10))

        # 使用 grid 布局管理器
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # 第一行 Label1
        label1 = ttk.Label(self, text="将此窗口左上角对准炮弹落点", style='TLabel')
        label1.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=0, pady=0)

        # 第二行 Label2
        label2 = ttk.Label(self, text="", style='TLabel')
        label2.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=0, pady=0)
        self.label = label2
        self.update_force()

        # 第三行 三个按钮 A, B, X
        button_a = ttk.Button(self, text="计算", command=self.aim)
        button_a.grid(row=2, column=0, sticky="nsew", padx=0, pady=0)

        button_b = ttk.Button(self, text="发射", command=self.shot)
        button_b.grid(row=2, column=1, sticky="nsew", padx=0, pady=0)

        button_x = ttk.Button(self, text="关闭", command=self.destroy)
        button_x.grid(row=2, column=2, sticky="nsew", padx=0, pady=0)
