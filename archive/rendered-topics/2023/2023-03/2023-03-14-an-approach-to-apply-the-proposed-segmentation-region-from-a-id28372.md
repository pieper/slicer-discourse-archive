# An approach to apply the proposed segmentation region from an ML model to DICOM data 

**Topic ID**: 28372
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/an-approach-to-apply-the-proposed-segmentation-region-from-an-ml-model-to-dicom-data/28372

---

## Post #1 by @mlh (2023-03-14 11:40 UTC)

<p>Hi all,<br>
I would like to create a new extension which can do the following task:</p>
<ul>
<li>Click a point on a DICOM data on Slicer (e.g. a point in a specific human organ)</li>
<li>Get that point and image, then pass them to the ML model. The model will output a proposed region for segmentation.</li>
<li>Pass the model’s output to Slicer and segment the region on Slicer.</li>
</ul>
<p>I highly appreciate if you guys can recommend an approach to do those task. Thank you!</p>

---

## Post #2 by @pieper (2023-03-14 13:17 UTC)

<p>Sounds reasonable.  You should review MONAI Label and TotalSegmentator to see what’s already possible.  Then read the programming tutorials and read through the script repository.</p>

---
