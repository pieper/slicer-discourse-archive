---
topic_id: 2596
title: "Segmentation According To A Chosen Midsagittal Plane"
date: 2018-04-16
url: https://discourse.slicer.org/t/2596
---

# Segmentation according to a chosen midsagittal plane

**Topic ID**: 2596
**Date**: 2018-04-16
**URL**: https://discourse.slicer.org/t/segmentation-according-to-a-chosen-midsagittal-plane/2596

---

## Post #1 by @Arnaud (2018-04-16 11:43 UTC)

<p>hi everyone,</p>
<p>I’m working on surgical planning in facial bone repositioning. I’m focusing actually on broken zygomatic bones.<br>
To plane the repositioning I use the mirroring of the normal side. (considering that the patient is symmetric…)</p>
<p>To dot it I first readjust the CT scan to obtain a symmetry between the image of left and right side of the patient (ACPC transform)</p>
<p>Then I’d like to segment the normal side according to the midsagital plane to mirror this segment on the broken side ans obtain the “perfect” projection of the repositioning.<br>
For now i don’t know how to segment according to a specific plane???</p>
<p>I use a tricky method with the rectangular scissors but as I can’t follow perfectly the midsagittal plane my mirroring is not perfect…</p>
<p>Is anyone can help me?</p>
<p>thanks for helping me.</p>

---

## Post #2 by @lassoan (2018-04-17 03:35 UTC)

<p>You can segment on any plane. It is not necessary to use a plane that you’ll later use for mirroring.</p>
<p>Instead of ACPC transform, you can mirror your volume (apply a transformation matrix of <code>diagonal(-1, 1, 1, 1)</code>) and register it to the original volume to get an accurate mirroring transform. You can either use automatic intensity-based registration (General registration (BRAINS) module) or you can use landmark-based registration (Fiducial registration module in SlicerIGT extension) to find the mirroring transform.</p>
<p>Once you have your segmentation completed on one side, clone the segmentation node, apply the mirroring transform, harden the transform, and copy the mirrored segment to the original segmentation.</p>
<p>If you get stuck at any point then let us know.</p>

---

## Post #3 by @Arnaud (2018-04-27 09:50 UTC)

<p>Thanks a lot for this very detailed answer. I’ll try and let you know if I get stuck.</p>

---
