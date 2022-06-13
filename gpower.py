#!/usr/bin/env python3

import gi
from subprocess import run
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Main_window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Power Menu")

        self.set_border_width(50)
        self.button = Gtk.Button("Power off")
        self.button.connect("clicked", self.poweroff)
        self.add(self.button)

    def poweroff(self, widget):
        run("i3lock -c 00000000", shell=True)

window = Main_window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
