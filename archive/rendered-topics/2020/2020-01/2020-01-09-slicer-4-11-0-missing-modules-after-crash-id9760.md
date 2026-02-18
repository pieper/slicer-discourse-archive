# Slicer 4.11.0 missing modules after crash

**Topic ID**: 9760
**Date**: 2020-01-09
**URL**: https://discourse.slicer.org/t/slicer-4-11-0-missing-modules-after-crash/9760

---

## Post #1 by @Camiel (2020-01-09 15:19 UTC)

<p>Hello,</p>
<p>I have been using Slicer for a while with great success. However, yesterday, my computer crashed while i was running Slicer together with some other programs. When i tried to reload Slicer, i noticed several modules missing in the modules list. I also noticed aproximately 50 critical errors in the log.<br>
I have little knowledge about software debugging so i have no idea where to start or what information to provide…</p>
<p>Slicer version: 4.11.0-2019-06-14 r28295<br>
Windows 10 x64<br>
Some of the error messages:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘getSlicerRCFileName’ is not defined</p>
<p>Traceback (most recent call last):<br>
File “E:/Camiel/Uni/Stage II - OCON/Programma’s/Slicer/Slicer 4.11.0-2019-06-14/bin/…/lib/Slicer-4.11/qt-scripted-modules/CompareVolumes.py”, line 25, in <strong>init</strong><br>
“”").substitute({ ‘a’:parent.slicerWikiUrl, ‘b’:slicer.app.majorVersion, ‘c’:slicer.app.minorVersion })<br>
AttributeError: module ‘slicer’ has no attribute ‘app’</p>
<p>qSlicerPythonCppAPI::instantiateClass  - [ “CompareVolumes” ] - Failed to instantiate scripted pythonqt class “CompareVolumes” 0x1958c278398<br>
Fail to instantiate module  “CompareVolumes”</p>
<p>Traceback (most recent call last):<br>
File “E:/Camiel/Uni/Stage II - OCON/Programma’s/Slicer/Slicer 4.11.0-2019-06-14/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOM.py”, line 34, in <strong>init</strong><br>
self.parent.helpText += self.getDefaultModuleDocumentationLink()<br>
File “E:\Camiel\Uni\Stage II - OCON\Programma’s\Slicer\Slicer 4.11.0-2019-06-14\bin\Python\slicer\ScriptedLoadableModule.py”, line 52, in getDefaultModuleDocumentationLink<br>
self.parent.slicerWikiUrl, slicer.app.majorVersion, slicer.app.minorVersion, docPage)<br>
AttributeError: module ‘slicer’ has no attribute ‘app’</p>
<p>qSlicerPythonCppAPI::instantiateClass  - [ “DICOM” ] - Failed to instantiate scripted pythonqt class “DICOM” 0x1958c27cd58<br>
Fail to instantiate module  “DICOM”</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “E:\Camiel\Uni\Stage II - OCON\Programma’s\Slicer\Slicer 4.11.0-2019-06-14\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “E:/Camiel/Uni/Stage II - OCON/Programma’s/Slicer/Slicer 4.11.0-2019-06-14/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMPatcher.py”, line 3, in <br>
from <strong>main</strong> import vtk, qt, ctk, slicer<br>
ImportError: cannot import name ‘vtk’</p>
<p>Can anyone help me repair my Slicer? I read somewhere that reinstalling Slicer wont fix this since some files must be deleted or replaced or whatsoever?</p>
<p>Thanks in advance!</p>
<p>Camiel</p>

---

## Post #2 by @pieper (2020-01-09 15:41 UTC)

<p>It looks like your disk got corrupted.  Probably need to run some repair tool.  Yes, reinstalling Slicer is a good idea too.</p>

---

## Post #3 by @Camiel (2020-01-13 08:47 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Thanks for the reaction.</p>
<p>I have tried running repair tools but those didn’t find any corupted or broken files. I have also tried reinstalling Slicer. i have tried reinstaling the same version and also the most recent version. those, however, both showed the same problems.</p>
<p>Do you have any other suggestions?</p>
<p>Thanks in advance!</p>

---

## Post #4 by @pieper (2020-01-13 16:32 UTC)

<p>Ah, it looks like you installed Slicer in a directory with spaces and an apostrophe - that is probably the issue.</p>
<p><code>E:/Camiel/Uni/Stage II - OCON/Programma’s/</code></p>
<p>When you run the installer can you pick a place like <code>e:\slicer</code> or similar?</p>

---

## Post #5 by @lassoan (2020-01-13 19:20 UTC)

<p>Good catch - special characters in the path is a likely root cause of the issue. There are some more application startup troubleshooting instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Debugging_Slicer_application_startup_issues">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Debugging_Slicer_application_startup_issues</a></p>

---

## Post #6 by @Camiel (2020-01-14 07:45 UTC)

<p>Changing the install folder indeed solved the issue!<br>
Thanks for the help!</p>

---
