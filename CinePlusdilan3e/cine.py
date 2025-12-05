#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#

import wx

class Ventana1(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 354))
        self.SetTitle("Inicio de sesión - CinePlus")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("logo.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetBackgroundColour(wx.Colour(0, 255, 0))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        ibBienvenidos = wx.StaticText(self.panel_1, wx.ID_ANY, "Bienvenido a CinePlus", style=wx.ALIGN_CENTER_HORIZONTAL)
        ibBienvenidos.SetMinSize((132, 35))
        ibBienvenidos.SetForegroundColour(wx.Colour(0, 0, 0))
        ibBienvenidos.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        sizer_1.Add(ibBienvenidos, 0, wx.EXPAND, 0)

        Iblogo = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("logo.png", wx.BITMAP_TYPE_ANY))
        sizer_1.Add(Iblogo, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        ibUsuario = wx.StaticText(self.panel_1, wx.ID_ANY, "Usuario", style=wx.ALIGN_CENTER_HORIZONTAL)
        ibUsuario.SetMinSize((445, 20))
        sizer_1.Add(ibUsuario, 0, 0, 0)

        self.tfUsuario = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.tfUsuario.SetMinSize((200, 27))
        self.tfUsuario.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Arial Narrow"))
        sizer_1.Add(self.tfUsuario, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        ibClave = wx.StaticText(self.panel_1, wx.ID_ANY, "Contraseña", style=wx.ALIGN_CENTER_HORIZONTAL)
        ibClave.SetMinSize((445, 20))
        ibClave.SetForegroundColour(wx.Colour(0, 0, 0))
        sizer_1.Add(ibClave, 0, 0, 0)

        self.tfClave = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        self.tfClave.SetMinSize((200, 27))
        self.tfClave.SetFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Arial Narrow"))
        sizer_1.Add(self.tfClave, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.btnEntrar = wx.Button(self.panel_1, wx.ID_ANY, "Entrar")
        self.btnEntrar.SetMinSize((120, 35))
        sizer_1.Add(self.btnEntrar, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)

        self.btnSalir = wx.Button(self.panel_1, wx.ID_ANY, "Salir")
        sizer_1.Add(self.btnSalir, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)

        self.panel_1.SetSizer(sizer_1)
        self.Layout()

        self.btnEntrar.Bind(wx.EVT_BUTTON, self.confirmar_usuario_clave)
        self.btnSalir.Bind(wx.EVT_BUTTON, self.cerrar_programa)

    def confirmar_usuario_clave(self, event):
        nombre = self.tfUsuario.GetValue()
        clave = self.tfClave.GetValue()

        if nombre == "Dilan" and clave == "131":
            print(f"¡Bienvenido, {nombre}! Acceso autorizado.")
            v2 = Ventana2(None)
            v2.Show()
            self.Hide()
        else:
            print("Acceso denegado. Usuario o clave incorrectos.")
            wx.MessageBox("Usuario o contraseña incorrectos", "Error", wx.OK | wx.ICON_ERROR)
        event.Skip()

    def cerrar_programa(self, event):
        pregunta = wx.MessageDialog(self, "Se cerrará la ventana.\n¿Está seguro que desea salir?", 
                                   "Confirmar salida", style=wx.YES_NO | wx.ICON_QUESTION)
        respuesta = pregunta.ShowModal()
        pregunta.Destroy()

        if respuesta == wx.ID_YES:
            print("¡Bye!")
            self.Close()
        event.Skip()

class Ventana2(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((493, 617))
        self.SetTitle("Taquilla")

        # Variables de instancia
        self.subtotal = 0
        self.adultos = 0
        self.menores = 0
        self.informacion = ""
        self.horarioSeleccionado = ""

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetBackgroundColour(wx.Colour(148, 255, 216))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridSizer(1, 3, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        bitmap_1 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/taquilla.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_1, 0, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "TAQUILLA")
        label_1.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, 0, "Cooper Black"))
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)

        bitmap_2 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/taquilla.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_2, 0, wx.EXPAND, 0)

        grid_sizer_2 = wx.GridSizer(1, 3, 0, 0)
        sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)

        grid_sizer_6 = wx.GridSizer(3, 1, 0, 0)
        grid_sizer_2.Add(grid_sizer_6, 1, wx.EXPAND, 0)

        self.lbPelicula = wx.StaticText(self.panel_1, wx.ID_ANY, "Pelicula:")
        self.lbPelicula.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_6.Add(self.lbPelicula, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.lbSala = wx.StaticText(self.panel_1, wx.ID_ANY, "Sala:")
        self.lbSala.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_6.Add(self.lbSala, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.lbHorario = wx.StaticText(self.panel_1, wx.ID_ANY, "Horario:")
        self.lbHorario.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_6.Add(self.lbHorario, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        grid_sizer_7 = wx.GridSizer(3, 1, 0, 0)
        grid_sizer_2.Add(grid_sizer_7, 1, wx.EXPAND, 0)

        self.cmbPelicula = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=["F1", "Karate Kid", "Cars"], style=wx.CB_DROPDOWN)
        grid_sizer_7.Add(self.cmbPelicula, 0, wx.ALIGN_CENTER, 0)

        self.lbVerSala = wx.StaticText(self.panel_1, wx.ID_ANY, "--")
        self.lbVerSala.SetFont(wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_7.Add(self.lbVerSala, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)

        grid_sizer_8 = wx.GridSizer(2, 2, 0, 0)
        grid_sizer_7.Add(grid_sizer_8, 1, wx.EXPAND, 0)

        self.rbHorario1 = wx.RadioButton(self.panel_1, wx.ID_ANY, "00:00")
        grid_sizer_8.Add(self.rbHorario1, 0, wx.ALIGN_CENTER, 0)

        self.rbHorario2 = wx.RadioButton(self.panel_1, wx.ID_ANY, "00:00")
        grid_sizer_8.Add(self.rbHorario2, 0, wx.ALIGN_CENTER, 0)

        self.rbHorario3 = wx.RadioButton(self.panel_1, wx.ID_ANY, "00:00")
        grid_sizer_8.Add(self.rbHorario3, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_8.Add((0, 0), 0, 0, 0)

        self.bmPelicula = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/logo.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_2.Add(self.bmPelicula, 0, 0, 0)

        label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, "BOLETOS")
        label_6.SetFont(wx.Font(11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, 0, "Cooper Black"))
        sizer_1.Add(label_6, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        grid_sizer_3 = wx.GridSizer(1, 2, 0, 0)
        sizer_1.Add(grid_sizer_3, 1, wx.EXPAND, 0)

        self.lbAdultos = wx.StaticText(self.panel_1, wx.ID_ANY, "Adultos ($80) :")
        self.lbAdultos.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_3.Add(self.lbAdultos, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.tfAdultos = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.tfAdultos.SetMinSize((113, 23))
        grid_sizer_3.Add(self.tfAdultos, 0, wx.ALIGN_CENTER, 0)

        grid_sizer_4 = wx.GridSizer(1, 2, 0, 0)
        sizer_1.Add(grid_sizer_4, 1, wx.EXPAND, 0)

        self.lbMenores = wx.StaticText(self.panel_1, wx.ID_ANY, "Menores ($70) :")
        self.lbMenores.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_4.Add(self.lbMenores, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.tfMenores = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        grid_sizer_4.Add(self.tfMenores, 0, wx.ALIGN_CENTER, 0)

        self.lbSubtotal = wx.StaticText(self.panel_1, wx.ID_ANY, "Subtotal: $0.00")
        self.lbSubtotal.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        sizer_1.Add(self.lbSubtotal, 0, wx.EXPAND, 0)

        grid_sizer_5 = wx.GridSizer(1, 2, 0, 0)
        sizer_1.Add(grid_sizer_5, 1, wx.EXPAND, 0)

        self.btnLimpiar = wx.Button(self.panel_1, wx.ID_ANY, "Limpiar")
        self.btnLimpiar.SetMinSize((110, 40))
        self.btnLimpiar.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_5.Add(self.btnLimpiar, 0, wx.ALIGN_CENTER | wx.ALL, 4)

        self.btnSiguiente = wx.Button(self.panel_1, wx.ID_ANY, "Siguiente")
        self.btnSiguiente.SetMinSize((110, 40))
        self.btnSiguiente.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_5.Add(self.btnSiguiente, 0, wx.ALIGN_CENTER | wx.ALL, 4)

        self.panel_1.SetSizer(sizer_1)
        self.Layout()

        self.cmbPelicula.Bind(wx.EVT_COMBOBOX, self.seleccionPelicula)
        self.rbHorario1.Bind(wx.EVT_RADIOBUTTON, self.seleccionHorario1)
        self.rbHorario2.Bind(wx.EVT_RADIOBUTTON, self.seleccionHorario2)
        self.rbHorario3.Bind(wx.EVT_RADIOBUTTON, self.seleccionHorario3)
        self.tfAdultos.Bind(wx.EVT_TEXT_ENTER, self.sumarAdultos)
        self.tfMenores.Bind(wx.EVT_TEXT_ENTER, self.sumarMenores)
        self.btnLimpiar.Bind(wx.EVT_BUTTON, self.limpiarTaquilla)
        self.btnSiguiente.Bind(wx.EVT_BUTTON, self.siguienteVentana)

    def cargar_imagen(self, ruta):
        bitmap = wx.Bitmap(ruta, wx.BITMAP_TYPE_ANY)
        self.bmPelicula.SetBitmap(bitmap)

    def seleccionPelicula(self, event):
        pelicula = self.cmbPelicula.GetValue()
        imagen = ""
        sala = ""
        horario1 = horario2 = horario3 = ""
        print(f"Película seleccionada: {pelicula}")

        if pelicula == "F1":
            imagen = "imagenes/pelicula1.png"
            sala = "1"
            horario1 = "11:00"
            horario2 = "13:00"
            horario3 = "15:00"
        elif pelicula == "Karate Kid":
            imagen = "imagenes/pelicula2.png"
            sala = "2"
            horario1 = "12:00"
            horario2 = "14:30"
            horario3 = "17:00"
        elif pelicula == "Cars":
            imagen = "imagenes/pelicula3.png"
            sala = "3"
            horario1 = "10:30"
            horario2 = "12:00"
            horario3 = "14:00"

        self.cargar_imagen(imagen)
        self.lbVerSala.SetLabel(sala)
        self.rbHorario1.SetLabel(horario1)
        self.rbHorario2.SetLabel(horario2)
        self.rbHorario3.SetLabel(horario3)
        self.informacion = f"Película: {pelicula}\nSala: {sala}"
        print(f"Listo para disfrutar de \n{self.informacion}")
        event.Skip()

    def seleccionHorario1(self, event):
        self.horarioSeleccionado = self.rbHorario1.GetLabel()
        event.Skip()

    def seleccionHorario2(self, event):
        self.horarioSeleccionado = self.rbHorario2.GetLabel()
        event.Skip()

    def seleccionHorario3(self, event):
        self.horarioSeleccionado = self.rbHorario3.GetLabel()
        event.Skip()

    def sumarAdultos(self, event):
        try:
            self.adultos = int(self.tfAdultos.GetValue())
            subtotal_a = self.adultos * 80
            self.subtotal = subtotal_a + (self.menores * 70)
            self.lbSubtotal.SetLabel(f"Subtotal: ${self.subtotal:.2f}")
        except ValueError:
            wx.MessageBox("Por favor ingresa un número válido", "Error", wx.OK | wx.ICON_ERROR)
        event.Skip()

    def sumarMenores(self, event):
        try:
            self.menores = int(self.tfMenores.GetValue())
            subtotal_b = self.menores * 70
            self.subtotal = (self.adultos * 80) + subtotal_b
            self.lbSubtotal.SetLabel(f"Subtotal: ${self.subtotal:.2f}")
        except ValueError:
            wx.MessageBox("Por favor ingresa un número válido", "Error", wx.OK | wx.ICON_ERROR)
        event.Skip()

    def limpiarValores_Campos(self):
        self.subtotal = 0
        self.adultos = 0
        self.menores = 0
        self.informacion = ""
        self.horarioSeleccionado = ""

        self.cargar_imagen("imagenes/logo.png")
        self.rbHorario1.SetLabel("00:00")
        self.rbHorario2.SetLabel("00:00")
        self.rbHorario3.SetLabel("00:00")
        self.rbHorario1.SetValue(False)
        self.rbHorario2.SetValue(False)
        self.rbHorario3.SetValue(False)
        self.cmbPelicula.SetSelection(wx.NOT_FOUND)
        self.lbVerSala.SetLabel("---")
        self.tfAdultos.SetValue("0")
        self.tfMenores.SetValue("0")
        self.lbSubtotal.SetLabel("Subtotal: $0.00")

    def limpiarTaquilla(self, event):
        self.limpiarValores_Campos()
        event.Skip()

    def siguienteVentana(self, event):
        # Validar selección
        if not self.horarioSeleccionado or self.horarioSeleccionado == "00:00":
            wx.MessageBox("Por favor selecciona un horario", "Error", wx.OK | wx.ICON_WARNING)
            return
            
        if self.cmbPelicula.GetSelection() == wx.NOT_FOUND:
            wx.MessageBox("Por favor selecciona una película", "Error", wx.OK | wx.ICON_WARNING)
            return

        self.informacion = f"{self.informacion}\nHorario: {self.horarioSeleccionado}"
        self.informacion = f"{self.informacion}\nAdultos: {self.adultos}"
        self.informacion = f"{self.informacion}\nMenores: {self.menores}"
        self.informacion = f"{self.informacion}\nSubtotal: ${self.subtotal:.2f}"

        pregunta = wx.MessageDialog(
            self,
            f"Confirmación de Taquilla.\n"
            f"¿Está seguro que desea adquirir?\n\n{self.informacion}",
            "Taquilla",
            style=wx.YES_NO | wx.ICON_QUESTION
        )

        respuesta = pregunta.ShowModal()
        pregunta.Destroy()

        if respuesta == wx.ID_YES:
            print(f"Venta de Taquilla realizada\n{self.informacion}")
            v3 = Ventana3(None, informacion=self.informacion, subtotal=self.subtotal)
            v3.Show()
            self.limpiarValores_Campos()
            self.Hide()
        elif respuesta == wx.ID_NO:
            self.limpiarValores_Campos()
        event.Skip()

class Ventana3(wx.Frame):
    def __init__(self, parent, informacion="", subtotal=0):
        super().__init__(parent, style=wx.DEFAULT_FRAME_STYLE)
        self.SetSize((753, 544))
        self.SetTitle("Dulcería")
        print(f"Datos de la ventana 2:\nInformación: {informacion}\nSubtotal: {subtotal}")

        # Variables de instancia
        self.infoDulceria = ""
        self.subtotalDulceria = 0
        self.infoTaquilla = informacion
        self.subtotalTaquilla = subtotal

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetBackgroundColour(wx.Colour(60, 39, 245))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer_1 = wx.GridSizer(1, 3, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        bitmap_1 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/dulceria.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_1, 0, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "DULCERIA")
        label_1.SetForegroundColour(wx.Colour(0, 0, 0))
        label_1.SetFont(wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)

        bitmap_2 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/dulceria.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_2, 0, wx.EXPAND, 0)

        grid_sizer_2 = wx.GridSizer(1, 2, 0, 0)
        sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)

        grid_sizer_8 = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_2.Add(grid_sizer_8, 1, wx.EXPAND, 0)

        self.spComboB = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_8.Add(self.spComboB, 0, 0, 0)

        grid_sizer_9 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_8.Add(grid_sizer_9, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Básico $75")
        label_2.SetFont(wx.Font(11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_9.Add(label_2, 0, 0, 0)

        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "Palomitas Ch\nRefresco Ch")
        grid_sizer_9.Add(label_3, 0, 0, 0)

        bitmap_3 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/comboB.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_8.Add(bitmap_3, 0, 0, 0)

        grid_sizer_10 = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_2.Add(grid_sizer_10, 1, wx.EXPAND, 0)

        self.spComboC = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_10.Add(self.spComboC, 0, 0, 0)

        grid_sizer_11 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_10.Add(grid_sizer_11, 1, wx.EXPAND, 0)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "Cuates $130")
        label_4.SetFont(wx.Font(11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_11.Add(label_4, 0, 0, 0)

        label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, "Palomitas md\n2 Refrescos md")
        grid_sizer_11.Add(label_5, 0, 0, 0)

        bitmap_4 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/comboC.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_10.Add(bitmap_4, 0, 0, 0)

        grid_sizer_3 = wx.GridSizer(1, 2, 0, 0)
        sizer_1.Add(grid_sizer_3, 1, wx.EXPAND, 0)

        grid_sizer_12 = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_3.Add(grid_sizer_12, 1, wx.EXPAND, 0)

        self.spComboF = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_12.Add(self.spComboF, 0, 0, 0)

        grid_sizer_13 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_12.Add(grid_sizer_13, 1, wx.EXPAND, 0)

        label_6 = wx.StaticText(self.panel_1, wx.ID_ANY, "Familiar $200")
        label_6.SetFont(wx.Font(11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_13.Add(label_6, 0, 0, 0)

        label_7 = wx.StaticText(self.panel_1, wx.ID_ANY, "Palomitas G\n2 Refrescos G\nDulce")
        grid_sizer_13.Add(label_7, 0, 0, 0)

        bitmap_5 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/comboF.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_12.Add(bitmap_5, 0, 0, 0)

        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        grid_sizer_3.Add(self.panel_2, 1, wx.EXPAND, 0)

        grid_sizer_4 = wx.GridSizer(1, 2, 0, 0)
        sizer_1.Add(grid_sizer_4, 1, wx.EXPAND, 0)

        grid_sizer_14 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_4.Add(grid_sizer_14, 1, wx.EXPAND, 0)

        bitmap_6 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/palomitas.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_14.Add(bitmap_6, 0, 0, 0)

        grid_sizer_15 = wx.FlexGridSizer(4, 1, 0, 0)
        grid_sizer_14.Add(grid_sizer_15, 1, wx.EXPAND, 0)

        label_8 = wx.StaticText(self.panel_1, wx.ID_ANY, "Palomitas")
        label_8.SetFont(wx.Font(11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_15.Add(label_8, 0, 0, 0)

        grid_sizer_16 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_15.Add(grid_sizer_16, 1, wx.EXPAND, 0)

        self.spPalomitasCh = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_16.Add(self.spPalomitasCh, 0, 0, 0)

        label_9 = wx.StaticText(self.panel_1, wx.ID_ANY, "Chicas $30")
        grid_sizer_16.Add(label_9, 0, 0, 0)

        grid_sizer_17 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_15.Add(grid_sizer_17, 1, wx.EXPAND, 0)

        self.spPalomitasMd = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_17.Add(self.spPalomitasMd, 0, 0, 0)

        label_10 = wx.StaticText(self.panel_1, wx.ID_ANY, "Medianas $50")
        grid_sizer_17.Add(label_10, 0, 0, 0)

        grid_sizer_18 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_15.Add(grid_sizer_18, 1, wx.EXPAND, 0)

        self.spPalomitasG = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_18.Add(self.spPalomitasG, 0, 0, 0)

        label_11 = wx.StaticText(self.panel_1, wx.ID_ANY, "Grandes $80")
        grid_sizer_18.Add(label_11, 0, 0, 0)

        grid_sizer_19 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_4.Add(grid_sizer_19, 1, wx.EXPAND, 0)

        bitmap_7 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/refresco.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_19.Add(bitmap_7, 0, 0, 0)

        grid_sizer_20 = wx.FlexGridSizer(3, 1, 0, 0)
        grid_sizer_19.Add(grid_sizer_20, 1, wx.EXPAND, 0)

        label_12 = wx.StaticText(self.panel_1, wx.ID_ANY, "Refrescos")
        label_12.SetFont(wx.Font(11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_20.Add(label_12, 0, 0, 0)

        grid_sizer_21 = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_20.Add(grid_sizer_21, 1, wx.EXPAND, 0)

        label_13 = wx.StaticText(self.panel_1, wx.ID_ANY, "Tamaño")
        grid_sizer_21.Add(label_13, 0, 0, 0)

        label_14 = wx.StaticText(self.panel_1, wx.ID_ANY, "Sabor")
        grid_sizer_21.Add(label_14, 0, 0, 0)

        label_15 = wx.StaticText(self.panel_1, wx.ID_ANY, "Cantidad")
        grid_sizer_21.Add(label_15, 0, 0, 0)

        grid_sizer_23 = wx.GridSizer(1, 4, 0, 0)
        grid_sizer_20.Add(grid_sizer_23, 1, wx.EXPAND, 0)

        self.cmbTamano = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=["chico", "mediano", "grande"], style=wx.CB_DROPDOWN)
        self.cmbTamano.SetMinSize((60, 20))
        grid_sizer_23.Add(self.cmbTamano, 0, 0, 0)

        self.cmbSabor = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=["fresa", "naranja", "piña"], style=wx.CB_DROPDOWN)
        self.cmbSabor.SetMinSize((60, 20))
        grid_sizer_23.Add(self.cmbSabor, 0, 0, 0)

        self.spCantidad = wx.SpinCtrl(self.panel_1, wx.ID_ANY, "0", min=0, max=100)
        grid_sizer_23.Add(self.spCantidad, 0, 0, 0)

        self.btnAgregar = wx.Button(self.panel_1, wx.ID_ANY, "Agregar")
        self.btnAgregar.SetMinSize((75, 23))
        self.btnAgregar.SetBackgroundColour(wx.Colour(192, 192, 192))
        grid_sizer_23.Add(self.btnAgregar, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        grid_sizer_5 = wx.GridSizer(1, 2, 0, 0)
        sizer_1.Add(grid_sizer_5, 1, wx.EXPAND, 0)

        grid_sizer_24 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_5.Add(grid_sizer_24, 1, wx.EXPAND, 0)

        label_16 = wx.StaticText(self.panel_1, wx.ID_ANY, "Productos Agregados:")
        label_16.SetFont(wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_24.Add(label_16, 0, 0, 0)

        self.lbProductosAgregados = wx.StaticText(self.panel_1, wx.ID_ANY, "---")
        self.lbProductosAgregados.SetFont(wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_24.Add(self.lbProductosAgregados, 0, 0, 0)

        grid_sizer_25 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_5.Add(grid_sizer_25, 1, wx.EXPAND, 0)

        label_18 = wx.StaticText(self.panel_1, wx.ID_ANY, "Subtotal Dulcería:")
        label_18.SetFont(wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_25.Add(label_18, 0, 0, 0)

        self.lbSubtotal = wx.StaticText(self.panel_1, wx.ID_ANY, "$00.00")
        self.lbSubtotal.SetForegroundColour(wx.Colour(255, 0, 0))
        self.lbSubtotal.SetFont(wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_25.Add(self.lbSubtotal, 0, 0, 0)

        grid_sizer_6 = wx.GridSizer(1, 2, 0, 0)
        sizer_1.Add(grid_sizer_6, 1, wx.EXPAND, 0)

        self.btnLimpiar = wx.Button(self.panel_1, wx.ID_ANY, "Limpiar")
        self.btnLimpiar.SetMinSize((120, 40))
        self.btnLimpiar.SetFont(wx.Font(11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_6.Add(self.btnLimpiar, 0, wx.ALIGN_CENTER | wx.ALL, 4)

        self.btnSiguiente = wx.Button(self.panel_1, wx.ID_ANY, "Siguiente")
        self.btnSiguiente.SetMinSize((120, 40))
        self.btnSiguiente.SetFont(wx.Font(11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Constantia"))
        grid_sizer_6.Add(self.btnSiguiente, 0, wx.ALIGN_CENTER | wx.ALL, 4)

        self.panel_1.SetSizer(sizer_1)
        self.Layout()

        self.spComboB.Bind(wx.EVT_SPINCTRL, self.calcularComboBasico)
        self.spComboC.Bind(wx.EVT_SPINCTRL, self.calcularComboCuates)
        self.spComboF.Bind(wx.EVT_SPINCTRL, self.calcularComboFamiliar)
        self.spPalomitasCh.Bind(wx.EVT_SPINCTRL, self.calcularPalomitasCh)
        self.spPalomitasMd.Bind(wx.EVT_SPINCTRL, self.calcularPalomitasMd)
        self.spPalomitasG.Bind(wx.EVT_SPINCTRL, self.calcularPalomitasG)
        self.btnAgregar.Bind(wx.EVT_BUTTON, self.agregarRefresco)
        self.btnLimpiar.Bind(wx.EVT_BUTTON, self.limpiarDulceria)
        self.btnSiguiente.Bind(wx.EVT_BUTTON, self.siguienteDulceria)

    def calcularComboBasico(self, event):
        numero = int(self.spComboB.GetValue())
        subtotalcombo = numero * 75
        self.subtotalDulceria = self.subtotalDulceria + subtotalcombo
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria:.2f}")
        self.infoDulceria = self.infoDulceria + f"{numero} Combos Básicos\n"
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def calcularComboCuates(self, event):
        numero = int(self.spComboC.GetValue())
        subtotalcombo = numero * 130
        self.subtotalDulceria = self.subtotalDulceria + subtotalcombo
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria:.2f}")
        self.infoDulceria = self.infoDulceria + f"{numero} Combo Cuates\n"
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def calcularComboFamiliar(self, event):
        numero = int(self.spComboF.GetValue())
        subtotalcombo = numero * 200
        self.subtotalDulceria = self.subtotalDulceria + subtotalcombo
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria:.2f}")
        self.infoDulceria = self.infoDulceria + f"{numero} Combo Familiar\n"
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def calcularPalomitasCh(self, event):
        numero = int(self.spPalomitasCh.GetValue())
        subtotalcombo = numero * 30
        self.subtotalDulceria = self.subtotalDulceria + subtotalcombo
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria:.2f}")
        self.infoDulceria = self.infoDulceria + f"{numero} Palomitas Chicas\n"
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def calcularPalomitasMd(self, event):
        numero = int(self.spPalomitasMd.GetValue())
        subtotalcombo = numero * 50
        self.subtotalDulceria = self.subtotalDulceria + subtotalcombo
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria:.2f}")
        self.infoDulceria = self.infoDulceria + f"{numero} Palomitas Medianas\n"
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def calcularPalomitasG(self, event):
        numero = int(self.spPalomitasG.GetValue())
        subtotalcombo = numero * 80
        self.subtotalDulceria = self.subtotalDulceria + subtotalcombo
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria:.2f}")
        self.infoDulceria = self.infoDulceria + f"{numero} Palomitas Grandes\n"
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def agregarRefresco(self, event):
        numero = int(self.spCantidad.GetValue())
        tamanyo = self.cmbTamano.GetValue()
        sabor = self.cmbSabor.GetValue()
        
        if numero == 0:
            wx.MessageBox("Por favor ingresa una cantidad válida", "Error", wx.OK | wx.ICON_WARNING)
            return
            
        if tamanyo == "chico":
            subtotalrefresco = numero * 25
        elif tamanyo == "mediano":
            subtotalrefresco = numero * 40
        elif tamanyo == "grande":
            subtotalrefresco = numero * 60
        else:
            wx.MessageBox("Por favor selecciona un tamaño", "Error", wx.OK | wx.ICON_WARNING)
            return

        self.subtotalDulceria = self.subtotalDulceria + subtotalrefresco
        self.lbSubtotal.SetLabel(f"${self.subtotalDulceria:.2f}")

        self.infoDulceria = self.infoDulceria + f"{numero} Refresco: {sabor} tamaño {tamanyo}\n"
        self.lbProductosAgregados.SetLabel(self.infoDulceria)
        event.Skip()

    def limpiarD(self):
        self.subtotalDulceria = 0
        self.infoDulceria = ""

        self.spComboB.SetValue(0)
        self.spComboC.SetValue(0)
        self.spComboF.SetValue(0)
        self.spPalomitasCh.SetValue(0)
        self.spPalomitasMd.SetValue(0)
        self.spPalomitasG.SetValue(0)
        self.spCantidad.SetValue(0)
        self.cmbSabor.SetSelection(wx.NOT_FOUND)
        self.cmbTamano.SetSelection(wx.NOT_FOUND)
        self.lbProductosAgregados.SetLabel("---")
        self.lbSubtotal.SetLabel("$00.00")

    def limpiarDulceria(self, event):
        self.limpiarD()
        event.Skip()

    def siguienteDulceria(self, event):
        if not self.infoDulceria:
            wx.MessageBox("No has seleccionado ningún producto de dulcería", "Advertencia", wx.OK | wx.ICON_WARNING)
            return
            
        pregunta = wx.MessageDialog(self,
            f"Confirmación de Dulcería.\n"
            f"¿Está seguro que desea adquirir?\n\n{self.infoDulceria}\n"
            f"Subtotal Dulcería: ${self.subtotalDulceria:.2f}",
            "Dulcería", style=wx.YES_NO | wx.ICON_QUESTION)

        respuesta = pregunta.ShowModal()
        pregunta.Destroy()

        if respuesta == wx.ID_YES:
            v4 = Ventana4(None, 
                         informacion=self.infoTaquilla,
                         subtotal=self.subtotalTaquilla,
                         informacion2=self.infoDulceria,
                         subtotal2=self.subtotalDulceria)
            v4.Show()
            self.limpiarD()
            self.Hide()
        elif respuesta == wx.ID_NO:
            self.limpiarD()
        event.Skip()

class Ventana4(wx.Frame):
    def __init__(self, parent, informacion="", subtotal=0, informacion2="", subtotal2=0):
        kwds = {"style": wx.DEFAULT_FRAME_STYLE}
        wx.Frame.__init__(self, parent, **kwds)
        self.SetSize((400, 500))
        self.SetTitle("Ticket - Resumen de Compra")

        # Variables de instancia
        self.infoTaquilla = informacion
        self.infoDulceria = informacion2
        self.subtotalTaquilla = subtotal
        self.subtotalDulceria = subtotal2
        self.total = self.subtotalTaquilla + self.subtotalDulceria

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetBackgroundColour(wx.Colour(255, 143, 176))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        # TÍTULO TICKET
        grid_sizer_1 = wx.GridSizer(1, 3, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        bitmap_1 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/boletov2.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_1, 0, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "TICKET")
        label_1.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        grid_sizer_1.Add(label_1, 0, wx.ALIGN_CENTER, 0)

        bitmap_2 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("imagenes/boletov2.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_2, 0, wx.EXPAND, 0)

        # SECCIÓN TAQUILLA
        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "TAQUILLA")
        label_2.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        sizer_1.Add(label_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 10)

        self.lbTaquilla = wx.StaticText(self.panel_1, wx.ID_ANY, f"{self.infoTaquilla}")
        self.lbTaquilla.SetMinSize((350, 100))
        self.lbTaquilla.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Arial"))
        sizer_1.Add(self.lbTaquilla, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.lbSubtotalTaquilla = wx.StaticText(self.panel_1, wx.ID_ANY, f"Subtotal Taquilla: ${self.subtotalTaquilla:.2f}")
        self.lbSubtotalTaquilla.SetForegroundColour(wx.Colour(35, 35, 142))
        self.lbSubtotalTaquilla.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        sizer_1.Add(self.lbSubtotalTaquilla, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 10)

        # SECCIÓN DULCERÍA
        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "DULCERÍA")
        label_3.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        sizer_1.Add(label_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 10)

        self.lbDulceria = wx.StaticText(self.panel_1, wx.ID_ANY, f"{self.infoDulceria}")
        self.lbDulceria.SetMinSize((350, 100))
        self.lbDulceria.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Arial"))
        sizer_1.Add(self.lbDulceria, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.lbSubtotalDulceria = wx.StaticText(self.panel_1, wx.ID_ANY, f"Subtotal Dulcería: ${self.subtotalDulceria:.2f}")
        self.lbSubtotalDulceria.SetForegroundColour(wx.Colour(35, 35, 142))
        self.lbSubtotalDulceria.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        sizer_1.Add(self.lbSubtotalDulceria, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 10)

        # LÍNEA SEPARADORA
        static_line = wx.StaticLine(self.panel_1, wx.ID_ANY)
        sizer_1.Add(static_line, 0, wx.EXPAND | wx.ALL, 10)

        # TOTAL
        self.lbTotal = wx.StaticText(self.panel_1, wx.ID_ANY, f"TOTAL: ${self.total:.2f}")
        self.lbTotal.SetForegroundColour(wx.Colour(189, 0, 0))
        self.lbTotal.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        sizer_1.Add(self.lbTotal, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.BOTTOM, 10)

        # BOTONES
        grid_sizer_2 = wx.GridSizer(1, 2, 20, 20)
        sizer_1.Add(grid_sizer_2, 1, wx.EXPAND | wx.ALL, 20)

        self.btnCancelar = wx.Button(self.panel_1, wx.ID_ANY, "Cancelar")
        self.btnCancelar.SetMinSize((120, 40))
        self.btnCancelar.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        self.btnCancelar.SetBackgroundColour(wx.Colour(255, 100, 100))
        grid_sizer_2.Add(self.btnCancelar, 0, wx.ALIGN_CENTER | wx.ALL, 4)

        self.btnFinalizar = wx.Button(self.panel_1, wx.ID_ANY, "Finalizar")
        self.btnFinalizar.SetMinSize((120, 40))
        self.btnFinalizar.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Arial"))
        self.btnFinalizar.SetBackgroundColour(wx.Colour(100, 255, 100))
        grid_sizer_2.Add(self.btnFinalizar, 0, wx.ALIGN_CENTER | wx.ALL, 4)

        self.panel_1.SetSizer(sizer_1)
        self.Layout()

        self.btnCancelar.Bind(wx.EVT_BUTTON, self.cancelarVenta)
        self.btnFinalizar.Bind(wx.EVT_BUTTON, self.finalizarVenta)

    def cancelarVenta(self, event):
        pregunta = wx.MessageDialog(self,
            "¿Está seguro de cancelar esta venta?\n"
            "Todos los datos se perderán.",
            "Cancelar Venta",
            style=wx.YES_NO | wx.ICON_WARNING)
        
        respuesta = pregunta.ShowModal()
        pregunta.Destroy()
        
        if respuesta == wx.ID_YES:
            print("Venta cancelada")
            self.Close()
            
            # Mostrar ventana principal
            app = wx.GetApp()
            if app and hasattr(app, 'frame'):
                app.frame.Show()
        event.Skip()

    def finalizarVenta(self, event):
        mensaje = (
            f"VENTA FINALIZADA\n\n"
            f"Taquilla: ${self.subtotalTaquilla:.2f}\n"
            f"Dulcería: ${self.subtotalDulceria:.2f}\n"
            f"TOTAL: ${self.total:.2f}\n\n"
            f"¡Gracias por su compra!"
        )
        
        wx.MessageBox(mensaje, "Venta Finalizada", wx.OK | wx.ICON_INFORMATION)
        
        print(f"Venta finalizada - Total: ${self.total:.2f}")
        
        # Cerrar esta ventana
        self.Close()
        
        # Mostrar ventana de inicio
        app = wx.GetApp()
        if app and hasattr(app, 'frame'):
            app.frame.Show()
        event.Skip()

class MyAppCinePlus(wx.App):
    def OnInit(self):
        self.frame = Ventana1(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == "__main__":
    appCinePlus = MyAppCinePlus(0)
    appCinePlus.MainLoop()