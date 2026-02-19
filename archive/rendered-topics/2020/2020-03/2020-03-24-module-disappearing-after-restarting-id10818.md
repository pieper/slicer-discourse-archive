---
topic_id: 10818
title: "Module Disappearing After Restarting"
date: 2020-03-24
url: https://discourse.slicer.org/t/10818
---

# Module disappearing after restarting

**Topic ID**: 10818
**Date**: 2020-03-24
**URL**: https://discourse.slicer.org/t/module-disappearing-after-restarting/10818

---

## Post #1 by @Queen_Rei (2020-03-24 19:48 UTC)

<p>Howdy~</p>
<p><strong>I have run into an issue where when I add these lines of code:</strong></p>
<p>loadedVolumeNode = slicer.util.loadVolume(‘Z:/Something/LumbarCT’, {}, returnNode=True)<br>
vol=slicer.util.getNode(‘Lumbar*’)<br>
vol.GetImageData().GetDimensions()</p>
<p><strong>then my module stops updating and then when I restart it gives me the following error:</strong><br>
Traceback (most recent call last):<br>
File “Z:/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/ExtensionWizard.py”, line 273, in selectExtension<br>
xd = SlicerWizard.ExtensionDescription(sourcedir=path)<br>
File “Z:\Slicer 4.10.2\bin\Python\SlicerWizard\ExtensionDescription.py”, line 136, in <strong>init</strong><br>
self._setProjectAttribute(“homepage”, p, required=True)<br>
File “Z:\Slicer 4.10.2\bin\Python\SlicerWizard\ExtensionDescription.py”, line 183, in <em>setProjectAttribute<br>
v = project.getValue("EXTENSION</em>" + name.upper(), default, substitute)<br>
File “Z:\Slicer 4.10.2\bin\Python\SlicerWizard\ExtensionProject.py”, line 280, in getValue<br>
raise KeyError(“script does not set %r” % name)<br>
KeyError: “script does not set ‘EXTENSION_HOMEPAGE’”</p>
<p>My ultimate goal is to import a DICOM from a file on my PC, segment it automatically, then export it onto a file on my PC. This is the importing part of this ultimate goal.</p>
<p>Thank you advance! Always a pleasure to learn more~</p>

---

## Post #2 by @lassoan (2020-03-24 20:07 UTC)

<p>You only need to use the ExtensionWizard once, to create your module. Once your module is created, you can update it by clicking on “Reload” button in Reload&amp;Test section of the module GUI.</p>
<p>If your module does not show up in the module list then add its path to additional module paths in menu: Edit / Application settings / Modules.</p>

---

## Post #3 by @Queen_Rei (2020-03-24 21:15 UTC)

<p>I have been doing that as well. When I comment out the lines of code I outlined above for importing, the module reappears.</p>
<p><strong>When I uncomment it, then I get the following error and module disappears on restart</strong><br>
Traceback (most recent call last):<br>
File “Z:\Slicer 4.10.2\bin\Python\slicer\ScriptedLoadableModule.py”, line 195, in onReload<br>
slicer.util.reloadScriptedModule(self.moduleName)<br>
File “Z:\Slicer 4.10.2\bin\Python\slicer\util.py”, line 623, in reloadScriptedModule<br>
moduleName, fp, filePath, (’.py’, ‘r’, imp.PY_SOURCE))<br>
File “Z:/LoadSegMod/DicomTesting/SegmentDicom/SegmentDicom.py”, line 158<br>
vol = slicer.util.getNode(‘Lumbar*’)<br>
^<br>
IndentationError: unindent does not match any outer indentation level</p>

---

## Post #4 by @lassoan (2020-03-24 22:32 UTC)

<p>Python failed to parse your file due to an indentation error. You need to pay very close attention to correct indentation when developing in Python - you must not mix spaces and tabs for indentation, and all lines in the same block must have the same number of leading spaces or tabs.</p>

---
