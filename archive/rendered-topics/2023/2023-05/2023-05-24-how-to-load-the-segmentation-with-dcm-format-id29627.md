# How to load the segmentation with dcm format?

**Topic ID**: 29627
**Date**: 2023-05-24
**URL**: https://discourse.slicer.org/t/how-to-load-the-segmentation-with-dcm-format/29627

---

## Post #1 by @Liang_Ma (2023-05-24 11:18 UTC)

<h2><a name="p-95242-operating-system-ubuntu2004-slicer-version-522-1" class="anchor" href="#p-95242-operating-system-ubuntu2004-slicer-version-522-1" aria-label="Heading link"></a>Operating system: Ubuntu20.04<br>
Slicer version: 5.2.2</h2>
<p>I have some dcm data download from TCIA, which typically contains the dicom series and a segmentation file also with dcm format.<br>
My problem is, I cannot figure out a way that demonstrates both the usual 3D volume and the segmentation (with different color) at the same time, on the same viewing, by using 3d slicer.<br>
I had some experience by using itk-snap for that purpose–simply load the 3D volume and then load the segmentation (usually nii.gz format). But here on on 3d slicer, I couldn’t do that, after studying for half day.<br>
Anyone can help to give some suggestion, better with some step-by-step guide or video tutorial?</p>

---

## Post #2 by @lassoan (2023-05-24 16:10 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#dicom-import">Reader for DICOM Segmentation IOD is provided by QuantitativeReporting extension</a>. Install this extension before attempting to load segmentations from DICOM.</p>
<p>If you load a segmentation from a NRRD or NIFTI image file then choose “Segmentation” in the “Description” column in the “Add Data” window.</p>
<p>Rationale: The same file can be interpreted many ways. For example an “image” file may contain a CT image, a segmentation, a displacement field, a transform, etc. Often it is impossible to tell automaticall how an image should be used, but the user has to specify it. In ITK-Snap, you use a different menu actions (“Open main image” or “Open segmentation”) to tell how to use the image. But in Slicer you have dozens of data types (images, segmentations, transforms, models, tables, points, curves, planes, etc.) that can be loaded from many different file formats. Therefore, in Slicer it would not be feasible to use dedicated file loading menu actions, but there is one centralized “Add data” window and you can set in the “Description” column how each data file should be loaded.</p>

---

## Post #3 by @Liang_Ma (2023-05-30 11:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="29627">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#dicom-import" rel="noopener nofollow ugc">QuantitativeReporting extension </a>.</p>
</blockquote>
</aside>
<p>Thanks, however, I can not find the “Quantitative reporting” extension in the extension manager.  The closer one is “DCMQI”… Can you please suggest where can I find the right extension?</p>

---

## Post #4 by @lassoan (2023-05-30 19:29 UTC)

<p>You can go to the “Install extensions” tab and type “Quantitative” in the searchbox in the top-right corner.</p>

---
