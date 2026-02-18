# Radiation Therapy and AI assisted segmentation?

**Topic ID**: 29475
**Date**: 2023-05-15
**URL**: https://discourse.slicer.org/t/radiation-therapy-and-ai-assisted-segmentation/29475

---

## Post #1 by @Dave90 (2023-05-15 14:38 UTC)

<p>Hi, I’m a radiation therapist that’s rather new in this space. I’m looking for any information on using slicers auto segmentation to get those defined contours into Radiation therapy planning software like Eclipse.</p>
<p>I watched the PerkLab research channel on YouTube showing him using these tools to contour CT scans with TotalSegmentator. the amount of time that this would save our oncology department has me very interested. has anyone heard of ways to export those files back to RT software or keep them on the Diacom?</p>

---

## Post #2 by @pieper (2023-05-15 14:40 UTC)

<p>I don’t know that anyone has tried the full process, but all the pieces should be there if you are willing to work through them.  You can install the TotalSegmentator and SlicerRT extensions and let us know how it goes.</p>

---

## Post #3 by @lassoan (2023-05-16 20:02 UTC)

<p>Yes, you can use SlicerRT extension to export selected segments (e.g., organs at risk) as DICOM RT structure set (see instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">here</a>).</p>
<p>I’ve tested DICOM RT export on the CTLiver sample data set and it takes about 10 minutes to export all the 100+ structures that TotalSegmentator provides, It is because there are many large and complex structures, which needs to be cut and converted to parallel contours.</p>
<p>If you want to store detailed segmentation results in DICOM then I would recommend to store it as DICOM Segmentation object (using QuantitativeReporting extension). Import/export of 100 segments in this format would be slow, too (and you may run out of memory during importing because currently Slicer loads each segment one by one before merging them into one array), but the advantage of this format is that it can store the binary labelmap representation directly, preserving all details (instead of converting to parallel contours for storage and then rasterizing the contours to get the labelmap representation).</p>

---
