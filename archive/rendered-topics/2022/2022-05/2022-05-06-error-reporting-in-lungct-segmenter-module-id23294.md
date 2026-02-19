---
topic_id: 23294
title: "Error Reporting In Lungct Segmenter Module"
date: 2022-05-06
url: https://discourse.slicer.org/t/23294
---

# Error reporting in LungCT segmenter module

**Topic ID**: 23294
**Date**: 2022-05-06
**URL**: https://discourse.slicer.org/t/error-reporting-in-lungct-segmenter-module/23294

---

## Post #1 by @zhongheng (2022-05-06 05:37 UTC)

<p>Hi,<br>
I have the below error when creating segmentation for lung CT; How can i solve this?<br>
Fail to compute results (‘right lung’, labelmapSegmentStatisticsPlugin.centroid_ras)</p>

---

## Post #2 by @rbumm (2022-05-06 08:46 UTC)

<p>This is probably related to the issue you posted on Lung CT Analyzer Github concerning the input volume. I suggest that you start out by downloading 3D Slicers CTChest sample dataset</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6879d0a85fe7286abf8ef71f8235ff94fc37c4e.png" data-download-href="/uploads/short-url/zaU0vtNRzMmWJUSIci9YcMRIRY2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6879d0a85fe7286abf8ef71f8235ff94fc37c4e_2_334x500.png" alt="image" data-base62-sha1="zaU0vtNRzMmWJUSIci9YcMRIRY2" width="334" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6879d0a85fe7286abf8ef71f8235ff94fc37c4e_2_334x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6879d0a85fe7286abf8ef71f8235ff94fc37c4e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6879d0a85fe7286abf8ef71f8235ff94fc37c4e.png 2x" data-dominant-color="C6C3C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">408×610 77.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and use this as the input for the Lung CT Segmenter.</p>

---

## Post #3 by @rbumm (2022-05-06 10:48 UTC)

<p>With your own data, I would recommend importing them into Slicer as DICOM files, then doing the run in the segmenter.</p>

---

## Post #4 by @zhongheng (2022-05-06 23:01 UTC)

<p>Thank you for your reply. I can solve the first issue and successful in loading the volume. I firstly convert tiff series image into dicom file and it can be got in the dropdown list. but the error is still exist. I can do the the sample dataset. I will try to contact the staff from radiology to give me DICOM file.</p>

---
