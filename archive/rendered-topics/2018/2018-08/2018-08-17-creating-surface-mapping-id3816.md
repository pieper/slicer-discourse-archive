---
topic_id: 3816
title: "Creating Surface Mapping"
date: 2018-08-17
url: https://discourse.slicer.org/t/3816
---

# creating surface mapping

**Topic ID**: 3816
**Date**: 2018-08-17
**URL**: https://discourse.slicer.org/t/creating-surface-mapping/3816

---

## Post #1 by @Tareq_Aro (2018-08-17 17:14 UTC)

<p>I have volume Ultrasound data and I am able to reconstruct object volume from it.<br>
Is there a way to reconstruct surface mapping using the software? as in to see only the first layer of the desired object creating a continuous surface?</p>
<p>thank you</p>

---

## Post #2 by @pieper (2018-08-17 21:15 UTC)

<p>You mean like a segmentation? See: <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></p>

---

## Post #3 by @Tareq_Aro (2018-08-20 18:40 UTC)

<p>thank you for your reply.</p>
<p>i basically need to do surface rendering but for the inside of a hollow viscus…</p>
<p>I am looking at kidney or a urinary bladder with my ultrasound images - and I would like to make a rendering of the interior surface of the structure and not the exterior one - how can i do that?</p>
<p>thank you</p>
<p>tareq</p>

---

## Post #4 by @lassoan (2018-08-20 19:08 UTC)

<p>To see the internal surface of a model or segmentation you have several options:</p>
<ul>
<li>Simplest: go inside - center the 3D view and zoom in until you get inside (for models, make sure you set Visible sides: all).</li>
<li>If input is segmentation node: make it hollow using Hollow effect in Segment editor, and then cut it using scissors or erase effect.</li>
<li>If input is model node: clip it using Models module and move slice views.</li>
</ul>
<p>You can use any of the methods for any input by converting between model&lt;-&gt;segmentation node using Segmentations module (Import/Export section).</p>

---
