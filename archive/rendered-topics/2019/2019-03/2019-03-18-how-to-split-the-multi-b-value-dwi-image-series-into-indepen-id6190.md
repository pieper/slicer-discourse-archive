---
topic_id: 6190
title: "How To Split The Multi B Value Dwi Image Series Into Indepen"
date: 2019-03-18
url: https://discourse.slicer.org/t/6190
---

# How to split the Multi-b value DWI image series into independent images with high b value and low B value

**Topic ID**: 6190
**Date**: 2019-03-18
**URL**: https://discourse.slicer.org/t/how-to-split-the-multi-b-value-dwi-image-series-into-independent-images-with-high-b-value-and-low-b-value/6190

---

## Post #1 by @hss003 (2019-03-18 12:45 UTC)

<p>how to split  the Multi-b value DWI image series into independent images with high b value and low B value.</p>

---

## Post #2 by @fedorov (2019-03-18 15:50 UTC)

<p>You can load your DWI DICOM series as a multivolume, which is a 4d image where 4th dimension (in case of a DWI series) will be the b-value. If you toggle “Advanced” mode in DICOM browser, and “Examine” the DWI series, you will see MultiVolume as one of the options to load it, if your series was recognized as a multivolume. Once you loaded it, you can use MultVolumeExplorer module to look at the images for the specific b-values, and you can also extract individual images as separate scalar volumes.</p>
<p>Note that this will only work if your DWI image is a trace image.</p>

---

## Post #3 by @zhangfanmark (2019-03-18 16:15 UTC)

<p>In SlicerDMRI (<a href="http://dmri.slicer.org" rel="nofollow noopener">http://dmri.slicer.org</a>), we have a module “Extract DWI Shells”, which is designed specifically for extracting DW images at b-values of interest. This module should be available in Slicer, after you install SlicerDMRI. However, it seems the nightly version of Slicer does not show the extension manager to install SlicerDMRI. I suggest that you wait a little until this is fixed to use this module. For now, you can try what Fedorov suggested on DICOM data.</p>
<p>Regards,<br>
Fan</p>

---

## Post #4 by @lassoan (2023-03-21 03:09 UTC)



---
