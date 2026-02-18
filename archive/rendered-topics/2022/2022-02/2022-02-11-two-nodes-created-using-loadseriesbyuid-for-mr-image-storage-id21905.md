# Two nodes created using loadSeriesByUID for MR Image Storage SOPClass

**Topic ID**: 21905
**Date**: 2022-02-11
**URL**: https://discourse.slicer.org/t/two-nodes-created-using-loadseriesbyuid-for-mr-image-storage-sopclass/21905

---

## Post #1 by @CJohnson (2022-02-11 02:31 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226<br>
Expected behavior: One MRMLScalarVolumeNode should be created<br>
Actual behavior: Two MRMLScalarVolumeNode (s) are created, one has only one slice with the time series tools activated and the other is a standard scrollable volume. This was not an issue when I was using Slicer’s version 4.11.20200930.</p>
<p>My script uses the DICOMUtils function loadSeriesByUID to load  image volumes. The dicom tag for my test image has a SOPClassUID of ‘1.2.840.10008.5.1.4.1.1.4’ but there are no triggerTime dicom tags.</p>
<p>I can see that because of the SOP Class, both the DICOMImageSequencePlugin and the DICOMScalarVolumePlugin are enabled as possible plugins to use for image loading. The problem is that the confidence assigned to these loadable plugins is not addressed in the loadSeriesByUID function - so both plugins execute their load function.</p>
<p>Can the loadSeriesByUID function be changed to look at the confidences or should I modify how I load images in my script?</p>

---

## Post #2 by @lassoan (2022-02-11 05:33 UTC)

<p>As far as I remember, this problem has been already fixed. Please check if you can reproduce the problem in the latest Slicer Preview Release.</p>

---

## Post #3 by @CJohnson (2022-02-13 01:04 UTC)

<p>Thank you  - Everything works in the Slicer Preview Release.</p>

---
