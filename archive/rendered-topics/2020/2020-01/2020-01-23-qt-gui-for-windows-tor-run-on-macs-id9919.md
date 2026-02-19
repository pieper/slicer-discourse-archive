---
topic_id: 9919
title: "Qt Gui For Windows Tor Run On Macs"
date: 2020-01-23
url: https://discourse.slicer.org/t/9919
---

# Qt GUI for windows tor run on macs

**Topic ID**: 9919
**Date**: 2020-01-23
**URL**: https://discourse.slicer.org/t/qt-gui-for-windows-tor-run-on-macs/9919

---

## Post #1 by @Fabi-LiU (2020-01-23 10:10 UTC)

<p>Operating system:Windows 10<br>
Slicer version: 4.10.1<br>
Expected behavior: GUI to run also in MAC<br>
Actual behavior:GUI runs in windows</p>
<p>Hello,<br>
I created a GUI using Qt (e.g. to make different windows and push-buttons) and a python code to run these Qt files. I added it to slicer as an extension (following the instructions in “Developing and contributing extensions for 3D Slicer”). I also had to modify a bit some files from slicer (within bin for instance launchersettings and application executable). It runs nicely in my computer but I would like others to use it.<br>
What it does is basically to provide the user with an interface where she(he) can select files that contain “mrmls” which the user can explore further.<br>
I imagined that by changing the 3Dslicer configuration on each user computer (and adding the python script)it would work but it didn’t (I’m still checking if I didn’t skip any file), specially on macs. Do  you recommend another way to provide a QT made GUI? or even change the way to do the GUI itself?</p>
<p>Thanks in advance!<br>
Fabiola</p>

---

## Post #2 by @lassoan (2020-01-23 10:51 UTC)

<p>See how to implement custom applications or slicelets <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">here</a>. Does this example work on your computer?</p>

---
