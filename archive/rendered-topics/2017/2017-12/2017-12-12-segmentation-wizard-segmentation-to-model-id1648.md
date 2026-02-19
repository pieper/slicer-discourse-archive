---
topic_id: 1648
title: "Segmentation Wizard Segmentation To Model"
date: 2017-12-12
url: https://discourse.slicer.org/t/1648
---

# Segmentation Wizard; segmentation to model

**Topic ID**: 1648
**Date**: 2017-12-12
**URL**: https://discourse.slicer.org/t/segmentation-wizard-segmentation-to-model/1648

---

## Post #1 by @CaDi (2017-12-12 13:54 UTC)

<p>Hi,</p>
<p>using the segmentation wizard, I was abble to perform a perfect segmentation of my ROI. However, my usual workflow of manual segmentation was to do the following:</p>
<ul>
<li>Manual segmentation in segment editor</li>
<li>Export to model (using the -&gt; Segmentations option, export to “model” in Export/Import models and labelmaps)</li>
<li>Manipulating the model in the model module</li>
</ul>
<p>However, after using the segmentation wizard, I’m stucked in the segmentation process. I can see my green segmentation (2D slices), but can’t see the 3D view int he segmentation editor. In the “master volume”, the new volume appears ("…thresholded"). But I don’t know how to export this into a model.<br>
I tried different things, choosing the thresholded volume in the segmentation module, added segment and tried to export. But I think, I missed something here, perhaps someone can help me  here?</p>
<p>Best regards,<br>
Carsten</p>

---

## Post #2 by @cpinter (2017-12-12 15:08 UTC)

<p>I assume the output of the Segmentation Wizard is a labelmap. In that case you can create a new segmentation node in the Segmentations module (very top), go to the bottom, import the labelmap to the segmentation (choose Import and Labelmap), then you can export it as a model node in the same section (choose Export and Models).</p>

---

## Post #3 by @CaDi (2017-12-13 06:38 UTC)

<p>Thank you very much, that worked!</p>

---
