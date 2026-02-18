# Problem with Slicer built in release mode on Windows

**Topic ID**: 23534
**Date**: 2022-05-23
**URL**: https://discourse.slicer.org/t/problem-with-slicer-built-in-release-mode-on-windows/23534

---

## Post #1 by @olevs (2022-05-23 12:29 UTC)

<p>Hi,<br>
Building Slicer in release mode with Visual Studio Community 2022 (Qt 5.15.2) gives some errors when trying to run the application. I’ve tested this with the 5.0.2 Slicer git tag.</p>
<p>Starting Slicer gives the following output:<br>
Switch to module:  “Welcome”<br>
“QFormBuilder was unable to create a custom widget of the class ‘ctkCollapsibleButton’; defaulting to base class ‘QWidget’.”<br>
“QFormBuilder was unable to create a custom widget of the class ‘ctkCollapsibleGroupBox’; defaulting to base class ‘QGroupBox’.”<br>
“QFormBuilder was unable to create a custom widget of the class ‘ctkCollapsibleGroupBox’; defaulting to base class ‘QGroupBox’.”<br>
“QFormBuilder was unable to create a custom widget of the class ‘ctkCollapsibleGroupBox’; defaulting to base class ‘QGroupBox’.”</p>
<p>And trying to open a module like “Add DICOM Data” gives:<br>
“QFormBuilder was unable to create a custom widget of the class ‘qMRMLSubjectHierarchyTreeView’; defaulting to base class ‘QTreeView’.”<br>
“QFormBuilder was unable to create a custom widget of the class ‘ctkCollapsibleButton’; defaulting to base class ‘QWidget’.”<br>
“QFormBuilder was unable to create a custom widget of the class ‘ctkCollapsibleButton’; defaulting to base class ‘QWidget’.”<br>
“QFormBuilder was unable to create a custom widget of the class ‘ctkDirectoryButton’; defaulting to base class ‘QWidget’.”<br>
“QFormBuilder was unable to create a custom widget of the class ‘ctkCollapsibleButton’; defaulting to base class ‘QWidget’.”<br>
Database folder does not contain ctkDICOM.sql file: C:/Users/olevs/Documents/SlicerDICOMDatabase<br>
Traceback (most recent call last):<br>
File “D:/d/S-release-22/Slicer-build/lib/Slicer-5.0/qt-scripted-modules/DICOM.py”, line 608, in setup<br>
self.ui.subjectHierarchyTree.setMRMLScene(slicer.mrmlScene)<br>
AttributeError: QTreeView has no attribute named ‘setMRMLScene’</p>

---

## Post #2 by @olevs (2022-05-24 11:07 UTC)

<p>Building the same code in release mode with Visual Studio Professional 2019 seems to work ok, but requires Visual Studio to be updated with the latest patches.</p>

---
