# Gestion des Étudiants - Projet XML

Ce projet a pour objectif de gérer les étudiants de la classe GINF2, leurs notes pour les modules et leur emploi du temps. Il utilise XML, XSD, DTD, XSLT, XSL-FO, XQuery et le langage Python.

## Contenu du Projet

- [Introduction](#introduction)
- [Fichiers Excel](#fichiers-excel)
- [Fichiers XML](#fichiers-xml)
- [Transformations XSLT](#transformations-xslt)
- [Génération de PDF avec XSL-FO](#génération-de-pdf-avec-xsl-fo)
- [Requêtes XQuery](#requêtes-xquery)
- [Application Desktop avec Tkinter](#application-desktop-avec-tkinter)
- [Comment Contribuer](#comment-contribuer)
- [Licence](#licence)

## Introduction

Ce projet a été créé dans le cadre de la gestion des étudiants de la classe GINF2. Il utilise diverses technologies XML pour stocker, valider et présenter les données des étudiants.

## Fichiers Excel

Le projet utilise trois fichiers Excel pour stocker les informations sur les étudiants, les notes des modules et la liste des modules. Ces fichiers sont :
- `etudiants.xlsx` : Informations sur les étudiants (code, nom, prénom, sexe).
- `notes.xlsx` : Notes de toutes les matières pour chaque module et étudiant.
- `modules.xlsx` : Liste des modules avec leurs matières associées.
- `Emplois.xlsx` : L'emploi du temps.

## Fichiers XML

Les fichiers XML sont générés à partir des fichiers Excel à l'aide de scripts Python. Les fichiers XML résultants incluent :
- `etudiants.xml` : Informations sur les étudiants.
- `notes_modules.xml` : Notes des modules pour chaque étudiant.
- `modules.xml` : Liste des modules avec leurs matières.

## Transformations XSLT

Les fichiers XML sont transformés en fichiers HTML à l'aide de XSLT pour générer des relevés de notes, des cartes d'étudiants, des attestations de scolarité, et des emplois du temps.

## Génération de PDF avec XSL-FO

Les fichiers XML sont également transformés en fichiers XSL-FO pour la génération de fichiers PDF. Ces fichiers PDF incluent des versions formatées des relevés de notes, cartes d'étudiants et attestations de scolarité.

## Requêtes XQuery

Des requêtes XQuery sont utilisées pour extraire des informations spécifiques des fichiers XML, facilitant ainsi l'accès à des données précises.

## Application Desktop avec Tkinter

Une application desktop a été développée en utilisant Tkinter en Python. L'application offre une interface utilisateur pour rechercher et afficher les emplois du temps, les attestations de scolarité et les relevés de notes des étudiants.



