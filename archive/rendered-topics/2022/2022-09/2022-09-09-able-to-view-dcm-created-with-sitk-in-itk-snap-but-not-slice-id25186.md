# Able to view DCM created with SITK in ITK Snap but not Slicer

**Topic ID**: 25186
**Date**: 2022-09-09
**URL**: https://discourse.slicer.org/t/able-to-view-dcm-created-with-sitk-in-itk-snap-but-not-slicer/25186

---

## Post #1 by @SaraLyn (2022-09-09 23:47 UTC)

<p>Hello!</p>
<p>I have written a 3D DCM with SITK and am able to view it in ITK Snap. However, this DCM has color overlays which ITK Snap only displays greyscale, so I would like to view it in Slicer. For this project, the image must be saved as DCM.</p>
<p>The DCM, as written, is not viewable in Slicer. If I use the DICOM Patcher plugin in 3D Slicer, it produces DCM slices stored in individual folders that load properly into Slicer. Modifications to the DCM header produced by Slicer include: Image Position &amp; Instance Number.</p>
<p>However, this change appears off. For example, in the patched image, slice 0 has Image Position -z of -2.5 whereas slice 3 has z position 37.1 in spite of the fact that slice thickness is 3.6 mm. The original DCM I wrote has correct z positions of slice 0: -2.5 and slice 3: 8.3</p>
<p>Directions here were used as a basis to write the DCM:<br>
<a href="https://simpleitk.readthedocs.io/en/v1.1.0/Examples/DicomSeriesReadModifyWrite/Documentation.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://simpleitk.readthedocs.io/en/v1.1.0/Examples/DicomSeriesReadModifyWrite/Documentation.html</a></p>
<p>When I attempt to load a single DCM into Slicer, I get the message:</p>
<p>Error: Loading [DCM_slice.dcm] - load failed.</p>
<p>Is there minimal header info that must be included to load a DCM into slicer that is not included in the above example?</p>
<p>Are there changes being made other than to the DCM header by the Patcher?</p>
<p>Is there a way to see what exactly is causing the load to fail in Slicer?</p>
<p>Please let me know if you have any suggestions how to approach this. Thank you!</p>

---

## Post #2 by @lassoan (2022-09-10 12:49 UTC)

<aside class="quote no-group" data-username="SaraLyn" data-post="1" data-topic="25186">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e5b9ba/48.png" class="avatar"> SaraLyn:</div>
<blockquote>
<p>this DCM has color overlays which ITK Snap</p>
</blockquote>
</aside>
<p>Image overlays are very obsolete method for limited annotation of images that was never intended to be used for storing image segmentation. I would strongly recommend not to use it.</p>
<p>Instead, DICOM Segmentation Object should be used for storing image segmentation.</p>
<p>Slicer can read/write segmentation as DICOM Segmentation Object after you install Quantitative Reporting extension. Outside Slicer, you can use DCMQI tool to read/write DICOM Segmentation Objects.</p>

---
