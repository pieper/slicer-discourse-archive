---
topic_id: 7330
title: "Interpolation Between Slices"
date: 2019-06-27
url: https://discourse.slicer.org/t/7330
---

# Interpolation Between Slices

**Topic ID**: 7330
**Date**: 2019-06-27
**URL**: https://discourse.slicer.org/t/interpolation-between-slices/7330

---

## Post #1 by @Juicy (2019-06-27 03:28 UTC)

<p>Hi,</p>
<p>I have a CT scan of a head which was acquired with 4mm slices. I am trying to reduce some of the step artefacts in the segment. There seems to not be a very smooth interpolation between the axial slices. If you look in the coronal and saggital slices you can see fairly distinct steps in the volume.</p>
<p>I have tried re-sampling the volume to have isotropic voxels with both the Crop Volume module and the Resample Scalar Volume module. I have tried various interpolation methods: linear, bspline, etc the bspline is slightly better than linear but none improve it particularly. I have tried upping the voxel size all around to 1mm square, this does improve the steps but also looses a considerable amount detail in the segment.</p>
<p>Are there any suggestions to improve the interpolation and reduce these step artefacts in the volume? Usually using making Isotropic voxels works quite well at getting rid of these but this doesn’t seem to work so well on this scan as the steps seem to be in the<br>
actual volume no matter what the voxel size. Perhaps there is some kind of filter which can reduce the steppyness of the volume?</p>
<p>Thanks for reading,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7dc43b9cc84b586d4ec906654d3073bafac338a.jpeg" data-download-href="/uploads/short-url/sw2VJIP0siRqxIyrlIBmS6XV1R8.jpeg?dl=1" title="Slicer%20Question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7dc43b9cc84b586d4ec906654d3073bafac338a_2_690x456.jpeg" alt="Slicer%20Question" data-base62-sha1="sw2VJIP0siRqxIyrlIBmS6XV1R8" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7dc43b9cc84b586d4ec906654d3073bafac338a_2_690x456.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7dc43b9cc84b586d4ec906654d3073bafac338a_2_1035x684.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7dc43b9cc84b586d4ec906654d3073bafac338a.jpeg 2x" data-dominant-color="9C9D9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer%20Question</span><span class="informations">1297×858 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Operating system: Windows 7<br>
Slicer version: 4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2019-06-27 03:54 UTC)

<p>Extremely sparse volumes, such as yours, are not well suited for 3D reconstruction or analysis. <a href="https://discourse.slicer.org/t/fetal-lung-volume-calculation/578/5">You cannot utilize high in-plane resolution if your slices are so far apart</a>, as there is no information about how to fill the huge 4mm gaps between the slices.</p>
<p>To make the volume less sparse, you can crop volume with “Isotropic spacing” enabled (and increase “Spacing scale” if the volume is getting too big). You may try to further reduce staircase artifact by using <a href="https://discourse.slicer.org/t/fetal-lung-volume-calculation/578/7">Smoothing effect</a>.</p>

---

## Post #3 by @Juicy (2019-06-27 04:19 UTC)

<p>Thanks for the reply.</p>
<p>I suppose the best option would be to have a scan protocol which limits the slice spacing to 1mm-2mm or there abouts. However I don’t think this scan was taken with bio-models in mind so I was trying to see what I could do with the data as is.</p>
<p>I may try and see if the volume data is still on the CT scanner. If so they may be able to reslice the data to 1mm slices.</p>
<p>The difficulty I have found with the smoothing effects is that while they get rid of some of the steps they tend to loose a lot of fine detail etc.</p>
<p>Thanks again.</p>

---

## Post #4 by @lassoan (2019-06-27 04:28 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="3" data-topic="7330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>The difficulty I have found with the smoothing effects is that while they get rid of some of the steps they tend to loose a lot of fine detail etc.</p>
</blockquote>
</aside>
<p>This is exactly the inherent problem with sparse data. You  cannot utilize the fine details in the image slice directly, if those details are completely missing in large areas between two slices.</p>

---

## Post #5 by @Lorensen (2019-06-27 04:49 UTC)

<p>I started to implement this <a href="https://www.insight-journal.org/browse/publication/881" rel="nofollow noopener">Insight Journal Article</a> as an ITK remote module. My github repo is <a href="https://github.com/lorensen/ShapeBasedInterpolation" rel="nofollow noopener">here</a>.</p>
<p>I could attempt to revive it.</p>

---

## Post #6 by @lassoan (2019-06-27 05:12 UTC)

<p>Would this algorithm work for grayscale images?</p>
<p>For labelmap interpolation we have already integrated <a href="http://insight-journal.org/browse/publication/977" rel="nofollow noopener">this</a> ITK algorithm. I’m not sure it the method described in the Boydev2012 paper would be significantly better.</p>

---

## Post #7 by @Lorensen (2019-06-27 13:37 UTC)

<p>Boydev is for grey scale images.</p>

---

## Post #8 by @lassoan (2019-06-28 22:45 UTC)

<p>Great. It would be interesting to see how the Boydev method results compare to a simple bspline or sinc image interpolation.</p>

---

## Post #9 by @kayarre (2020-02-06 04:03 UTC)

<p>Is there a way to create a sparse volume that has gaps?</p>
<p>I am thinking of using an alpha channel that essentially blanks out slices that are absent?</p>
<p>The use case here is histology slices that have a known thickness  ( say 5 microns) and then a 25 micron gap until the next slice?<br>
The problem I see is that the image volume size will explode and be difficult to test on.</p>
<p>Any thoughts on how slicer could be used here or where ITK/VTK would make it easier?</p>

---

## Post #10 by @lassoan (2020-02-06 04:17 UTC)

<p>This should be no problem at all. You can create a “mask” segment that only contains the editable regions and then select that segment in Segment Editor / Masking / Editable area. -&gt; Inside Mask segment. To not clutter the viewers, you can hide the mask segment  or make it almost completely transparent.</p>

---
