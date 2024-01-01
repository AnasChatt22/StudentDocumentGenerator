declare variable $idEtudiant external;

<html>
   <head>

         <link rel="stylesheet" type="text/css" href="attestation.css" />
   </head>
   <body>
      <div class="top-box">
        <div style="width:99%;margin:auto;margin-top:5px;display:flex;flex-direction:row;align-items:center;justify-content: space-between;">
           <div style="text-align:left">
             <h2>Université Abdelmalek Essaadi</h2>
             <h2>Ecole Nationale Des Sciences Appliquées de Tanger</h2>
             <h2 style="text-decoration:underline">service des Affaires Estudiantines</h2>
             </div>
             <img src='logoensat.png' height='70px' width='100px'></img>
             <div style="text-align:right">
            <h2>المدرسة الوطنية للعلوم التطبيقية طنجة</h2>
            <h2>جامعة عبدالمالك السعدي</h2>
            <h2 style="text-decoration:underline">مصلحة الشؤون الطلابية</h2>
            </div>
        </div>

      </div>
      <div style="display:flex;flex-direction:column;text-align :center;">
        <div style="width:60%;text-align:center;display:block;margin:auto;">
             <h1 style="display:inline-block;padding:6px 38px; font-size:24px;text-decoration:underline">ATTESTATION DE SCOLARITE</h1>
        </div>
      </div>


     { for $Etudiant in doc("GINF2.xml")//Etudiant
      where $Etudiant/@id_etudiant = $idEtudiant
      return
      <div>
           <div style="display:flex;flex-direction:column;text-align :left;">
             <div style="width:99%;margin-left:10px;margin-top:5px;display:flex;flex-direction:row;align-items:center;justify-content: space-between;">
                 <h2>Le Directeur de l'Ecole Nationale des Sciences Appliquées de Tanger atteste que l'étudiant: </h2>
             </div>
             <div style="margin-left:10px;text-align:left;margin-top:5px;display:flex ; flex-direction:row ;align-items:center">
                <h2 style="font-weight:200">Monsieur </h2 ><h2 style="font-weight:600;padding-left:15px">{$Etudiant/Nom} {$Etudiant/Prenom}</h2>
             </div>
             <div style="margin-left:10px;text-align:left;margin-top:5px;display:flex ; flex-direction:row ;align-items:center">
                <h2 style="font-weight:200">Numéro de la carte nationale d'étudiant :  </h2 ><h2 style="font-weight:600;padding-left:15px">{$idEtudiant}</h2>
             </div>
             <div style="margin-left:10px;text-align:left;margin-top:5px;display:flex ; flex-direction:row ;align-items:center">
                <h2 style="font-weight:200">né le  :  </h2 ><h2 style="font-weight:600;padding-left:15px">{string($Etudiant/@date_naissance)}</h2>
             </div>
             <div style="margin-left:10px;text-align:left;margin-top:5px;display:flex ; flex-direction:row ;align-items:center">
                <h2 style="font-weight:200">Poursuit ses études à l'école Nationale des Sciences Appliquées de Tanger pour l'année universitaire 2023/2024 .</h2>
             </div>
             <div style="margin-left:10px;text-align:left;margin-top:5px;display:flex ; flex-direction:row ;align-items:center">
                <h2 style="font-weight:200;text-decoration:underline">Diplome  :  </h2 ><h2 style="font-weight:400;padding-left:15px">Génie Informatique </h2>
             </div>
             <div style="margin-left:10px;text-align:left;margin-top:5px;display:flex ; flex-direction:row ;align-items:center">
                <h2 style="font-weight:200;text-decoration:underline">Filière  :  </h2 ><h2 style="font-weight:400;padding-left:15px">Génie Informatique </h2>
             </div>
             <div style="margin-left:10px;text-align:left;margin-top:5px;display:flex ; flex-direction:row ;align-items:center">
                <h2 style="font-weight:200;text-decoration:underline">Année  :  </h2 ><h2 style="font-weight:400;padding-left:15px">2° Année Génie Informatique </h2>
             </div>
           </div>

        </div>
       }
       <div style="margin-top:10px;text-align:center;float:right">
       <h2>Fait à Tanger le
       {let $currentDay := day-from-date(current-date())
            return <span>{ day-from-date(current-date())}/{ month-from-date(current-date())}/{ year-from-date(current-date())}</span>
        }
        </h2>
        <h2>Le Directeur </h2>
       </div>

       <div style="margin-top:50px;text-align:right;float:right;width:100%">
       <hr/>
       <div style="width:99%;margin:auto;margin-top:5px;display:flex;flex-direction:row;align-items:center;justify-content: space-between;">
           <div style="text-align:left">
             <div style="text-align:left;margin-top:5px;display:flex ; flex-direction:row ;align-items:center">
             <h2 style="font-weight:200;text-decoration:underline">Adresse  :  </h2 ><h2 style="font-weight:400;padding-left:5px">B.P 416 Tanger Principale, Tanger, Maroc </h2>
             </div>
             <h2 style='margin-left:30px;font-weight:200'>(MAROC) Site : ensat.ac.ma</h2>
             <h2 style='margin-left:30px;font-weight:200'>Téléphone : (+212) 539393744</h2>
             </div>

        </div>
        <hr/>
        <div style="display:flex;flex-direction:column;text-align :center;margin:0 auto;margin-bottom:40px;">
             <h2 style="display:inline-block; ">Le présent document n'est déliveré qu'en un seul exemplaire .</h2>
             <h2 style="display:inline-block; ">Il appartient à l'étudiant d'en faire des photocopies certifiées conformes.</h2>

      </div>
       </div>

    </body>
</html>
