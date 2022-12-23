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

    button = ft.FloatingActionButton(content = ft.Image(src = "images/Among Us.svg", color=ft.colors.WHITE),
                               shape=ft.CircleBorder(),
                                bgcolor=ft.colors.GREEN,

                               )
    def toggle(e):
        global x
        global button
        x = not x
        print(x)

        if x:
            button.bgcolor = ft.colors.RED
        else:
            button.bgcolor = ft.colors.GREEN

        page.update()

    button.on_click = toggle

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

    '''page.add(
        ft.Stack([images,
            ft.Column([
            screentext,
            ft.Row(
                controls=[button],
                alignment=ft.MainAxisAlignment.CENTER,
            ),])
        ]
        )
    )'''

    page.add(
        ft.Container(
            ft.Stack(
                [
                    ft.Container(
                        images,
                        left=0,
                        right=0,
                        top=0,
                        bottom=0,
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                screentext,
                                ft.Row([button], alignment=ft.MainAxisAlignment.CENTER),
                            ]
                        )
                    ),
                ]
            )
        )
    )

    while True:
        if x:
            images.content = ft.Image(
                    src="https://i.scdn.co/image/ab67616d0000b273cfa5f6193f930ec445785be2",
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                    width=page.width,
                    height=page.height,
                )
            t = detector()
            screentext.content = ctext(t)
            page.update()
        else:
            screentext.content = ft.Text("")
            images.content = ft.Text("")
            page.update()

ft.app(target=main)