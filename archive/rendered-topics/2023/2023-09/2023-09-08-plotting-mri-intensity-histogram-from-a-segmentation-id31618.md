# Plotting MRI intensity histogram from a segmentation

**Topic ID**: 31618
**Date**: 2023-09-08
**URL**: https://discourse.slicer.org/t/plotting-mri-intensity-histogram-from-a-segmentation/31618

---

## Post #1 by @SHADI (2023-09-08 13:49 UTC)

<p>Operating system: Windows 10<br>
Slicer version:5.4<br>
Expected behavior<br>
how can I plot an intensity histogram using 3Dslicer?</p>

---

## Post #2 by @lassoan (2023-09-08 16:52 UTC)

<p>Histogram rarely contains information that is relevant for end users, so we haven’t created a GUI for this feature, but you can get it by a few lines of Python code. See a complete example (including generating sample data, computing the histogram, and plotting the result) in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">script repository</a>.</p>

---
