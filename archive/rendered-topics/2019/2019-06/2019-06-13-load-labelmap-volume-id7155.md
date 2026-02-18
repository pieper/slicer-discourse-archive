# Load LabelMap volume

**Topic ID**: 7155
**Date**: 2019-06-13
**URL**: https://discourse.slicer.org/t/load-labelmap-volume/7155

---

## Post #1 by @thu.nguyen (2019-06-13 11:38 UTC)

<p>Operating system: Mac Os 10.11.6<br>
Slicer version: 4.8.1, 4.10.0, 4.10.2<br>
Expected behavior: Load a Nifti file (unsigned char) as LabelMap volume<br>
Actual behavior: 3DSlicer does nothing, even when the LabelMap option is not selected.</p>
<p>Hi,</p>
<p>I have a problem loading my Segmentation into 3DSlicer.<br>
Normally it works but at some point, 3DSlicer resufed to load all unsigned char Nifti files. I tried to load the volume as normal volume (unselect LabelMap option) and tried to use different versions of 3DSlicer but nothing works.</p>
<p>Thanks for your help</p>

---

## Post #2 by @lassoan (2019-06-13 11:39 UTC)

<p>Is there any error message in the application log? Can you send us a sample for file?</p>

---

## Post #3 by @thu.nguyen (2019-06-13 11:52 UTC)

<p>I did not know that I can view the error log.<br>
I found the error. There was a problem with the name of the file. It works now.<br>
Thank you so much for your help.</p>

---
