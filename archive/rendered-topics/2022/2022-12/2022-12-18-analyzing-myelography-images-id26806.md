# Analyzing myelography images

**Topic ID**: 26806
**Date**: 2022-12-18
**URL**: https://discourse.slicer.org/t/analyzing-myelography-images/26806

---

## Post #1 by @Lohi (2022-12-18 10:33 UTC)

<p>Hi;<br>
Well, new challenges for me…I have some GB of imaging from 3 myelography sessions, which included the fluoroscopy (sp?) and fast CT imaging.<br>
Are there any tutorials, or other documentation regarding myelography? It seems that the signs could be rather subtle, and slicer seems a very good tool for really ‘squeezing out’ fine data.</p>
<p>Thanks !</p>

---

## Post #2 by @lassoan (2022-12-18 17:12 UTC)

<p>Myelography is a 2D imaging method - the images are 2D X-ray projection images. Therefore, I don’t think any specific tools are developed for their analysis in Slicer.</p>
<p>The fluoroscopy images should load correctly into Slicer and you should be able to browse the images using sequence toolbar. If you load multiple series then you need to choose the sequence browser node in the toolbar that corresponds to the image shown in the viewers. This is somewhat inconvenient. If it makes image review very tedious then let us know and we’ll try to simplify this.</p>
<p>Probably the contrast agent will be hardly visible in the native images (the contrast just makes the images very slightly darker). You can make the changes very visible by subtracting the contrast-free images from the contrasted images. You can do that by loading the series twice, choose a contrasted frame of one sequence and contrast-free frame of the other sequence and use <code>Subtract scalar volumes</code> module to compute the difference between them. This could be also made more convenient. If you share an anonymized data set (e.g., the DICOM series saved into a seq.nrrd file) then we may be able to develop a module that automates this subtraction procedure.</p>

---

## Post #3 by @Lohi (2022-12-18 19:20 UTC)

<p>thanks, Andras!</p>
<p>I’m kind of jumping in at the deep end, and have a bit of ‘brain fog’ to contend with, but I’m moving my Slicer and Horos work to a faster machine(4 core i7 @ 3 GHz), that is more dedicated to larger tasks, leaving day-to-day stuff on the other machine.</p>
<p>Merçi, Danke, Arrigato!</p>

---
