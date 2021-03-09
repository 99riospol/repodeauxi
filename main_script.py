import os
import inspect
import requests

from ciscoconfparse import CiscoConfParse
from fpdf import FPDF

eleccio=input("Escribe el nombre del fichero a tratar: ")

class PDF(FPDF):
    def header(self):
        if self.page_no() != 1:  # Cabecera a tot menys a la primera pàgina
            # Set up a logo
            self.image('logo.png', 150, 10, 33)
            self.set_font('Helvetica', '', 12)
            self.cell(
                0, 10, 'Informació infraestructura de Xarxa TecnoCampus ('+eleccio+')')
            # Line break
            self.ln(17)
        else:  # Portada de la pagina 1
            self.set_fill_color(245, 198, 66)
            self.rect(20, 20, 3, 250, 'F')
            self.image('logo.png', 150, 40, 50)
            self.set_font('Times', '', 24)
            self.ln(100)
            self.cell(0, 2, '         Informació infraestructura', 0, 0)
            self.set_font('Times', '', 24)
            self.ln(20)
            self.cell(0, 2, '         de Xarxa TecnoCampus', 0, 0)
            self.set_font('Times', '', 24)
            self.ln(20)
            self.cell(0, 2, '         (Ex1)', 0, 0)
            self.set_font('Times', '', 24)
            self.ln(30)
            self.cell(0, 2, '          Febrer 2021', 0, 0)
    # Page footer

    def footer(self):  # peu de pagina menys a la primera
        if self.page_no() != 1:
            self.set_y(-15)
            self.set_font('Times', 'B', 8)
            # Page number
            self.cell(0, 10, 'Page '+str(self.page_no())+'/14', 0, 0, 'R')
