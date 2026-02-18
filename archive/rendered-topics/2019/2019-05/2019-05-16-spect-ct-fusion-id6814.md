# spect ct fusion

**Topic ID**: 6814
**Date**: 2019-05-16
**URL**: https://discourse.slicer.org/t/spect-ct-fusion/6814

---

## Post #1 by @kotzasm (2019-05-16 12:33 UTC)

<p>Operating system: windows<br>
Slicer version:4.10.1<br>
Expected behavior:<br>
Actual behavior:<br>
how can I fuse SPECT and CT dcm images and perform roi segmentation simultaneously on both data sets in order to get the ROI counts?<br>
Thanks in advance</p>

---

## Post #2 by @fbaerenfaenger (2021-02-16 19:02 UTC)

<p>Hi,<br>
Could you find a solution for your problem?</p>
<p>Best regards</p>

---

## Post #3 by @lassoan (2021-02-16 19:35 UTC)

<p>I don’t think there should be a problem at all. To get started with image segmentation in Slicer, you can check out this <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">documentation page</a>. If you have any specific questions then let us know.</p>

---

## Post #4 by @jw_yi (2022-08-16 14:41 UTC)

<p>Fusion of reconstructed SPECT images with CT is not a problem, however, it seems 3D slicer cannot show the counts in the ROI, but only voxels in the ROI. I wonder if there is any solution?<br>
Thanks so much!!</p>

---

## Post #5 by @lassoan (2022-08-16 15:52 UTC)

<p>You can get several metrics of a segmented region of an image (not just the volume, but mean, minimum, maximum, standard deviation, etc.) using Segment Statistics module. Would this be sufficient for you?</p>

---

## Post #6 by @jw_yi (2022-08-17 05:25 UTC)

<p>Thank you so much, Lassoan. however, counts in the ROI is a specific parameter in nuclear medicine, it dose not parallel to the Voxel or volume.It just like SUV in PET, but not a normalized paramter. It seems that in the Segment statistics module, i can’t find this parameter.</p>

---

## Post #7 by @lassoan (2022-08-17 10:27 UTC)

<p>You need to compute the quantity you want to measure (“counts”) using numpy, scipy, or any higher-level library available for this in Python or C++. Then you can use Segment Statistics module to compute statistics on it in selected regions.</p>

---

## Post #8 by @jw_yi (2022-08-18 02:02 UTC)

<p>Thank you，Lassoan！I’ll have a try!</p>

---
