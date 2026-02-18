# Unable to install Slicer in c:\Program Files

**Topic ID**: 18020
**Date**: 2021-06-08
**URL**: https://discourse.slicer.org/t/unable-to-install-slicer-in-c-program-files/18020

---

## Post #1 by @edboas (2021-06-08 17:52 UTC)

<p>When I try to install Slicer 4.11 on Windows 10, I get the following error message:<br>
“Error opening file for writing:<br>
C:\Program Files\Slicer 4.11.20210226\Slicer.exe”</p>

---

## Post #2 by @lassoan (2021-06-08 18:05 UTC)

<p>It is not recommended to install 3D Slicer into a folder that can be written by administrators only (such as “C:\Program Files”) because then you need to start Slicer as an administrator each time you want to install extensions or Python packages.</p>
<p>Instead, we changed the default location to be in a folder that the user owns (<code>c:\Users\username\AppData\Local</code>). Many modern software does the same (such as Google Chrome, Dropbox, Webex, Visual Studio Code, Slack, Autodesk applications, Gimp, FreeCAD, Python, Github desktop, …) to avoid the need to have administrator access (UAC elevation popup) to install the application or to install plugins.</p>
<p>If you want a locked-down installation, shared between multiple users on the same computer then you can start the Slicer installer as an administrator and complete the installation process, then start the Slicer application as an administrator and install all the extensions and Python packages that you want to make available to your users.</p>

---

## Post #3 by @edboas (2021-06-09 17:43 UTC)

<p>interesting, thank you for the explanation!</p>

---
