---
topic_id: 21362
title: "How To Change The Parameters Of The Reconstruction"
date: 2022-01-08
url: https://discourse.slicer.org/t/21362
---

# how to change the parameters of the reconstruction?

**Topic ID**: 21362
**Date**: 2022-01-08
**URL**: https://discourse.slicer.org/t/how-to-change-the-parameters-of-the-reconstruction/21362

---

## Post #1 by @yoav_benhaim (2022-01-08 16:32 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11.20210226</p>
<p>I have axiel sections of CT and I want to determine the depth of each section in the reconstruction as well as the distance between each two pixels in length and width.<br>
Does the 3D slicer automatically take this data from the header when uploading dicom files?</p>
<p>Where can you see this data?<br>
Want to make sure the dimensions of the model are indeed correct.</p>
<p>And can I change these parameters?<br>
This is important because I want to import them after segmentation as a jpeg image without converting them back to dicom<br>
thank you for helping</p>

---

## Post #2 by @mikebind (2022-01-10 18:40 UTC)

<p>Yes, Slicer reads and respects the spacing data from DICOM headers.  You can see what has been imported in the “Volumes” module, in the “Volume Information” section, where you can also change this data if needed.</p>

---
