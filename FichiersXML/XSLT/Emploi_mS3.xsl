<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/">
        <html>
            <head>
                <style>
                    @page {
                    size: A4 landscape;
                    }
                    body {
                    font-family: "Calibri", sans-serif;
                    padding: 5px;
                    position: relative;
                    }
                    table {
                    width: 100%;
                    border-spacing: 10px;
                    }
                    td {
                    border: 2px #dddddd;
                    border-radius: 15px;
                    text-align: center; /* Center align text */
                    width: 200px;
                    }
                    th {
                    border: 2px #dddddd;
                    border-radius: 15px;
                    text-align: center; /* Center align text */
                    padding: 5px; /* Add padding for spacing */
                    background-color: #f2f2f2;
                    width: 40px;
                    }
                    .type-TP {
                    background-color: #aaffaa; /* Light Green for TP */
                    }
                    .type-Cours {
                    background-color: #ddaaff; /* Light Purple for Cours */
                    }
                    .type-TD {
                    background-color: #ffffaa; /* Light Yellow for TD */
                    }
                </style>
            </head>
            <body>
                <center>
                    <xsl:apply-templates select="//Mi_semestre[@numero='3']"/>
                </center>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="Mi_semestre">
        <h2 style="margin: 5px;">Mi-semestre
            <xsl:value-of select="@numero"/>
        </h2>
        <table>
            <tr>
                <th>Heures</th>
                <xsl:for-each select="Semaine/Jour">
                    <th>
                        <xsl:value-of select="@nom"/>
                    </th>
                </xsl:for-each>
            </tr>
            <tr>
                <th>9:00</th>
                <xsl:for-each select="Semaine/Jour">
                    <xsl:for-each select="Seance[contains(@debut, '9:00') and contains(@fin, '10:30')]">
                        <td rowspan="4" class="type-{@type}">
                            <xsl:value-of select="concat(substring(@debut, 1, 5), ' - ', substring(@fin, 1, 5))"/>
                            <br/>
                            <xsl:value-of select="Matière/Designation"/>
                            <br/>
                            <xsl:value-of select="Matière/Professeur"/>
                            <br/>
                            <xsl:value-of select="Matière/Salle"/>
                        </td>
                    </xsl:for-each>
                </xsl:for-each>
            </tr>
            <tr>
                <th>9:30</th>
            </tr>
            <tr>
                <th>10:00</th>
            </tr>
            <tr>
                <th>10:30</th>
            </tr>
            <tr>
                <th>11:00</th>
                <xsl:for-each select="Semaine/Jour">
                    <xsl:for-each select="Seance[contains(@debut, '11:00') and contains(@fin, '12:30')]">
                        <td rowspan="4" class="type-{@type}">
                            <xsl:value-of select="concat(substring(@debut, 1, 5), ' - ', substring(@fin, 1, 5))"/>
                            <br/>
                            <xsl:value-of select="Matière/Designation"/>
                            <br/>
                            <xsl:value-of select="Matière/Professeur"/>
                            <br/>
                            <xsl:value-of select="Matière/Salle"/>
                        </td>
                    </xsl:for-each>
                </xsl:for-each>
            </tr>
            <tr>
                <th>11:30</th>
            </tr>
            <tr>
                <th>12:00</th>
            </tr>
            <tr>
                <th>12:30</th>
            </tr>
            <tr>
                <th>13:00</th>
            </tr>
            <tr>
                <th>13:30</th>
                <xsl:for-each select="Semaine/Jour">
                    <xsl:for-each select="Seance[contains(@debut, '13:30') and contains(@fin, '15:00')]">
                        <td rowspan="4" class="type-{@type}">
                            <xsl:value-of select="concat(substring(@debut, 1, 5), ' - ', substring(@fin, 1, 5))"/>
                            <br/>
                            <xsl:value-of select="Matière/Designation"/>
                            <br/>
                            <xsl:value-of select="Matière/Professeur"/>
                            <br/>
                            <xsl:value-of select="Matière/Salle"/>
                        </td>
                    </xsl:for-each>
                </xsl:for-each>
            </tr>
            <tr>
                <th>14:00</th>
            </tr>
            <tr>
                <th>14:30</th>
                <xsl:for-each select="Semaine/Jour">
                    <xsl:for-each select="Seance[contains(@debut, '14:30') and contains(@fin, '16:00')]">
                        <td rowspan="4" class="type-{@type}">
                            <xsl:value-of select="concat(substring(@debut, 1, 5), ' - ', substring(@fin, 1, 5))"/>
                            <br/>
                            <xsl:value-of select="Matière/Designation"/>
                            <br/>
                            <xsl:value-of select="Matière/Professeur"/>
                            <br/>
                            <xsl:value-of select="Matière/Salle"/>
                        </td>
                    </xsl:for-each>
                </xsl:for-each>
            </tr>
            <tr>
                <th>15:00</th>
            </tr>
            <tr>
                <th>15:30</th>
                <xsl:for-each select="Semaine/Jour">
                    <xsl:variable name="currentDay" select="@nom"/>
                    <xsl:if test="Seance[contains(@debut, '15:30') and contains(@fin, '17:00')]">
                        <xsl:for-each select="Seance[contains(@debut, '15:30') and contains(@fin, '17:00')]">
                            <td rowspan="4" class="type-{@type}">
                                <xsl:value-of select="concat(substring(@debut, 1, 5), ' - ', substring(@fin, 1, 5))"/>
                                <br/>
                                <xsl:value-of select="Matière/Designation"/>
                                <br/>
                                <xsl:value-of select="Matière/Professeur"/>
                                <br/>
                                <xsl:value-of select="Matière/Salle"/>
                            </td>
                        </xsl:for-each>
                    </xsl:if>
                </xsl:for-each>
            </tr>

            <tr>
                <th>16:00</th>
            </tr>
            <tr>
                <th>16:30</th>
                <xsl:for-each select="Semaine/Jour">
                    <xsl:for-each select="Seance[contains(@debut, '16:30') and contains(@fin, '18:00')]">
                        <td rowspan="4" class="type-{@type}">
                            <xsl:value-of select="concat(substring(@debut, 1, 5), ' - ', substring(@fin, 1, 5))"/>
                            <br/>
                            <xsl:value-of select="Matière/Designation"/>
                            <br/>
                            <xsl:value-of select="Matière/Professeur"/>
                            <br/>
                            <xsl:value-of select="Matière/Salle"/>
                        </td>
                    </xsl:for-each>
                </xsl:for-each>
            </tr>
            <tr>
                <th>17:00</th>
            </tr>
            <tr>
                <th>17:30</th>
            </tr>
            <tr>
                <th>18:00</th>
            </tr>
        </table>
    </xsl:template>
</xsl:stylesheet>