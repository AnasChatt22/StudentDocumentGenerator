import os
import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import messagebox, filedialog

import customtkinter as ctk
from PIL import Image

import Generation.Generate as gn
import HomePage as hp


def SignIn(root):
    # Fonts
    InputFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=18)
    HeadingFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=48, weight="bold")
    ButtonsFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=16, weight="bold")
    # Images
    image_emploi = ctk.CTkImage(light_image=Image.open("./Images/emploi.png"), size=(88, 96))
    image_rlv_gen = ctk.CTkImage(light_image=Image.open("./Images/relv_gen.png"), size=(88, 96))
    logo_ensat = ctk.CTkImage(light_image=Image.open("./Images/logoensat.png"), size=(110, 80))

    def Telecharger(button):
        file_types = [("PDF files", "*.pdf")]
        match button:
            case "emploi":
                options = {
                    'quiet': '',
                    'encoding': 'utf-8',
                    'page-width': '1300px',
                    'page-height': '835px'
                }
                xml_emploi = "../FichiersXML/XML/Emploi.xml"
                xsl_emploi = "../FichiersXML/XSLT/Emploi.xsl"
                pdf_output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=file_types,
                                                          initialfile="EmploisGINF2")
                if pdf_output:
                    if gn.generate_pdf_from_xslt(xml_emploi, xsl_emploi, pdf_output, options):
                        messagebox.showinfo("Info de Téléchargement", "Emploi du temps téléchargé avec succès !")
                        os.system(f'start {pdf_output}')
                    else:
                        messagebox.showerror("Info de Téléchargement", "Erreur de téléchargement")
            case "rlv_gen":
                options = {
                    'quiet': '',
                    'encoding': 'utf-8',
                    'page-width': '2000px',
                    'page-height': '800px'
                }
                xml_rlv_gen = "../FichiersXML/XML/GINF2.xml"
                xsl_rlv_gen = "../FichiersXML/XSLT/releve_general.xsl"
                pdf_output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=file_types,
                                                          initialfile="RelevéGINF2")
                if pdf_output:
                    if gn.generate_pdf_from_xslt(xml_rlv_gen, xsl_rlv_gen, pdf_output, options):
                        messagebox.showinfo("Info de Téléchargement",
                                            "Relevé général de notes téléchargé avec succès !")
                        os.system(f'start {pdf_output}')
                else:
                    messagebox.showerror("Info de Téléchargement", "Erreur de téléchargement")

    def sign_in():
        if len(id_etd_input.get()) == 0:
            messagebox.showerror("Invalid Inputs", "Erreur! ID étudiant ne peut pas être vide")
            return

        result = check_id_etudiant_exists(id_etd_input.get())

        if result:
            nom, prenom, id_etudiant, moyenneGen = result
            frameSignIn.destroy()
            hp.HomePage(root, nom, prenom, moyenneGen, id_etudiant)
        else:
            messagebox.showerror("Invalid Inputs", "Erreur! ID étudiant n'existe pas")

    def check_id_etudiant_exists(id_etudiant):
        tree = ET.parse('../FichiersXML/XML/GINF2.xml')
        root_xml = tree.getroot()

        # Search for the given id_etudiant
        for etudiant in root_xml.findall('.//Etudiant'):
            if etudiant.get('id_etudiant') == id_etudiant:
                # Collect Nom and Prenom and return as a tuple
                nom = etudiant.find('Nom').text
                prenom = etudiant.find('Prenom').text
                moyenneGen = etudiant.find('MoyenneGenerale').text
                return nom, prenom, id_etudiant, moyenneGen

    frameSignIn = ctk.CTkFrame(master=root, fg_color="#fff", bg_color="#fff")
    frameSignIn.pack(fill=tk.BOTH, expand=True)

    frameFormSignIn = ctk.CTkFrame(master=frameSignIn, width=600, fg_color="transparent")
    frameFormSignIn.pack(side=tk.RIGHT, fill=tk.Y)

    frameButtons_signIn = ctk.CTkFrame(master=frameSignIn, width=590, height=590, fg_color="#f8f8f8")
    frameButtons_signIn.place(x=305, y=300, anchor=tk.CENTER)

    # Logo ensat
    label_logo_signIn = ctk.CTkLabel(master=frameFormSignIn, text="", image=logo_ensat)
    label_logo_signIn.place(x=480, y=1)

    # Sign In Heading
    heading_signIn = ctk.CTkLabel(frameFormSignIn, text="Information étudiant", font=HeadingFont, text_color="#000")
    heading_signIn.place(x=300, y=150, anchor=tk.CENTER)

    # Id etudiant Input
    id_etd_input = ctk.CTkEntry(frameFormSignIn, width=250, height=40, font=InputFont,
                                placeholder_text="Id etudiant", text_color="#000")
    id_etd_input.place(x=300, y=250, anchor=tk.CENTER)

    # Search Button
    SearchButton = ctk.CTkButton(frameFormSignIn, text="Chercher", font=InputFont, width=55, height=35,
                                 text_color="#fff",
                                 hover_color="#f4a024", fg_color="#294a70", cursor="hand2", command=sign_in)
    SearchButton.place(x=300, y=300, anchor=tk.CENTER)

    # Labels
    Labelemploi = ctk.CTkLabel(master=frameButtons_signIn, font=ButtonsFont, width=380, height=230,
                               text="Emplois du temps", text_color="#000", fg_color="#a3d3f1",
                               bg_color="transparent", corner_radius=20, image=image_emploi,
                               compound="top")
    Labelemploi.place(x=100, y=20)

    LabelRelvgen = ctk.CTkLabel(master=frameButtons_signIn, font=ButtonsFont, width=380, height=230,
                                text="Relevé général", text_color="#000", fg_color="#a3d3f1",
                                bg_color="transparent", corner_radius=20, image=image_rlv_gen,
                                compound="top")
    LabelRelvgen.place(x=100, y=300)

    # Buttons
    emploiButton = ctk.CTkButton(frameButtons_signIn, text="Télécharger", font=InputFont, width=55, height=30,
                                 text_color="#fff",
                                 hover_color="#f4a024", fg_color="#294a70", cursor="hand2",
                                 command=lambda: Telecharger("emploi"))
    emploiButton.place(x=280, y=270, anchor=tk.CENTER)

    rlv_genButton = ctk.CTkButton(frameButtons_signIn, text="Télécharger", font=InputFont, width=55, height=30,
                                  text_color="#fff",
                                  hover_color="#f4a024", fg_color="#294a70", cursor="hand2",
                                  command=lambda: Telecharger("rlv_gen"))

    rlv_genButton.place(x=280, y=550, anchor=tk.CENTER)
