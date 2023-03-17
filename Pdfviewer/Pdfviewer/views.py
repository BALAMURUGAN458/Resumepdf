from django.shortcuts import render
import webbrowser


def pdf():
    path = "D:/bala resume/N.BALAMURUGAN(02-10-2000.pdf"
    return webbrowser.open_new(path)


pdf()
