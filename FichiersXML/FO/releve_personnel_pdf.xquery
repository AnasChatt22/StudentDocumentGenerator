declare variable $idEtudiant external;

<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
      <fo:layout-master-set>
        <fo:simple-page-master master-name="A4" page-height="29.7cm" page-width="21cm" margin-top="2cm" margin-bottom="2cm" margin-left="1cm" margin-right="1cm">
          <fo:region-body/>
        </fo:simple-page-master>
      </fo:layout-master-set>
      <fo:page-sequence master-reference="A4">
        <fo:flow flow-name="xsl-region-body">
          <fo:block font-family="Helvetica, Arial, sans-serif" font-size="8pt">
            <fo:block-container border="1px solid black" text-align='center' padding="10px 0px">
              <fo:block >
                <fo:inline font-weight="bold" text-align="center">Université Abdelmalek Essaadi</fo:inline>
              </fo:block>
              <fo:block font-weight="200">Année universitaire 2023/2024 </fo:block>
            </fo:block-container>
            <fo:block-container text-align="center">
              <fo:block margin="12px auto" text-align="center">
                <fo:inline font-weight="bold" text-align="center">Ecole Nationale Des Sciences Appliquées de Tanger</fo:inline>
              </fo:block>
              <fo:block-container border="2px solid black" width="80%"  margin="0px 10%" text-align="center" background-color="#808080">
                <fo:block font-size="18pt" padding="6px 28px">RELEVE DE NOTES ET RESULTATS</fo:block>
              </fo:block-container>
              <fo:block-container border="2px solid black" width="60%" margin="0px 20%" text-align="center" background-color="#808080" margin-top="15px">
                <fo:block font-size="16pt" padding="0px 18px">Session 1</fo:block>
              </fo:block-container>
            </fo:block-container>

<fo:block-container width="100%">

    {
      for $etudiant in doc("../XML/GINF2.xml")//Etudiant[@id_etudiant = $idEtudiant]
      return
      <fo:block margin-top='20px' width="100%">
        <fo:inline font-weight="600" width="100%">{string($etudiant/Nom)}&#160;{string($etudiant/Prenom)}</fo:inline>
        <fo:block margin-top='10px'><fo:inline>N° Etudiant : </fo:inline><fo:inline>{string($etudiant/@id_etudiant)}</fo:inline></fo:block>
        <fo:block margin-top='10px' margin-bottom='20px'><fo:inline>Né le  : </fo:inline><fo:inline>{string($etudiant/@date_naissance)}</fo:inline></fo:block>

        <fo:table  width=" 100%"  border="1px solid black" border-collapse="collapse" text-align="center">
        <fo:table-column border="1px solid black" column-number="1"  />
        <fo:table-column border="1px solid black" column-number="2"  />
        <fo:table-column border="1px solid black" column-number="3"  />
        <fo:table-column border="1px solid black" column-number="4"  />

           <fo:table-header background-color="#cce">
            <fo:table-row>
              <fo:table-cell padding="6px"><fo:block>Modules</fo:block></fo:table-cell>
              <fo:table-cell padding="6px"><fo:block>Note/Barème</fo:block></fo:table-cell>
              <fo:table-cell padding="6px"><fo:block>Session</fo:block></fo:table-cell>
              <fo:table-cell padding="6px"><fo:block>Pts Jury</fo:block></fo:table-cell>
            </fo:table-row>
           </fo:table-header>
            <fo:table-body>

          {
            for $module in $etudiant//Module
            return
            <fo:table-row border="1px solid black">
              <fo:table-cell text-align="left" padding="6px" ><fo:block>{string($module/@id_module)} : {string($module/Designation)}</fo:block></fo:table-cell>
              <fo:table-cell padding="6px"><fo:block>{string($module/Moyenne)}/20</fo:block></fo:table-cell>
              <fo:table-cell padding="6px"><fo:block>S{string($module/Semestre)} 2023/2024</fo:block></fo:table-cell>
              <fo:table-cell padding="6px" ><fo:block>-</fo:block></fo:table-cell>
            </fo:table-row>
          }
          {
            let $moy := sum($etudiant/Module/Moyenne) div count($etudiant//Module)
            return
            <fo:table-row font-weight="600">
                <fo:table-cell padding="6px">
                    <fo:block>Resultat d'admission</fo:block>
                </fo:table-cell>
                <fo:table-cell padding="6px">
                    <fo:block>{format-number($moy, '0.00')}</fo:block>
                </fo:table-cell>
                <fo:table-cell padding="6px" background-color="{if ($moy >= 16) then '#33B2FF' else
                                                 if ($moy >= 14) then '#33FF36' else
                                                 if ($moy >= 12) then '#FFF933' else
                                                 '#FF3333'}">
                    <fo:block>
                        {if ($moy >= 12) then 'ADMIS' else 'REFUSE'}
                    </fo:block>
                </fo:table-cell>
            </fo:table-row>
            }
          </fo:table-body>
        </fo:table>
        </fo:block>
    }

      </fo:block-container>
    <fo:block-container margin-top="40px" font-weight="600" width="100%">
    <fo:block>
      <fo:inline>Fait à Tanger le </fo:inline>
        {
          let $currentDay := day-from-date(current-date())
          return <fo:inline>{day-from-date(current-date())}/{month-from-date(current-date())}/{year-from-date(current-date())}</fo:inline>
        }

      </fo:block>
      <fo:block>Le Directeur de l'Ecole Nationale Des Sciences Appliquées de Tanger</fo:block>
    </fo:block-container>
</fo:block>
</fo:flow>
</fo:page-sequence>
</fo:root>
