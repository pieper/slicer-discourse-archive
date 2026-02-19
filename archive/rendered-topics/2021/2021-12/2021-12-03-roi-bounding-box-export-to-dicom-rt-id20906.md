---
topic_id: 20906
title: "Roi Bounding Box Export To Dicom Rt"
date: 2021-12-03
url: https://discourse.slicer.org/t/20906
---

# ROI bounding box export to DICOM RT

**Topic ID**: 20906
**Date**: 2021-12-03
**URL**: https://discourse.slicer.org/t/roi-bounding-box-export-to-dicom-rt/20906

---

## Post #1 by @alireza (2021-12-03 22:21 UTC)

<p>Is it possible to export ROI bounding box annotations to DICOM RT (I know it is not the perfect export type, but I need it to be DICOM RT)? When I export it, and import it back it doesn’t show what I expect (contours).</p>
<p>Here is what I’m doing in more detail:</p>
<ol>
<li>
<p>I have loaded a study and drawn a 3D bounding box<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc6893fba3914dc2a5ed6be154bc7d6bccee9499.jpeg" data-download-href="/uploads/short-url/vrP6g4zcEKjVu6q5T7m0f89v7xD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc6893fba3914dc2a5ed6be154bc7d6bccee9499_2_624x500.jpeg" alt="image" data-base62-sha1="vrP6g4zcEKjVu6q5T7m0f89v7xD" width="624" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc6893fba3914dc2a5ed6be154bc7d6bccee9499_2_624x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc6893fba3914dc2a5ed6be154bc7d6bccee9499_2_936x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc6893fba3914dc2a5ed6be154bc7d6bccee9499_2_1248x1000.jpeg 2x" data-dominant-color="43434B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1287×1031 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>I put the MarkupsROI under the CT series in data hierarchy<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/380a7fa4bb0150d7e0c4e0a0bcc166f4ce181a67.png" alt="image" data-base62-sha1="7ZLelUKxraRHwMyneAsmeqyTBxJ" width="510" height="104"></p>
</li>
<li>
<p>Right click on the Series and select RT as the export type<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97160f4f24b3bc54be9bee3f88f6c84891135b9f.png" data-download-href="/uploads/short-url/lyzmnt89UH95e3MO67VH5uL33vV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97160f4f24b3bc54be9bee3f88f6c84891135b9f_2_529x500.png" alt="image" data-base62-sha1="lyzmnt89UH95e3MO67VH5uL33vV" width="529" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97160f4f24b3bc54be9bee3f88f6c84891135b9f_2_529x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97160f4f24b3bc54be9bee3f88f6c84891135b9f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97160f4f24b3bc54be9bee3f88f6c84891135b9f.png 2x" data-dominant-color="EAEAEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">654×617 62.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>It creates bunch of dicom files, but none are RT struct<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d3b2d31e65afec2ddae4b5cd91610195dfebc4e.png" data-download-href="/uploads/short-url/4aADaDR4xwrYw2axkGMwAiXFDHw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d3b2d31e65afec2ddae4b5cd91610195dfebc4e_2_690x234.png" alt="image" data-base62-sha1="4aADaDR4xwrYw2axkGMwAiXFDHw" width="690" height="234" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d3b2d31e65afec2ddae4b5cd91610195dfebc4e_2_690x234.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d3b2d31e65afec2ddae4b5cd91610195dfebc4e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d3b2d31e65afec2ddae4b5cd91610195dfebc4e.png 2x" data-dominant-color="D9DDE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">784×267 66.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>

---

## Post #2 by @cpinter (2021-12-07 09:40 UTC)

<p>Hi Alireza,</p>
<p>Annotation objects cannot be exported to DICOM RT structure sets, only segmentations. So from the study you want to export, only the CT is actually considered. I’m not aware of an easy way to convert ROI node to segmentation node. What I can suggest is that you define the ROI using Segment Editor’s Scissors effect. If you replace the MarkupsROI node with that segmentation node in your sucbject hierarchy and do the export the same way then the ox should be exported to RTSS.</p>

---

## Post #3 by @alireza (2021-12-07 13:56 UTC)

<p>Thanks Csaba for your reply.</p>

---
