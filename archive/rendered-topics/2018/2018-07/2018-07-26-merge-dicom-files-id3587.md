# Merge Dicom Files

**Topic ID**: 3587
**Date**: 2018-07-26
**URL**: https://discourse.slicer.org/t/merge-dicom-files/3587

---

## Post #1 by @ajsenelle (2018-07-26 17:25 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I have taken multiple CT scans of the parts of one object. Now i have 4 Dicom Files. I wish to combine these files so that there is only one scan of the object whole. Can slicer help?</p>

---

## Post #2 by @pieper (2018-07-26 18:16 UTC)

<p>Probably yes - a lot depends on exactly how they were scanned and whether there’s any information that would allow you to put them together automatically or if you need to do some steps manually.</p>
<p>Generally speaking you can make a target volume large enough to hold the full object (say, with the Crop Volume module) and then you could add in the other volumes with Add Scalar Volume either as-is or after transforming them to the right locations.</p>
<p>It might help for you to post some screenshots of the volumes and describe some more about how the scans were obtained and what you need to accomplish.</p>

---
