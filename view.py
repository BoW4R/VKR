import customtkinter as ct
from tkinter import *

import settings
from controller import get_sensors, calculate_desired_speed


class Window(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Вычисление оптимальной скорости")
        self.geometry(f"{settings.VIEW_WINDOW_PARAMS['width']}x"
                      f"{settings.VIEW_WINDOW_PARAMS['height']}+"
                      f"{settings.VIEW_WINDOW_PARAMS['x_shift']}+"
                      f"{settings.VIEW_WINDOW_PARAMS['y_shift']}")
        self.resizable(False, False)
        self.bind_all("<Key>", self._on_key_release, "+")
        ct.set_appearance_mode("light")
        self.distance = StringVar()
        self.temperature = StringVar()
        self.humidity = StringVar()
        self.desired_speed = StringVar()
        self.init_data()
        self.init_menu()

    def init_data(self):
        data = get_sensors()
        data["desired_speed"] = round(calculate_desired_speed(data), 2)
        self.distance.set(data["distance_to_obstacle"])
        self.temperature.set(data["temperature"])
        self.humidity.set(data["humidity"])
        self.desired_speed.set(data["desired_speed"])

    def _on_key_release(self, event):
        """Позволяет копировать, вставлять и вырезать при русской раскладке"""
        ctrl = (event.state & 0x4) != 0
        if event.keycode == 88 and ctrl and event.keysym.lower() != "x":
            event.widget.event_generate("<<Cut>>")

        if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
            event.widget.event_generate("<<Paste>>")

        if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
            event.widget.event_generate("<<Copy>>")

        if event.keycode == 65 and ctrl and event.keysym.lower() != "a":
            event.widget.event_generate("<<SelectAll>>")

    def init_menu(self):
        """Инициализация вкладок окна"""
        window_tabview = ct.CTkTabview(self)
        window_tabview.pack(fill='both', expand=TRUE)
        frame_names = ["Отображение", "Редактор"]
        for name in frame_names:
            window_tabview.add(name)
            window_tabview.tab(name).grid_columnconfigure(0)
        self.init_main(window_tabview.tab(frame_names[0]))
        self.init_settings(window_tabview.tab(frame_names[1]))

    def init_main(self, frame):
        """Инициализация вкладки создания аккаунтов"""
        fields = {
            "Расстояние: ": self.distance,
            "Температура: ": self.temperature,
            "Влажность: ": self.humidity,
            "Оптимальная скорость: ": self.desired_speed,
        }
        for index, (field_name, field_value) in enumerate(fields.items()):
            ct.CTkLabel(
                frame,
                text=field_name,
                font=ct.CTkFont(size=settings.VIEW_FONT_SIZE),
            ).grid(column=0, row=index, pady=3, padx=(150, 3), sticky="e")
            ct.CTkLabel(
                frame,
                textvariable=field_value,
                font=ct.CTkFont(size=settings.VIEW_FONT_SIZE),
            ).grid(column=1, row=index, pady=3, sticky="w")

        update_button = ct.CTkButton(
            frame,
            text="Обновить датчики",
            font=ct.CTkFont(size=settings.VIEW_FONT_SIZE),
            command=self.init_data
        )
        update_button.grid(column=0, columnspan=2, row=4, pady=3, padx=(140, 0))

    def init_settings(self, frame) -> None:
        """Инициализация вкладки с настройками"""
        pass

    # def report_callback_exception(self, exc, val, tb) -> None:
    #     if exc is AccountProcessingError:
    #         self.feedback_text.set(val)


def mainloop():
    app = Window()
    app.mainloop()
