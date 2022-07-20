#!/usr/bin/env python3

import gi
from subprocess import run
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Main_window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Power Menu")

        self.set_border_width(20)

        # self.power = Gtk.Button("Power off")
        # self.power.connect("clicked", self.poweroff)
        # self.add(self.power)

        self.lockbutton = Gtk.Button("Lock")
        self.lockbutton.connect("clicked", self.lock)
        self.add(self.lockbutton)

        self.sleep= Gtk.Button("Lock")
        self.sleep.connect("clicked", self.suspend)
        self.add(self.sleep)

    def lock(self, widget):
        run("i3lock -c 00000000", shell=True)

    def suspend(self, widget):
        run("systemctl suspend", shell=True)

    def poweroff(self, widget):
        run("poweroff", shell=True)


window = Main_window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
