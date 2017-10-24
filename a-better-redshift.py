#!/usr/bin/python3.5

import os
import gi
import signal
import time

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
gi.require_version('Notify', '0.7')
from gi.repository import Notify as notify

from set_temperature import TemperatureWindow
from set_brightness import BrightnessWindow


def main():
    cwd = os.path.dirname(__file__) + '/icon.png'
    print(cwd)
    indicator = appindicator.Indicator.new("Indicator Volume", os.path.abspath(
        cwd), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()


def build_menu():
    menu = gtk.Menu()

    info = gtk.MenuItem("Click to refresh stats")
    info.connect('activate', refresh, info)
    menu.append(info)

    init()

    temperature = gtk.MenuItem('Set Temperature')
    temperature.connect('activate', set_temperature)
    menu.append(temperature)

    brightness = gtk.MenuItem('Set Brightness')
    brightness.connect('activate', set_brightness)
    menu.append(brightness)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)


    menu.show_all()
    return menu

def init():
    config_path = os.path.abspath(os.path.dirname(__file__)) + "/config"
    file_name = config_path + "/brightness.txt"
    brightness = "10"
    if os.path.exists(file_name):
        with open(file_name, 'rb') as f:
            try:
                brightness = f.read()
            except Exception as e:  # whatever reader errors you care about
                print("ERROR "+e)
                # setting temperature
    print("BRIGHTNESS _ A-BETTER-REDSHIFT "+str(int(brightness)))
    brightness=str(int(brightness))
    if brightness == "10":
        brightness = "1"
    else:
        brightness = "0." + str(int(brightness))


    file_name = config_path + "/temperature.txt"
    int_temperature = 7000
    if os.path.exists(file_name):
        with open(file_name, 'rb') as f:
            try:
                temperature = f.readline()
                int_temperature = int(temperature)
            except(e):  # whatever reader errors you care about
                print("ERROR "+e)
                # setting temperature

    os.system("killall -q redshift")
    command = "redshift -l 40:40 -t " + str(int_temperature) + ":" + str(int_temperature) + " -b " + brightness + ":" + brightness + " &"
    os.system(command)
    print(command)

def refresh(_, info):
    config_path = os.path.abspath(os.path.dirname(__file__)) + "/config"
    file_name = config_path + "/brightness.txt"
    brightness = "10"
    if os.path.exists(file_name):
        with open(file_name, 'rb') as f:
            try:
                brightness = f.read()
            except Exception as e:  # whatever reader errors you care about
                print("ERROR "+e)
                # setting temperature
    print("BRIGHTNESS _ A-BETTER-REDSHIFT "+str(int(brightness)))
    brightness=str(int(brightness))
    if brightness == "10":
        brightness = "1"
    else:
        brightness = "0." + str(int(brightness))


    file_name = config_path + "/temperature.txt"
    int_temperature = 7000
    if os.path.exists(file_name):
        with open(file_name, 'rb') as f:
            try:
                temperature = f.readline()
                int_temperature = int(temperature)
            except(e):  # whatever reader errors you care about
                print("ERROR "+e)
                # setting temperature

    info.set_label("b: "+brightness+"; t: "+str(int_temperature))

def set_temperature(_):
    win1 = TemperatureWindow()
    win1.set_position(gtk.WindowPosition.CENTER)
    win1.show_all()
    win1.set_resizable(False)


def set_brightness(_):
    win1 = BrightnessWindow()
    win1.set_position(gtk.WindowPosition.CENTER)
    win1.show_all()
    win1.set_resizable(False)


def quit(_):
    os.system("killall -q redshift")
    abs_path = os.path.abspath(os.path.dirname(__file__))
    os.system("rm -r __pycache__")
    gtk.main_quit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
