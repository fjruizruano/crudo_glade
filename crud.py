#!/usr/bin/python
# -*- coding: utf-8 -*-

# Al principio es necesario crear una base de datos con MySQL
# $ mysql -u root -p
# > CREATE DATABASE DBdeCrud;
# > GRANT ON ALL DBdeCrud.* TO "crud"@"localhost" IDENTIFIED BY "crudpass";
# > USE DBdeCrud
# > QUIT

import MySQLdb

import pygtk
import gtk as Gtk

class Crud_GUI:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("crud.glade")
        self.handlers = {"onDeleteWindow": Gtk.main_quit,
                        "onCrearActivate": self.onCrearActivate,
                        "onObtenerActivate": self.onObtenerActivate,
                        "onActualizarActivate": self.onActualizarActivate,
                        "onBorrarActivate": self.onBorrarActivate,
                        "onAboutDialog": self.onAboutDialog,
                        "onCloseAbout": self.onCloseAbout,}
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("window1")
        self.window.show_all()

    def changed_cb(self, cbox):
        model=cbox.get_model()
        index=cbox.get_active()
        if index > -1:
            print model[index][0], "selected"
        return

    def onCrearActivate(self, menuitem):
        self.crear = menuitem.get_label()

        self.window = self.builder.get_object("window1")
        cbox = self.builder.get_object("combobox1")
        store = Gtk.ListStore(str)
#        store.append(["foobar"])
#       cbox.set_model(store)
#        tree_iter = cbox.get_active_iter()
#       if tree_iter != None:
#           model = cbox.get_model()
#           value = model[tree_iter][0]
#           priority.append(value)            
        
        cell = Gtk.CellRendererText()
        cbox.pack_start(cell, True)
        cbox.add_attribute(cell, "text", 0)
        self.window.add(cbox)
        cbox.set_wrap_width(5)
        for n in range(50):
            store.append(["Item %d" %n])
        cbox.set_model(store)
        cbox.connect("changed", self.changed_cb)
        cbox.set_active(0)
        self.window.show_all()

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        Conexion.commit()
        micursor = Conexion.cursor()
        print micursor
        try:
            micursor.execute("DROP TABLE New;")
        except:
            pass

        micursor.execute("CREATE TABLE New (id INT, Edad INT);")
        
        print "HOLA"
        return True

    def onObtenerActivate(self, menuitem):
        self.obtener = menuitem.get_label()
       
        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        micursor = Conexion.cursor()
        micursor.execute("SELECT * FROM New;")
        print micursor.fetchone()


    def onActualizarActivate(self, menuitem):
        self.actualizar = menuitem.get_label()

        entry1 = self.builder.get_object("entry1")
        entry2 = self.builder.get_object("entry2")
        entry3 = self.builder.get_object("entry3")

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        micursor = Conexion.cursor()
        micursor.execute("INSERT INTO New (id, Edad) VALUES (1,8);")
        print micursor.fetchone()

        entry1.set_text("TEST\nTEST2")
        entry2.set_text("2")
        entry3.set_text("5")

    def onBorrarActivate(self, menuitem):
        self.borrar = menuitem.get_label()

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        micursor = Conexion.cursor()
        micursor.execute("DELETE FROM New;")
        print micursor.fetchone()

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
