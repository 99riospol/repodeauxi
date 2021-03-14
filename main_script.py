import os
import yaml
import inspect
import requests
import re

from datetime import datetime
from ciscoconfparse import CiscoConfParse
from fpdf import FPDF

eleccio=input("Escribe el nombre del fichero a tratar: ")
with open(eleccio) as f:
        dd=yaml.load(f, Loader=yaml.FullLoader)

class PDF(FPDF):
    def header(self):
        if self.page_no() != 1:  # Cabecera a tot menys a la primera pàgina
            # Set up a logo
            self.image('logo.png', 150, 10, 33)
            self.set_font('Times', '', 12)
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

            #Taking actual month
            aux=datetime.now()
            format=aux.strftime('%m')
            if format=='01': kk="Gener"
            if format=='02': kk="Febrer"
            if format=='03': kk="Març"
            if format=='04': kk="Abril"
            if format=='05': kk="Maig"
            if format=='06': kk="Juni"
            if format=='07': kk="Juliol"
            if format=='08': kk="Agost"
            if format=='09': kk="Septembre"
            if format=='10': kk="Octubre"
            if format=='11': kk="Novembre"
            if format=='12': kk="Decembre" 
            self.cell(0, 2, '          '+kk+' 2021', 0, 0)
    # Page footer

    def footer(self):  # peu de pagina menys a la primera
        if self.page_no() != 1:
            self.set_y(-15)
            self.set_font('Times', 'B', 8)
            # Page number
            if eleccio=="Ex1":  
                self.cell(0, 10, 'Page '+str(self.page_no())+'/16', 0, 0, 'R')
            elif eleccio=="Ex2":
                self.cell(0, 10, 'Page '+str(self.page_no())+'/13', 0, 0, 'R')
            else:
                self.cell(0, 10, 'Page '+str(self.page_no())+'/15', 0, 0, 'R')
                
