 <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="1.0">
    <xsl:template match="/">
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <fo:layout-master-set>
        <fo:simple-page-master master-name="A4" page-height="297mm" page-width="410mm">
            <fo:region-body margin-top="5mm" margin-bottom="20mm" margin-left="5mm" margin-right="5mm"/>
        </fo:simple-page-master>
    </fo:layout-master-set>
    <fo:page-sequence master-reference="A4">
        <fo:flow flow-name="xsl-region-body">
            <fo:block font-family="Helvetica, Arial, sans-serif" font-size="8pt">
   <fo:table>
       <fo:table-header>
           <fo:table-row  >
               <fo:table-cell border=" 0px" background-color=" white">
                   <fo:block></fo:block>
               </fo:table-cell>
               <fo:table-cell border=" 0px" background-color=" white">
                   <fo:block></fo:block>
               </fo:table-cell >
               <fo:table-cell border=" 0px" background-color=" white">
                   <fo:block></fo:block>
               </fo:table-cell>
               <xsl:for-each select="Etudiants/Etudiant[1]/Module[Semestre=3]">
                   <fo:table-cell border="1pt solid black" number-columns-spanned="3" background-color=" #cce ">
                       <fo:block><xsl:value-of select="Designation"/>  </fo:block>
                   </fo:table-cell>
               </xsl:for-each>
           </fo:table-row>
       </fo:table-header>
       <fo:table-body>

           <fo:table-row  >
               <fo:table-cell border="1pt solid black">
                            <fo:block>Code Apogé</fo:block>
                        </fo:table-cell>
               <fo:table-cell border="1pt solid black">
                            <fo:block>Nom</fo:block>
                        </fo:table-cell>
               <fo:table-cell border="1pt solid black" >
                            <fo:block>Prénom</fo:block>
                        </fo:table-cell>
                        <xsl:for-each select="Etudiants/Etudiant[1]/Module[Semestre=3]">

                            <fo:table-cell border="1pt solid black" text-align="left" background-color="rgb(228, 240, 245)">
                                <fo:block> <xsl:value-of select="Matiere[1]/Designation"/></fo:block>
                                </fo:table-cell>
                            <fo:table-cell border="1pt solid black" text-align="left" background-color="rgb(228, 240, 245)">
                                <fo:block> <xsl:value-of select="Matiere[last()]/Designation"/> </fo:block>
                                </fo:table-cell>
                            <fo:table-cell border="1pt solid black" font-weight="600" text-align="left" background-color="rgb(228, 240, 150)">
                                <fo:block>MOYENNE</fo:block>
                            </fo:table-cell>
                        </xsl:for-each>
               <fo:table-cell border="1pt solid black" font-weight="600" text-align="left">
                            <fo:block>MOYENNE</fo:block>
                        </fo:table-cell>
                    </fo:table-row>
                        <xsl:for-each select="Etudiants/Etudiant">
                            <xsl:variable name="total" />
                            <fo:table-row >
                                <fo:table-cell border="1pt solid black">
                                    <fo:block><xsl:value-of select="@id_etudiant"/> </fo:block>
                                </fo:table-cell>
                                <fo:table-cell border="1pt solid black" >
                                    <fo:block><xsl:value-of select="Nom"/>  </fo:block>
                                </fo:table-cell>
                                <fo:table-cell border="1pt solid black" >
                                    <fo:block><xsl:value-of select="Prenom"/>     </fo:block>
                                </fo:table-cell>
                                <xsl:for-each select="Module[Semestre=3]">

                                    <fo:table-cell border="1pt solid black" >
                                        <fo:block><xsl:value-of select="Matiere[1]/Note"/>     </fo:block>
                                        </fo:table-cell>
                                    <fo:table-cell border="1pt solid black">
                                        <fo:block> <xsl:value-of select="Matiere[last()]/Note"/> </fo:block>
                                        </fo:table-cell>
                                    <xsl:choose>
                                        <xsl:when test="Moyenne &gt; 8">
                                            <xsl:choose>
                                                <xsl:when test="Moyenne &gt; 12">
                                                    <xsl:choose>
                                                        <xsl:when test="Moyenne &gt; 14">
                                                            <xsl:choose>
                                                                <xsl:when test="Moyenne &gt; 16">
                                                                    <fo:table-cell border="1pt solid black" text-align="center" background-color="#33B2FF"><fo:block> <xsl:value-of select="Moyenne" /></fo:block></fo:table-cell>
                                                                </xsl:when>
                                                                <xsl:otherwise>
                                                                    <fo:table-cell border="1pt solid black" text-align="center" background-color="#33FF36"><fo:block> <xsl:value-of select="Moyenne" /></fo:block></fo:table-cell>
                                                                </xsl:otherwise>
                                                            </xsl:choose>
                                                        </xsl:when>
                                                        <xsl:otherwise>
                                                            <fo:table-cell border="1pt solid black" text-align='center' background-color="#FFF933"><fo:block> <xsl:value-of select="Moyenne" /></fo:block></fo:table-cell>
                                                        </xsl:otherwise>
                                                    </xsl:choose>
                                                </xsl:when>
                                                <xsl:otherwise>
                                                    <fo:table-cell  border="1pt solid black" text-align="center" background-color="#FFA233"> <fo:block><xsl:value-of select="Moyenne" /></fo:block></fo:table-cell>
                                                    </xsl:otherwise>
                                            </xsl:choose>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <fo:table-cell border="1pt solid black" text-align="center" background-color="#FF3333"><fo:block> <xsl:value-of select="Moyenne" /></fo:block></fo:table-cell>
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
                                                                <fo:table-cell border="1pt solid black" text-align="center" background-color="#33B2FF"> <fo:block><xsl:value-of select="MoyenneSemestre3" /></fo:block></fo:table-cell>
                                                            </xsl:when>
                                                            <xsl:otherwise>
                                                                <fo:table-cell border="1pt solid black" text-align="center" background-color="#33FF36"> <fo:block><xsl:value-of select="MoyenneSemestre3" /></fo:block></fo:table-cell>
                                                            </xsl:otherwise>
                                                        </xsl:choose>
                                                    </xsl:when>
                                                    <xsl:otherwise>
                                                        <fo:table-cell border="1pt solid black" text-align="center" background-color="#FFF933"><fo:block> <xsl:value-of select="MoyenneSemestre3" /></fo:block></fo:table-cell>
                                                    </xsl:otherwise>
                                                </xsl:choose>
                                            </xsl:when>
                                            <xsl:otherwise>
                                                <fo:table-cell border="1pt solid black" text-align="center" background-color="#FFA233"><fo:block> <xsl:value-of select="MoyenneSemestre3" /></fo:block></fo:table-cell>
                                            </xsl:otherwise>
                                        </xsl:choose>
                                    </xsl:when>
                                    <xsl:otherwise>
                                        <fo:table-cell border="1pt solid black" text-align="center" background-color="#FF3333"><fo:block> <xsl:value-of select="MoyenneSemestre3" /></fo:block></fo:table-cell>
                                    </xsl:otherwise>
                                </xsl:choose>
                            </fo:table-row>
                        </xsl:for-each>
       </fo:table-body>
                </fo:table>

</fo:block>
        </fo:flow>
    </fo:page-sequence>
</fo:root>
                </xsl:template>
</xsl:stylesheet>