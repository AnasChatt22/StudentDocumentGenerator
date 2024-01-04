<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0">
    <xsl:output method="html" indent="yes"/>
    <xsl:param name="id_etudiant"/>

    <!-- Match the root element -->
    <xsl:template match="/">
        <!-- Output the HTML structure for the certificate -->
        <html>
            <head>
                <title>Attestation de réussite</title>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
                <style type="text/css">
                    @page{
                    size: A4;
                    }
                    hr {
                    height: 2px;
                    margin: 5px 0;
                    border: none;
                    border-top: 2px solid #000;
                    width: 25%; /* Adjust the width as needed */
                    }
                    body {
                    font-family: "Calibri", sans-serif;
                    padding: 30px;
                    position: relative;
                    }
                </style>
            </head>
            <body>
                <center>
                    <h3>UNIVERSITÉ ABDELMALEK ESSAÂDI</h3>
                    <h4 style="margin: 0px">جامعة عبد المالك السعدي</h4>
                    <h3 style="border: 1px solid #000; display: inline-block; padding: 3px 70px;">ATTESTATION DE
                        REUSSITE
                    </h3>
                    <br/>
                    <br/>
                    <p>Le Directeur de l'Ecole Nationale des Sciences Appliquées de Tanger atteste que</p>
                    <!-- Apply the template for the first Etudiant element -->
                    <xsl:apply-templates select="Etudiants/Etudiant[@id_etudiant = $id_etudiant]"/>
                </center>
            </body>
        </html>
    </xsl:template>

    <!-- Match the Etudiant element -->
    <xsl:template match="Etudiant">
        <!-- Output the certificate information -->
        <p>
            <strong>
                <xsl:if test="@sexe = 'Homme'">
                    Monsieur
                </xsl:if>
                <xsl:if test="@sexe = 'Femme'">
                    Madmoiselle
                </xsl:if>
                <xsl:value-of select="Nom"/>
                <xsl:text> </xsl:text>
                <xsl:value-of select="Prenom"/>
            </strong>
        </p>
        <p>
            né le
            <xsl:value-of select="@date_naissance"/>
        </p>
        <p>
            a été déclaré(e) admis au niveau
        </p>
        <p>
            <strong>2ºAnnée Génie Informatique</strong>
        </p>
        <p>au title de l'année universitaire 2023/2024 avec la mention
            <xsl:choose>
                <xsl:when test="./MoyenneGenerale >= 16">Très Bien</xsl:when>
                <xsl:when test="./MoyenneGenerale >= 14">Bien</xsl:when>
                <xsl:when test="./MoyenneGenerale >= 12">Assez Bien</xsl:when>
                <xsl:otherwise>Admis(e)</xsl:otherwise>
            </xsl:choose>
        </p>
        <hr/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>

        <p style="text-align: right; padding-right: 100px; ">Fait à TANGER, le 26 septembre 2024</p>
        <br/>
        <br/>
        <br/>
        <p style="text-align: left; padding-left: 100px;">Nº étudiant :
            <xsl:value-of select="@id_etudiant"/>
        </p>
        <p style="text-align: right; padding-right: 180px; ">Le Directeur</p>
        <br/>
        <br/>
        <p style="text-align: left; padding-left: 80px; font-size: 13px">
            Avis important: Il ne peut être délivré qu'un seul exemplaire de cette attestation.
            Aucun duplica ne sera fourni.
        </p>


    </xsl:template>

</xsl:stylesheet>
