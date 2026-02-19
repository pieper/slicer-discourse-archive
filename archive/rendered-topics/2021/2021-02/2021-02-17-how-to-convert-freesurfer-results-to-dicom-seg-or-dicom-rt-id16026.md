---
topic_id: 16026
title: "How To Convert Freesurfer Results To Dicom Seg Or Dicom Rt"
date: 2021-02-17
url: https://discourse.slicer.org/t/16026
---

# How to convert freesurfer results to DICOM-SEG or DICOM-RT?

**Topic ID**: 16026
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/how-to-convert-freesurfer-results-to-dicom-seg-or-dicom-rt/16026

---

## Post #1 by @hwkim0325 (2021-02-17 06:16 UTC)

<p>I would like to export the result (.mgz) of freesurfer to dicom-seg or dicom-RT.</p>
<p>What I’ve done so far is</p>
<p>(A) open mgz in the segmentation editor module, export it as the nifti format. But, all the segmentation labels have been messed up.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/639cd38bf46eafef6453c8285fcadb42f146834a.png" data-download-href="/uploads/short-url/eddgE4qpq9cw6GQNkAT82HlfFMe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/639cd38bf46eafef6453c8285fcadb42f146834a_2_496x500.png" alt="image" data-base62-sha1="eddgE4qpq9cw6GQNkAT82HlfFMe" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/639cd38bf46eafef6453c8285fcadb42f146834a_2_496x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/639cd38bf46eafef6453c8285fcadb42f146834a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/639cd38bf46eafef6453c8285fcadb42f146834a.png 2x" data-dominant-color="9E9DA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">594×598 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0368d5a48c62c4d786e814fe5dab637fb4ba2f2.png" data-download-href="/uploads/short-url/vZtPvKTQLBVotVuVhrbm7mCfkIi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0368d5a48c62c4d786e814fe5dab637fb4ba2f2.png" alt="image" data-base62-sha1="vZtPvKTQLBVotVuVhrbm7mCfkIi" width="398" height="500" data-dominant-color="E6E9F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">553×693 26.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(B) open the mgz file, add the new study, export as DICOM and DICOM-RT. But I received the following error message</p>
<blockquote>
<p>Segmentation object export failed.<br>
‘None Type’ object has no attribute ‘GetAttribute’</p>
</blockquote>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/9573203897731ae2bfadae56def5d2b754599b32.png" alt="image" data-base62-sha1="lk5NxP8c7irrmmcGMYxITwfNfbA" width="569" height="440"></p>

---

## Post #2 by @lassoan (2021-02-17 12:26 UTC)

<p>DICOM RT structure set can only store simple contours, not such complex segmentations as a FreeSurfer brain segmentation.</p>
<p>DICOM Segmentation Object can store arbitrarily complex segmentation. However, it requires you to refer to a reference image and that reference image must have UIDs for each frame.</p>
<p>If you don’t have the input DICOM image anymore then you can create a dummy image by the following steps:</p>
<ul>
<li>export the segmentation to a labelmap volume</li>
<li>convert the labelmap volume to scalar volume (using Volumes module → Volume Information → Convert to scalar volume)</li>
<li>export the volume to DICOM using scalar volume exporter (UIDs are generated during export), and loading that exported image</li>
<li>load the image from the DICOM database</li>
</ul>
<p>We could certainly make things simpler by automatically generating dummy volumes, but since segmentation has limited use without a real referenced volume, there has not been many requests for this.</p>
<aside class="quote no-group" data-username="hwkim0325" data-post="1" data-topic="16026">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hwkim0325/48/9940_2.png" class="avatar"> hwkim0325:</div>
<blockquote>
<p>open mgz in the segmentation editor module, export it as the nifti format. But, all the segmentation labels have been messed up</p>
</blockquote>
</aside>
<p>Nifti file format cannot store segment names in the file, therefore you need to use an external colormap file. If you use freesurfer then you can load the segmentation as a volume, then in Volumes module choose the freesurfer colormap, and then convert it to segmentation.</p>

---
