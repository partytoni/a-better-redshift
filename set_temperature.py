#!/usr/bin/python3.5
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os


class TemperatureWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Set Temperature")
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
            if int(value) < 1000 or int(value) > 25000:
                label.set_text("Insert a value between 1000 and 25000")
                return
        except TypeError:
            value = "7000"
        except Exception as e:
            label.set_text("Insert a real number")
            print("ERROR "+str(e))
            return
        # saving to file temperature.txt
        config_path = os.path.abspath(os.path.dirname(__file__)) + "/config"
        if not os.path.exists(config_path):
            os.system("mkdir " + config_path)
        os.system("rm " + config_path + "/temperature.txt")
        os.system("echo " + value + " > " +
                  config_path + "/temperature.txt")

        # reading brightness
        file_name = config_path + "/brightness.txt"
        int_brightness = 1
        if os.path.exists(file_name):
            with open(file_name, 'rb') as f:
                try:
                    brightness = f.readline()
                    int_brightness = int(brightness)
                except:  # whatever reader errors you care about
                    print("ERROR\n\n")
                    # setting temperature
        print("INT BRIGHTNESS _ SET TEMPERATURE: "+str(int_brightness))
        if int_brightness == 10:
            brightness = "1"
        else:
            brightness = "0." + str(int_brightness)

        os.system("killall -q redshift")
        command = "redshift -l 40:40 -t " + value + ":" + value + " -b " + brightness + ":" + brightness + " &"
        os.system(command)
        print(command)
        self.destroy()
