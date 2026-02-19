---
topic_id: 4948
title: "3Dslicer For Measuring Pectoralis Area On Axial Ct Slice"
date: 2018-12-04
url: https://discourse.slicer.org/t/4948
---

# 3DSlicer for measuring pectoralis area on axial CT slice

**Topic ID**: 4948
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/3dslicer-for-measuring-pectoralis-area-on-axial-ct-slice/4948

---

## Post #1 by @Benjamin_Fortson (2018-12-04 03:27 UTC)

<p>Hi,</p>
<p>I’m completely new to 3DSlicer. Can it be used to measure the area and average density of the pectoralis muscle on an axial CT slice? Is this process called segmentation, or is that something else?</p>
<p>Thanks,</p>
<p>Ben</p>

---

## Post #2 by @pieper (2018-12-04 13:40 UTC)

<p>Hi Ben -</p>
<p>Yes, segmentation would be a part of the process.  Basically you would load the CT, use the Segment Editor to draw the muscle region of interest, then use Segment Statistics to get the average CT density and the muscle volume (the area times the slice the slice spacing).</p>
<p>You could start with these tutorials:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Image_Segmentation" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Image_Segmentation</a></p>
<p>-Steve</p>

---

## Post #3 by @Benjamin_Fortson (2018-12-05 01:37 UTC)

<p>Great! Thanks for getting me on the right track.</p>

---
