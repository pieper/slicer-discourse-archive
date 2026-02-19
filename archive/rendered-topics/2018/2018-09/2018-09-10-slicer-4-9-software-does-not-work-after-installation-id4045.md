---
topic_id: 4045
title: "Slicer 4 9 Software Does Not Work After Installation"
date: 2018-09-10
url: https://discourse.slicer.org/t/4045
---

# SLICER 4.9 software does not work after installation.

**Topic ID**: 4045
**Date**: 2018-09-10
**URL**: https://discourse.slicer.org/t/slicer-4-9-software-does-not-work-after-installation/4045

---

## Post #1 by @zhaoduanyun (2018-09-10 13:32 UTC)

<p>Operating system:Windows 7 Pro SP1 64 bit<br>
Slicer version:4.9 nightlybuild<br>
Expected behavior:Running normally after installation<br>
Actual behavior:The software was installed successfully, but double-clicking on the icon didn’t respond，or the interface starts to flash past, and then there is no response. I’ve deleted the.Ini file from the NA-MIC directory, but it still does not solve any problems, while earlier versions can run normally.</p>

---

## Post #2 by @lassoan (2018-09-10 17:32 UTC)

<p>Graphics card minimum requirements have been increased in Slicer-4.9. What is your graphics card brand and model? What is the graphics card driver version?</p>
<p>Updating your driver may fix the issue. If it does not help, follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Debugging_Slicer_application_startup_issues">these instructions</a>.</p>

---

## Post #3 by @zhaoduanyun (2018-09-11 14:33 UTC)

<p>Thank you for your reply.<br>
My graphics card is NVIDIA GeForce GTX950,and the driver version is 10.18.13.6143,it is the latest version.<br>
I don’t think it’s a problem with the graphics card or the driver. Some colleagues think it is a problem with the win7 system. It is not very compatible with the slicer 4.9. So I also ran eventvwr.exe trying to find some clues, but found nothing.</p>

---

## Post #4 by @cpinter (2018-09-11 14:38 UTC)

<p>Is there a log file? If yes, what is in there? You can find it in your user’s Temp folder called Slicer_NNNNN_DATE_TIME.log.</p>

---

## Post #5 by @zhaoduanyun (2018-09-11 15:14 UTC)

<p>Thank you for your reply.<br>
In this TEMP directory, I found the .log files, but they are all about the versions that were previously runable, while  there are no files for this inoperable version.<br>
In a word, the program doesn’t seem to have been run. It left no trace.<br>
It’s very strange.</p>

---

## Post #6 by @lassoan (2018-09-11 18:31 UTC)

<p>Probably you’ll find a solution if you continue with the instructions on the link referenced above (check “There may be conflicting DLLs in your system path” section).</p>

---
