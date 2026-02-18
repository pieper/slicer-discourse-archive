# How to write data into regedit in slicer?

**Topic ID**: 27736
**Date**: 2023-02-10
**URL**: https://discourse.slicer.org/t/how-to-write-data-into-regedit-in-slicer/27736

---

## Post #1 by @jay1987 (2023-02-10 06:14 UTC)

<p>i have made a simple application use 3dslicer , and wants to write some data into regedit<br>
but write data into regedit in win10 need administrator privileges<br>
i have tryed some code in netword and in chatgpt,it doesn’t work<br>
dear community ,does anyone knows how to write data into regedit in slicer or how to obtain administrator privileges in slicer?</p>

---

## Post #2 by @cpinter (2023-02-10 09:57 UTC)

<p>I suggest you use the ini file (see <code>QSettings</code>) to store configuration specific information.</p>

---

## Post #3 by @jay1987 (2023-02-10 10:37 UTC)

<p>i agree with you pinter<br>
if i can’t find solution to write to the regedit, i will use the solution to wirte into QSetting</p>

---
