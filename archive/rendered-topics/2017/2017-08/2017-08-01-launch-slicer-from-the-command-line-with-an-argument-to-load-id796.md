# Launch slicer from the command line with an argument to load a file

**Topic ID**: 796
**Date**: 2017-08-01
**URL**: https://discourse.slicer.org/t/launch-slicer-from-the-command-line-with-an-argument-to-load-a-file/796

---

## Post #1 by @tkuraku (2017-08-01 01:36 UTC)

<p>I would like to be able to launch slicer via command line (from python) and have it automatically load and display a specified nrrd file. Is this possible? I searched some of the documentation but I couldn’t quite find what I wanted.</p>

---

## Post #2 by @lassoan (2017-08-01 01:45 UTC)

<p>See these examples:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Launching_Slicer" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Launching_Slicer</a></p>

---

## Post #3 by @moselhy (2017-08-01 15:28 UTC)

<p>Say you have Slicer.exe in "C:\Program Files\Slicer 4.7.0-2017-07-29\Slicer.exe"<br>
and you have a Nrrd file in “C:\CTACardio.nrrd”</p>
<p>You would run this in Command Prompt:</p>
<p>“C:\Program Files\Slicer 4.7.0-2017-07-29\Slicer.exe” “C:\CTACardio.nrrd”</p>

---

## Post #4 by @tkuraku (2017-08-01 16:26 UTC)

<p>Thank you both. This solves my problem!</p>

---
