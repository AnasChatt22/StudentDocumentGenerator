declare variable $idEtudiant external;

<html>
   <head>
        <link rel="stylesheet" type="text/css" href="../FichiersXML/CSS/releve_personnel.css" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
   </head>
   <body>
      <div class="top-box">
        <div style="width:99%;margin:auto;margin-top:5px;display:flex;flex-direction:row;align-items:center;justify-content: space-between;">
            <h1>Université Abdelmalek Essaadi</h1>
            <h1>جامعة عبدالمالك السعدي</h1>
        </div>
        <div style="width:100%">
             <h2 style="margin:auto;display:block;font-weight:200">Année universitaire 2023/2024  السنة الجامعية</h2>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;text-align :center;">
        <div style="width:99%;margin:auto;margin-top:5px;display:flex;flex-direction:row;align-items:center;justify-content: space-between;">
            <h2>Ecole Nationale Des Sciences Appliquées de Tanger</h2>
            <h2>المدرسة الوطنية للعلوم التطبيقية طنجة</h2>
        </div>
        <div style="width:60%;border:2px solid black;text-align:center;display:block;margin:auto;background-color:#808080;">
             <h1 style="display:inline-block;padding:6px 38px; font-size:24px;">RELEVE DE NOTES ET RESULTATS</h1>
        </div>
        <div style="width:60%;border:2px solid black;text-align:center;display:block;margin:auto;background-color:#808080;margin-top: 15px;">
             <h1 style="display:inline-block;padding:0px 88px; font-size:18px;">Session 1</h1>
        </div>
      </div>


     { for $Etudiant in doc("../XML/GINF2.xml")//Etudiant
      where $Etudiant/@id_etudiant = $idEtudiant
      return
      <div>
           <div style="display:flex;flex-direction:column;text-align :left;">
             <div style="width:99%;margin:auto;margin-top:5px;display:flex;flex-direction:row;align-items:center;justify-content: space-between;">
                 <h2>{$Etudiant/Nom} {$Etudiant/Prenom}</h2>
             </div>
             <div style="width:99%;margin:auto;margin-top:5px;display:flex;flex-direction:row;text-align:left;justify-content: space-between;">
                 <h2 style="font-weight:200">N°Etudiant : {$Etudiant/@id_etudiant/string()}</h2>
             </div>
             <div style="width:99%;margin:auto;margin-top:5px;display:flex;flex-direction:row;text-align:left;justify-content: space-between;">
                 <h2 style="font-weight:200">Né le  : { $Etudiant/@date_naissance/string()}</h2>
             </div>
           </div>
           <table border="1" style="width:100%;border:1px solid black;border-collapse:collapse">
           <tr >
            <th>Modules</th>
            <th>Note/Barème</th>
            <th>Session</th>
            <th>Points Jury</th>
            </tr>
            { for $module in $Etudiant//Module
              return
              <tr >
                  <td style="max-width:200px;">{$module/@id_module/string()} :
                  { for $matiere in $module//Matiere
                     return <span>{$matiere/Designation},</span>
                   }
                  </td>
                  <td style="text-align:center">{$module/Moyenne}/20</td>
                  <td style="text-align:center">S{$module/Semestre} 2023/2024</td>
                  <td style="text-align:center"></td>
              </tr>
            }
                  {
                     let $moy := sum($Etudiant/Module/Moyenne) div count($Etudiant//Module)
                     return
                    <tr style="border: 0px">
                     <td style="max-width:200px;font-weight:600">Resultat d'admission S{$Etudiant/Module[1]/Semestre}</td>
                     <td style="text-align:center;font-weight:600">
                     <span>{fn:format-number($moy,'0.00')}</span>
                     </td>
                     {if ($moy >= 12)
                      then
                     <td style="text-align:center;font-weight:600">ADMIS</td>
                      else
                     <td style="text-align:center;font-weight:600">REFUSE</td>
                     }
                     {if ($moy >= 12)
                      then
                        if ($moy >= 14 )
                        then
                          if ($moy >= 16 )
                          then
                              <td style="text-align:center;font-weight:600">Très Bien</td>
                          else
                            <td style="text-align:center;font-weight:600">Bien</td>
                        else
                          <td style="text-align:center;font-weight:600">Passable</td>
                      else
                      <td style="text-align:center;font-weight:600"></td>
                     }
                    </tr>
                  }

           </table>
        </div>
       }
       <div style="margin-top:100px;margin-bottom:10px;">
       <h2>Fait à Tanger le
       {let $currentDay := day-from-date(current-date())
            return <span>{ day-from-date(current-date())}/{ month-from-date(current-date())}/{ year-from-date(current-date())}</span>
        }
        </h2>
        <h2>Le Directeur de l'Ecole Nationale Des Sciences Appliquées de Tanger</h2>
       </div>

    </body>
</html>
