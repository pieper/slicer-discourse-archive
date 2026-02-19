---
topic_id: 2287
title: "Surface Similarity Of A Model"
date: 2018-03-11
url: https://discourse.slicer.org/t/2287
---

# Surface similarity of a model

**Topic ID**: 2287
**Date**: 2018-03-11
**URL**: https://discourse.slicer.org/t/surface-similarity-of-a-model/2287

---

## Post #1 by @Joelle (2018-03-11 14:27 UTC)

<p>Hi</p>
<p>I got an image of a person and my goal is to compare the left and the right side of the face and get the similarity or difference of it’s surface. Best would be to only compare a region of interest.</p>
<p>This is an example of an input data:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f1091ac3a312c4ddf92ee00c905d27a7ddfed13.jpeg" data-download-href="/uploads/short-url/4qOiDpGy8GqZ4jQdeVYCzx3Vof9.jpg?dl=1" title="47" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f1091ac3a312c4ddf92ee00c905d27a7ddfed13_2_690x375.jpg" alt="47" data-base62-sha1="4qOiDpGy8GqZ4jQdeVYCzx3Vof9" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f1091ac3a312c4ddf92ee00c905d27a7ddfed13_2_690x375.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f1091ac3a312c4ddf92ee00c905d27a7ddfed13_2_1035x562.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f1091ac3a312c4ddf92ee00c905d27a7ddfed13_2_1380x750.jpg 2x" data-dominant-color="9092BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">47</span><span class="informations">2962×1610 397 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>sample .vtk file (<a href="https://www.dropbox.com/s/5239zh4og3mroc3/sample%20face.vtk?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - sample face.vtk - Simplify your life</a>)</p>
<p>What have I done so far:<br>
I was able to mirror the model and then tried comparing the surface using the CMFreg (<a href="https://www.slicer.org/wiki/Documentation/4.4/Extensions/CMFreg" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.4/Extensions/CMFreg - Slicer Wiki</a>) extension feature surface registration (<a href="https://www.slicer.org/wiki/Documentation/4.4/Modules/SurfaceRegistration" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.4/Modules/SurfaceRegistration - Slicer Wiki</a>). I wasn’t able to compare the faces so far.</p>
<p>I’m relatively new to 3D Slicer and therefor would appreciate any advice to solve this problem.</p>
<p>Thanks<br>
Joëlle</p>
<p>Operating system: Mac os x<br>
Slicer version: 4.7</p>

---

## Post #2 by @timeanddoctor (2018-03-11 14:48 UTC)

<p>After getting a mirror modle(example: Cura,free software), you can define the modle with different colors, and then register by transform(or surface registration in SlicerIGT module). You will find the different areas.</p>

---

## Post #3 by @lassoan (2018-03-11 17:33 UTC)

<p>You can mirror a model using Surface Toolbox module, register using SlicerIGT extensions Fiducial registration wizard module, and fine-tune using Model registration module. You can compute differences using Model distance extension.</p>

---

## Post #4 by @Joelle (2018-03-14 18:11 UTC)

<p>Thanks a lot for the answer.<br>
With your help I was able to mirror the model and then apply fiducial registration. The IGT Extension gives me the RMS error for the total model. I would like to calculate only the RMS for a specific region. My idea is to crop the image before mirroring but.</p>
<p>Are there other better options to calculate the RMS for a specific region?</p>
<p>Again thanks a lot, you were a great help. Wouldn’t have achieved it without your comments.</p>

---
