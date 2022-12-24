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
                ft.Text(s, size = 25, color=ft.colors.WHITE),
                alignment=ft.alignment.center,
                )

    button = ft.FloatingActionButton(
        icon=ft.icons.MIC_OFF_ROUNDED,
        shape=ft.CircleBorder(),
        bgcolor=ft.colors.RED,
    )

    screentext = ft.AnimatedSwitcher(
        ctext(""),
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.EASE_IN_OUT_SINE,
        switch_out_curve=ft.AnimationCurve.EASE_IN_OUT_SINE,
    )

    images = ft.AnimatedSwitcher(
        ft.Image(),
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.EASE_IN_OUT_SINE,
        switch_out_curve=ft.AnimationCurve.EASE_IN_OUT_SINE,
    )

    def toggle(e):
        global x
        global button
        x = not x
        print(x)

        if x:
            button.bgcolor = ft.colors.GREEN
            button.icon = ft.icons.MIC_ROUNDED
        else:
            button.bgcolor = ft.colors.RED
            button.icon = ft.icons.MIC_OFF_ROUNDED
            screentext.content = ctext("")
            images.content = ctext("")

        page.update()

    button.on_click = toggle

    page.add(
        ft.Container(
            ft.Column(
                [
                    ft.Container(
                        images,
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                screentext,
                                ft.ResponsiveRow([button], alignment=ft.MainAxisAlignment.CENTER),
                            ]
                        ),
                    ),
                ]
            )
        )
    )

    while True:
        if x:
            t = detector()
            screentext.content = ctext(t)
            if t == "imposter":
                images.content = ft.Image(
                    src="https://i.scdn.co/image/ab67616d0000b273cfa5f6193f930ec445785be2",
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                    width=page.width,
                    height=page.height,
                )
            else:
                images.content = ft.Text("")
            page.update()
        else:
            screentext.content = ft.Text("")
            images.content = ft.Text("")
            page.update()

ft.app(target=main)