pdf = PDF()
pdf.add_page()
pdf.set_font('Times', 'B', 14)
pdf.add_page()
if eleccio=="Ex1":
    # INDEX
    pdf.cell(0, 10, 'ÍNDEX', 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.- Introducció............................................................................................................................................4', 0, 1)
    pdf.cell(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.1.- Descripció........................................................................................................................4', 0, 1)
    pdf.cell(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.2.- Objectius..........................................................................................................................4', 0, 1)
    pdf.cell(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.3.- Descripció General de les infraestructures...................................................................4', 0, 1)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.- Configuració dels dispositius................................................................................................................5', 0, 1)

    cont = 0
    indexList = list()
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            for c2_obj in c1_obj.children:
                if "label:" in c2_obj.text:
                    indexList.append(str(c2_obj.text).replace("label:", ""))
    # 2.1
    cont = 0
    pdf.set_font('Times', 'B', 12)
    pdf.cell(20)
    pdf.cell(0, 10, '2.1.-' +
            indexList[cont]+'....................................................................................................5', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.1.1.- Interfícies..............................................................................................................5', 0, 1)
    pdf.cell(20)

    # 2.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.-' +
            indexList[cont]+'..............................................................................................................................6', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.1.- Configuració criptogràfica del dispositiu...........................................................5', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.2.- Interfícies...............................................................................................................6', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.3.- Configuració dels protocols de enrutament........................................................6', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.4.- Configuració de Llistes de Control Accés...........................................................6', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.5- Configuració de Banners.......................................................................................7', 0, 1)
    pdf.cell(20)
    # 2.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.-' +
            indexList[cont]+'................................................................................................................................8', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.1.- Configuració criptogràfica del dispositiu.............................................................8', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.2.- Interfícies.................................................................................................................8', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.3.- Configuració dels protocols de enrutament.........................................................8', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.4.- Configuració de Llistes de Control Accés.............................................................8', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.5.- Configuració de Banners........................................................................................9', 0, 1)
    pdf.cell(20)

    # 2.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.-' +
            indexList[cont]+'.................................................................................................................................10', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.1.- Configuració criptogràfica del dispositiu.............................................................10', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.2.- Interfícies..................................................................................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.3.- Configuració dels protocols de enrutament...........................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.4.- Configuració de Llistes de Control Accés..............................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.5.- Configuració de Banners.........................................................................................12', 0, 1)
    pdf.cell(20)

    # 2.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.-' +
            indexList[cont]+'......................................................................................................12', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.1.- Interfícies................................................................................................................13', 0, 1)
    pdf.cell(20)

    # 2.6
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.-' +
            indexList[cont]+'......................................................................................................13', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.1.- Interfícies................................................................................................................13', 0, 1)
    pdf.cell(20)

    # 2.7
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.-' +
            indexList[cont]+'............................................................................................................................13', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.1.- Interfícies................................................................................................................13', 0, 1)
    pdf.cell(20)

    # 2.8
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.-' +
            indexList[cont]+'............................................................................................................................13', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.1.- Interfícies................................................................................................................14', 0, 1)
    pdf.cell(20)

    # 2.9
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.-' +
            indexList[cont]+'............................................................................................................................14', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.1.- Interfícies................................................................................................................14', 0, 1)

    # 3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '3.- Interfícies..................................................................................................................................................14', 0, 1)

    # Introduction
    pdf.add_page()
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, '1.- Introducció', 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.1- Descripció', 0, 1)
    pdf.set_font('Times', '', 12)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'lab'):
        for c1_obj in intf_obj.children:
            if "title:" in c1_obj.text:
                titul = str(c1_obj.text).replace("title:", "")

    pdf.multi_cell(0, 10, 'El present document descriu la topologia realitzada amb la configuració ' +
                titul+' a la \nempresa TecnoCampus.', 0, 1, 'L')

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.2- Objectius', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.multi_cell(0, 10, "El objectiu d'aquest document és la de formalitzar el traspàs d'informació al equip tècnic \nresponsable del manteniment de les infraestructures instal·lades. Aquesta informació fa \nreferencia al disseny, instal·lació i configuració dels dispositius i sistemes afectats per la implementació.", 0, 1, 'L')
    pdf.cell(0, 10, 'La present documentació inclou:', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) +
            ' Descripció general de les infraestructures instal·lades', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+' Configuració de les interfícies de xarxa', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) +
            ' Configuració de les polítiques per les connexions VPN', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+" Configuració dels protocols d'enrutament", 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+" Configuració de les llistes de control d'accés", 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+' Configuració dels banners', 0, 1)

    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, '1.3.- Descripció General de les infraestructures', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Actualment la topologia té la següent distribució: ', 0, 1)
    pdf.ln(10)

    pdf.image('Image1.png', x=None, y=None, w=150)

    contId = 0
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id:" in c1_obj.text:
                contId = contId+1
    contLinks = 0
    idList = list()
    portList = list()
    parse = CiscoConfParse('Ex1')

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n1" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList.append(
                                            str(c4_obj.text).replace("label:", ""))

    pdf.cell(10)
    pdf.cell(0, 5, 'En aquesta topologia tenim '+str(contId) +
            ' equips, connectats a través de '+str(contLinks)+' links', 0, 1, 'L')

    # Configuració Dispositius
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, '2.- Configuració dels dispositius', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'A continuació, es detalla la configuració dels diferents dispositius: ', 0, 1)
    cont = 0
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.1.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.1.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    count = 0
    while count < len(idList):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList[count]+' :'+portList[count], 0, 1)
        count = count+1


    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.- '+indexList[cont], 0, 1)
    cont = cont+1

    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el 11 de Novembre del 2020 a les 20:40:33 UTC  ', 0, 1, 'L')

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.1.- Configuració criptogràfica del dispositiu', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu té la següent configuració de crypto: ', 0, 1, 'L')
    pdf.cell(10)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "10.2.2.2":
                                        res = y
    pdf.set_font('Times', '', 12)

    pdf.cell(0, 10, chr(150) + ' Connexió amb '+res, 0, 1)
    pdf.cell(20)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "10":
                                        res = y

    pdf.cell(0, 10, chr(149)+' Política de regles número :'+res, 0, 1)
    pdf.cell(30)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "aes":
                                            res = y

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "256":
                                            res1 = y

    pdf.cell(0, 10, chr(164)+' Encriptació '+res+', '+res1, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "pre-share":
                                            res = y
    pdf.cell(0, 10, chr(164)+' Autenticació '+res, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "5":
                                            res = y
    pdf.cell(0, 10, chr(164)+' Diffie-Helmann grup '+res, 0, 1)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "vpnpa55":
                                        res = y
    pdf.cell(20)
    pdf.cell(0, 10, chr(149)+' Contrasenya ISAKMP: '+res, 0, 1)
    pdf.cell(20)
    pdf.cell(0, 10, chr(149)+' Configuració VPN: ', 0, 1)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "VPN":
                                        res = y
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' Conjunt de transformació: '+res, 0, 1)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "esp-aes":
                                        res = y
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' Configuració Encriptació ESP: '+res, 0, 1)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "esp-sha-hmac":
                                        res = y
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' Configuració Signatura ESP: '+res, 0, 1)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "tunnel":
                                            res = y
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' Mode '+res, 0, 1)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "110":
                                            res = y
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' ACL número '+res, 0, 1)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.2.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és', 0, 1, 'L')
    idList1 = list()
    portList1 = list()
    contLinks = 0
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList1.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList1.append(
                                            str(c4_obj.text).replace("label:", ""))

    ex1 = list()
    ex2 = list()
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.1.1":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.0":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.1.1.2":
                                            ex2.append(y)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.252":
                                            ex2.append(y)
    count = 0
    while count < len(idList1):
        pdf.cell(10)
        if count == 0:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList1[0]+' :'+portList1[0]+':', 0, 1)
        if count == 1:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList1[1]+' :'+portList1[1]+':'+ex1[0]+' ('+ex1[1]+')', 0, 1)
        if count == 2:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList1[count]+' :'+portList1[count]+':'+ex2[0]+' ('+ex2[1]+')', 0, 1)
        if count == 3:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList1[3]+' :'+portList1[3]+':', 0, 1)
        if count == 4:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList1[4]+' :'+portList1[4]+':', 0, 1)
        count = count+1

    # 2.2.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.2.3.- Configuració dels protocols d'enrutament", 0, 1)
    pdf.set_font('Times', '', 12)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "ospf":
                                        res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "100":
                                        res1 = y
    pdf.cell(0, 10, "El protocol de enrutament utilitzat és "+res.upper() +
            " "+res1+", amb la següent configuració (xarxes publicades):", 0, 1, 'L')
    pdf.cell(10)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "0":
                                            res = y
    pdf.cell(0, 10, chr(150) + ' Àrea ' + res+':', 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.1.1.0":
                                            res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "0.0.0.3":
                                            res1 = y
    pdf.cell(0, 10, chr(149) + ' Xarxa '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.1.0":
                                            res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "0.0.0.255":
                                            res1 = y
    pdf.cell(0, 10, chr(149) + ' Xarxa '+res+' màscara invertida '+res1, 0, 1)

    # 2.2.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.2.4.- Configuració de Llistes de Control d'Accés", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurada la següent ACL:", 0, 1)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "110":
                                        res = y
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) + ' Número ' + res+':', 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "ip":
                                        res = y

    pdf.cell(0, 10, chr(149) + ' PERMIT ('+res.upper()+')', 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.1.0":
                                        res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "0.0.0.255":
                                        res1 = y
    pdf.cell(0, 10, chr(164)+' ORIGEN: '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.3.0":
                                        res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "0.0.0.255":
                                        res1 = y
    pdf.cell(0, 10, chr(164)+' DESTÍ: '+res+' màscara invertida '+res1, 0, 1)

    # 2.2.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.2.5.- Configuració de Banners", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurats els següents Banners:", 0, 1)
    pdf.cell(10)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "exec":
                                        res = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "incoming":
                                        res1 = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "login":
                                        res2 = y
    pdf.cell(10)
    count = 0
    while count < len(ex1):
        ex1.pop(count)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "*" in c3_obj.text:
                                ex1.append(str(c3_obj.text))
    count = 0
    while count < len(ex1):
        if count >= 0 and count < 8:
            if count == 0:
                pdf.cell(0, 10, chr(150) + ' ' + res, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        elif count >= 8 and count < 15:
            if count == 8:
                pdf.cell(0, 10, chr(150) + ' ' + res1, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        else:
            if count == 16:
                pdf.cell(0, 10, chr(150) + ' ' + res2, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        count = count+1

    # 2.3
    # pdf.set_link(lab2, y=-1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.- '+indexList[cont], 0, 1)
    cont = cont+1
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "20:18:36":
                                        res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "UTC":
                                        res1 = y

    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el 11 de Novembre del 2020 a les '+res+' '+res1, 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.1.- Configuració criptogràfica del dispositiu', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu no té configuració de crypto ', 0, 1, 'L')
    pdf.set_font('Times', 'B', 12)

    # 2.3.2
    pdf.cell(0, 10, '2.3.2.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')
    idList2 = list()
    portList2 = list()
    contLinks = 0
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList2.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList2.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(ex1):
        ex1.pop(count)
    count = 0
    while count < len(ex2):
        ex2.pop(count)
    ex3 = list()
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.1.1.1":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.252":
                                            ex1.append(y)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.2.1":
                                            ex2.append(y)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.0":
                                            ex2.append(y)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.2.2.1":
                                            ex3.append(y)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.252":
                                            ex3.append(y)
    count = 0
    while count < len(idList2):
        pdf.cell(10)
        if count == 0:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[0]+' :'+portList2[0]+':', 0, 1)
        if count == 1:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[1]+' :'+portList2[1]+':'+ex1[0]+' ('+ex1[1]+')', 0, 1)
        if count == 2:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[count]+' :'+portList2[count]+':'+ex2[0]+' ('+ex2[1]+')', 0, 1)
        if count == 3:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[3]+' :'+portList2[3]+':'+ex3[0]+' ('+ex3[1]+')', 0, 1)
        if count == 4:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[4]+' :'+portList2[4]+':', 0, 1)
        count = count+1

    # 2.3.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.3.3.- Configuració dels protocols d'enrutament", 0, 1)
    pdf.set_font('Times', '', 12)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "ospf":
                                        res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "100":
                                        res1 = y
    pdf.cell(0, 10, "El protocol de enrutament utilitzat és "+res.upper() +
            " "+res1+", amb la següent configuració (xarxes publicades):", 0, 1, 'L')
    pdf.cell(10)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "0":
                                            res = y
    pdf.cell(0, 10, chr(150) + ' Àrea ' + res+':', 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.1.1.0":
                                            res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "0.0.0.3":
                                            res1 = y
    pdf.cell(0, 10, chr(149) + ' Xarxa '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.2.2.0":
                                            res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "0.0.0.3":
                                            res1 = y
    pdf.cell(0, 10, chr(149) + ' Xarxa '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.2.0":
                                            res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "0.0.0.255":
                                            res1 = y
    pdf.cell(0, 10, chr(149) + ' Xarxa '+res+' màscara invertida '+res1, 0, 1)

    # 2.3.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.4.- Configuració de Llistes de Control de Accés', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu no té configurada cap  ACL.', 0, 1, 'L')
    pdf.set_font('Times', 'B', 12)
    # 2.3.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.3.5.- Configuració de Banners", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurats els següents Banners:", 0, 1)
    pdf.cell(10)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "exec":
                                        res = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "incoming":
                                        res1 = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "login":
                                        res2 = y
    pdf.cell(10)
    count = 0
    while count < len(ex1):
        ex1.pop(count)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "*" in c3_obj.text:
                                ex1.append(str(c3_obj.text))
    count = 0
    while count < len(ex1):
        if count >= 0 and count < 8:
            if count == 0:
                pdf.cell(0, 10, chr(150) + ' ' + res, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        elif count >= 8 and count < 15:
            if count == 8:
                pdf.cell(0, 10, chr(150) + ' ' + res1, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        else:
            if count == 16:
                pdf.cell(0, 10, chr(150) + ' ' + res2, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        count = count+1

    # 2.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.- '+indexList[cont], 0, 1)
    cont = cont+1
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "20:40:48":
                                        res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "UTC":
                                        res1 = y

    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el 11 de Novembre del 2020 a les '+res+' '+res1, 0, 1)

    # 2.4.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.1.- Configuració criptogràfica del dispositiu', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu té la següent configuració de crypto: ', 0, 1, 'L')
    pdf.cell(10)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "10.1.1.2":
                                        res = y
    pdf.set_font('Times', '', 12)

    pdf.cell(0, 10, chr(150) + ' Connexió amb '+res, 0, 1)
    pdf.cell(20)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "10":
                                        res = y

    pdf.cell(0, 10, chr(149)+' Política de regles número '+res+':', 0, 1)
    pdf.cell(30)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "aes":
                                            res = y

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "256":
                                            res1 = y

    pdf.cell(0, 10, chr(164)+' Encriptació '+res+', '+res1, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "pre-share":
                                            res = y
    pdf.cell(0, 10, chr(164)+' Autenticació '+res, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "5":
                                            res = y
    pdf.cell(0, 10, chr(164)+' Diffie-Helmann grup '+res, 0, 1)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "vpnpa55":
                                        res = y
    pdf.cell(20)
    pdf.cell(0, 10, chr(149)+' Contrasenya ISAKMP: '+res, 0, 1)
    pdf.cell(20)
    pdf.cell(0, 10, chr(149)+' Configuració VPN: ', 0, 1)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "VPN":
                                        res = y
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' Conjunt de transformació: '+res, 0, 1)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "esp-aes":
                                        res = y
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' Configuració Encriptació ESP: '+res, 0, 1)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "esp-sha-hmac":
                                        res = y
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' Configuració Signatura ESP: '+res, 0, 1)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "tunnel":
                                            res = y
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' Mode '+res, 0, 1)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "crypto" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "110":
                                            res = y
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' ACL número '+res, 0, 1)

    # 2.4.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.2.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és:', 0, 1, 'L')
    idList3 = list()
    portList3 = list()
    contLinks = 0
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList3.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList3.append(
                                            str(c4_obj.text).replace("label:", ""))
    count = 0
    while count < len(ex1):
        ex1.pop(count)
    count = 0
    while count < len(ex2):
        ex2.pop(count)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.2.2.2":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.252":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.3.1":
                                            ex2.append(y)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.0":
                                            ex2.append(y)
    count = 0
    while count < len(idList1):
        pdf.cell(10)
        if count == 0:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList3[0]+' :'+portList3[0]+':', 0, 1)
        if count == 1:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList3[1]+' :'+portList3[1]+':'+ex1[0]+' ('+ex1[1]+')', 0, 1)
        if count == 2:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList3[count]+' :'+portList3[count]+':'+ex2[0]+' ('+ex2[1]+')', 0, 1)
        if count == 3:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList3[3]+' :'+portList3[3]+':', 0, 1)
        if count == 4:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList3[4]+' :'+portList3[4]+':', 0, 1)
        count = count+1

    # 2.4.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.4.3.- Configuració dels protocols d'enrutament", 0, 1)
    pdf.set_font('Times', '', 12)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "ospf":
                                        res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "100":
                                        res1 = y
    pdf.cell(0, 10, "El protocol de enrutament utilitzat és "+res.upper() +
            " "+res1+", amb la següent configuració (xarxes publicades):", 0, 1, 'L')
    pdf.cell(10)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "0":
                                            res = y
    pdf.cell(0, 10, chr(150) + ' Àrea ' + res+':', 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.2.2.0":
                                            res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "0.0.0.3":
                                            res1 = y
    pdf.cell(0, 10, chr(149) + ' Xarxa '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.3.0":
                                            res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "0.0.0.255":
                                            res1 = y
    pdf.cell(0, 10, chr(149) + ' Xarxa '+res+' màscara invertida '+res1, 0, 1)

    # 2.4.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.4.4.- Configuració de Llistes de Control d'Accés", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurada la següent ACL:", 0, 1)

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "110":
                                        res = y
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) + ' Número ' + res+':', 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "ip":
                                        res = y

    pdf.cell(0, 10, chr(149) + ' PERMIT ('+res.upper()+')', 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.3.0":
                                        res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "0.0.0.255":
                                        res1 = y
    pdf.cell(0, 10, chr(164)+' ORIGEN: '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.1.0":
                                        res = y
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "0.0.0.255":
                                        res1 = y
    pdf.cell(0, 10, chr(164)+' DESTÍ: '+res+' màscara invertida '+res1, 0, 1)

    # 2.4.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.4.5.- Configuració de Banners", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurats els següents Banners:", 0, 1)
    pdf.cell(10)
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "exec":
                                        res = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "incoming":
                                        res1 = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "login":
                                        res2 = y
    pdf.cell(10)
    count = 0
    while count < len(ex1):
        ex1.pop(count)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "*" in c3_obj.text:
                                ex1.append(str(c3_obj.text))
    count = 0
    while count < len(ex1):
        if count >= 0 and count < 8:
            if count == 0:
                pdf.cell(0, 10, chr(150) + ' ' + res, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        elif count >= 8 and count < 15:
            if count == 8:
                pdf.cell(0, 10, chr(150) + ' ' + res1, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        else:
            if count == 16:
                pdf.cell(0, 10, chr(150) + ' ' + res2, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        count = count+1

    # 2.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    contLinks = 0
    idList4 = list()
    portList4 = list()
    parse = CiscoConfParse('Ex1')

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList4.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList4.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList4):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList4[count]+' :'+portList4[count], 0, 1)
        count = count+1

    # 2.6
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    contLinks = 0
    idList5 = list()
    portList5 = list()
    parse = CiscoConfParse('Ex1')

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList5.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList5.append(
                                            str(c4_obj.text).replace("label:", ""))
    count = 0
    while count < len(idList5):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList5[count]+' :'+portList5[count], 0, 1)
        count = count+1

    # 2.7
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.1.3/24":
                                        res = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.1.1":
                                        res1 = y

    contLinks = 0
    idList6 = list()
    portList6 = list()
    parse = CiscoConfParse('Ex1')

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList6.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList6.append(
                                            str(c4_obj.text).replace("label:", ""))
    count = 0
    while count < len(idList6):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList6[count]+' :'+portList6[count]+'. Configuració IP:'+res+' (DG:'+res1+')', 0, 1)
        count = count+1

    # 2.8
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.2.3/24":
                                        res = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.2.1":
                                        res1 = y
    contLinks = 0
    idList7 = list()
    portList7 = list()
    parse = CiscoConfParse('Ex1')

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList7.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList7.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList7):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList7[count]+' :'+portList7[count]+'. Configuració IP:'+res+' (DG:'+res1+')', 0, 1)
        count = count+1

    # 2.9
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.3.3/24":
                                        res = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.3.1":
                                        res1 = y

    contLinks = 0
    idList8 = list()
    portList8 = list()
    parse = CiscoConfParse('Ex1')

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList8.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList8.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList8):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList8[count]+' :'+portList8[count]+'. Configuració IP:'+res+' (DG:'+res1+')', 0, 1)
        count = count+1

    # 2.9
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '3.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'La configuració de les interfícies (links) de interconnexió entre equips és: ', 0, 1, 'L')

    # LINK10
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "alpine-a":
                                name1 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id1 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n1" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "unmanaged-switch-0":
                                name2 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id2 = y

    pdf.cell(0, 10, chr(150) + ' Link 10: connecta '+id1 +
            ' ('+name1+')'+' amb ' + id2+' ('+name2+')', 0, 1)

    # LINK 11
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n1" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "unmanaged-switch-0":
                                name3 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id3 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-1":
                                name4 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id4 = y

    pdf.cell(0, 10, chr(150) + ' Link 11: connecta '+id3 +
            ' ('+name3+')'+' amb ' + id4+' ('+name4+')', 0, 1)

    # LINK 12
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-1":
                                name5 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        id5 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-2":
                                name6 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id6 = y

    pdf.cell(0, 10, chr(150) + ' Link 12: connecta '+id5 +
            ' ('+name5+')'+' amb ' + id6+' ('+name6+')', 0, 1)

    # LINK 13
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-2":
                                name7 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        id7 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "unmanaged-switch-1":
                                name8 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id8 = y

    pdf.cell(0, 10, chr(150) + ' Link 13: connecta '+id7 +
            ' ('+name7+')'+' amb ' + id8+' ('+name8+')', 0, 1)

    # LINK 14
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-2":
                                name9 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i3":
                                        id9 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-3":
                                name10 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id10 = y

    pdf.cell(0, 10, chr(150) + ' Link 14: connecta '+id9 +
            ' ('+name9+')'+' amb ' + id10+' ('+name10+')', 0, 1)

    # LINK 15
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "unmanaged-switch-1":
                                name11 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id11 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "alpine-b":
                                name12 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id12 = y

    pdf.cell(0, 10, chr(150) + ' Link 15: connecta '+id11 +
            ' ('+name11+')'+' amb ' + id12+' ('+name12+')', 0, 1)

    # LINK 16
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-3":
                                name13 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        id13 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "unmanaged-switch-2":
                                name14 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id14 = y

    pdf.cell(0, 10, chr(150) + ' Link 16: connecta '+id13 +
            ' ('+name13+')'+' amb ' + id14+' ('+name14+')', 0, 1)

    # LINK 17
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "unmanaged-switch-2":
                                name15 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id15 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "alpine-c":
                                name16 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id16 = y

    pdf.cell(0, 10, chr(150) + ' Link 17: connecta '+id15 +
            ' ('+name15+')'+' amb ' + id16+' ('+name16+')', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El resum de les adreces IP de les interfícies és: ', 0, 1, 'L')

    # Taula
    pdf.set_font('Times', '', 12)
    pdf.set_fill_color(0, 0, 255)
    pdf.cell(30, 10, "Xarxa", 1, 0)
    pdf.cell(30, 10, "Equip1", 1, 0)
    pdf.cell(20, 10, "Interfície1", 1, 0)
    pdf.cell(30, 10, "IP1", 1, 0)
    pdf.cell(30, 10, "Equip2", 1, 0)
    pdf.cell(20, 10, "Interfície2", 1, 0)
    pdf.cell(30, 10, "IP2", 1, 1)

    # FILA 1
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.1.1.1":
                                            ip1 = y
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.1.1.0":
                                            x1 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-2":
                                e1 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        i1 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-1":
                                e2 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        i2 = y

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.1.1.2":
                                            ip2 = y

    pdf.cell(30, 10, x1, 1, 0)
    pdf.cell(30, 10, e1, 1, 0)
    pdf.cell(20, 10, i1, 1, 0)
    pdf.cell(30, 10, ip1, 1, 0)
    pdf.cell(30, 10, e2, 1, 0)
    pdf.cell(20, 10, i2, 1, 0)
    pdf.cell(30, 10, ip2, 1, 1)

    # FILA 2
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.2.2.1":
                                            ip3 = y
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.2.2.0":
                                            x2 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-2":
                                e3 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i3":
                                        i3 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-3":
                                e4 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        i4 = y

    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.2.2.2":
                                            ip4 = y

    pdf.cell(30, 10, x2, 1, 0)
    pdf.cell(30, 10, e3, 1, 0)
    pdf.cell(20, 10, i3, 1, 0)
    pdf.cell(30, 10, ip3, 1, 0)
    pdf.cell(30, 10, e4, 1, 0)
    pdf.cell(20, 10, i4, 1, 0)
    pdf.cell(30, 10, ip4, 1, 1)

    # FILA 3
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.1.1":
                                            ip5 = y
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.1.0":
                                            x3 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-1":
                                e5 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        i5 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "alpine-a":
                                e6 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        i6 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.1.3/24":
                                        ip6 = "192.168.1.3"

    pdf.cell(30, 10, x3, 1, 0)
    pdf.cell(30, 10, e5, 1, 0)
    pdf.cell(20, 10, i5, 1, 0)
    pdf.cell(30, 10, ip5, 1, 0)
    pdf.cell(30, 10, e6, 1, 0)
    pdf.cell(20, 10, i6, 1, 0)
    pdf.cell(30, 10, ip6, 1, 1)

    # FILA 4
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.2.1":
                                            ip7 = y
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.2.0":
                                            x4 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-2":
                                e7 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        i7 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "alpine-b":
                                e8 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        i8 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.2.3/24":
                                        ip8 = "192.168.2.3"
    pdf.cell(30, 10, x4, 1, 0)
    pdf.cell(30, 10, e7, 1, 0)
    pdf.cell(20, 10, i7, 1, 0)
    pdf.cell(30, 10, ip7, 1, 0)
    pdf.cell(30, 10, e8, 1, 0)
    pdf.cell(20, 10, i8, 1, 0)
    pdf.cell(30, 10, ip8, 1, 1)

    # FILA 5
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.3.1":
                                            ip9 = y
                            if "router" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "192.168.3.0":
                                            x5 = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "iosv-3":
                                e9 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        i9 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "alpine-c":
                                e10 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        i10 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "192.168.3.3/24":
                                        ip10 = "192.168.3.3"

    pdf.cell(30, 10, x5, 1, 0)
    pdf.cell(30, 10, e9, 1, 0)
    pdf.cell(20, 10, i9, 1, 0)
    pdf.cell(30, 10, ip9, 1, 0)
    pdf.cell(30, 10, e10, 1, 0)
    pdf.cell(20, 10, i10, 1, 0)
    pdf.cell(30, 10, ip10, 1, 1)
    pdf.output("Ex1.pdf")

elif eleccio=="Ex2":
    # INDEX
    pdf.cell(0, 10, 'ÍNDEX', 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.- Introducció...........................................................................................................................................4', 0, 1)
    pdf.cell(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.1.- Descripció........................................................................................................................4', 0, 1)
    pdf.cell(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.2.- Objectius..........................................................................................................................4', 0, 1)
    pdf.cell(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.3.- Descripció General de les infraestructures...................................................................4', 0, 1)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.- Configuració dels dispositius................................................................................................................4', 0, 1)

    cont = 0
    indexList = list()
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            for c2_obj in c1_obj.children:
                if "label:" in c2_obj.text:
                    indexList.append(str(c2_obj.text).replace("label:", ""))
    # 2.1
    cont = 0
    df.set_font('Times', 'B', 12)
    pdf.cell(20)
    pdf.cell(0, 10, '2.1.-' +indexList[cont]+'................................................................................................................................4', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.1.1.- Interfícies..............................................................................................................4', 0, 1)
    pdf.cell(20)

    # 2.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.-' +indexList[cont]+'................................................................................................................................5', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.1.- Interfícies...............................................................................................................5', 0, 1)
    pdf.cell(20)
    # 2.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.-' +indexList[cont]+'.....................................................................................................................................5', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.1.- Configuració criptogràfica del dispositiu.............................................................5', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.2.- Interfícies.................................................................................................................5', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.3.- Configuració dels protocols de enrutament.........................................................5', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.4.- Configuració de Llistes de Control Accés.............................................................6', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.5.- Configuració de Banners........................................................................................6', 0, 1)
    pdf.cell(20)

    # 2.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.-' +indexList[cont]+'...................................................................................................................................7', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.1.- Interfícies..................................................................................................................8', 0, 1)
    pdf.cell(20)

    # 2.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.-' +indexList[cont]+'...................................................................................................................................8', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.1.- Interfícies..................................................................................................................8', 0, 1)
    pdf.cell(20)

    # 2.6
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.-' +indexList[cont]+'...........................................................................................................................8', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.1.- Interfícies..................................................................................................................8', 0, 1)
    pdf.cell(20)

    # 2.7
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.-' +indexList[cont]+'.....................................................................................................................................9', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.1.- Interfícies..................................................................................................................9', 0, 1)
    pdf.cell(20)

    # 2.8
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.-' +indexList[cont]+'................................................................................................................................9', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.1.- Configuració criptogràfica del dispositiu.............................................................9', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.2.- Interfícies.................................................................................................................9', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.3.- Configuració dels protocols de enrutament.........................................................9', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.4.- Configuració de Llistes de Control Accés.............................................................9', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.5.- Configuració de Banners........................................................................................10', 0, 1)
    pdf.cell(20)

    # 2.9
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.-' +indexList[cont]+'..................................................................................................................................11', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.1.- Configuració criptogràfica del dispositiu.............................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.2.- Interfícies.................................................................................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.3.- Configuració dels protocols de enrutament.........................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.4.- Configuració de Llistes de Control Accés.............................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.5.- Configuració de Banners........................................................................................12', 0, 1)
    pdf.cell(20)

    # 3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '3.- Interfícies................................................................................................................................13', 0, 1)

    # Introduction
    pdf.add_page()
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, '1.- Introducció', 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.1- Descripció', 0, 1)
    pdf.set_font('Times', '', 12)

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'lab'):
        for c1_obj in intf_obj.children:
            if "title:" in c1_obj.text:
                titul = str(c1_obj.text).replace("title:", "")

    pdf.multi_cell(0, 10, 'El present document descriu la topologia realitzada amb la configuració ' +titul+' a la \nempresa TecnoCampus.', 0, 1, 'L')

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.2- Objectius', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.multi_cell(0, 10, "El objectiu d'aquest document és la de formalitzar el traspàs d'informació al equip tècnic \nresponsable del manteniment de les infraestructures instal·lades. Aquesta informació fa \nreferencia al disseny, instal·lació i configuració dels dispositius i sistemes afectats per la implementació.", 0, 1, 'L')
    pdf.cell(0, 10, 'La present documentació inclou:', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) +
            ' Descripció general de les infraestructures instal·lades', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+' Configuració de les interfícies de xarxa', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) +
            ' Configuració de les polítiques per les connexions VPN', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+" Configuració dels protocols d'enrutament", 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+" Configuració de les llistes de control d'accés", 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+' Configuració dels banners', 0, 1)

    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, '1.3.- Descripció General de les infraestructures', 0, 1)

    contId = 0
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id:" in c1_obj.text:
                contId = contId+1

    contLinks = 0
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'links'):
        for c1_obj in intf_obj.children:
            if "id:" in c1_obj.text:
                contLinks = contLinks+1

    pdf.cell(10)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 5, 'En aquesta topologia tenim '+str(contId) +' equips, connectats a través de '+str(contLinks)+' links', 0, 1, 'L')

    # Configuració Dispositius
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, '2.- Configuració dels dispositius', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'A continuació, es detalla la configuració dels diferents dispositius: ', 0, 1)
    cont = 0

    # 2.1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.1.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.1.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    idList = list()
    portList = list()
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n0" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList[count]+' :'+portList[count], 0, 1)
        count = count+1

    # 2.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    idList1 = list()
    portList1 = list()

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n1" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                idList1.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList1.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList1):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +idList1[count]+' :'+portList1[count], 0, 1)
        count = count+1

    # 2.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.- '+indexList[cont], 0, 1)
    cont = cont+1

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "10:58:27":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "UTC":
                                        res1 = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "13":
                                        res2 = y


    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el ' +
            res2+' de Novembre del 2020 a les '+res+' '+res1, 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.1.- Configuració criptogràfica del dispositiu', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu no té configuració de crypto', 0, 1, 'L')
    # 2.3.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.2.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és', 0, 1, 'L')
    idList2 = list()
    portList2 = list()
    contLinks = 0
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList2.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList2.append(
                                            str(c4_obj.text).replace("label:", ""))

    ex1 = list()
    ex2 = list()
    ex3 = list()
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "172.22.34.65":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.224":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "172.22.34.97":
                                            ex2.append(y)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.240":
                                            ex2.append(y)

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "172.22.34.1":
                                            ex3.append(y)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.192":
                                            ex3.append(y)
    count = 0
    while count < len(idList2):
        pdf.cell(10)
        if count == 0:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[0]+' :'+portList2[0]+':', 0, 1)
        if count == 1:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[1]+' :'+portList2[1]+':'+ex1[0]+' ('+ex1[1]+')', 0, 1)
        if count == 2:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[count]+' :'+portList2[count]+':'+ex2[0]+' ('+ex2[1]+')', 0, 1)
        if count == 3:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[3]+' :'+portList2[3]+':'+ex3[0]+' ('+ex3[1]+')', 0, 1)
        if count == 4:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[4]+' :'+portList2[4]+':', 0, 1)
        count = count+1

    # 2.3.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.3.3.- Configuració dels protocols d'enrutament", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "En aquest cas tenim un configuració estàtica i no dinàmica", 0, 1)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "0.0.0.0":
                                    res = y
                                if y == "172.22.34.1":
                                    res1 = y

    pdf.cell(0, 10, "La xarxa es "+res+" amb máscara de " +
            res+" amb la ruta per defecta "+res1, 0, 1)

    # 2.3.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.3.4.- Configuració de Llistes de Control d'Accés", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurada la següent ACL:", 0, 1)

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "100":
                                        res = y
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) + ' Número ' + res+':', 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "tcp":
                                        res = y

    pdf.cell(0, 10, chr(149) + ' PERMIT ('+res.upper()+')', 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.64":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "0.0.0.31":
                                        res1 = y
    pdf.cell(0, 10, chr(164)+' ORIGEN: '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.3":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "www":
                                        res1 = y
    pdf.cell(0, 10, chr(164)+' DESTÍ: '+res +
            ' a través del port '+res1.upper(), 0, 1)

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "icmp":
                                        res = y
    pdf.cell(20)
    pdf.cell(0, 10, chr(149) + ' PERMIT ('+res.upper()+')', 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.64":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "0.0.0.31":
                                        res1 = y
    pdf.cell(0, 10, chr(164)+' ORIGEN: '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.3":
                                        res = y
    pdf.cell(0, 10, chr(164)+' DESTÍ: '+res, 0, 1)

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "101":
                                        res = y
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) + ' Número ' + res+':', 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "tcp":
                                        res = y

    pdf.cell(0, 10, chr(149) + ' PERMIT ('+res.upper()+')', 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.96":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "0.0.0.15":
                                        res1 = y
    pdf.cell(0, 10, chr(164)+' ORIGEN: '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.2":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "22":
                                        res1 = y
    pdf.cell(0, 10, chr(164)+' DESTÍ: '+res+' a través del port '+res1, 0, 1)

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "icmp":
                                        res = y
    pdf.cell(20)
    pdf.cell(0, 10, chr(149) + ' PERMIT ('+res.upper()+')', 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.96":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "0.0.0.15":
                                        res1 = y
    pdf.cell(0, 10, chr(164)+' ORIGEN: '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(30)

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "access-list" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.2":
                                        res = y
    pdf.cell(0, 10, chr(164)+' DESTÍ: '+res, 0, 1)

    # 2.3.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.3.5.- Configuració de Banners", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurats els següents Banners:", 0, 1)
    pdf.cell(10)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "exec":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "incoming":
                                        res1 = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "login":
                                        res2 = y
    pdf.cell(10)
    count = 0
    while count < len(ex1):
        ex1.pop(count)

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "*" in c3_obj.text:
                                ex1.append(str(c3_obj.text))
    count = 0
    while count < len(ex1):
        if count >= 0 and count < 8:
            if count == 0:
                pdf.cell(0, 10, chr(150) + ' ' + res, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        elif count >= 8 and count < 15:
            if count == 8:
                pdf.cell(0, 10, chr(150) + ' ' + res1, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        else:
            if count == 16:
                pdf.cell(0, 10, chr(150) + ' ' + res2, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        count = count+1

    # 2.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    idList3 = list()
    portList3 = list()

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                idList3.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList3.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList3):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList3[count]+' :'+portList3[count], 0, 1)
        count = count+1

    # 2.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    idList4 = list()
    portList4 = list()

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                idList4.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList4.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList4):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList4[count]+' :'+portList4[count], 0, 1)
        count = count+1

    # 2.6
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.62/26":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.1":
                                        res1 = y

    contLinks = 0
    idList5 = list()
    portList5 = list()

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList5.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList5.append(
                                            str(c4_obj.text).replace("label:", ""))
    count = 0
    while count < len(idList5):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList5[count]+' :'+portList5[count]+'. Configuració IP:'+res+' (DG:'+res1+')', 0, 1)
        count = count+1

    # 2.7
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "172.22.34.98/28":
                                    res = y
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "172.22.34.97":
                                        res1 = y

    contLinks = 0
    idList6 = list()
    portList6 = list()

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList6.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList6.append(
                                            str(c4_obj.text).replace("label:", ""))
    count = 0
    while count < len(idList6):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList6[count]+' :'+portList6[count]+'. Configuració IP:'+res+' (DG:'+res1+')', 0, 1)
        count = count+1

    # 2.8
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.- '+indexList[cont], 0, 1)
    cont = cont+1

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "07:54:36":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "UTC":
                                        res1 = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "11":
                                        res2 = y


    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el ' +
            res2+' de Novembre del 2020 a les '+res+' '+res1, 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.1.- Configuració criptogràfica del dispositiu', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu no té configuració de crypto', 0, 1, 'L')
    # 2.8.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.2.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és', 0, 1, 'L')
    idList7 = list()
    portList7 = list()
    contLinks = 0
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList7.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList7.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(ex1):
        ex1.pop(count)
    ex1 = list()
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "172.22.34.3":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.192":
                                            ex1.append(y)
    count = 0
    while count < len(idList7):
        pdf.cell(10)
        if count == 0:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList7[0]+' :'+portList7[0]+':', 0, 1)
        if count == 1:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList7[1]+' :'+portList7[1]+':'+ex1[0]+' ('+ex1[1]+')', 0, 1)
        if count == 2:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList7[count]+' :'+portList7[count], 0, 1)
        if count == 3:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList7[3]+' :'+portList7[3]+':', 0, 1)
        if count == 4:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList7[4]+' :'+portList7[4]+':', 0, 1)
        count = count+1

    # 2.8.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.8.3.- Configuració dels protocols d'enrutament", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "En aquest cas tenim un configuració estàtica i no dinàmica", 0, 1)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "0.0.0.0":
                                    res = y
                                if y == "172.22.34.1":
                                    res1 = y

    pdf.cell(0, 10, "La xarxa es "+res+" amb máscara de " +
            res+" amb la ruta per defecta "+res1, 0, 1)

    # 2.8.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.8.4.- Configuració de Llistes de Control d'Accés", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu no té configurada cap  ACL.", 0, 1)

    # 2.8.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.3.5.- Configuració de Banners", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurats els següents Banners:", 0, 1)
    pdf.cell(10)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "exec":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "incoming":
                                        res1 = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "login":
                                        res2 = y
    pdf.cell(10)
    count = 0
    while count < len(ex1):
        ex1.pop(count)

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "*" in c3_obj.text:
                                ex1.append(str(c3_obj.text))
    count = 0
    while count < len(ex1):
        if count >= 0 and count < 8:
            if count == 0:
                pdf.cell(0, 10, chr(150) + ' ' + res, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        elif count >= 8 and count < 15:
            if count == 8:
                pdf.cell(0, 10, chr(150) + ' ' + res1, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        else:
            if count == 16:
                pdf.cell(0, 10, chr(150) + ' ' + res2, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        count = count+1

    # 2.9
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.- '+indexList[cont], 0, 1)
    cont = cont+1

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "10:21:00":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "UTC":
                                        res1 = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "13":
                                        res2 = y


    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el ' +
            res2+' de Novembre del 2020 a les '+res+' '+res1, 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.1.- Configuració criptogràfica del dispositiu', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu no té configuració de crypto', 0, 1, 'L')
    # 2.9.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.2.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és', 0, 1, 'L')
    idList8 = list()
    portList8 = list()
    contLinks = 0
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList8.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList8.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(ex1):
        ex1.pop(count)
    ex1 = list()
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "172.22.34.2":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.192":
                                            ex1.append(y)
    count = 0
    while count < len(idList8):
        pdf.cell(10)
        if count == 0:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList8[0]+' :'+portList8[0]+':', 0, 1)
        if count == 1:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList8[1]+' :'+portList8[1]+':'+ex1[0]+' ('+ex1[1]+')', 0, 1)
        if count == 2:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList8[count]+' :'+portList8[count], 0, 1)
        if count == 3:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList8[3]+' :'+portList8[3]+':', 0, 1)
        if count == 4:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList8[4]+' :'+portList8[4]+':', 0, 1)
        count = count+1

    # 2.9.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.9.3.- Configuració dels protocols d'enrutament", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "En aquest cas tenim un configuració estàtica i no dinàmica", 0, 1)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "0.0.0.0":
                                    res = y
                                if y == "172.22.34.1":
                                    res1 = y

    pdf.cell(0, 10, "La xarxa es "+res+" amb máscara de " +
            res+" amb la ruta per defecta "+res1, 0, 1)

    # 2.9.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.9.4.- Configuració de Llistes de Control d'Accés", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu no té configurada cap  ACL.", 0, 1)

    # 2.9.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.9.5.- Configuració de Banners", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurats els següents Banners:", 0, 1)
    pdf.cell(10)
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "exec":
                                        res = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "incoming":
                                        res1 = y
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "login":
                                        res2 = y
    pdf.cell(10)
    count = 0
    while count < len(ex1):
        ex1.pop(count)

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "*" in c3_obj.text:
                                ex1.append(str(c3_obj.text))
    count = 0
    while count < len(ex1):
        if count >= 0 and count < 8:
            if count == 0:
                pdf.cell(0, 10, chr(150) + ' ' + res, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        elif count >= 8 and count < 15:
            if count == 8:
                pdf.cell(0, 10, chr(150) + ' ' + res1, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        else:
            if count == 16:
                pdf.cell(0, 10, chr(150) + ' ' + res2, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        count = count+1

    # 3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '3.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'La configuració de les interfícies (links) de interconnexió entre equips és: ', 0, 1, 'L')

    # LINK10
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n0" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "PC1":
                                name1 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id1 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n1" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SW1":
                                name2 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id2 = y

    pdf.cell(0, 10, chr(150) + ' Link 10: connecta '+id1 +
            ' ('+name1+')'+' amb ' + id2+' ('+name2+')', 0, 1)

    # LINK 11
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n1" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SW1":
                                name3 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id3 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "R1":
                                name4 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id4 = y

    pdf.cell(0, 10, chr(150) + ' Link 11: connecta '+id3 +
            ' ('+name3+')'+' amb ' + id4+' ('+name4+')', 0, 1)

    # LINK 12
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "PC2":
                                name5 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id5 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SW2":
                                name6 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id6 = y

    pdf.cell(0, 10, chr(150) + ' Link 12: connecta '+id5 +
            ' ('+name5+')'+' amb ' + id6+' ('+name6+')', 0, 1)

    # LINK 13
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SW2":
                                name7 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id7 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "R1":
                                name8 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        id8 = y

    pdf.cell(0, 10, chr(150) + ' Link 13: connecta '+id7 +
            ' ('+name7+')'+' amb ' + id8+' ('+name8+')', 0, 1)

    # LINK 14
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SERVER":
                                name9 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id9 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SW3":
                                name10 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id10 = y

    pdf.cell(0, 10, chr(150) + ' Link 14: connecta '+id9 +
            ' ('+name9+')'+' amb ' + id10+' ('+name10+')', 0, 1)

    # LINK 15
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SW3":
                                name11 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id11 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "R1":
                                name12 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i3":
                                        id12 = y

    pdf.cell(0, 10, chr(150) + ' Link 15: connecta '+id11 +
            ' ('+name11+')'+' amb ' + id12+' ('+name12+')', 0, 1)

    # LINK 16
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SSH":
                                name13 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id13 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SW3":
                                name14 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        id14 = y

    pdf.cell(0, 10, chr(150) + ' Link 16: connecta '+id13 +
            ' ('+name13+')'+' amb ' + id14+' ('+name14+')', 0, 1)

    # LINK 17
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "HTTP":
                                name15 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id15 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SW3":
                                name16 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i3":
                                        id16 = y

    pdf.cell(0, 10, chr(150) + ' Link 17: connecta '+id15 +
            ' ('+name15+')'+' amb ' + id16+' ('+name16+')', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El resum de les adreces IP de les interfícies és: ', 0, 1, 'L')

    # Taula
    pdf.set_font('Times', '', 12)
    pdf.set_fill_color(0, 0, 255)
    pdf.cell(30, 10, "Xarxa", 1, 0)
    pdf.cell(30, 10, "Equip1", 1, 0)
    pdf.cell(20, 10, "Interfície1", 1, 0)
    pdf.cell(30, 10, "IP1", 1, 0)
    pdf.cell(30, 10, "Equip2", 1, 0)
    pdf.cell(20, 10, "Interfície2", 1, 0)
    pdf.cell(30, 10, "IP2", 1, 1)

    # FILA 1
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "172.22.34.64":
                                    x1 = y

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "R1":
                                e1 = y
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "172.22.34.65":
                                            ip1 = y

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        i1 = y

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n0" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "172.22.34.66/27":
                                    aux1 = y.split("/")
                                    for kk in aux1:
                                        if(kk == "172.22.34.66"):
                                            ip2 = kk

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n0" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "PC1":
                                e2 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "i0":
                                    i2 = y

    pdf.cell(30, 10, x1, 1, 0)
    pdf.cell(30, 10, e1, 1, 0)
    pdf.cell(20, 10, i1, 1, 0)
    pdf.cell(30, 10, ip1, 1, 0)
    pdf.cell(30, 10, e2, 1, 0)
    pdf.cell(20, 10, i2, 1, 0)
    pdf.cell(30, 10, ip2, 1, 1)

    # FILA 2
    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "172.22.34.96":
                                    x2 = y

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "R1":
                                e3 = y
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "172.22.34.97":
                                            ip3 = y

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        i3 = y

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "172.22.34.98/28":
                                    aux1 = y.split("/")
                                    for kk in aux1:
                                        if(kk == "172.22.34.98"):
                                            ip4 = kk

    parse = CiscoConfParse('Ex2')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "PC2":
                                e4 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "i0":
                                    i4 = y

    pdf.cell(30, 10, x2, 1, 0)
    pdf.cell(30, 10, e3, 1, 0)
    pdf.cell(20, 10, i3, 1, 0)
    pdf.cell(30, 10, ip3, 1, 0)
    pdf.cell(30, 10, e4, 1, 0)
    pdf.cell(20, 10, i4, 1, 0)
    pdf.cell(30, 10, ip4, 1, 1)
    pdf.output("Ex2.pdf")

else:
    # INDEX
    pdf.cell(0, 10, 'ÍNDEX', 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.- Introducció............................................................................................................................................4', 0, 1)
    pdf.cell(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.1.- Descripció........................................................................................................................4', 0, 1)
    pdf.cell(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.2.- Objectius..........................................................................................................................4', 0, 1)
    pdf.cell(20)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.3.- Descripció General de les infraestructures...................................................................4', 0, 1)

    # 2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.- Configuració dels dispositius................................................................................................................4', 0, 1)

    cont = 0
    indexList = list()
    # i0
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            aux = c1_obj.text.split(" ")
            if "n0" in aux:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        indexList.append(str(c2_obj.text).replace("label:", ""))
    # i1
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            aux = c1_obj.text.split(" ")
            if "n1" in aux:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        indexList.append(str(c2_obj.text).replace("label:", ""))
    # i2
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            aux = c1_obj.text.split(" ")
            if "n2" in aux:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        indexList.append(str(c2_obj.text).replace("label:", ""))
    # i3
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            aux = c1_obj.text.split(" ")
            if "n3" in aux:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        indexList.append(str(c2_obj.text).replace("label:", ""))
    # i4
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            aux = c1_obj.text.split(" ")
            if "n4" in aux:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        indexList.append(str(c2_obj.text).replace("label:", ""))
    # i5
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            aux = c1_obj.text.split(" ")
            if "n5" in aux:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        indexList.append(str(c2_obj.text).replace("label:", ""))
    # i6
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            aux = c1_obj.text.split(" ")
            if "n6" in aux:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        indexList.append(str(c2_obj.text).replace("label:", ""))
    # i7
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            aux = c1_obj.text.split(" ")
            if "n7" in aux:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        indexList.append(str(c2_obj.text).replace("label:", ""))
    # i8
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            aux = c1_obj.text.split(" ")
            if "n8" in aux:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        indexList.append(str(c2_obj.text).replace("label:", ""))
    # i9
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            aux = c1_obj.text.split(" ")
            if "n9" in aux:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        indexList.append(str(c2_obj.text).replace("label:", ""))
    # 2.1
    cont = 0
    pdf.set_font('Times', 'B', 12)
    pdf.cell(20)
    pdf.cell(0, 10, '2.1.-' +
            indexList[cont]+'...............................................................................................................................4', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.1.1.- Interfícies..............................................................................................................5', 0, 1)

    # 2.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(20)
    pdf.cell(0, 10, '2.2.-' +
            indexList[cont]+'...............................................................................................................................5', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.1.- Interfícies..............................................................................................................5', 0, 1)
    pdf.cell(20)

    # 2.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.-' +
            indexList[cont]+'...............................................................................................................................5', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.1.- Interfícies...............................................................................................................5', 0, 1)
    pdf.cell(20)

    # 2.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.-' +
            indexList[cont]+'................................................................................................................................5', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.1.- Interfícies...............................................................................................................6', 0, 1)
    pdf.cell(20)

    # 2.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.-' +
            indexList[cont]+'....................................................................................................................................6', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.1.- Configuració criptogràfica del dispositiu.............................................................6', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.2.- Interfícies.................................................................................................................6', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.3.- Configuració dels protocols de enrutament.........................................................6', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.4.- Configuració de Llistes de Control Accés.............................................................7', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.5.- Configuració de Banners........................................................................................7', 0, 1)
    pdf.cell(20)

    # 2.6
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.-' +
            indexList[cont]+'..................................................................................................................................8', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.1.- Interfícies..................................................................................................................8', 0, 1)
    pdf.cell(20)

    # 2.7
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.-' +
            indexList[cont]+'...................................................................................................................................8', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.1.- Interfícies..................................................................................................................9', 0, 1)
    pdf.cell(20)

    # 2.8
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.-' +
            indexList[cont]+'.............................................................................................................................9', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.1.- Configuració criptogràfica del dispositiu.............................................................9', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.2.- Interfícies.................................................................................................................9', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.3.- Configuració dels protocols de enrutament..........................................................9', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.4.- Configuració de Llistes de Control Accés.............................................................9', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.5.- Configuració de Banners........................................................................................10', 0, 1)
    pdf.cell(20)

    # 2.9
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.-' +
            indexList[cont]+'.................................................................................................................................10', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.1.- Configuració criptogràfica del dispositiu..............................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.2.- Interfícies..................................................................................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.3.- Configuració dels protocols de enrutament...........................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.4.- Configuració de Llistes de Control Accés..............................................................11', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.5.- Configuració de Banners.........................................................................................12', 0, 1)
    pdf.cell(20)

    # 2.10
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.10.-' +
            indexList[cont]+'................................................................................................................................12', 0, 1)
    pdf.cell(30)
    cont = cont+1

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.10.1.- Configuració criptogràfica del dispositiu.............................................................13', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.10.2.- Interfícies.................................................................................................................13', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.10.3.- Configuració dels protocols de enrutament.........................................................13', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.10.4.- Configuració de Llistes de Control Accés.............................................................13', 0, 1)
    pdf.cell(30)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.10.5.- Configuració de Banners........................................................................................14', 0, 1)
    pdf.cell(20)

    # 3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '3.- Interfícies..................................................................................................................................15', 0, 1)

    # 1.0
    pdf.add_page()
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, '1.- Introducció', 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.1- Descripció', 0, 1)
    pdf.set_font('Times', '', 12)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'lab'):
        for c1_obj in intf_obj.children:
            if "title:" in c1_obj.text:
                titul = str(c1_obj.text).replace("title:", "")

    pdf.multi_cell(0, 10, 'El present document descriu la topologia realitzada amb la configuració ' +
                titul+' a la \nempresa TecnoCampus.', 0, 1, 'L')

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.2- Objectius', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.multi_cell(0, 10, "El objectiu d'aquest document és la de formalitzar el traspàs d'informació al equip tècnic \nresponsable del manteniment de les infraestructures instal·lades. Aquesta informació fa \nreferencia al disseny, instal·lació i configuració dels dispositius i sistemes afectats per la implementació.", 0, 1, 'L')
    pdf.cell(0, 10, 'La present documentació inclou:', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) +
            ' Descripció general de les infraestructures instal·lades', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+' Configuració de les interfícies de xarxa', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) +
            ' Configuració de les polítiques per les connexions VPN', 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+" Configuració dels protocols d'enrutament", 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+" Configuració de les llistes de control d'accés", 0, 1)
    pdf.cell(10)
    pdf.cell(0, 10, chr(150)+' Configuració dels banners', 0, 1)

    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, '1.3.- Descripció General de les infraestructures', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Actualment la topologia té la següent distribució: ', 0, 1)
    pdf.ln(10)

    contId = 0
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id:" in c1_obj.text:
                contId = contId+1

    contLinks = 0
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'links'):
        for c1_obj in intf_obj.children:
            if "id:" in c1_obj.text:
                contLinks = contLinks+1

    pdf.cell(10)
    pdf.cell(0, 5, 'En aquesta topologia tenim '+str(contId) +
            ' equips, connectats a través de '+str(contLinks)+' links', 0, 1, 'L')

    # 2.0 - Configuració Dispositius
    pdf.set_font('Times', 'B', 14)
    pdf.cell(0, 10, '2.- Configuració dels dispositius', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'A continuació, es detalla la configuració dels diferents dispositius: ', 0, 1)
    cont = 0

    # 2.1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.1.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.1.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    idList = list()
    portList = list()
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n0" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList[count]+' :'+portList[count], 0, 1)
        count = count+1

    # 2.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.2.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    count = 0
    while count < len(idList):
        idList.pop(count)
    count = 0
    while count < len(portList):
        portList.pop(count)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n1" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList[count]+' :'+portList[count], 0, 1)
        count = count+1

    # 2.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.3.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    count = 0
    while count < len(idList):
        idList.pop(count)
    count = 0
    while count < len(portList):
        portList.pop(count)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList[count]+' :'+portList[count], 0, 1)
        count = count+1

    # 2.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.4.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    count = 0
    while count < len(idList):
        idList.pop(count)
    count = 0
    while count < len(portList):
        portList.pop(count)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList.append(
                                            str(c4_obj.text).replace("label:", ""))

    count = 0
    while count < len(idList):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList[count]+' :'+portList[count], 0, 1)
        count = count+1

    # 2.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.- '+indexList[cont], 0, 1)
    cont = cont+1

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "12:03:59":
                                        res = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "UTC":
                                        res1 = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "15":
                                        res2 = y


    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el ' +
            res2+' de Novembre del 2020 a les '+res+' '+res1, 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.1.- Configuració criptogràfica del dispositiu', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu no té configuració de crypto', 0, 1, 'L')
    # 2.5.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.5.2.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és', 0, 1, 'L')

    idList2 = list()
    portList2 = list()
    contLinks = 0
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList2.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList2.append(
                                            str(c4_obj.text).replace("label:", ""))

    ex1 = list()
    ex2 = list()
    ex3 = list()
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.49":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.248":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.33":
                                            ex2.append(y)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.240":
                                            ex2.append(y)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.1":
                                            ex3.append(y)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.224":
                                            ex3.append(y)
    count = 0
    while count < len(idList2):
        pdf.cell(10)
        if count == 0:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[0]+' :'+portList2[0]+':', 0, 1)
        if count == 1:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[1]+' :'+portList2[1]+':'+ex1[0]+' ('+ex1[1]+')', 0, 1)
        if count == 2:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[count]+' :'+portList2[count]+':'+ex2[0]+' ('+ex2[1]+')', 0, 1)
        if count == 3:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[3]+' :'+portList2[3]+':'+ex3[0]+' ('+ex3[1]+')', 0, 1)
        if count == 4:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList2[4]+' :'+portList2[4]+':', 0, 1)
        count = count+1

    # 2.5.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.5.3.- Configuració dels protocols d'enrutament", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "No hi ha assignat cap protocol de enrutament", 0, 1, 'L')

    # 2.5.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.5.4.- Configuració de Llistes de Control d'Accés", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurada la següent ACL:", 0, 1)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "ICMP":
                                        res = y
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) + ' Nom ' + res+':', 0, 1)
    pdf.cell(20)
    pdf.cell(0, 10, chr(149) + ' PERMIT ('+res+')', 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                if "ICMP" in aux:
                                    for c4_obj in c3_obj.children:
                                        aux1 = c4_obj.text.split(" ")
                                        for y in aux1:
                                            if y == 'any':
                                                res = y
    pdf.cell(0, 10, chr(164)+' ORIGEN: '+res, 0, 1)
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' DESTÍ: '+res, 0, 1)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "SSH":
                                        res = y
    pdf.cell(10)
    pdf.cell(0, 10, chr(150) + ' Nom ' + res+':', 0, 1)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                if "SSH" in aux:
                                    for c4_obj in c3_obj.children:
                                        aux1 = c4_obj.text.split(" ")
                                        for y in aux1:
                                            if y == 'tcp':
                                                res = y


    pdf.cell(20)
    pdf.cell(0, 10, chr(149) + ' DENY ('+res.upper()+')', 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "SSH" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.34":
                                            res = y
    pdf.cell(0, 10, chr(164)+' ORIGEN: '+res, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "SSH" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.0":
                                            res = y
                                        if y == "0.0.0.31":
                                            res1 = y
                                        if y == "22":
                                            res2 = y

    pdf.cell(0, 10, chr(164)+' DESTÍ: '+res + ' màscara invertida ' +
            res1+' a través del port '+res2, 0, 1)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                if "SSH" in aux:
                                    for c4_obj in c3_obj.children:
                                        aux1 = c4_obj.text.split(" ")
                                        for y in aux1:
                                            if y == 'tcp':
                                                res = y
    pdf.cell(20)
    pdf.cell(0, 10, chr(149) + ' PERMIT ('+res.upper()+')', 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "SSH" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.32":
                                            res = y
                                        if y == "0.0.0.15":
                                            res1 = y
    pdf.cell(0, 10, chr(164)+' ORIGEN: '+res+' màscara invertida '+res1, 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "SSH" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.0":
                                            res = y
                                        if y == "0.0.0.31":
                                            res1 = y
                                        if y == "22":
                                            res2 = y
    pdf.cell(0, 10, chr(164)+' DESTÍ: '+res + ' màscara invertida ' +
            res1+' a través del port '+res2, 0, 1)
    pdf.cell(20)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                if "SSH" in aux:
                                    for c4_obj in c3_obj.children:
                                        aux1 = c4_obj.text.split(" ")
                                        for y in aux1:
                                            if y == 'icmp':
                                                res = y

    pdf.cell(0, 10, chr(149) + ' PERMIT ('+res.upper()+')', 0, 1)
    pdf.cell(30)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "SSH" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "any":
                                            res = y
    pdf.cell(0, 10, chr(164)+' ORIGEN: '+res, 0, 1)
    pdf.cell(30)
    pdf.cell(0, 10, chr(164)+' DESTÍ: '+res, 0, 1)

    # 2.5.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.5.5.- Configuració de Banners", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurats els següents Banners:", 0, 1)
    pdf.cell(10)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "exec":
                                        res = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "incoming":
                                        res1 = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "login":
                                        res2 = y
    pdf.cell(10)
    count = 0
    while count < len(ex1):
        ex1.pop(count)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "*" in c3_obj.text:
                                ex1.append(str(c3_obj.text))
    count = 0
    while count < len(ex1):
        if count >= 0 and count < 8:
            if count == 0:
                pdf.cell(0, 10, chr(150) + ' ' + res, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        elif count >= 8 and count < 15:
            if count == 8:
                pdf.cell(0, 10, chr(150) + ' ' + res1, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        else:
            if count == 16:
                pdf.cell(0, 10, chr(150) + ' ' + res2, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        count = count+1

    # 2.6
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.6.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    count = 0
    while count < len(idList):
        idList.pop(count)
    count = 0
    while count < len(portList):
        portList.pop(count)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList.append(
                                            str(c4_obj.text).replace("label:", ""))
    count = 0
    while count < len(idList):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList[count]+' :'+portList[count], 0, 1)
        count = count+1

    # 2.7
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.- '+indexList[cont], 0, 1)
    cont = cont+1
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.7.1.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és: ', 0, 1, 'L')

    count = 0
    while count < len(idList):
        idList.pop(count)
    count = 0
    while count < len(portList):
        portList.pop(count)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList.append(
                                            str(c4_obj.text).replace("label:", ""))
    count = 0
    while count < len(idList):
        pdf.cell(10)
        pdf.cell(0, 10, chr(150) + ' Link' +
                idList[count]+' :'+portList[count], 0, 1)
        count = count+1

    # 2.8
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.- '+indexList[cont], 0, 1)
    cont = cont+1

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "11:56:56":
                                        res = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "UTC":
                                        res1 = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "11":
                                        res2 = y
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el ' +
            res2+' de Novembre del 2020 a les '+res+' '+res1, 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.1.- Configuració criptogràfica del dispositiu', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu no té configuració de crypto', 0, 1, 'L')
    # 2.8.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.8.2.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és', 0, 1, 'L')

    idList3 = list()
    portList3 = list()
    contLinks = 0
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList3.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList3.append(
                                            str(c4_obj.text).replace("label:", ""))
    count = 0
    while count < len(ex1):
        ex1.pop(count)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.3":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.224":
                                            ex1.append(y)
    count = 0
    while count < len(idList3):
        pdf.cell(10)
        if count == 0:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList3[0]+' :'+portList3[0]+':', 0, 1)
        if count == 1:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList3[1]+' :'+portList3[1]+':'+ex1[0]+' ('+ex1[1]+')', 0, 1)
        if count == 2:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList3[2]+' :'+portList3[2]+':', 0, 1)
        if count == 3:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList3[3]+' :'+portList3[3]+':', 0, 1)
        if count == 4:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList3[4]+' :'+portList3[4]+':', 0, 1)
        count = count+1

    # 2.8.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.8.3.- Configuració dels protocols d'enrutament", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "No hi ha assignat cap protocol de enrutament", 0, 1, 'L')

    # 2.8.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.8.4.- Configuració de Llistes de Control d'Accés", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu no té ningúna configuració de ACL", 0, 1)

    # 2.8.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.8.5.- Configuració de Banners", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurats els següents Banners:", 0, 1)
    pdf.cell(10)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "exec":
                                        res = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "incoming":
                                        res1 = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "login":
                                        res2 = y
    pdf.cell(10)
    count = 0
    while count < len(ex1):
        ex1.pop(count)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "*" in c3_obj.text:
                                ex1.append(str(c3_obj.text))
    count = 0
    while count < len(ex1):
        if count >= 0 and count < 8:
            if count == 0:
                pdf.cell(0, 10, chr(150) + ' ' + res, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        elif count >= 8 and count < 15:
            if count == 8:
                pdf.cell(0, 10, chr(150) + ' ' + res1, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        else:
            if count == 16:
                pdf.cell(0, 10, chr(150) + ' ' + res2, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        count = count+1

    # 2.9
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.- '+indexList[cont], 0, 1)
    cont = cont+1

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "11:57:16":
                                        res = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "UTC":
                                        res1 = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "11":
                                        res2 = y
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el ' +
            res2+' de Novembre del 2020 a les '+res+' '+res1, 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.1.- Configuració criptogràfica del dispositiu', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu no té configuració de crypto', 0, 1, 'L')
    # 2.9.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.9.2.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és', 0, 1, 'L')

    idList4 = list()
    portList4 = list()
    contLinks = 0
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList4.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList4.append(
                                            str(c4_obj.text).replace("label:", ""))
    count = 0
    while count < len(ex1):
        ex1.pop(count)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.4":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.224":
                                            ex1.append(y)
    count = 0
    while count < len(idList4):
        pdf.cell(10)
        if count == 0:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList4[0]+' :'+portList4[0]+':', 0, 1)
        if count == 1:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList4[1]+' :'+portList4[1]+':'+ex1[0]+' ('+ex1[1]+')', 0, 1)
        if count == 2:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList4[2]+' :'+portList4[2]+':', 0, 1)
        if count == 3:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList4[3]+' :'+portList4[3]+':', 0, 1)
        if count == 4:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList4[4]+' :'+portList4[4]+':', 0, 1)
        count = count+1

    # 2.9.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.9.3.- Configuració dels protocols d'enrutament", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "No hi ha assignat cap protocol de enrutament", 0, 1, 'L')

    # 2.9.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.9.4.- Configuració de Llistes de Control d'Accés", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu no té ningúna configuració de ACL", 0, 1)

    # 2.9.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.9.5.- Configuració de Banners", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurats els següents Banners:", 0, 1)
    pdf.cell(10)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "exec":
                                        res = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "incoming":
                                        res1 = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "login":
                                        res2 = y
    pdf.cell(10)
    count = 0
    while count < len(ex1):
        ex1.pop(count)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "*" in c3_obj.text:
                                ex1.append(str(c3_obj.text))
    count = 0
    while count < len(ex1):
        if count >= 0 and count < 8:
            if count == 0:
                pdf.cell(0, 10, chr(150) + ' ' + res, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        elif count >= 8 and count < 15:
            if count == 8:
                pdf.cell(0, 10, chr(150) + ' ' + res1, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        else:
            if count == 16:
                pdf.cell(0, 10, chr(150) + ' ' + res2, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        count = count+1

    # 2.10
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.10.- '+indexList[cont], 0, 1)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "12:41:37":
                                        res = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "UTC":
                                        res1 = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "!" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "11":
                                        res2 = y
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el ' +
            res2+' de Novembre del 2020 a les '+res+' '+res1, 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.10.1.- Configuració criptogràfica del dispositiu', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El dispositiu no té configuració de crypto', 0, 1, 'L')
    # 2.10.2
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.10.2.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'Les interfícies i la seva configuració és', 0, 1, 'L')

    idList5 = list()
    portList5 = list()
    contLinks = 0
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                contLinks = contLinks+1
                                idList5.append(
                                    str(c3_obj.text).replace("- id:", ""))
                                for c4_obj in c3_obj.children:
                                    if "label:" in c4_obj.text:
                                        portList5.append(
                                            str(c4_obj.text).replace("label:", ""))
    count = 0
    while count < len(ex1):
        ex1.pop(count)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.34":
                                            ex1.append(y)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "255.255.255.240":
                                            ex1.append(y)
    count = 0
    while count < len(idList5):
        pdf.cell(10)
        if count == 0:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList5[0]+' :'+portList5[0]+':', 0, 1)
        if count == 1:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList5[1]+' :'+portList5[1]+':'+ex1[0]+' ('+ex1[1]+')', 0, 1)
        if count == 2:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList5[2]+' :'+portList5[2]+':', 0, 1)
        if count == 3:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList5[3]+' :'+portList5[3]+':', 0, 1)
        if count == 4:
            pdf.cell(0, 10, chr(150) + ' Link' +
                    idList5[4]+' :'+portList5[4]+':', 0, 1)
        count = count+1

    # 2.10.3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.10.3.- Configuració dels protocols d'enrutament", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "No hi ha assignat cap protocol de enrutament", 0, 1, 'L')

    # 2.10.4
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.10.4.- Configuració de Llistes de Control d'Accés", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu no té ningúna configuració de ACL", 0, 1)

    # 2.10.5
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, "2.10.5.- Configuració de Banners", 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, "El dispositiu té configurats els següents Banners:", 0, 1)
    pdf.cell(10)
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "exec":
                                        res = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "incoming":
                                        res1 = y
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "banner" in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "login":
                                        res2 = y
    pdf.cell(10)
    count = 0
    while count < len(ex1):
        ex1.pop(count)

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "*" in c3_obj.text:
                                ex1.append(str(c3_obj.text))
    count = 0
    while count < len(ex1):
        if count >= 0 and count < 8:
            if count == 0:
                pdf.cell(0, 10, chr(150) + ' ' + res, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        elif count >= 8 and count < 15:
            if count == 8:
                pdf.cell(0, 10, chr(150) + ' ' + res1, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        else:
            if count == 16:
                pdf.cell(0, 10, chr(150) + ' ' + res2, 0, 1)
            pdf.cell(0, 10, ex1[count], 0, 1)
        count = count+1


    # 3
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '3.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'La configuració de les interfícies (links) de interconnexió entre equips és: ', 0, 1, 'L')
    parse = CiscoConfParse('Ex3')
    # LINK10
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n1" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "PCA":
                                name1 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id1 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SWA":
                                name2 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id2 = y

    pdf.cell(0, 10, chr(150) + ' Link 10: connecta '+id1 +
            ' ('+name1+')'+' amb ' + id2+' ('+name2+')', 0, 1)

    # LINK 11
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n0" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "PCB":
                                name3 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id3 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SWB":
                                name4 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id4 = y

    pdf.cell(0, 10, chr(150) + ' Link 11: connecta '+id3 +
            ' ('+name3+')'+' amb ' + id4+' ('+name4+')', 0, 1)

    # LINK 12
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "RA":
                                name5 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id5 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n2" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SWA":
                                name6 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id6 = y

    pdf.cell(0, 10, chr(150) + ' Link 12: connecta '+id5 +
            ' ('+name5+')'+' amb ' + id6+' ('+name6+')', 0, 1)

    # LINK 13
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "RA":
                                name7 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        id7 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SWB":
                                name8 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id8 = y

    pdf.cell(0, 10, chr(150) + ' Link 13: connecta '+id7 +
            ' ('+name7+')'+' amb ' + id8+' ('+name8+')', 0, 1)

    # LINK 14
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "RA":
                                name9 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i3":
                                        id9 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SWC":
                                name10 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id10 = y

    pdf.cell(0, 10, chr(150) + ' Link 14: connecta '+id9 +
            ' ('+name9+')'+' amb ' + id10+' ('+name10+')', 0, 1)

    # LINK 15
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SWC":
                                name11 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id11 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "PCC":
                                name12 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i0":
                                        id12 = y

    pdf.cell(0, 10, chr(150) + ' Link 15: connecta '+id11 +
            ' ('+name11+')'+' amb ' + id12+' ('+name12+')', 0, 1)

    # LINK 16
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SWC":
                                name13 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        id13 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n7" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "HTTPC":
                                name14 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id14 = y

    pdf.cell(0, 10, chr(150) + ' Link 16: connecta '+id13 +
            ' ('+name13+')'+' amb ' + id14+' ('+name14+')', 0, 1)

    # LINK 17
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n5" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SWC":
                                name15 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i3":
                                        id15 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n8" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SSHC":
                                name16 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id16 = y

    pdf.cell(0, 10, chr(150) + ' Link 17: connecta '+id15 +
            ' ('+name15+')'+' amb ' + id16+' ('+name16+')', 0, 1)
    # LINK 18
    pdf.cell(10)
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n9" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SSHB":
                                name17 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        id17 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n3" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "SWB":
                                name18 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        id18 = y

    pdf.cell(0, 10, chr(150) + ' Link 18: connecta '+id17 +
            ' ('+name17+')'+' amb ' + id18+' ('+name18+')', 0, 1)

    pdf.set_font('Times', '', 12)
    pdf.cell(0, 10, 'El resum de les adreces IP de les interfícies és: ', 0, 1, 'L')

    # Taula
    pdf.set_font('Times', '', 12)
    pdf.set_fill_color(0, 0, 255)
    pdf.cell(30, 10, "Xarxa", 1, 0)
    pdf.cell(30, 10, "Equip1", 1, 0)
    pdf.cell(20, 10, "Interfície1", 1, 0)
    pdf.cell(30, 10, "IP1", 1, 0)
    pdf.cell(30, 10, "Equip2", 1, 0)
    pdf.cell(20, 10, "Interfície2", 1, 0)
    pdf.cell(30, 10, "IP2", 1, 1)

    # FILA 1
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.32":
                                            x1 = y

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "RA":
                                e1 = y
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.33":
                                            ip1 = y

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i2":
                                        i1 = y

    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n0" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "10.101.117.35/28":
                                    aux1 = y.split("/")
                                    for kk in aux1:
                                        if(kk == "10.101.117.35"):
                                            ip2 = kk

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n0" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "PCB":
                                e2 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "i0":
                                    i2 = y

    pdf.cell(30, 10, x1, 1, 0)
    pdf.cell(30, 10, e1, 1, 0)
    pdf.cell(20, 10, i1, 1, 0)
    pdf.cell(30, 10, ip1, 1, 0)
    pdf.cell(30, 10, e2, 1, 0)
    pdf.cell(20, 10, i2, 1, 0)
    pdf.cell(30, 10, ip2, 1, 1)

    # FILA 2
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.32":
                                            x2 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "RA":
                                e3 = y
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.49":
                                            ip3 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i1":
                                        i3 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n1" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "10.101.117.51/29":
                                    aux1 = y.split("/")
                                    for kk in aux1:
                                        if(kk == "10.101.117.51"):
                                            ip4 = kk

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n1" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "PCA":
                                e4 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "i0":
                                    i4 = y

    pdf.cell(30, 10, x2, 1, 0)
    pdf.cell(30, 10, e3, 1, 0)
    pdf.cell(20, 10, i3, 1, 0)
    pdf.cell(30, 10, ip3, 1, 0)
    pdf.cell(30, 10, e4, 1, 0)
    pdf.cell(20, 10, i4, 1, 0)
    pdf.cell(30, 10, ip4, 1, 1)

    # FILA 3
    parse = CiscoConfParse('Ex3')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "ip" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.0":
                                            x3 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "RA":
                                e5 = y
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "interface" in c3_obj.text:
                                for c4_obj in c3_obj.children:
                                    aux = c4_obj.text.split(" ")
                                    for y in aux:
                                        if y == "10.101.117.1":
                                            ip5 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n4" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            if "- id: " in c3_obj.text:
                                aux = c3_obj.text.split(" ")
                                for y in aux:
                                    if y == "i3":
                                        i5 = y

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "- id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "configuration:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "10.101.117.2/27":
                                    aux1 = y.split("/")
                                    for kk in aux1:
                                        if(kk == "10.101.117.2"):
                                            ip6 = kk

    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            if "id: n6" in c1_obj.text:
                for c2_obj in c1_obj.children:
                    if "label:" in c2_obj.text:
                        aux = c2_obj.text.split(" ")
                        for y in aux:
                            if y == "PCC":
                                e6 = y
                    if "interfaces:" in c2_obj.text:
                        for c3_obj in c2_obj.children:
                            aux = c3_obj.text.split(" ")
                            for y in aux:
                                if y == "i0":
                                    i6 = y

    pdf.cell(30, 10, x3, 1, 0)
    pdf.cell(30, 10, e5, 1, 0)
    pdf.cell(20, 10, i5, 1, 0)
    pdf.cell(30, 10, ip5, 1, 0)
    pdf.cell(30, 10, e6, 1, 0)
    pdf.cell(20, 10, i6, 1, 0)
    pdf.cell(30, 10, ip6, 1, 1)
    pdf.output("Ex3.pdf")