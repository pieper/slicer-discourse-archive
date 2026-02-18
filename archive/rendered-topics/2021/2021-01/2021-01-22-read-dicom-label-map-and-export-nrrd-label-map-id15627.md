# Read Dicom label map and export .nrrd label map

**Topic ID**: 15627
**Date**: 2021-01-22
**URL**: https://discourse.slicer.org/t/read-dicom-label-map-and-export-nrrd-label-map/15627

---

## Post #1 by @diehumblex (2021-01-22 14:27 UTC)

<p>Hi! i am trying to convert dicom label map into nrrd. on save only option i get is mrd mrml and seg.vtm</p>
<p>Any help would be appreciated. Thank you.</p>
<p>About Dataset: I am using HN1 dataset for this. Each patient contains 3 folders. 1 contains patients dicom scans while other 2 contains single dicom files. 1 labeled segment (~4MB) while other has named as ID(700kb). when i load only ID folder with single dicom file i get segments on slicer 3d and on loading folder named Segment i get metadata (not sure why its 4MB).</p>

---

## Post #2 by @lassoan (2021-01-22 14:47 UTC)

<p>Your segmentation is stored as RT structure set. This can be represented without information loss in <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#basic-concepts">closed surface representation</a>. If you simply save the scene then the segmentation is written to file as is - as a closed surface (VTK multi-block data set containing a surface mesh).</p>
<p>See information here about how to save segmentation as a labelmap volume file: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file" class="inline-onebox">Segmentations — 3D Slicer documentation</a></p>

---

## Post #3 by @diehumblex (2021-01-23 08:20 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for explaining this to me. I was able to export segments as Nrrd.</p>
<p>I have another question it would be great if you could help me with that too. As i mentioned above in my dataset there are 2 files one is of SEG modality and another is RTSTRUCT modality. My question is are the both files containing same info just in different modalities or both in combined form contain segmentation info? one file is 700kb and another is 4MB and when i try loading just ther 700kb RTstruct i was able to get the segments but when i load the 4MB SEG file i dont see anything.</p>

---

## Post #4 by @lassoan (2021-01-23 21:53 UTC)

<aside class="quote no-group" data-username="diehumblex" data-post="3" data-topic="15627">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ce7236/48.png" class="avatar"> diehumblex:</div>
<blockquote>
<p>My question is are the both files containing same info just in different modalities or both in combined form contain segmentation info? one file is 700kb and another is 4MB and when i try loading just ther 700kb RTstruct i was able to get the segments but when i load the 4MB SEG file i dont see anything.</p>
</blockquote>
</aside>
<p>SEG stores segmentation in binary labelmap representation, while RTSTRUCT stores it in planar contours representation. If you convert the RTSTRUCT to SEG then it is normal if its size is increased by 1-2 magnitudes (depending on the size of the image grid that you use for rasterizing the contours).</p>
<aside class="quote no-group" data-username="diehumblex" data-post="3" data-topic="15627">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ce7236/48.png" class="avatar"> diehumblex:</div>
<blockquote>
<p>when i load the 4MB SEG file i dont see anything</p>
</blockquote>
</aside>
<p>You need to install Quantitative Reporting extension and use a recent Slicer version. If you still have problems then send us an anonymized file that reproduces the issue, so that we can check if the file is invalid or Slicer needs improvement.</p>

---
