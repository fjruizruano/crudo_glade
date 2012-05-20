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
        try:
            micursor.execute("DROP TABLE New;")
        except:
            pass
        micursor.execute("CREATE TABLE New (id INT, Edad INT, Peso INT, Altura INT, IMC INT, Colesterol INT);")
        print "TABLA CREADA"

    def onObtenerActivate(self, menuitem):
        self.obtener = menuitem.get_label()

        entry7 = self.builder.get_object("entry7")
        entry2 = self.builder.get_object("entry2")
        entry3 = self.builder.get_object("entry3")
        entry4 = self.builder.get_object("entry4")
        entry5 = self.builder.get_object("entry5")
        entry6 = self.builder.get_object("entry6")

        ent7 = entry7.get_text()
        
        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        micursor = Conexion.cursor()
        micursor.execute("SELECT * FROM New WHERE id=%s;" % ent7 )
        num_reg = micursor.rowcount
        Conexion.commit()
        registro = micursor.fetchone()

        print registro

        entry2.set_text(str(registro[1]))
        entry3.set_text(str(registro[2]))
        entry4.set_text(str(registro[3]))
        entry5.set_text(str(registro[4]))
        entry6.set_text(str(registro[5]))

    def onActualizarActivate(self, menuitem):
        self.actualizar = menuitem.get_label()

        entry2 = self.builder.get_object("entry2")
        entry3 = self.builder.get_object("entry3")
        entry4 = self.builder.get_object("entry4")
        entry5 = self.builder.get_object("entry5")
        entry6 = self.builder.get_object("entry6")

        ent2 = entry2.get_text()
        ent3 = entry3.get_text()
        ent4 = entry4.get_text()
        ent5 = entry5.get_text()
        ent6 = entry6.get_text()

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        micursor = Conexion.cursor()
        micursor.execute("SELECT * FROM New;")
        num_reg = micursor.rowcount
        micursor.execute("INSERT INTO New (id, Edad, Peso, Altura, IMC, Colesterol) VALUES (%s, %s, %s, %s, %s, %s);" % (num_reg+1, ent2, ent3, ent4, ent5, ent6))
        micursor.execute("SELECT * FROM New WHERE id=%s;" % str(num_reg+1))
        print micursor.fetchone()

#        counter = micursor.execute("SELECT COUNT(*) FROM New;")

        Conexion.commit()

        registros = micursor.fetchmany(num_reg)
        for registro in registros:
            print registro

    def onBorrarActivate(self, menuitem):
        self.borrar = menuitem.get_label()

        entry7 = self.builder.get_object("entry7")
        ent7 = entry7.get_text()

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud")
        micursor = Conexion.cursor()
        micursor.execute("DELETE FROM New WHERE id=%s;" % ent7 ) #corregir
        print "borrado id %s" % ent7
     
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
