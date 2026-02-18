# STL measured values editable?

**Topic ID**: 11439
**Date**: 2020-05-06
**URL**: https://discourse.slicer.org/t/stl-measured-values-editable/11439

---

## Post #1 by @Hina1 (2020-05-06 22:48 UTC)

<p>Hi all,<br>
I am a 3D slicer beginner. Actually I am using png OCT images. And as we know field of view of OCT is 6 mm ( from L to R) and 2 to 1.5 mm (from A to P). After all the steps when I get my stl file and measuring the distance from ( L to R ) and (A to P) its shows 315 mm and 613 mm…<br>
Can I edit these values? As I have to be careful about the dimensions of the stl file for further finite element simulations.<br>
Thanks in advance for the help</p>
<p>Cheers,<br>
Hina</p>

---

## Post #2 by @pieper (2020-05-07 14:30 UTC)

<p>Hi -</p>
<p>Since png files don’t have the pixel size stored Slicer uses 1mm by default.  You can set the correct pixel size in the Volumes module and then your stl file will be generated to match.</p>

---

## Post #3 by @Hina1 (2020-05-08 04:49 UTC)

<p>Hi Pieper,<br>
Thank you very much. I solved my problem.</p>
<p>Cheers,<br>
Hina</p>

---
