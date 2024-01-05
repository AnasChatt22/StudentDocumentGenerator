declare variable $idEtudiant external;
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
      <fo:layout-master-set>
        <fo:simple-page-master master-name="A4" page-height="29.7cm" page-width="21cm" margin-top="2cm" margin-bottom="2cm" margin-left="1cm" margin-right="1cm">
          <fo:region-body/>
        </fo:simple-page-master>
      </fo:layout-master-set>
      <fo:page-sequence master-reference="A4">
        <fo:flow flow-name="xsl-region-body">

        <fo:block  font-size="8pt">
           <fo:block-container  width="99%" margin="auto" margin-top="5px" >
            <fo:block>
               <fo:inline padding-right="235px">Université Abdelmalek Essaadi</fo:inline>
               <fo:inline >Ecole Nationale Des Sciences Appliquées de Tanger</fo:inline>
            </fo:block>

             <fo:block text-align="center" margin-top="15px" >
                 <fo:inline >Service des Affaires Estudiantines</fo:inline>
             </fo:block>
          </fo:block-container>


        <fo:block width="99%">

            <fo:block width="60%" text-align="center" margin="auto" margin-top="30px">
              <fo:block padding="6px 38px" font-size="24px" text-decoration="underline">ATTESTATION DE SCOLARITE</fo:block>
            </fo:block>
          {
            for $Etudiant in doc("../XML/GINF2.xml")//Etudiant
            where $Etudiant/@id_etudiant = $idEtudiant
            return
              <fo:block-container>
              <fo:block >
             <fo:block >
                 <fo:block margin-top="20px" font-weight='600'>Le Directeur de l'Ecole Nationale des Sciences Appliquées de Tanger atteste que l'étudiant: </fo:block>
             </fo:block>
             <fo:block >
                <fo:block font-weight='600' margin-top="20px">{string($Etudiant/Nom)} &#160; {string($Etudiant/Prenom)}</fo:block>
             </fo:block>
             <fo:block margin-top="20px">
                <fo:inline >Numéro de la carte nationale d'étudiant :  </fo:inline ><fo:inline >{$idEtudiant}</fo:inline>
             </fo:block>
             <fo:block margin-top="20px">
                <fo:inline >né le  :  </fo:inline ><fo:inline font-weight='600' >{string($Etudiant/@date_naissance)}</fo:inline>
             </fo:block>
             <fo:block >
                <fo:block margin-top="20px" >Poursuit ses études à l'école Nationale des Sciences Appliquées de Tanger pour l'année universitaire 2023/2024 .</fo:block>
             </fo:block>
             <fo:block  margin-top="20px" >
                <fo:inline text-decoration="underline">Diplome  :  </fo:inline ><fo:inline >Génie Informatique </fo:inline>
             </fo:block>
             <fo:block margin-top="20px" >
                <fo:inline text-decoration="underline">Filière  :  </fo:inline ><fo:inline >Génie Informatique </fo:inline>
             </fo:block>
             <fo:block margin-top="20px">
                <fo:inline text-decoration="underline">Année  :  </fo:inline ><fo:inline >2° Année Génie Informatique </fo:inline>
             </fo:block>
           </fo:block>

        </fo:block-container>
          }

          <fo:block margin-top="20px" text-align="right" font-weight="600" margin-bottom="100px">
            <fo:block><fo:inline>Fait à Tanger le </fo:inline>
              {
                let $currentDay := day-from-date(current-date())
                return <fo:inline>{ day-from-date(current-date())}/{ month-from-date(current-date())}/{ year-from-date(current-date())}</fo:inline>
              }
            </fo:block>
            <fo:block>Le Directeur </fo:block>
          </fo:block>

          <fo:block >
            <fo:block  width="100%" text-align="left">
                <fo:inline><fo:leader leader-pattern="rule" padding="-45%" margin="-45%" rule-style="solid" rule-thickness="1pt" width="100%"/></fo:inline>
            </fo:block>
            <fo:block >
              <fo:block >
                <fo:block >
                  <fo:inline margin-top="10px" >Adresse  :  </fo:inline ><fo:inline >B.P 416 Tanger Principale, Tanger, Maroc </fo:inline>
                </fo:block>
                <fo:block margin-left="60px" margin-top="10px" >(MAROC) Site : ensat.ac.ma</fo:block>
                <fo:block margin-left="60px"  margin-top="10px"  margin-bottom="10px">Téléphone : (+212) 539393744</fo:block>
              </fo:block>
            </fo:block>
            <fo:block  width="100%" text-align="left">
                <fo:inline><fo:leader leader-pattern="rule" padding="-45%" margin="-45%" rule-style="solid" rule-thickness="1pt" width="100%"/></fo:inline>
            </fo:block>
            <fo:block width="60%" margin="10px 20%">
              <fo:block>Le présent document n'est délivré qu'en un seul exemplaire.</fo:block>
              <fo:block >Il appartient à l'étudiant d'en faire des photocopies certifiées conformes.</fo:block>
            </fo:block>
          </fo:block>
          </fo:block>
          </fo:block>
        </fo:flow>
      </fo:page-sequence>
</fo:root>
