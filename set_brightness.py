#!/usr/bin/python3.5
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os


class BrightnessWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Set Brightness")
        self.set_icon_from_file(os.path.dirname(__file__) + "/icon.png")

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(box)

        # ENTRY
        self.entry = Gtk.Entry()
        self.entry.set_width_chars(40)
        box.add(self.entry)
        self.label = Gtk.Label()
        box.add(self.label)

        # self.button = Gtk.Button(label="Search")
        # self.button.connect("clicked", self.on_button_clicked, self.entry)
        self.entry.connect("activate", self.on_button_clicked,
                           self.entry, self.label)
        # box.add(self.button)

    def on_button_clicked(self, widget, entry, label):
        value = entry.get_text()

        try:
            if int(value) < 1 or int(value) > 10:
                label.set_text("Insert a value between 1 and 10")
                return
        except TypeError:
            value = "10"
        except:
            label.set_text("Insert a real number")
            return


        config_path = os.path.abspath(os.path.dirname(__file__)) + "/config"
        if not os.path.exists(config_path):
            os.system("mkdir " + config_path)
        os.system("rm " + config_path + "/brightness.txt")
        os.system("echo " + value + " > " +
                  config_path + "/brightness.txt")

        # saving to file temperature.txt
        if value == "10":
            value = "1"
        else:
            value = "0." + value
        # reading temperature
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
        command="redshift -l 40:40 -b " + value + ":" + value + " -t " + str(int_temperature) + ":" + str(int_temperature) + " &"
        os.system(command)
        print(command)
        self.destroy()
