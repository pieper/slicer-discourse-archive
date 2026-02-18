# Share a GUI based on QT

**Topic ID**: 11954
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/share-a-gui-based-on-qt/11954

---

## Post #1 by @Fabi-LiU (2020-06-09 14:27 UTC)

<p>Hi,</p>
<p>I made a graphical user interface using Qtdesigner and a python code to run the ui files. The GUI  is planed to be used by researchers in the field of deep brain stimulation (including neurosurgeons and neurologists). What the GUI does is simply let the user select and visualize different studies (loaded as mrml files). I’ve been able to run the gui on my lap and pc by modifying some folders and files in 3DSlicer, i.e. launcher settings, add resources folder (with all the GUI ui files), the compiled py file and the cmakelists.txt…</p>
<p>My question is if there is a better or quicker way to run this GUI on any computer. I think it’s too cumbersome to modify files in 3DSlicer and I imagine physicians will be reluctant to do it.</p>
<p>Thank you in advance,<br>
Fabiola</p>

---

## Post #2 by @lassoan (2020-06-09 15:57 UTC)

<p>You can put your custom Slicer on a USB stick or a network share along with all data and ask the clinicians to run that application. If you want to provide an installer then you can create a custom application. See more details on this page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>

---

## Post #3 by @Fabi-LiU (2020-06-09 17:45 UTC)

<p>Thank you for the quick response!</p>

---
