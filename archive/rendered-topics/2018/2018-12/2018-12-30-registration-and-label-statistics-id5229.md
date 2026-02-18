# registration and label statistics

**Topic ID**: 5229
**Date**: 2018-12-30
**URL**: https://discourse.slicer.org/t/registration-and-label-statistics/5229

---

## Post #1 by @Ludovic_Ferrer (2018-12-30 14:02 UTC)

<p>Hi everybody,<br>
I am using 3Dslicer4.10 on windows 10 and I am experiencing a strange behaviour when I want to quantify voxels content values after registration between 2 images.<br>
In short:<br>
2 volumes are registrated with 2 procedures (rigid, non-rigid).  I rapidly segmented one of 2 with <code>Editor tool</code> to get a labelmap with just one label. To get counts inside my label, I used   <code>Label statistics</code>. Swaping the transform on registrated image doesn’t affect results in <code>label statitics</code> whereas it does so when performing the same operation by importing the labelmap in <code>Segment editor tool</code>. Do I missed something ?<br>
Here is a bundle that contains the 2 datasets and registration transform: <a href="https://uncloud.univ-nantes.fr/index.php/s/pmryzmKNgstyHGE" rel="nofollow noopener">https://uncloud.univ-nantes.fr/index.php/s/pmryzmKNgstyHGE</a></p>
<p>Best wishes<br>
Ludovic</p>

---

## Post #2 by @lassoan (2018-12-30 14:44 UTC)

<p>Editor module has many limitations (for example the one that you have noticed). Use Segment Editor module and Segment Statistics modules instead.</p>

---

## Post #3 by @Ludovic_Ferrer (2018-12-31 14:00 UTC)

<p>Thank you Andras, I finally came to the same conclusion.<br>
Regards</p>

---
