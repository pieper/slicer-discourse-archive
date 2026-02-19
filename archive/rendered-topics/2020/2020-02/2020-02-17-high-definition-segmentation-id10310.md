---
topic_id: 10310
title: "High Definition Segmentation"
date: 2020-02-17
url: https://discourse.slicer.org/t/10310
---

# High definition segmentation

**Topic ID**: 10310
**Date**: 2020-02-17
**URL**: https://discourse.slicer.org/t/high-definition-segmentation/10310

---

## Post #1 by @ThomPote (2020-02-17 13:50 UTC)

<p>Hi,</p>
<p>In addition to this topic <a href="https://discourse.slicer.org/t/segmentation-with-higher-resolution/7495">Segmentation High resolution</a>, what are the different methods to increase definition in segmentation ?</p>
<ol>
<li>
<p>How can we increase resolution ?</p>
</li>
<li>
<p>How can we remedy to pixelated image on external contours ?</p>
</li>
</ol>
<p>Thanks for your help</p>

---

## Post #2 by @lassoan (2020-02-17 14:26 UTC)

<p>To remove pixelation from contours, you need to increase the resolution (reduce spacing) of the binary labelmap representation in your segmentation node. To achieve this, you can follow these steps in recent Slicer Preview Releases:</p>
<ul>
<li>If master representation of your segmentation is “Binary labelmap”: you can click on the “set geometry” button in Segment Editor: <a href="https://discourse.slicer.org/t/smooth-object-volume-statistics/3596" class="inline-onebox">Smooth Object volume statistics </a>.</li>
<li>If master representation is “Closed surface” or “Planar contours” (because you created the segmentation by importing a model node or RT structure set) then you can:
<ul>
<li>Go to “Segmentations” module, “Representations” section</li>
<li>Click “Update” button in “Binary labelmap” row (click “Create” button first if “Update” button is not there)</li>
<li>Select a conversion path in the top section, then in “Reference image geometry” row click “Specify geometry” button</li>
<li>Select a node to specify region size and adjust spacing parameters</li>
<li>Click “Convert”</li>
</ul>
</li>
</ul>

---
