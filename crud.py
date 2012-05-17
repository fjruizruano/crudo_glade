#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

import pygtk
import gtk as Gtk

class Crud_GUI:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("crud.glade")
        self.handlers = {"onDeleteWindow": Gtk.main_quit,
                        "onAboutDialog": self.onAboutDialog,
                        "onCloseAbout": self.onCloseAbout,}
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("window1")
        self.window.show_all()

    def onAboutDialog(self, *args):
        self.about = self.builder.get_object("aboutdialog1")
        self.about.show_all()

    def onCloseAbout(self, *args):
        self.about = self.builder.get_object("aboutdialog1")
        self.about.hide()

def main():
    window = Crud_GUI()
    Gtk.main()
    
    return 0

if __name__ == "__main__":
    main()
