---
topic_id: 2262
title: "Handle Hole Identification And Navigation In Segmentation Mr"
date: 2018-03-07
url: https://discourse.slicer.org/t/2262
---

# Handle/hole identification and navigation in segmentation MRI volume

**Topic ID**: 2262
**Date**: 2018-03-07
**URL**: https://discourse.slicer.org/t/handle-hole-identification-and-navigation-in-segmentation-mri-volume/2262

---

## Post #1 by @JvD (2018-03-07 16:00 UTC)

<p>Dear all,</p>
<p>I am working with brain MRI data in Slicer 4.4.0 on Ubuntu 14.04.<br>
I have automatically generated gray/white matter segmentations that I need to correct for miss classifications, and especially handles (loops of gray/white matter, which are anatomically impossible).<br>
For this, I am using the Model Maker Module to build 3D meshes of the gray and white matter, and I am then correcting the handles and holes manually.<br>
I have a couple questions about this process:</p>
<p>-Is it possible to click on the mesh and automatically navigate to that position in the red,  yellow, and green windows?<br>
-Is there a way of automatically identifying (and maybe fixing) the holes/handles?<br>
-Once I adjust the segmentation in the 2D panes, is there a way to make the 3D mesh update automatically?</p>
<p>Please let me know if you need more information.<br>
Thank you very much for your input!</p>

---

## Post #2 by @cpinter (2018-03-07 16:17 UTC)

<p>Hi Jelle,</p>
<p>Please use Slicer 4.8.1 or later, as 4.4.0 is more than three years old now.<br>
Also use the newer Segment Editor module, as it is more advanced than the original Editor module. See <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">documentation</a> for more information, and there are various tutorials, such as <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">this</a>.</p>
<p>To your questions (in 4.8.1 or later):</p>
<ul>
<li>If you hold down shift when moving your mouse in the 3D view, the slice views will jump there</li>
<li>There is no feature to identify of holes (as far as I know), but you can identify connected components in the Islands effect. To patch holes you can use many of the tools such as Paint or Surface Cut (in SegmentEditorExtraEffects extension)</li>
<li>In Segment Editor, it is automaticaly updated</li>
</ul>

---

## Post #3 by @JvD (2018-03-08 11:23 UTC)

<p>Dear Csaba,</p>
<p>thank you very much for your reply.<br>
I have now updated Slicer to 4.8.1, and am exploring the options you described.</p>
<p>Cheers!</p>

---
