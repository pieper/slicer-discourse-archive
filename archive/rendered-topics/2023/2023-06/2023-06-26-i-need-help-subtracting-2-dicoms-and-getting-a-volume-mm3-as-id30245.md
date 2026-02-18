# I need help subtracting 2 DICOMs and getting a volume (mm3) as result   

**Topic ID**: 30245
**Date**: 2023-06-26
**URL**: https://discourse.slicer.org/t/i-need-help-subtracting-2-dicoms-and-getting-a-volume-mm3-as-result/30245

---

## Post #1 by @Manita (2023-06-26 20:51 UTC)

<p>Hi, I need help. I’m new here.</p>
<p>I have 2 DICOM from the same patient. One before the intervention and one after. I can see there’s a difference, but I would like to get the volumetric difference between the two files.<br>
I would appreciate a step by step, since I’m pretty new.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2023-06-27 02:41 UTC)

<p>Is it for assessing fat resorption for breast reconstruction?<br>
What imaging modality did you use?</p>

---

## Post #3 by @Manita (2023-06-27 12:19 UTC)

<p>Thanks for answering.</p>
<p>I want to calculate the hard tissue/bone gain or loss of the procedure, comparing two DICOMs of the same patient taken at different times. I can visually see the difference of both surfaces, but I would like to calculate the volume of such difference</p>

---

## Post #4 by @lassoan (2023-06-27 14:05 UTC)

<p>You can measure volume difference of bone and tissue by the following steps:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">Register the images.</a></li>
<li>Segment the same region in both images using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">Segment Editor</a>. Enable overlap in Masking settings.</li>
<li>Use Erase effect or Logical operators effect to remove regions that are farther away from the region of interest. Use the same region for all segments.</li>
<li>Use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">Segment Statistics</a> module to get volume of each segment</li>
</ul>

---

## Post #5 by @Manita (2023-06-28 00:44 UTC)

<p>Thank you for answering.</p>
<p>I’m just unable to grasp how to use this.</p>

---

## Post #6 by @lassoan (2023-06-28 02:40 UTC)

<p>You can start with learning how to segment the bone using Segment Editor. <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">This page</a> is a good starting point. There are also lots of tutorials on youtube.</p>

---
