from pocketsphinx import LiveSpeech
from playsound import playsound
import flet as ft
import _thread

x = False
button = None

def main(page: ft.Page):
    page.title = "Among Us Detector"
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    global button

    def detector():
        for phrase in LiveSpeech():
            print(phrase)
            if str(phrase).find("imposter") != -1 or str(phrase).find("crew mate") != -1:
                _thread.start_new_thread(playsound, ("audio/role_reveal.mp3",))
            elif str(phrase).find("emergency") != -1 or str(phrase).find("meeting") != -1:
                _thread.start_new_thread(playsound, ("audio/emergency_meeting.mp3",))
            elif str(phrase).find("among") != -1:
                _thread.start_new_thread(playsound, ("audio/amogus.mp3",))
            return str(phrase)

    def ctext(s):
        return ft.Container(
                ft.Text(s, size = 25),
                alignment=ft.alignment.center,
                )

    button = ft.ElevatedButton(text="amog",
                               style=ft.ButtonStyle(#shape=ft.CircleBorder(),
                                                    padding=30,
                                                    bgcolor=ft.colors.GREEN, ),
                               )

    def toggle(e):
        global x
        global button
        x = not x
        print(x)

        if x:
            button.style.bgcolor = ft.colors.RED
        else:
            button.style.bgcolor = ft.colors.GREEN

        page.update()

    button.on_click = toggle

    c = ft.AnimatedSwitcher(
        ctext(""),
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.EASE_IN_OUT_SINE,
        switch_out_curve=ft.AnimationCurve.EASE_IN_OUT_SINE,
    )

    page.add(
        c,
        ft.ResponsiveRow(
            controls=[button],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    while True:
        if x:
            t = detector()
            c.content = ctext(t)
            page.update()
        else:
            c.content = ctext("")
            page.update()

ft.app(target=main)