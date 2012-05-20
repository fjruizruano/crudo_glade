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

    # definimos función Crear tabla
    def onCrearActivate(self, menuitem):
        self.crear = menuitem.get_label()

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud") # conectamos a al base de datos
        Conexion.commit()
        micursor = Conexion.cursor()
        try:
            micursor.execute("DROP TABLE New;") # borramos tabla New si existe
        except:
            pass
        micursor.execute("CREATE TABLE New (id INT, Edad INT, Peso INT, Altura INT, IMC INT, Colesterol INT);") # creamos tabla
        
        label1 = self.builder.get_object("label1")
        label1.set_label("TABLA CREADA") # informamos el proceso

    # definimos función Obtener información de la base de datos
    def onObtenerActivate(self, menuitem):
        self.obtener = menuitem.get_label()

        entry7 = self.builder.get_object("entry7")
        entry2 = self.builder.get_object("entry2")
        entry3 = self.builder.get_object("entry3")
        entry4 = self.builder.get_object("entry4")
        entry5 = self.builder.get_object("entry5")
        entry6 = self.builder.get_object("entry6")
        ent7 = entry7.get_text()
        
        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud") # conectamos a la base de datos
        micursor = Conexion.cursor()
        micursor.execute("SELECT * FROM New WHERE id=%s;" % ent7 ) # seleccionamos elemento con el ID indicado por el usuario
        num_reg = micursor.rowcount # contamos número de elementos
        Conexion.commit()
        registro = micursor.fetchone()

        print registro

        # escribimos la salidad de cada elemento en la GUI
        entry2.set_text(str(registro[1]))
        entry3.set_text(str(registro[2]))
        entry4.set_text(str(registro[3]))
        entry5.set_text(str(registro[4]))
        entry6.set_text(str(registro[5]))

        label1 = self.builder.get_object("label1")
        label1.set_label("OBTENIENDO ELEMENTO %s" % ent7) # informamos el proceso


    def onActualizarActivate(self, menuitem):
        self.actualizar = menuitem.get_label()

        entry2 = self.builder.get_object("entry2")
        entry3 = self.builder.get_object("entry3")
        entry4 = self.builder.get_object("entry4")
        entry5 = self.builder.get_object("entry5")
        entry6 = self.builder.get_object("entry6")
        entry7 = self.builder.get_object("entry7")

        # recogemos la información de cada campo introducida por el usuario
        ent7 = entry7.get_text()
        ent2 = entry2.get_text()
        ent3 = entry3.get_text()
        ent4 = entry4.get_text()
        ent5 = entry5.get_text()
        ent6 = entry6.get_text()

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud") # conectamos a la base de datos
        micursor = Conexion.cursor()
        # escribimos un nuevo elemento en la tabla según la información introducida por el usuario
        micursor.execute("INSERT INTO New (id, Edad, Peso, Altura, IMC, Colesterol) VALUES (%s, %s, %s, %s, %s, %s);" % (ent7, ent2, ent3, ent4, ent5, ent6))
        micursor.execute("SELECT * FROM New WHERE id=%s;" % ent7 )
        print micursor.fetchone()

        Conexion.commit()

        label1 = self.builder.get_object("label1")
        label1.set_label("GUARDADO ELEMENTO %s" % ent7) # informamos el proceso

    # definimos la función borrar elemento de la tabla
    def onBorrarActivate(self, menuitem):
        self.borrar = menuitem.get_label()

        entry7 = self.builder.get_object("entry7")
        ent7 = entry7.get_text() # recogemos ID indicada por el usuario

        Conexion = MySQLdb.connect(host="localhost", user="crud", passwd = "crudpass", db= "DBdeCrud") # conectamos a la base de datos
        micursor = Conexion.cursor()
        micursor.execute("DELETE FROM New WHERE id=%s;" % ent7 ) # borramos el elemento con la ID indicada por le usuario
        print "borrado id %s" % ent7

        label1 = self.builder.get_object("label1")
        label1.set_label("BORRADO ELEMENTO %s" % ent7) # informamos el proceso

    # definimos ventana About
    def onAboutDialog(self, *args):
        self.about = self.builder.get_object("aboutdialog1")
        self.about.show_all()

    # definimos cierre de la ventana About
    def onCloseAbout(self, *args):
        self.about = self.builder.get_object("aboutdialog1")
        self.about.hide()

def main():
    window = Crud_GUI()
    Gtk.main() 
    return 0

if __name__ == "__main__":
    main()
