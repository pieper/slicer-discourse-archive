---
topic_id: 3148
title: "Slicer Remote Access"
date: 2018-06-12
url: https://discourse.slicer.org/t/3148
---

# Slicer Remote access

**Topic ID**: 3148
**Date**: 2018-06-12
**URL**: https://discourse.slicer.org/t/slicer-remote-access/3148

---

## Post #1 by @anandmulay3 (2018-06-12 10:02 UTC)

<p>Slicer is not running when we try to access it through remote desktop service, but its working if we working on the same machine (PC).<br>
does it require any permission ??</p>

---

## Post #2 by @anandmulay3 (2018-06-12 10:59 UTC)

<p>i tried to look into log file , it shows AttributeError: ‘module’ object has no attribute ‘My-scripbtable module’<br>
im running may batch file remotely ,<br>
if i run same batch file that particular machine it is running very well without any error…</p>

---

## Post #3 by @lassoan (2018-06-12 12:56 UTC)

<p>Slicer 4.9 minimum OpenGL requirements have been increased. Does this answer your questions? <a href="https://issues.slicer.org/view.php?id=4252">https://issues.slicer.org/view.php?id=4252</a></p>
<p>If not, then please write exact version of your Slicer, operating system, and remote desktop application.</p>

---

## Post #4 by @anandmulay3 (2018-06-13 07:20 UTC)

<p>Windows 7<br>
OpenGl 3.3<br>
Slicer r27236<br>
Windows remote desktop</p>

---

## Post #5 by @anandmulay3 (2018-06-13 07:34 UTC)

<p>its just crashes on slicer startup when slicer loads its modules</p>

---

## Post #6 by @ihnorton (2018-06-13 13:42 UTC)

<p>The link from <code>lassoan</code> above describes the issue: Windows RDP client does not support newer OpenGL versions, and so Slicer crashes – unfortunately without a useful error message yet. The suggestion is to try VNC or NoMachine. I can confirm NoMachine works with recent Slicer builds from a Mac client to a Linux host. I haven’t tried it with a Windows client, but it should probably work fine.</p>

---

## Post #7 by @anandmulay3 (2018-06-14 08:09 UTC)

<p>yes NoMachine works- confirm, for Windows , thank you <a class="mention" href="/u/lassoan">@lassoan</a> &amp; <a class="mention" href="/u/ihnorton">@ihnorton</a>.</p>

---

## Post #8 by @lassoan (2018-06-14 13:12 UTC)

<p>I can confirm that VNC and TeamViewer works on Windows, too. Windows Remote Desktop works as well, but you need to start Slicer before connecting to the computer (using a batch file, as described <a href="https://issues.slicer.org/view.php?id=4252#c14081">here</a>).</p>

---

## Post #11 by @lassoan (2023-03-21 02:01 UTC)



---