pdf = PDF()
pdf.add_page()
pdf.set_font('Times', 'B', 14)
pdf.add_page()
if eleccio=="Ex1":
    # INDEX
    pdf.cell(0, 10, 'ÍNDEX', 0, 1)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.- Introducció............................................................................................................................................4', 0, 1)
    pdf.cell(10)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.1.- Descripció........................................................................................................................4', 0, 1)
    pdf.cell(10)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.2.- Objectius..........................................................................................................................4', 0, 1)
    pdf.cell(10)
    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '1.3.- Descripció General de les infraestructures...................................................................4', 0, 1)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(0, 10, '2.- Configuració dels dispositius................................................................................................................5', 0, 1)
    pdf.cell(20)
    pdf.set_font('Times','B',12)
    ii=1
    pag=4
    for k in dd['nodes']:
        if(ii==9):
            pdf.add_page()
        else:
            pdf.ln(4)
        pdf.cell(10)
        if(ii==2):
            pag=5
        if(ii==3):
            pag=7
        if(ii==4):
            pag=8
        if(ii==5):
            pag=10
        if(ii==7):
            pag=pag+1
        pdf.cell(0, 10, '2.'+ str(ii) +'.- '+ k['label'] +'............................................................................................................... '+ str(pag),0,1,'L',False)
        cc=1
        if "Building configuration..." in k['configuration']:
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0,0,'2.'+ str(ii) +'.'+ str(cc) +'.- Configuració criptogràfica del dispositiu............................................................................ '+ str(pag),0,1,'L',False)
            cc=cc+1
        if(pag==8):
            pag=pag+1
        pdf.ln(4)
        pdf.cell(20)
        pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Interfícies........................................................................................................................... '+ str(pag),0,1,'L',False)
        cc=cc+1
        if "Building configuration..." in k['configuration']:
            if(pag==5):
                pag=pag+1
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Configuració dels protocols d`enrutament......................................................................... '+ str(pag),0,1,'L',False)
            cc=cc+1
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Configuració de Llistes de Control d`Accés....................................................................... '+ str(pag),0,1,'L',False)
            cc=cc+1
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Configuració de Banners .................................................................................................. '+ str(pag),0,1,'L',False)
            cc=cc+1
        ii=ii+1
    
    pdf.ln(4)
    pdf.cell(0, 10, '3.- Interfícies....................................................................................................................................... '+ str(pag),0,1,'L',False)
    cont = 0
    indexList = list()
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            for c2_obj in c1_obj.children:
                if "label:" in c2_obj.text:
                    indexList.append(str(c2_obj.text).replace("label:", ""))
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
    pdf.ln(10)
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
    
    ips= list()
    intf= list()
    term=list()
    xxs= list()
    idx=1
    for klk in dd['nodes']:
        pdf.set_font('Times', 'B', 12)
        pdf.ln(8)
        pdf.cell(0, 0, '2.'+str(idx)+'.- '+ klk['label'], 0, 1)
        pdf.ln(6)
        ms=1
        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', '', 10)
            #Date and Time
            xx='UTC'
            match=re.search(xx, klk['configuration'])
            s=match.start()
            e=match.end()
            time=klk['configuration'][(s-9):(e)]
            date=klk['configuration'][(e+5):(e+16)]

            pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el '+ date +' a les '+ time, 0, 1)
            pdf.set_font('Times', 'B', 12)
            pdf.ln(9)
            pdf.cell(0, 10, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració criptogràfica del dispositiu', 0, 1)
            pdf.set_font('Times', '', 12)
            pdf.ln(7)
            if "crypto" in klk['configuration']:
                pdf.cell(0, 10, 'El dispositiu té la següent configuració de crypto:', 0, 1)
                pdf.ln(4)
                pdf.cell(20)
                xx='set peer'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                ip=klk['configuration'][(e+1):(e+9)]
                pdf.cell(0, 10, '-    Conexió amb '+ ip +':', 0, 1)
                pdf.ln(6)
                pdf.cell(30)
                #Cojer numero
                xx='isakmp policy'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                numero=klk['configuration'][(e+1):(e+3)]
                pdf.cell(0, 10, 'o   Política de regles número '+ numero +':', 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer encript
                xx='encr aes'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                ee=klk['configuration'][(e-3):(e+4)]
                pdf.cell(0, 0, '·    Encriptació '+ ee, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer authentification
                xx='authentication'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                auth=klk['configuration'][(e+1):(e+10)]
                pdf.cell(0, 10, '·    Autenticació '+ auth, 0, 1)
                pdf.ln(2)
                pdf.cell(40)
                #Cojer group
                xx='group'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                group=klk['configuration'][(e+1)]
                pdf.cell(0, 10, '·    Diffie-Helmann grup '+ group, 0, 1)
                pdf.ln(6)
                pdf.cell(30)
                #Cojer key
                xx='isakmp key'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                key=klk['configuration'][(e+1):(e+8)]
                pdf.cell(0, 10, 'o   Contrasenya ISAKMP: '+ key, 0, 1)
                pdf.ln(6)
                pdf.cell(30)
                pdf.cell(0, 10, 'o   Configuració VPN:', 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer tranform
                xx='ipsec transform-set'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                tt=klk['configuration'][(e+1):(e+4)]
                pdf.cell(0, 10, '·    Conjunt de transformació '+ tt, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer encriptaci
                enc=klk['configuration'][(e+5):(e+12)]
                pdf.cell(0, 10, '·    Configuració Encriptació ESP: '+ enc, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer signatur
                sgn=klk['configuration'][(e+13):(e+25)]
                pdf.cell(0, 10, '·    Configuració Signatura ESP: '+ sgn, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer mode
                mod=klk['configuration'][(e+32):(e+38)]
                pdf.cell(0, 10, '·    Mode '+ mod, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer acl
                pattern='match address'
                match=re.search(pattern, klk['configuration'])
                e=match.end()
                acl=klk['configuration'][(e+1):(e+4)]
                pdf.cell(0, 10, '·    ACL número '+ acl, 0, 1)
            else:
                pdf.cell(0, 10, 'El dispositiu no té configuració de crypto', 0, 1)
            
            ms=ms+1

        pdf.set_font('Times', 'B', 12)
        if "Building configuration..." in klk['configuration']:
            pdf.ln(4)
        pdf.cell(0, 10, '2.'+ str(idx) +'.'+ str(ms) +'.- Interfícies', 0, 1)
        pdf.set_font('Times', '', 11)
        pdf.cell(0, 10, 'Les interfícies i la seva configuració és:', 0, 1)
        pdf.ln(4)

        for q in klk['interfaces']:
            pdf.cell(25)
            xx=q['label']
            ff=re.search(xx, klk['configuration'])
            ipAddr=''
            if ff!=None:
                e=ff.end()
                if "no" not in klk['configuration'][(e):(e+5)]:
                    ipAddr=klk['configuration'][(e+13):(e+38)]
                    xx='255.255'
                    ff=re.search(xx, ipAddr)
                    if ff != None:
                        s=ff.start()
                        term.append(klk['label'])
                        intf.append(q['id'])
                        ips.append(ipAddr[:s])

                        ipAddr=': '+ipAddr[:s]+'('+ipAddr[s:len(ipAddr)]+')'
                if 'alpine' in klk['node_definition']:
                    term.append(klk['label'])
                    intf.append(q['id'])

                    ipAddr=' (DG: '+ipAddr[13:]+')'
                    xx='ip addr add'
                    ff=re.search(xx, klk['configuration'])
                    e=ff.end()
                    ips.append(klk['configuration'][(e+1):(e+12)])

                    ipAddr='. Configuració IP: '+klk['configuration'][(e+1):(e+15)]+ ipAddr
            
            pdf.cell(0, 10, '-    Link '+ q['id']+': '+ q['label']+ ipAddr, 0, 1)
            pdf.ln(5)
        ms=ms+1

        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', 'B', 12)
            pdf.ln(5)
            pdf.cell(0, 10, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració dels protocols d enrutament', 0, 1)
            pdf.set_font('Times', '', 11)
            #Cojer protocol
            xx='router ospf'
            match=re.search(xx, klk['configuration'])
            if(match!=None):
                e=match.end()
            protocol=klk['configuration'][(e-4):(e+4)]
            pdf.cell(0, 0, 'El protocol d enrutament utilitzat és '+ protocol.upper() +', amb la següent configuració (xarxes publicades):', 0, 1)
            pdf.ln(4)
            pdf.cell(10)
            #Cojer area
            xx='area'
            match=re.search(xx, klk['configuration'])
            if(match!=None):
                e=match.end()
            area=klk['configuration'][e+1]
            pdf.cell(0, 10, '-    Àrea '+ area+':', 0, 1)
            #Cojer network
            xx='network'
            match=re.search(xx, klk['configuration'])
            if(match!=None):
                s=match.end()
            s=s+1
            network=""
            while klk['configuration'][s]!='!':
                network=network+klk['configuration'][s]
                s=s+1
            num=klk['configuration'].count("area")
            network=network.replace("network", "")
            network=network.replace("area 0", "")
            while num>0:
                xx=' '
                match=re.search(xx, network)
                if(match!= None):
                    x=match.end()
                    if network[:x-1] not in xxs:
                        xxs.append(network[:x-1])
                    parte1=network[:x-1]+' màscara invertida '
                    network=network[x:]
                    network=network[2:]
                    match=re.search(pattern, network)
                    parte2=network[:x-1]
                    network=network[x:]
                    net=parte1+parte2
                pdf.ln(7)
                pdf.cell(20)
                pdf.cell(0, 0, 'o   Xarxa '+ net, 0, 1)
                num=num-1 
            ms=ms+1

        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', 'B', 12)
            pdf.ln(9)
            pdf.cell(0, 0, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració de Llistes de Control d Accés', 0, 1)
            pdf.set_font('Times', '', 11)
            pdf.ln(7)
            if "access-list" in klk['configuration']:
                pdf.cell(0, 0, 'El dispositiu té configurada la següent ACL:', 0, 1)
                pdf.ln(7)
                pdf.cell(10)
                #Cojer acclist
                xx='access-list'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                acclist=klk['configuration'][(e+1):(e+4)]
                pdf.cell(0, 0, '-    Número '+acclist, 0, 1)
                pdf.ln(5)
                pdf.cell(20)
                #Cojer permit
                xx='permit'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                permit=klk['configuration'][(e+1):(e+3)]
                pdf.cell(0, 10, 'o   PERMIT ('+ permit.upper() +'):', 0, 1)
                pdf.ln(1)
                pdf.cell(30)
                #Cojer origen y desti
                xx='control-plane'
                match=re.search(xx, klk['configuration'])
                s=match.start()
                origdest=klk['configuration'][(e+4):(s-2)]
                xx=' '
                match=re.search(xx, origdest)
                if(match!= None):
                    x=match.end()
                    origen=origdest[:x-1]+' màscara invertida '+origdest[x:x+9]
                    origdest=origdest[x:]
                    match=re.search(pattern, klk['configuration'])
                    x=match.start()
                    origdest=origdest[x+2:]
                    match=re.search(pattern, klk['configuration'])
                    x=match.start()
                    desti=origdest[:x+3]+' màscara invertida '+origdest[x+3:x+13]
                pdf.cell(0, 10, '·   ORIGEN: '+origen, 0, 1)
                pdf.ln(2)
                pdf.cell(30)
                pdf.cell(0, 10, '·   DESTÍ: '+desti, 0, 1)
            else:
                pdf.cell(0, 10, 'El dispositiu no té configurada cap ACL.', 0, 1)

            ms=ms+1

        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', 'B', 12)
            pdf.ln(9)
            pdf.cell(0, 0, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració de Banners', 0, 1)
            pdf.set_font('Times', '', 11)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(7)
            pdf.cell(0, 0, 'El dispositiu té configurats els següent Banners:', 0, 1)
            pdf.ln(7)

            #Cojer banner
            xx='banner'
            match=re.search(xx, klk['configuration'])
            e=match.end()
            xx='line con 0'
            match=re.search(xx, klk['configuration'])
            s=match.start()
            banner=klk['configuration'][(e+1):(s-2)]
            banner="    -    "+banner
            banner=banner.replace("banner", "    -    ")
            banner=banner.replace("^CCC", " ")
            banner=banner.replace("^C", " ")
            pdf.cell(18)
            pdf.multi_cell(170, 8, banner, 0, 'J', False)
            ms=ms+1
        idx=idx+1 
    #3.- 
    pdf.set_font('Times', '', 20)
    pdf.ln(5)
    pdf.cell(18)
    pdf.cell(10, 10, '3.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 10)
    pdf.ln(3)
    pdf.cell(18)
    pdf.cell(0, 10, 'La configuració de les interfícies (links) d interconnexió entre equips és:', 0, 1)
    pdf.ln(8)
    for q in dd['links']:
        pdf.cell(25)
        pdf.set_font('Times', 'B', 11)

        #Cojer id
        ids='1'+q['id'][1]

        pdf.cell(0, 0, '-    Link '+ids, 0, 1)
        pdf.set_font('Times', '', 11)
        pdf.cell(44)

        #Cojer nombres label con su id
        lab1=''
        lab2=''
        for n in dd['nodes']:
            if q['n1'] == n['id']:
                lab1=n['label']
            if q['n2'] == n['id']:
                lab2=n['label']

        pdf.cell(0, 0, ': conecta '+ q['i1'] +' ('+ lab1 +')'+' amb '+ q['i2']+' ('+ lab2 +')', 0, 1)
        pdf.ln(5)

    pdf.ln(3)
    pdf.cell(18)
    pdf.cell(0, 0, 'El resum de les adreces IP de les interfícies és:', 0, 1)
    #TABLA
    pdf.ln(5)
    pdf.cell(13)
    if len(xxs)!=0:
        pdf.cell(23, 10, "Xarxa", 0, 0)
    pdf.cell(23, 10, "Equip1", 0, 0)
    pdf.cell(23, 10, "Interfície1", 0, 0)
    pdf.cell(23, 10, "IP1", 0, 0)
    pdf.cell(23, 10, "Equip2", 0, 0)
    pdf.cell(23, 10, "Interfície2", 0, 0)
    pdf.cell(23, 10, "IP2", 0, 0)
    pdf.ln(6)
    l=0
    while l< len(term):
        pdf.cell(13)
        if len(xxs)!=0:
            if l==0:
                pdf.cell(23, 10, xxs[l], 0, 0)
            else:
                pdf.cell(23, 10, xxs[int(l/2)], 0, 0)
        pdf.cell(23, 10, term[l], 0, 0)
        pdf.cell(23, 10, intf[l], 0, 0)
        pdf.cell(23, 10, ips[l], 0, 0)
        if(l+1!=len(term)):
            pdf.cell(23, 10, term[l+1], 0, 0)
            pdf.cell(23, 10, intf[l+1], 0, 0)
            pdf.cell(23, 10, ips[l+1], 0, 0)
            pdf.ln(5)
        else:
            pdf.ln(5)
        
        l=l+2
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

    pdf.cell(20)
    pdf.set_font('Times','B',12)
    ii=1
    pag=4
    for k in dd['nodes']:
        if(ii==9):
            pdf.add_page()
        else:
            pdf.ln(4)
        pdf.cell(10)
        if(ii==2):
            pag=5
        if(ii==3):
            pag=7
        if(ii==4):
            pag=8
        if(ii==5):
            pag=10
        if(ii==7):
            pag=pag+1
        pdf.cell(0, 10, '2.'+ str(ii) +'.- '+ k['label'] +'............................................................................................................... '+ str(pag),0,1,'L',False)
        cc=1
        if "Building configuration..." in k['configuration']:
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0,0,'2.'+ str(ii) +'.'+ str(cc) +'.- Configuració criptogràfica del dispositiu............................................................................ '+ str(pag),0,1,'L',False)
            cc=cc+1
        if(pag==8):
            pag=pag+1
        pdf.ln(4)
        pdf.cell(20)
        pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Interfícies........................................................................................................................... '+ str(pag),0,1,'L',False)
        cc=cc+1
        if "Building configuration..." in k['configuration']:
            if(pag==5):
                pag=pag+1
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Configuració dels protocols d`enrutament......................................................................... '+ str(pag),0,1,'L',False)
            cc=cc+1
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Configuració de Llistes de Control d`Accés....................................................................... '+ str(pag),0,1,'L',False)
            cc=cc+1
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Configuració de Banners .................................................................................................. '+ str(pag),0,1,'L',False)
            cc=cc+1
        ii=ii+1
    
    pdf.ln(4)
    pdf.cell(0, 10, '3.- Interfícies....................................................................................................................................... '+ str(pag),0,1,'L',False)
    cont = 0
    indexList = list()
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            for c2_obj in c1_obj.children:
                if "label:" in c2_obj.text:
                    indexList.append(str(c2_obj.text).replace("label:", ""))
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
    pdf.ln(10)
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
    
    ips= list()
    intf= list()
    term=list()
    xxs= list()
    idx=1
    for klk in dd['nodes']:
        pdf.set_font('Times', 'B', 12)
        pdf.ln(8)
        pdf.cell(0, 0, '2.'+str(idx)+'.- '+ klk['label'], 0, 1)
        pdf.ln(6)
        ms=1
        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', '', 10)
            #Date and Time
            xx='UTC'
            match=re.search(xx, klk['configuration'])
            s=match.start()
            e=match.end()
            time=klk['configuration'][(s-9):(e)]
            date=klk['configuration'][(e+5):(e+16)]

            pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el '+ date +' a les '+ time, 0, 1)
            pdf.set_font('Times', 'B', 12)
            pdf.ln(9)
            pdf.cell(0, 10, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració criptogràfica del dispositiu', 0, 1)
            pdf.set_font('Times', '', 12)
            pdf.ln(7)
            if "crypto" in klk['configuration']:
                pdf.cell(0, 10, 'El dispositiu té la següent configuració de crypto:', 0, 1)
                pdf.ln(4)
                pdf.cell(20)
                xx='set peer'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                ip=klk['configuration'][(e+1):(e+9)]
                pdf.cell(0, 10, '-    Conexió amb '+ ip +':', 0, 1)
                pdf.ln(6)
                pdf.cell(30)
                #Cojer numero
                xx='isakmp policy'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                numero=klk['configuration'][(e+1):(e+3)]
                pdf.cell(0, 10, 'o   Política de regles número '+ numero +':', 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer encript
                xx='encr aes'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                ee=klk['configuration'][(e-3):(e+4)]
                pdf.cell(0, 0, '·    Encriptació '+ ee, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer authentification
                xx='authentication'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                auth=klk['configuration'][(e+1):(e+10)]
                pdf.cell(0, 10, '·    Autenticació '+ auth, 0, 1)
                pdf.ln(2)
                pdf.cell(40)
                #Cojer group
                xx='group'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                group=klk['configuration'][(e+1)]
                pdf.cell(0, 10, '·    Diffie-Helmann grup '+ group, 0, 1)
                pdf.ln(6)
                pdf.cell(30)
                #Cojer key
                xx='isakmp key'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                key=klk['configuration'][(e+1):(e+8)]
                pdf.cell(0, 10, 'o   Contrasenya ISAKMP: '+ key, 0, 1)
                pdf.ln(6)
                pdf.cell(30)
                pdf.cell(0, 10, 'o   Configuració VPN:', 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer tranform
                xx='ipsec transform-set'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                tt=klk['configuration'][(e+1):(e+4)]
                pdf.cell(0, 10, '·    Conjunt de transformació '+ tt, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer encriptaci
                enc=klk['configuration'][(e+5):(e+12)]
                pdf.cell(0, 10, '·    Configuració Encriptació ESP: '+ enc, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer signatur
                sgn=klk['configuration'][(e+13):(e+25)]
                pdf.cell(0, 10, '·    Configuració Signatura ESP: '+ sgn, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer mode
                mod=klk['configuration'][(e+32):(e+38)]
                pdf.cell(0, 10, '·    Mode '+ mod, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer acl
                pattern='match address'
                match=re.search(pattern, klk['configuration'])
                e=match.end()
                acl=klk['configuration'][(e+1):(e+4)]
                pdf.cell(0, 10, '·    ACL número '+ acl, 0, 1)
            else:
                pdf.cell(0, 10, 'El dispositiu no té configuració de crypto', 0, 1)
            
            ms=ms+1

        pdf.set_font('Times', 'B', 12)
        if "Building configuration..." in klk['configuration']:
            pdf.ln(4)
        pdf.cell(0, 10, '2.'+ str(idx) +'.'+ str(ms) +'.- Interfícies', 0, 1)
        pdf.set_font('Times', '', 11)
        pdf.cell(0, 10, 'Les interfícies i la seva configuració és:', 0, 1)
        pdf.ln(4)

        for q in klk['interfaces']:
            pdf.cell(25)
            xx=q['label']
            ff=re.search(xx, klk['configuration'])
            ipAddr=''
            if ff!=None:
                e=ff.end()
                if "no" not in klk['configuration'][(e):(e+5)]:
                    ipAddr=klk['configuration'][(e+13):(e+38)]
                    xx='255.255'
                    ff=re.search(xx, ipAddr)
                    if ff != None:
                        s=ff.start()
                        term.append(klk['label'])
                        intf.append(q['id'])
                        ips.append(ipAddr[:s])

                        ipAddr=': '+ipAddr[:s]+'('+ipAddr[s:len(ipAddr)]+')'
                if 'alpine' in klk['node_definition']:
                    term.append(klk['label'])
                    intf.append(q['id'])

                    ipAddr=' (DG: '+ipAddr[13:]+')'
                    xx='ip addr add'
                    ff=re.search(xx, klk['configuration'])
                    e=ff.end()
                    ips.append(klk['configuration'][(e+1):(e+12)])

                    ipAddr='. Configuració IP: '+klk['configuration'][(e+1):(e+15)]+ ipAddr
            
            pdf.cell(0, 10, '-    Link '+ q['id']+': '+ q['label']+ ipAddr, 0, 1)
            pdf.ln(5)
        ms=ms+1

        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', 'B', 12)
            pdf.ln(5)
            pdf.cell(0, 10, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració dels protocols d enrutament', 0, 1)
            pdf.set_font('Times', '', 11)
            #Cojer protocol
            xx='router ospf'
            match=re.search(xx, klk['configuration'])
            if(match!=None):
                e=match.end()
            protocol=klk['configuration'][(e-4):(e+4)]
            pdf.cell(0, 0, 'El protocol d enrutament utilitzat és '+ protocol.upper() +', amb la següent configuració (xarxes publicades):', 0, 1)
            pdf.ln(4)
            pdf.cell(10)
            #Cojer area
            xx='area'
            match=re.search(xx, klk['configuration'])
            if(match!=None):
                e=match.end()
            area=klk['configuration'][e+1]
            pdf.cell(0, 10, '-    Àrea '+ area+':', 0, 1)
            #Cojer network
            xx='network'
            match=re.search(xx, klk['configuration'])
            if(match!=None):
                s=match.end()
            s=s+1
            network=""
            while klk['configuration'][s]!='!':
                network=network+klk['configuration'][s]
                s=s+1
            num=klk['configuration'].count("area")
            network=network.replace("network", "")
            network=network.replace("area 0", "")
            while num>0:
                xx=' '
                match=re.search(xx, network)
                if(match!= None):
                    x=match.end()
                    if network[:x-1] not in xxs:
                        xxs.append(network[:x-1])
                    parte1=network[:x-1]+' màscara invertida '
                    network=network[x:]
                    network=network[2:]
                    match=re.search(pattern, network)
                    parte2=network[:x-1]
                    network=network[x:]
                    net=parte1+parte2
                pdf.ln(7)
                pdf.cell(20)
                pdf.cell(0, 0, 'o   Xarxa '+ net, 0, 1)
                num=num-1 
            ms=ms+1

        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', 'B', 12)
            pdf.ln(9)
            pdf.cell(0, 0, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració de Llistes de Control d Accés', 0, 1)
            pdf.set_font('Times', '', 11)
            pdf.ln(7)
            if "access-list" in klk['configuration']:
                pdf.cell(0, 0, 'El dispositiu té configurada la següent ACL:', 0, 1)
                pdf.ln(7)
                pdf.cell(10)
                #Cojer acclist
                xx='access-list'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                acclist=klk['configuration'][(e+1):(e+4)]
                pdf.cell(0, 0, '-    Número '+acclist, 0, 1)
                pdf.ln(5)
                pdf.cell(20)
                #Cojer permit
                xx='permit'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                permit=klk['configuration'][(e+1):(e+3)]
                pdf.cell(0, 10, 'o   PERMIT ('+ permit.upper() +'):', 0, 1)
                pdf.ln(1)
                pdf.cell(30)
                #Cojer origen y desti
                xx='control-plane'
                match=re.search(xx, klk['configuration'])
                s=match.start()
                origdest=klk['configuration'][(e+4):(s-2)]
                xx=' '
                match=re.search(xx, origdest)
                if(match!= None):
                    x=match.end()
                    origen=origdest[:x-1]+' màscara invertida '+origdest[x:x+9]
                    origdest=origdest[x:]
                    match=re.search(pattern, klk['configuration'])
                    x=match.start()
                    origdest=origdest[x+2:]
                    match=re.search(pattern, klk['configuration'])
                    x=match.start()
                    desti=origdest[:x+3]+' màscara invertida '+origdest[x+3:x+13]
                pdf.cell(0, 10, '·   ORIGEN: '+origen, 0, 1)
                pdf.ln(2)
                pdf.cell(30)
                pdf.cell(0, 10, '·   DESTÍ: '+desti, 0, 1)
            else:
                pdf.cell(0, 10, 'El dispositiu no té configurada cap ACL.', 0, 1)

            ms=ms+1

        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', 'B', 12)
            pdf.ln(9)
            pdf.cell(0, 0, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració de Banners', 0, 1)
            pdf.set_font('Times', '', 11)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(7)
            pdf.cell(0, 0, 'El dispositiu té configurats els següent Banners:', 0, 1)
            pdf.ln(7)

            #Cojer banner
            xx='banner'
            match=re.search(xx, klk['configuration'])
            e=match.end()
            xx='line con 0'
            match=re.search(xx, klk['configuration'])
            s=match.start()
            banner=klk['configuration'][(e+1):(s-2)]
            banner="    -    "+banner
            banner=banner.replace("banner", "    -    ")
            banner=banner.replace("^CCC", " ")
            banner=banner.replace("^C", " ")
            pdf.cell(18)
            pdf.multi_cell(170, 8, banner, 0, 'J', False)
            ms=ms+1
        idx=idx+1 
    #3.- 
    pdf.set_font('Times', '', 20)
    pdf.ln(5)
    pdf.cell(18)
    pdf.cell(10, 10, '3.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 10)
    pdf.ln(3)
    pdf.cell(18)
    pdf.cell(0, 10, 'La configuració de les interfícies (links) d interconnexió entre equips és:', 0, 1)
    pdf.ln(8)
    for q in dd['links']:
        pdf.cell(25)
        pdf.set_font('Times', 'B', 11)

        #Cojer id
        ids='1'+q['id'][1]

        pdf.cell(0, 0, '-    Link '+ids, 0, 1)
        pdf.set_font('Times', '', 11)
        pdf.cell(44)

        #Cojer nombres label con su id
        lab1=''
        lab2=''
        for n in dd['nodes']:
            if q['n1'] == n['id']:
                lab1=n['label']
            if q['n2'] == n['id']:
                lab2=n['label']

        pdf.cell(0, 0, ': conecta '+ q['i1'] +' ('+ lab1 +')'+' amb '+ q['i2']+' ('+ lab2 +')', 0, 1)
        pdf.ln(5)

    pdf.ln(3)
    pdf.cell(18)
    pdf.cell(0, 0, 'El resum de les adreces IP de les interfícies és:', 0, 1)
    #TABLA
    pdf.ln(5)
    pdf.cell(13)
    if len(xxs)!=0:
        pdf.cell(23, 10, "Xarxa", 0, 0)
    pdf.cell(23, 10, "Equip1", 0, 0)
    pdf.cell(23, 10, "Interfície1", 0, 0)
    pdf.cell(23, 10, "IP1", 0, 0)
    pdf.cell(23, 10, "Equip2", 0, 0)
    pdf.cell(23, 10, "Interfície2", 0, 0)
    pdf.cell(23, 10, "IP2", 0, 0)
    pdf.ln(6)
    l=0
    while l< len(term):
        pdf.cell(13)
        if len(xxs)!=0:
            if l==0:
                pdf.cell(23, 10, xxs[l], 0, 0)
            else:
                pdf.cell(23, 10, xxs[int(l/2)], 0, 0)
        pdf.cell(23, 10, term[l], 0, 0)
        pdf.cell(23, 10, intf[l], 0, 0)
        pdf.cell(23, 10, ips[l], 0, 0)
        if(l+1!=len(term)):
            pdf.cell(23, 10, term[l+1], 0, 0)
            pdf.cell(23, 10, intf[l+1], 0, 0)
            pdf.cell(23, 10, ips[l+1], 0, 0)
            pdf.ln(5)
        else:
            pdf.ln(5)
        
        l=l+2
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
    pdf.cell(20)
    pdf.set_font('Times','B',12)
    ii=1
    pag=4
    for k in dd['nodes']:
        if(ii==9):
            pdf.add_page()
        else:
            pdf.ln(4)
        pdf.cell(10)
        if(ii==2):
            pag=5
        if(ii==3):
            pag=7
        if(ii==4):
            pag=8
        if(ii==5):
            pag=10
        if(ii==7):
            pag=pag+1
        pdf.cell(0, 10, '2.'+ str(ii) +'.- '+ k['label'] +'............................................................................................................... '+ str(pag),0,1,'L',False)
        cc=1
        if "Building configuration..." in k['configuration']:
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0,0,'2.'+ str(ii) +'.'+ str(cc) +'.- Configuració criptogràfica del dispositiu............................................................................ '+ str(pag),0,1,'L',False)
            cc=cc+1
        if(pag==8):
            pag=pag+1
        pdf.ln(4)
        pdf.cell(20)
        pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Interfícies........................................................................................................................... '+ str(pag),0,1,'L',False)
        cc=cc+1
        if "Building configuration..." in k['configuration']:
            if(pag==5):
                pag=pag+1
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Configuració dels protocols d`enrutament......................................................................... '+ str(pag),0,1,'L',False)
            cc=cc+1
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Configuració de Llistes de Control d`Accés....................................................................... '+ str(pag),0,1,'L',False)
            cc=cc+1
            pdf.ln(4)
            pdf.cell(20)
            pdf.cell(0, 10, '2.'+ str(ii) +'.'+ str(cc) +'.- Configuració de Banners .................................................................................................. '+ str(pag),0,1,'L',False)
            cc=cc+1
        ii=ii+1
    
    pdf.ln(4)
    pdf.cell(0, 10, '3.- Interfícies....................................................................................................................................... '+ str(pag),0,1,'L',False)
    cont = 0
    indexList = list()
    parse = CiscoConfParse('Ex1')
    for intf_obj in parse.find_objects(r'nodes'):
        for c1_obj in intf_obj.children:
            for c2_obj in c1_obj.children:
                if "label:" in c2_obj.text:
                    indexList.append(str(c2_obj.text).replace("label:", ""))
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
    pdf.ln(10)
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
    
    ips= list()
    intf= list()
    term=list()
    xxs= list()
    idx=1
    for klk in dd['nodes']:
        pdf.set_font('Times', 'B', 12)
        pdf.ln(8)
        pdf.cell(0, 0, '2.'+str(idx)+'.- '+ klk['label'], 0, 1)
        pdf.ln(6)
        ms=1
        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', '', 10)
            #Date and Time
            xx='UTC'
            match=re.search(xx, klk['configuration'])
            s=match.start()
            e=match.end()
            time=klk['configuration'][(s-9):(e)]
            date=klk['configuration'][(e+5):(e+16)]

            pdf.cell(0, 10, 'El darrer canvi de la configuració va ser el '+ date +' a les '+ time, 0, 1)
            pdf.set_font('Times', 'B', 12)
            pdf.ln(9)
            pdf.cell(0, 10, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració criptogràfica del dispositiu', 0, 1)
            pdf.set_font('Times', '', 12)
            pdf.ln(7)
            if "crypto" in klk['configuration']:
                pdf.cell(0, 10, 'El dispositiu té la següent configuració de crypto:', 0, 1)
                pdf.ln(4)
                pdf.cell(20)
                xx='set peer'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                ip=klk['configuration'][(e+1):(e+9)]
                pdf.cell(0, 10, '-    Conexió amb '+ ip +':', 0, 1)
                pdf.ln(6)
                pdf.cell(30)
                #Cojer numero
                xx='isakmp policy'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                numero=klk['configuration'][(e+1):(e+3)]
                pdf.cell(0, 10, 'o   Política de regles número '+ numero +':', 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer encript
                xx='encr aes'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                ee=klk['configuration'][(e-3):(e+4)]
                pdf.cell(0, 0, '·    Encriptació '+ ee, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer authentification
                xx='authentication'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                auth=klk['configuration'][(e+1):(e+10)]
                pdf.cell(0, 10, '·    Autenticació '+ auth, 0, 1)
                pdf.ln(2)
                pdf.cell(40)
                #Cojer group
                xx='group'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                group=klk['configuration'][(e+1)]
                pdf.cell(0, 10, '·    Diffie-Helmann grup '+ group, 0, 1)
                pdf.ln(6)
                pdf.cell(30)
                #Cojer key
                xx='isakmp key'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                key=klk['configuration'][(e+1):(e+8)]
                pdf.cell(0, 10, 'o   Contrasenya ISAKMP: '+ key, 0, 1)
                pdf.ln(6)
                pdf.cell(30)
                pdf.cell(0, 10, 'o   Configuració VPN:', 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer tranform
                xx='ipsec transform-set'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                tt=klk['configuration'][(e+1):(e+4)]
                pdf.cell(0, 10, '·    Conjunt de transformació '+ tt, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer encriptaci
                enc=klk['configuration'][(e+5):(e+12)]
                pdf.cell(0, 10, '·    Configuració Encriptació ESP: '+ enc, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer signatur
                sgn=klk['configuration'][(e+13):(e+25)]
                pdf.cell(0, 10, '·    Configuració Signatura ESP: '+ sgn, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer mode
                mod=klk['configuration'][(e+32):(e+38)]
                pdf.cell(0, 10, '·    Mode '+ mod, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                #Cojer acl
                pattern='match address'
                match=re.search(pattern, klk['configuration'])
                e=match.end()
                acl=klk['configuration'][(e+1):(e+4)]
                pdf.cell(0, 10, '·    ACL número '+ acl, 0, 1)
            else:
                pdf.cell(0, 10, 'El dispositiu no té configuració de crypto', 0, 1)
            
            ms=ms+1

        pdf.set_font('Times', 'B', 12)
        if "Building configuration..." in klk['configuration']:
            pdf.ln(4)
        pdf.cell(0, 10, '2.'+ str(idx) +'.'+ str(ms) +'.- Interfícies', 0, 1)
        pdf.set_font('Times', '', 11)
        pdf.cell(0, 10, 'Les interfícies i la seva configuració és:', 0, 1)
        pdf.ln(4)

        for q in klk['interfaces']:
            pdf.cell(25)
            xx=q['label']
            ff=re.search(xx, klk['configuration'])
            ipAddr=''
            if ff!=None:
                e=ff.end()
                if "no" not in klk['configuration'][(e):(e+5)]:
                    ipAddr=klk['configuration'][(e+13):(e+38)]
                    xx='255.255'
                    ff=re.search(xx, ipAddr)
                    if ff != None:
                        s=ff.start()
                        term.append(klk['label'])
                        intf.append(q['id'])
                        ips.append(ipAddr[:s])

                        ipAddr=': '+ipAddr[:s]+'('+ipAddr[s:len(ipAddr)]+')'
                if 'alpine' in klk['node_definition']:
                    term.append(klk['label'])
                    intf.append(q['id'])

                    ipAddr=' (DG: '+ipAddr[13:]+')'
                    xx='ip addr add'
                    ff=re.search(xx, klk['configuration'])
                    e=ff.end()
                    ips.append(klk['configuration'][(e+1):(e+12)])

                    ipAddr='. Configuració IP: '+klk['configuration'][(e+1):(e+15)]+ ipAddr
            
            pdf.cell(0, 10, '-    Link '+ q['id']+': '+ q['label']+ ipAddr, 0, 1)
            pdf.ln(5)
        ms=ms+1

        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', 'B', 12)
            pdf.ln(5)
            pdf.cell(0, 10, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració dels protocols d enrutament', 0, 1)
            pdf.set_font('Times', '', 11)
            #Cojer protocol
            xx='router ospf'
            match=re.search(xx, klk['configuration'])
            if(match!=None):
                e=match.end()
            protocol=klk['configuration'][(e-4):(e+4)]
            pdf.cell(0, 0, 'El protocol d enrutament utilitzat és '+ protocol.upper() +', amb la següent configuració (xarxes publicades):', 0, 1)
            pdf.ln(4)
            pdf.cell(10)
            #Cojer area
            xx='area'
            match=re.search(xx, klk['configuration'])
            if(match!=None):
                e=match.end()
            area=klk['configuration'][e+1]
            pdf.cell(0, 10, '-    Àrea '+ area+':', 0, 1)
            #Cojer network
            xx='network'
            match=re.search(xx, klk['configuration'])
            if(match!=None):
                s=match.end()
            s=s+1
            network=""
            while klk['configuration'][s]!='!':
                network=network+klk['configuration'][s]
                s=s+1
            num=klk['configuration'].count("area")
            network=network.replace("network", "")
            network=network.replace("area 0", "")
            while num>0:
                xx=' '
                match=re.search(xx, network)
                if(match!= None):
                    x=match.end()
                    if network[:x-1] not in xxs:
                        xxs.append(network[:x-1])
                    parte1=network[:x-1]+' màscara invertida '
                    network=network[x:]
                    network=network[2:]
                    match=re.search(pattern, network)
                    parte2=network[:x-1]
                    network=network[x:]
                    net=parte1+parte2
                pdf.ln(7)
                pdf.cell(20)
                pdf.cell(0, 0, 'o   Xarxa '+ net, 0, 1)
                num=num-1 
            ms=ms+1

        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', 'B', 12)
            pdf.ln(9)
            pdf.cell(0, 0, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració de Llistes de Control d Accés', 0, 1)
            pdf.set_font('Times', '', 11)
            pdf.ln(7)
            if "access-list" in klk['configuration']:
                pdf.cell(0, 0, 'El dispositiu té configurada la següent ACL:', 0, 1)
                pdf.ln(7)
                pdf.cell(10)
                #Cojer acclist
                xx='access-list'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                acclist=klk['configuration'][(e+1):(e+4)]
                pdf.cell(0, 0, '-    Número '+acclist, 0, 1)
                pdf.ln(5)
                pdf.cell(20)
                #Cojer permit
                xx='permit'
                match=re.search(xx, klk['configuration'])
                e=match.end()
                permit=klk['configuration'][(e+1):(e+3)]
                pdf.cell(0, 10, 'o   PERMIT ('+ permit.upper() +'):', 0, 1)
                pdf.ln(1)
                pdf.cell(30)
                #Cojer origen y desti
                xx='control-plane'
                match=re.search(xx, klk['configuration'])
                s=match.start()
                origdest=klk['configuration'][(e+4):(s-2)]
                xx=' '
                match=re.search(xx, origdest)
                if(match!= None):
                    x=match.end()
                    origen=origdest[:x-1]+' màscara invertida '+origdest[x:x+9]
                    origdest=origdest[x:]
                    match=re.search(pattern, klk['configuration'])
                    x=match.start()
                    origdest=origdest[x+2:]
                    match=re.search(pattern, klk['configuration'])
                    x=match.start()
                    desti=origdest[:x+3]+' màscara invertida '+origdest[x+3:x+13]
                pdf.cell(0, 10, '·   ORIGEN: '+origen, 0, 1)
                pdf.ln(2)
                pdf.cell(30)
                pdf.cell(0, 10, '·   DESTÍ: '+desti, 0, 1)
            else:
                pdf.cell(0, 10, 'El dispositiu no té configurada cap ACL.', 0, 1)

            ms=ms+1

        if "Building configuration..." in klk['configuration']:
            pdf.set_font('Times', 'B', 12)
            pdf.ln(9)
            pdf.cell(0, 0, '2.'+ str(idx) +'.'+ str(ms) +'.- Configuració de Banners', 0, 1)
            pdf.set_font('Times', '', 11)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(7)
            pdf.cell(0, 0, 'El dispositiu té configurats els següent Banners:', 0, 1)
            pdf.ln(7)

            #Cojer banner
            xx='banner'
            match=re.search(xx, klk['configuration'])
            e=match.end()
            xx='line con 0'
            match=re.search(xx, klk['configuration'])
            s=match.start()
            banner=klk['configuration'][(e+1):(s-2)]
            banner="    -    "+banner
            banner=banner.replace("banner", "    -    ")
            banner=banner.replace("^CCC", " ")
            banner=banner.replace("^C", " ")
            pdf.cell(18)
            pdf.multi_cell(170, 8, banner, 0, 'J', False)
            ms=ms+1
        idx=idx+1 
    #3.- 
    pdf.set_font('Times', '', 20)
    pdf.ln(5)
    pdf.cell(18)
    pdf.cell(10, 10, '3.- Interfícies', 0, 1)
    pdf.set_font('Times', '', 10)
    pdf.ln(3)
    pdf.cell(18)
    pdf.cell(0, 10, 'La configuració de les interfícies (links) d interconnexió entre equips és:', 0, 1)
    pdf.ln(8)
    for q in dd['links']:
        pdf.cell(25)
        pdf.set_font('Times', 'B', 11)

        #Cojer id
        ids='1'+q['id'][1]

        pdf.cell(0, 0, '-    Link '+ids, 0, 1)
        pdf.set_font('Times', '', 11)
        pdf.cell(44)

        #Cojer nombres label con su id
        lab1=''
        lab2=''
        for n in dd['nodes']:
            if q['n1'] == n['id']:
                lab1=n['label']
            if q['n2'] == n['id']:
                lab2=n['label']

        pdf.cell(0, 0, ': conecta '+ q['i1'] +' ('+ lab1 +')'+' amb '+ q['i2']+' ('+ lab2 +')', 0, 1)
        pdf.ln(5)

    pdf.ln(3)
    pdf.cell(18)
    pdf.cell(0, 0, 'El resum de les adreces IP de les interfícies és:', 0, 1)
    #TABLA
    pdf.ln(5)
    pdf.cell(13)
    if len(xxs)!=0:
        pdf.cell(23, 10, "Xarxa", 0, 0)
    pdf.cell(23, 10, "Equip1", 0, 0)
    pdf.cell(23, 10, "Interfície1", 0, 0)
    pdf.cell(23, 10, "IP1", 0, 0)
    pdf.cell(23, 10, "Equip2", 0, 0)
    pdf.cell(23, 10, "Interfície2", 0, 0)
    pdf.cell(23, 10, "IP2", 0, 0)
    pdf.ln(6)
    l=0
    while l< len(term):
        pdf.cell(13)
        if len(xxs)!=0:
            if l==0:
                pdf.cell(23, 10, xxs[l], 0, 0)
            else:
                pdf.cell(23, 10, xxs[int(l/2)], 0, 0)
        pdf.cell(23, 10, term[l], 0, 0)
        pdf.cell(23, 10, intf[l], 0, 0)
        pdf.cell(23, 10, ips[l], 0, 0)
        if(l+1!=len(term)):
            pdf.cell(23, 10, term[l+1], 0, 0)
            pdf.cell(23, 10, intf[l+1], 0, 0)
            pdf.cell(23, 10, ips[l+1], 0, 0)
            pdf.ln(5)
        else:
            pdf.ln(5)
        
        l=l+2
    pdf.output("Ex3.pdf")
