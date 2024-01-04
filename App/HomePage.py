import tkinter as tk
from tkinter import filedialog, messagebox

import customtkinter as ctk
from PIL import Image

import DownloadPDF as xp
import SignIn as si


def HomePage(root, nom, prenom, moyenneGen, id_etudiant):
    def logout():
        frameHome.destroy()
        root.update()
        si.SignIn(root)

    def Telecharger(button):
        file_types = [("PDF files", "*.pdf")]
        match button:
            case "rlv_note":
                pass
            case "att_sco":
                pass
            case "att_reuss":
                xml_att_reuss = "../FichiersXML/XML/GINF2.xml"
                xsl_att_reuss = "../FichiersXML/XSLTanas/Attestation_reussite.xsl"
                if float(moyenneGen) < 12:
                    messagebox.showwarning("Attention", "Etudiant non admis (Moyenne < 12)")
                else:
                    pdf_output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=file_types,
                                                              initialfile=f"Attestation_reussite_{prenom}_{nom}")
                    if pdf_output:
                        if xp.Download_Att_reuss(xml_att_reuss, xsl_att_reuss, pdf_output, id_etudiant):
                            messagebox.showinfo("Info de Téléchargement", "Attestaion de réussite téléchargée !")
            case "carte_etd":
                xml_carte_etd = "../FichiersXML/XML/GINF2.xml"
                xsl_carte_etd = "../FichiersXML/XSLTanas/CarteEtd.xsl"
                pdf_output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=file_types,
                                                          initialfile=f"Carte_étudiant_{prenom}_{nom}")
                if pdf_output:
                    if xp.Download_CarteEtd(xml_carte_etd, xsl_carte_etd, pdf_output, id_etudiant):
                        messagebox.showinfo("Info de Téléchargement", "Carte d'étudiant téléchargée !")

    # Fonts
    ButtonsFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=16, weight="bold")
    # images
    image_Home_1 = ctk.CTkImage(light_image=Image.open("./Images/card.png"), size=(88, 96))
    image_Home_2 = ctk.CTkImage(light_image=Image.open("./Images/releve_note.png"), size=(88, 96))
    image_Home_3 = ctk.CTkImage(light_image=Image.open("./Images/attes_reus.png"), size=(88, 96))
    image_Home_4 = ctk.CTkImage(light_image=Image.open("./Images/attes_scol.png"), size=(100, 96))

    # Main frame Home Page
    frameHome = ctk.CTkFrame(master=root, fg_color="#f8fafc", bg_color="#f8fafc")
    frameHome.pack(fill=tk.BOTH, expand=True)

    # Logout button
    image_logout = ctk.CTkImage(light_image=Image.open("./Images/logout.png"), size=(33, 36))
    image_logout_button = ctk.CTkButton(master=frameHome, font=ButtonsFont, width=40, height=40,
                                        fg_color="#7F8CD9", text="", hover_color="#DAE5F4", cursor="hand2",
                                        bg_color="transparent", corner_radius=20, image=image_logout,
                                        command=logout)
    image_logout_button.place(x=550, y=10)

    # Nom et Prenom Etudiant
    label_font = ctk.CTkFont(family="Arial", size=14, weight="bold")
    label_etud = ctk.CTkLabel(master=frameHome, font=label_font,
                              text=f"{prenom} {nom}")
    label_etud.place(x=520, y=70)

    # Buttons
    InputFont = ctk.CTkFont(family="Microsoft YaHei UI Light", size=18)

    button_rlv_note = ctk.CTkButton(master=frameHome, text="télécharger", hover_color="#DAE5F4", fg_color="#7F8CD9",
                                    cursor="hand2", font=InputFont, width=50, height=25, text_color="#000",
                                    command=lambda: Telecharger("rlv_note"))
    button_att_sco = ctk.CTkButton(master=frameHome, text="télécharger", hover_color="#DAE5F4", fg_color="#7F8CD9",
                                   cursor="hand2", font=InputFont, width=50, height=25, text_color="#000",
                                   command=lambda: Telecharger("att_sco"))
    button_att_reuss = ctk.CTkButton(master=frameHome, text="télécharger", hover_color="#DAE5F4", fg_color="#7F8CD9",
                                     cursor="hand2", font=InputFont, width=50, height=25, text_color="#000",
                                     command=lambda: Telecharger("att_reuss"))
    button_carte_etd = ctk.CTkButton(master=frameHome, text="télécharger", hover_color="#DAE5F4", fg_color="#7F8CD9",
                                     cursor="hand2", font=InputFont, width=50, height=25, text_color="#000",
                                     command=lambda: Telecharger("carte_etd"))

    # Labels
    label_rlv_note = ctk.CTkLabel(master=frameHome, font=ButtonsFont, width=320, height=230,
                                  text="Relève de note", text_color="#000", fg_color="#DAE5F4",
                                  bg_color="transparent", corner_radius=20, image=image_Home_2,
                                  compound="top")
    label_rlv_note.place(x=40, y=20)
    button_rlv_note.place(x=200, y=270, anchor=tk.CENTER)

    label_att_sco = ctk.CTkLabel(master=frameHome, font=ButtonsFont, width=320, height=230,
                                 text="Attestation de scolarité", text_color="#000", fg_color="#DAE5F4",
                                 bg_color="transparent", corner_radius=20, image=image_Home_4,
                                 compound="top")
    label_att_sco.place(x=840, y=20)
    button_att_sco.place(x=1000, y=270, anchor=tk.CENTER)

    label_att_reuss = ctk.CTkLabel(master=frameHome, font=ButtonsFont, width=320, height=230,
                                   text="Attestation de reussite", text_color="#000",
                                   fg_color="#DAE5F4", image=image_Home_3, bg_color="transparent", corner_radius=20,
                                   compound="top")
    label_att_reuss.place(x=840, y=300)
    button_att_reuss.place(x=1000, y=550, anchor=tk.CENTER)

    label_carte_etd = ctk.CTkLabel(master=frameHome, font=ButtonsFont, width=320, height=230,
                                   text="Carte d'Etudiant", text_color="#000",
                                   fg_color="#DAE5F4", image=image_Home_1,
                                   bg_color="transparent", corner_radius=20,
                                   compound="top")
    label_carte_etd.place(x=40, y=300)
    button_carte_etd.place(x=200, y=550, anchor=tk.CENTER)
