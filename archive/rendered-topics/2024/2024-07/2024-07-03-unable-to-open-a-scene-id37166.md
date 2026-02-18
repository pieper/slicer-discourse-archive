# Unable to open a scene

**Topic ID**: 37166
**Date**: 2024-07-03
**URL**: https://discourse.slicer.org/t/unable-to-open-a-scene/37166

---

## Post #1 by @Noa (2024-07-03 08:06 UTC)

<p>Hello, I’ve been using slicer to create a .mrb scene but when I try to open it I get this message :</p>
<ul>
<li>Error: Loading C:/Users/Eleve/Desktop/Scene010724.mrb - ERROR: In vtkXMLParser.cxx, line 380<br>
vtkMRMLParser (000001C6ABFA85D0): Error parsing XML in stream at line 234, column 1090, byte index 71922: not well-formed (invalid token)</li>
<li>Error: Loading C:/Users/Eleve/Desktop/Scene010724.mrb - Syntax error in scene file.</li>
</ul>
<p>I can open other Slicer documents but not this one, and this happens every time I save and open a new Slicer scene. Can somewone please help me?<br>
Thank you in advance.</p>

---

## Post #2 by @cpinter (2024-07-03 11:51 UTC)

<p>What Slicer version do you use? Did you use the same Slicer version for saving the scene as what you use opening it? If not what are these versions?</p>

---

## Post #3 by @Noa (2024-07-03 12:02 UTC)

<p>hi,<br>
I use slicer 5.6.1 to build the scene and to reopen it. I think the problem is that I named one of my segmentation with “&amp;”. I corrected it with notepadd++ but now I can’t manage to open back the txt file in slicer…</p>

---

## Post #4 by @cpinter (2024-07-05 11:05 UTC)

<p>It is possible that the character is the culprit. All MRB files are essentially the data files and their mrml descriptor file zipped together. Try to open it as a zip, extract it in a directory and open the .mrml file. If it has the special character too and it doesn’t open try to sanitize the file name.</p>

---
