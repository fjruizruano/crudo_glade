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

    def onCrearActivate(self, menuitem):
        self.crear = menuitem.get_label()

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        Conexion.commit()
        micursor = Conexion.cursor()
        print micursor
        try:
            micursor.execute("DROP TABLE New;")
        except:
            pass
        micursor.execute("CREATE TABLE New (id INT, Edad INT, Peso INT, Altura INT, IMC INT, Colesterol INT);")
        return True

    def onObtenerActivate(self, menuitem):
        self.obtener = menuitem.get_label()
        
        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        micursor = Conexion.cursor()
        counter = micursor.execute("SELECT COUNT(*) FROM New;")
        micursor.execute("SELECT * FROM New;")
        registros = micursor.fetchmany(counter)
        for registro in registros:
            print registro


    def onActualizarActivate(self, menuitem):
        self.actualizar = menuitem.get_label()

        entry1 = self.builder.get_object("entry1")
        entry2 = self.builder.get_object("entry2")
        entry3 = self.builder.get_object("entry3")
        entry4 = self.builder.get_object("entry4")
        entry5 = self.builder.get_object("entry5")
        entry6 = self.builder.get_object("entry6")

        ent1 = entry1.get_text()
        ent2 = entry2.get_text()
        ent3 = entry3.get_text()
        ent4 = entry4.get_text()
        ent5 = entry5.get_text()
        ent6 = entry6.get_text()

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        micursor = Conexion.cursor()
        micursor.execute("INSERT INTO New (id, Edad, Peso, Altura, IMC, Colesterol) VALUES (%s, %s, %s, %s, %s, %s);" % (ent1, ent2, ent3, ent4, ent5, ent6))
        print micursor.fetchmany(1)


#        entry1.set_text("TEST\nTEST2")
#        entry2.set_text("2")
#        entry3.set_text("5")

    def onBorrarActivate(self, menuitem):
        self.borrar = menuitem.get_label()

        entry1 = self.builder.get_object("entry1")
        ent1 = entry1.get_text()

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        micursor = Conexion.cursor()
        micursor.execute("DELETE FROM New;") #corregir
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
