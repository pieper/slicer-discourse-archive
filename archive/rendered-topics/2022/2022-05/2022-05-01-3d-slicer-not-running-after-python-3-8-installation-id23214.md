# 3D Slicer not running after Python 3.8 installation

**Topic ID**: 23214
**Date**: 2022-05-01
**URL**: https://discourse.slicer.org/t/3d-slicer-not-running-after-python-3-8-installation/23214

---

## Post #1 by @NiinaIn3D (2022-05-01 08:36 UTC)

<p>Hi everyone, couple of days ago I had a program installed which required also installing Python 3.8. After this 3D Slicer will no longer run. Any ideas what I could do to fix the issue? From end user perspective I have about zero idea of Python, so if you know a fix please be patient, might take me a bit to get it done.</p>
<p>I’m running the latest stable version of 3D Slicer in Windows 10. For an added bonus it’s a university asset so I don’t have admin rights to the device.</p>
<p>Thanks,</p>
<p>Niina</p>

---

## Post #2 by @pieper (2022-05-02 16:45 UTC)

<p>Slicer’s environment is self-contained and should be robust against changes made to the rest of the system.  What was the other software?</p>
<p>You don’t need admin rights to install Slicer, just pick a directory where you have permission and you should be good to go.  Try a fresh install and see what happens.</p>

---

## Post #3 by @NiinaIn3D (2022-05-03 06:34 UTC)

<p>Thanks for the reply.</p>
<p>The other software is called Drishti <a href="https://github.com/nci/drishti" rel="noopener nofollow ugc">https://github.com/nci/drishti</a>, it’s an open source 3D visualisation software. To use one of its packages IT had to install the latest version of Python (3.8), after this 3D Slicer stopped working. Does anyone know why this might be happening?</p>
<p>To see if I can install 3D Slicer with my current user rights I downloaded the latest preview release, and put the .exe file on the Desktop. When running the file I get an error message saying the app has been blocked by system admin.</p>

---

## Post #4 by @pieper (2022-05-03 12:35 UTC)

<p>Installing different python versions or other software would not normally break slicer, but it sounds like your computer is locked down in in ways that interfere with normal operation.  Perhaps someone who works in a similar environment can offer some suggestions.</p>

---
