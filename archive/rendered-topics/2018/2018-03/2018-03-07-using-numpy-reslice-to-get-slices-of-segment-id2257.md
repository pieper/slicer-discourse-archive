---
topic_id: 2257
title: "Using Numpy Reslice To Get Slices Of Segment"
date: 2018-03-07
url: https://discourse.slicer.org/t/2257
---

# Using numpy reslice to get slices of segment

**Topic ID**: 2257
**Date**: 2018-03-07
**URL**: https://discourse.slicer.org/t/using-numpy-reslice-to-get-slices-of-segment/2257

---

## Post #1 by @hherhold (2018-03-07 13:42 UTC)

<p>Hey guys (and especially Andras! (<a class="mention" href="/u/lassoan">@lassoan</a>)</p>
<p>A while back Andras helped me with a super handy python script to calculate the area of a segment’s slices slice-by-slice and put it in a table. I’ve been working on putting this into a general-use module where it uses the new plot functions to make graphs - not sure if it will be useful to anybody but me, but there it is.</p>
<p>The core of the script he provided used reslice() to reformat the segmentation data into an array of slices:.</p>
<pre><code>segmentationNode = getNode('Segmentation')
segmentId = 'Segment_1'
vimage = segmentationNode.GetBinaryLabelmapRepresentation(segmentId)

narray = vtk.util.numpy_support.vtk_to_numpy(vimage.GetPointData().GetScalars())
vshape = vimage.GetDimensions()
narrayBySlice = narray.reshape([-1,vshape[1]*vshape[2]])
</code></pre>
<p>Then the number of nonzero voxels is counted, and so on. For axial, coronal, and saggital I use different indexes into the vshape array for reshaping the array - [0] * [1], [0] * [2]. (I’m pretty sure this is where I’m going wrong. But I digress.)</p>
<p>The issue I’m having is that this works great in one direction. As a test case, I made a simple segment with a single sphere. In the axial direction, I get a very smooth curve:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/247b17008cce8257c35bb29d67e1e61d1e3fa549.png" data-download-href="/uploads/short-url/5cIUhj1KDPeYk0ul8VNC3zEeNS1.png?dl=1" title="42%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/247b17008cce8257c35bb29d67e1e61d1e3fa549_2_615x500.png" alt="42%20AM" data-base62-sha1="5cIUhj1KDPeYk0ul8VNC3zEeNS1" width="615" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/247b17008cce8257c35bb29d67e1e61d1e3fa549_2_615x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/247b17008cce8257c35bb29d67e1e61d1e3fa549_2_922x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/247b17008cce8257c35bb29d67e1e61d1e3fa549_2_1230x1000.png 2x" data-dominant-color="F9FAF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">42%20AM</span><span class="informations">1298×1054 28.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I switch to the coronal and saggital directions, the curve is very choppy - the values jump up and down around the “correct” curve line:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0e3391fce387b647d171cabf8257d0cc8c7a2fa.png" data-download-href="/uploads/short-url/rwmuR0KbgDL5cN7xRgtV02bfV6G.png?dl=1" title="56%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0e3391fce387b647d171cabf8257d0cc8c7a2fa_2_609x500.png" alt="56%20AM" data-base62-sha1="rwmuR0KbgDL5cN7xRgtV02bfV6G" width="609" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0e3391fce387b647d171cabf8257d0cc8c7a2fa_2_609x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0e3391fce387b647d171cabf8257d0cc8c7a2fa_2_913x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0e3391fce387b647d171cabf8257d0cc8c7a2fa_2_1218x1000.png 2x" data-dominant-color="F8F8F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">56%20AM</span><span class="informations">1302×1068 27.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m pretty sure this is just a misunderstanding on my part on how reslice works.</p>
<p>Here’s a snippet of how I’m doing reslice for each direction:</p>
<pre><code>  if direction == "Axial":
    narrayBySlice = narray.reshape([-1,vshape[0]*vshape[1]])
  if direction == "Coronal":
    narrayBySlice = narray.reshape([-1,vshape[0]*vshape[2]])
  if direction == "Saggital":
    narrayBySlice = narray.reshape([-1,vshape[1]*vshape[2]])
</code></pre>
<p>I’ve put the <a href="https://gist.github.com/hherhold/0492146f70ef0fc511b7b21410264481" rel="noopener nofollow ugc">module code in a gist</a> for perusal if that helps.</p>
<p>Thank you in advance for any help anyone can give!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2018-03-07 22:05 UTC)

<p>To reslice a numpy along a different axis, it is not enough to reshape. You need to swap the axes as well. See <a href="https://stackoverflow.com/questions/35226115/numpy-reshaping-multdimensional-array-through-arbitrary-axis">https://stackoverflow.com/questions/35226115/numpy-reshaping-multdimensional-array-through-arbitrary-axis</a></p>

---

## Post #3 by @hherhold (2018-03-12 12:17 UTC)

<p>Got it - this was very helpful, as always.</p>
<p>I don’t know if this kind of plot would be generally useful, but I’m happy to package it up and upload it if you think others might use it.</p>
<p>Thanks again!!!</p>
<p>-Hollister</p>

---

## Post #4 by @lassoan (2018-03-12 13:00 UTC)

<p>Any working examples may be useful for others. You can save it as a github Gist and copy the link here.</p>

---

## Post #5 by @hherhold (2018-03-12 13:21 UTC)

<p>Sounds good - <a href="https://gist.github.com/hherhold/0492146f70ef0fc511b7b21410264481" rel="nofollow noopener">Here it is.</a></p>
<p>Thanks again for your help!</p>
<p>-Hollister</p>

---
