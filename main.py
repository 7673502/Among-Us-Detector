from pocketsphinx import LiveSpeech
from playsound import playsound
import flet as ft
import _thread
import time

x = False
button = None

def main(page: ft.Page):
    page.title = "Among Us Detector"
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.fonts = {
        "JetBrains Mono" : "https://github.com/7673502/Among-Us-Detector/blob/main/font/JetBrainsMono-Regular.ttf?raw=true"
    }

    page.theme = ft.Theme(font_family = "JetBrains Mono")

    global button

    def find_multiple(text, keys):
        for i in keys:
            if text.find(i) != -1:
                return True
        return False

    def detector():
        for phrase in LiveSpeech():
            print(phrase)
            if find_multiple(str(phrase), ["imposter", "crew mate", "impostor"]):
                _thread.start_new_thread(playsound, ("audio/role_reveal.mp3",))
            elif find_multiple(str(phrase), ["emergency", "meeting", "suspic"]):
                _thread.start_new_thread(playsound, ("audio/emergency_meeting.mp3",))
            elif find_multiple(str(phrase), ["among drip"]):
                _thread.start_new_thread(playsound, ("audio/among_drip.mp3",))
            elif find_multiple(str(phrase), ["among"]):
                _thread.start_new_thread(playsound, ("audio/amogus.mp3",))
            return str(phrase)

    def ctext(s):
        return ft.Container(
            ft.Text(s,
                    size = 25,
                    color=ft.colors.WHITE),
            alignment=ft.alignment.center,
        )

    button = ft.FloatingActionButton(
        content=ft.Icon(name=ft.icons.MIC_OFF_ROUNDED, color=ft.colors.WHITE),
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
        ctext(""),
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=500,
        reverse_duration=500,
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
            button.content=ft.Icon(name=ft.icons.MIC_ROUNDED, color=ft.colors.WHITE)
        else:
            button.bgcolor = ft.colors.RED
            button.content=ft.Icon(name=ft.icons.MIC_OFF_ROUNDED, color=ft.colors.WHITE)
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
            if find_multiple(t, ["imposter", "suspic", "impostor"]):
                images.content = ft.Image(
                    src="https://github.com/7673502/Among-Us-Detector/blob/main/images/impostersus.jpeg?raw=true",
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                    width=page.width,
                    height=page.height,
                )
                page.update()
                time.sleep(2)
            elif find_multiple(t, ["emergency", "meeting"]):
                images.content = ft.Image(
                    src="https://github.com/7673502/Among-Us-Detector/blob/main/images/emergencymeeting.png?raw=true",
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                    width=page.width,
                    height=page.height,
                )
                page.update()
                time.sleep(2)
            elif find_multiple(t, ["among", "crew mate"]):
                images.content = ft.Image(
                    src="https://github.com/7673502/Among-Us-Detector/blob/main/images/redcrewmate.png?raw=true",
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10),
                    width=page.width,
                    height=page.height,
                )
                page.update()
                time.sleep(2)
            images.content = ft.Text("")
            page.update()
        else:
            screentext.content = ft.Text("")
            images.content = ft.Text("")
            page.update()

ft.app(target=main)