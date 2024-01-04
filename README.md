## Student Management - XML Project

This project aims to manage the students of the GINF2 class, their grades for modules, and their schedule. It utilizes XML, XSD, DTD, XSLT, XSL-FO, XQuery, and the Python language.

## Project Contents

- [Introduction](#introduction)
- [Excel Files](#excel-files)
- [XML Files](#xml-files)
- [XSLT Transformations](#xslt-transformations)
- [PDF Generation with XSL-FO](#pdf-generation-with-xsl-fo)
- [XQuery Queries](#xquery-queries)
- [Desktop Application with Tkinter](#desktop-application-with-tkinter)

## Introduction

This project was created for the management of GINF2 class students. It employs various XML technologies to store, validate, and present student data.

## Excel Files

The project uses three Excel files to store information about students, module grades, and the list of modules. These files are:
- `students.xlsx`: Information about students (code, name, surname, gender).
- `modules.xlsx`: List of modules with their associated subjects and responsables.
- `Emploi.xlsx`: Time Schedule.

## XML Files

XML files are generated from Excel files using Python scripts. The resulting XML files include:
- `students.xml`: Data about students and subjects for each module.
- `Emploi.xml`: Time Schedule Data.

## XSLT Transformations

XML files are transformed into HTML files using XSLT to generate grade reports, student cards, certificates of enrollment, and schedules.

## PDF Generation with HTML, XSL-FO, XSLT and XQuery

XML files are also transformed into XSL-FO files for PDF file generation. These PDF files include formatted versions of grade reports, student cards, and certificates of enrollment.


## Desktop Application with CustomTkinter

A desktop application has been developed using CustomTkinter in Python. The application provides a user interface to search and display schedules, certificates of enrollment, and grade reports for students.
