<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    <xsl:template match="/">
        <html>
            <head>
                <title>Employees</title>
                <style type="text/css">
                    @page{
                    size: a4 landscape;
                    }
                    body {
                    margin-top:100px;
                    font-family: Helvetica, Arial, sans-serif;
                    font-size : 8px;
                    }
                    .header {
                    color: #FFFFFF;
                    }
                    table {
                    font-family: arial, sans-serif;
                    border-collapse: collapse;
                    width: 100%;
                    margin:auto;
                    }
                    th{
                    position: sticky;
                    vertical-align: bottom;
                    background-color: #cce;
                    }

                    td, th {
                    border: 1px solid black;
                    text-align: left;
                    padding: 8px;
                    padding-left:1px;
                    }

                </style>
            </head>
            <body>
                <table>
                    <tr>
                        <th style= "border: 0px solid #dddddd;background-color: white;">
                        </th>
                        <th style= "border: 0px solid #dddddd;background-color: white;">
                        </th >
                        <th style= "border: 0px solid #dddddd;background-color: white;">
                        </th>
                        <xsl:for-each select="Etudiants/Etudiant[1]/Module[Semestre=3]">

                                <th colspan="3" style="background-color: #cce; ">
                                    <xsl:value-of select="Designation"/>
                                </th>


                        </xsl:for-each>
                    </tr>
                    <tr>
                        <td style=" min-width:25px;max-width:25px;text-align:left;font-weight:600;">
                            <p>Code Apogé</p>
                        </td>
                        <td style="min-width:30px;max-width:30px;text-align:center;font-weight:600;">
                            <p>Nom</p>
                        </td>
                        <td style="min-width:30px;max-width:30px;text-align:center;font-weight:600;">
                            <p>Prénom</p>
                        </td>
                        <xsl:for-each select="Etudiants/Etudiant[1]/Module[Semestre=3]">

                            <td style="min-width:15px;max-width:15px;text-align:left; background-color:rgb(228, 240, 245);">
                                    <xsl:value-of select="Matiere[1]/Designation"/>
                                </td>
                            <td style="min-width:15px;max-width:15px;text-align:left; background-color:rgb(228, 240, 245);">
                                    <xsl:value-of select="Matiere[last()]/Designation"/>
                                </td>
                            <td style="min-width:15px;max-width:15px;font-weight:600;text-align:left;background-color:rgb(228, 240, 150);">
                                <p>MOYENNE</p>
                            </td>
                        </xsl:for-each>
                        <td style="min-width:15px;max-width:15px;font-weight:600;text-align:left;">
                            <p>MOYENNE</p>
                        </td>
                    </tr>
                        <xsl:for-each select="Etudiants/Etudiant">
                            <xsl:variable name="total" />
                            <tr>
                                <td style="min-width:20px;max-width:20px;">
                                    <xsl:value-of select="@id_etudiant"/>
                                </td>
                                <td style="min-width:35px;max-width:35px;">
                                    <xsl:value-of select="Nom"/>
                                </td>
                                <td style="min-width:25px;max-width:25px;text-align:right;padding-right:1px">
                                    <xsl:value-of select="Prenom"/>
                                </td>
                                <xsl:for-each select="Module[Semestre=3]">

                                    <td style="min-width:15px;max-width:15px;text-align:center;">
                                            <xsl:value-of select="Matiere[1]/Note"/>
                                        </td>
                                    <td style="min-width:15px;max-width:15px;text-align:center;">
                                            <xsl:value-of select="Matiere[last()]/Note"/>
                                        </td>
                                    <xsl:choose>
                                        <xsl:when test="Moyenne &gt; 8">
                                            <xsl:choose>
                                                <xsl:when test="Moyenne &gt; 12">
                                                    <xsl:choose>
                                                        <xsl:when test="Moyenne &gt; 14">
                                                            <xsl:choose>
                                                                <xsl:when test="Moyenne &gt; 16">
                                                                    <td style="text-align:center;background-color:#33B2FF"> <xsl:value-of select="Moyenne" /></td>
                                                                </xsl:when>
                                                                <xsl:otherwise>
                                                                    <td style="text-align:center;background-color:#33FF36"> <xsl:value-of select="Moyenne" /></td>
                                                                </xsl:otherwise>
                                                            </xsl:choose>
                                                        </xsl:when>
                                                        <xsl:otherwise>
                                                            <td style="text-align:center;background-color:#FFF933"> <xsl:value-of select="Moyenne" /></td>
                                                        </xsl:otherwise>
                                                    </xsl:choose>
                                                </xsl:when>
                                                <xsl:otherwise>
                                                    <td style="text-align:center;background-color:#FFA233"> <xsl:value-of select="Moyenne" /></td>
                                                </xsl:otherwise>
                                            </xsl:choose>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <td style="text-align:center;background-color:#FF3333"> <xsl:value-of select="Moyenne" /></td>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                </xsl:for-each>
                                <xsl:choose>
                                    <xsl:when test="MoyenneSemestre3 &gt; 8">
                                        <xsl:choose>
                                            <xsl:when test="MoyenneSemestre3 &gt; 12">
                                                <xsl:choose>
                                                    <xsl:when test="MoyenneSemestre3 &gt; 14">
                                                        <xsl:choose>
                                                            <xsl:when test="MoyenneSemestre3 &gt; 16">
                                                                <td style="text-align:center;background-color:#33B2FF"> <xsl:value-of select="MoyenneSemestre3" /></td>
                                                            </xsl:when>
                                                            <xsl:otherwise>
                                                                <td style="text-align:center;background-color:#33FF36"> <xsl:value-of select="MoyenneSemestre3" /></td>
                                                            </xsl:otherwise>
                                                        </xsl:choose>
                                                    </xsl:when>
                                                    <xsl:otherwise>
                                                        <td style="text-align:center;background-color:#FFF933"> <xsl:value-of select="MoyenneSemestre3" /></td>
                                                    </xsl:otherwise>
                                                </xsl:choose>
                                            </xsl:when>
                                            <xsl:otherwise>
                                                <td style="text-align:center;background-color:#FFA233"> <xsl:value-of select="MoyenneSemestre3" /></td>
                                            </xsl:otherwise>
                                        </xsl:choose>
                                    </xsl:when>
                                    <xsl:otherwise>
                                        <td style="text-align:center;background-color:#FF3333"> <xsl:value-of select="MoyenneSemestre3" /></td>
                                    </xsl:otherwise>
                                </xsl:choose>
                            </tr>
                        </xsl:for-each>

                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>