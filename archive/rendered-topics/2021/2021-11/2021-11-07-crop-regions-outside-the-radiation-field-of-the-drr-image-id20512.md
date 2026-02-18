# Crop regions outside the radiation field of the DRR image

**Topic ID**: 20512
**Date**: 2021-11-07
**URL**: https://discourse.slicer.org/t/crop-regions-outside-the-radiation-field-of-the-drr-image/20512

---

## Post #1 by @shahrokh (2021-11-07 12:43 UTC)

<p>Dear Users and Developers</p>
<p>I want to crop DRR image with the Beam. To be more precise, I want to do the following steps:</p>
<p>1- Loading the DRR image taken from the TPS system (for example, <strong>RTIMAGE</strong> related to <strong>Med Tangent</strong> radiation field);<br>
2- Loading RTPlan (for example, including as <strong>Med Tangent</strong> radiation field)<br>
3- Cutting a part of the DRR image that is outside the radiation field (zeroing this region).<br>
Can you give me some guidance?</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2021-11-08 02:27 UTC)

<p>Since beams are special model nodes, it is very easy to mask volumes with them:</p>
<ul>
<li>select the volume that you want to mask (blank out regions from it) as background volume</li>
<li>go to the Segment Editor module to create a segmentation node</li>
<li>go to the Segmentations module and import the beam as a segment, using Export/import… → Import → Models</li>
<li>go to Segment Editor module and use Mask volume to blank out the volume outside the segment</li>
</ul>

---

## Post #3 by @shahrokh (2021-11-09 13:21 UTC)

<p>Dear Andras</p>
<p>Thanks a lot for your guidance.<br>
I can do it.</p>
<p>Best regards.<br>
Shahrokh</p>

---
