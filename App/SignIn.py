import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import messagebox, filedialog

import customtkinter as ctk
from PIL import Image

import DownloadPDF as xp
import HomePage as hp


def SignIn(root):
    # Fonts
    InputFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=18)
    HeadingFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=48, weight="bold")
    ButtonsFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=16, weight="bold")
    # Images
    image_emploi = ctk.CTkImage(light_image=Image.open("./Images/emploi.png"), size=(88, 96))
    image_rlv_gen = ctk.CTkImage(light_image=Image.open("./Images/relv_gen.png"), size=(88, 96))

    def Telecharger(button):
        match button:
            case "emploi":
                xml_emploi = "../FichiersXML/XML/Emploi.xml"
                xsl_emploi = "../FichiersXML/XSLTanas/EmploisAll.xsl"
                file_types = [("PDF files", "*.pdf")]
                pdf_output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=file_types, initialfile="EmploisGINF2")
                print(pdf_output)
                if pdf_output:
                    if xp.Download_emploi(xml_emploi, xsl_emploi, pdf_output):
                        messagebox.showinfo("Info de Téléchargement", "Emploi du temps téléchargé avec succès !")
            case "rlv_gen":
                pass

    def sign_in():
        id_etudiant = id_etd_input.get()

        if id_etudiant == "":
            messagebox.showerror("Invalid Inputs", "Error! Username/Password cannot be empty")
            return

        result = check_id_etudiant_exists(id_etudiant)

        if result:
            nom, prenom, id_etudiant, moyenneGen = result
            frameSignIn.destroy()
            hp.HomePage(root, nom, prenom, moyenneGen, id_etudiant)
        else:
            messagebox.showerror("Invalid Inputs", "Error! Invalid id_etudiant")

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

        return None

    frameSignIn = ctk.CTkFrame(master=root, fg_color="#fff", bg_color="#fff")
    frameSignIn.pack(fill=tk.BOTH, expand=True)

    frameFormSignIn = ctk.CTkFrame(master=frameSignIn, width=600, fg_color="#fff")
    frameFormSignIn.pack(side=tk.RIGHT, fill=tk.Y)

    frameButtons_signIn = ctk.CTkFrame(master=frameSignIn, width=590, height=590, fg_color="#f8fafc")
    frameButtons_signIn.place(x=305, y=300, anchor=tk.CENTER)

    # Sign In Heading
    heading_signIn = ctk.CTkLabel(frameFormSignIn, text="Information étudiant", font=HeadingFont, text_color="#000")
    heading_signIn.place(x=300, y=120, anchor=tk.CENTER)

    # Id etudiant Input
    id_etd_input = ctk.CTkEntry(frameFormSignIn, width=250, height=40, font=InputFont,
                                placeholder_text="Id etudiant", text_color="#000")
    id_etd_input.place(x=300, y=250, anchor=tk.CENTER)

    # Search Button
    SearchButton = ctk.CTkButton(frameFormSignIn, text="Chercher", font=InputFont, width=55, height=35,
                                 text_color="#000",
                                 hover_color="#DAE5F4", fg_color="#7F8CD9", cursor="hand2", command=sign_in)
    SearchButton.place(x=300, y=320, anchor=tk.CENTER)

    # Labels
    Labelemploi = ctk.CTkLabel(master=frameButtons_signIn, font=ButtonsFont, width=380, height=230,
                               text="Emplois du temps", text_color="#000", fg_color="#DAE5F4",
                               bg_color="transparent", corner_radius=20, image=image_emploi,
                               compound="top")
    Labelemploi.place(x=100, y=20)

    LabelRelvgen = ctk.CTkLabel(master=frameButtons_signIn, font=ButtonsFont, width=380, height=230,
                                text="Relevé général", text_color="#000", fg_color="#DAE5F4",
                                bg_color="transparent", corner_radius=20, image=image_rlv_gen,
                                compound="top")
    LabelRelvgen.place(x=100, y=300)

    # Buttons
    emploiButton = ctk.CTkButton(frameButtons_signIn, text="Télécharger", font=InputFont, width=55, height=30,
                                 text_color="#000",
                                 hover_color="#DAE5F4", fg_color="#7F8CD9", cursor="hand2",
                                 command=lambda: Telecharger("emploi"))
    emploiButton.place(x=280, y=270, anchor=tk.CENTER)

    rlv_genButton = ctk.CTkButton(frameButtons_signIn, text="Télécharger", font=InputFont, width=55, height=30,
                                  text_color="#000",
                                  hover_color="#DAE5F4", fg_color="#7F8CD9", cursor="hand2",
                                  command=lambda: Telecharger("rlv_gen"))

    rlv_genButton.place(x=280, y=550, anchor=tk.CENTER)
