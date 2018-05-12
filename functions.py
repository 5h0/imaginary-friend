import os
import webbrowser


def _shutdown():
    os.system("poweroff")


def _restart():
    os.system("reboot")


def _terminal():
    os.system("konsole")

def _mail():
    webbrowser.open('https://www.google.com/gmail/', new=2)


def _facebook():
    webbrowser.open('https://www.facebook.com/', new=2)


def _youtube():
    webbrowser.open('https://www.youtube.com/', new=2)


def _deezer():
    webbrowser.open('https://www.deezer.com/en/', new=2)


def _browser():
    webbrowser.open('https://www.google.com/', new=2)
