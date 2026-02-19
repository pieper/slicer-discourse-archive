---
topic_id: 9297
title: "Create New Vector Volume"
date: 2019-11-25
url: https://discourse.slicer.org/t/9297
---

# Create new vector volume

**Topic ID**: 9297
**Date**: 2019-11-25
**URL**: https://discourse.slicer.org/t/create-new-vector-volume/9297

---

## Post #1 by @sthirumal (2019-11-25 17:54 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.1</p>
<p>I am trying to create a new vector volume (since I need a colour image) and am wondering how to go about coding this.</p>

---

## Post #2 by @lassoan (2019-11-25 19:48 UTC)

<p>You can create a new volume node as shown in this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume</a></p>
<p>For creating a vector volume: use <code>vtkMRMLVectorVolumeNode</code> instead of <code>vtkMRMLScalarVolumeNode</code> and in <code>AllocateScalars</code> use 3 components instead of just 1.</p>

---

## Post #3 by @sthirumal (2019-11-27 16:53 UTC)

<p>Thank you Andras! For some reason when I assign a volume to my new empty vector volume, the image is being rotated 180 degrees. The array of voxels for the volume is correct and so I’m confused why it is appearing as rotated. Let me know if you have any idea of why this is the case!</p>
<p>Expected output:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2521c776be2d1f150fc1b2d747b24d4f269d7f2a.png" data-download-href="/uploads/short-url/5iu2lJUutek0jWXvfX2LXPguKmK.png?dl=1" title="rotated%20-%20expected" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2521c776be2d1f150fc1b2d747b24d4f269d7f2a_2_499x500.png" alt="rotated%20-%20expected" data-base62-sha1="5iu2lJUutek0jWXvfX2LXPguKmK" width="499" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2521c776be2d1f150fc1b2d747b24d4f269d7f2a_2_499x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2521c776be2d1f150fc1b2d747b24d4f269d7f2a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2521c776be2d1f150fc1b2d747b24d4f269d7f2a.png 2x" data-dominant-color="626D17"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rotated%20-%20expected</span><span class="informations">604×605 787 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Actual output:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb10d3c7f0c3ae084a456cf2adfa65d648b681f9.png" data-download-href="/uploads/short-url/qGRl20G7bkhypMqyWzZPQF86dJL.png?dl=1" title="rotated%20-%20actual" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb10d3c7f0c3ae084a456cf2adfa65d648b681f9_2_500x500.png" alt="rotated%20-%20actual" data-base62-sha1="qGRl20G7bkhypMqyWzZPQF86dJL" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb10d3c7f0c3ae084a456cf2adfa65d648b681f9_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb10d3c7f0c3ae084a456cf2adfa65d648b681f9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb10d3c7f0c3ae084a456cf2adfa65d648b681f9.png 2x" data-dominant-color="626D17"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rotated%20-%20actual</span><span class="informations">607×606 791 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-11-27 16:56 UTC)

<p>Slicer uses RAS coordinate system. If your image array is in LPS coordinate system (this is the most common) then you need to set <code>imageDirections = [[-1,0,0], [0,-1,0], [0,0,1]]</code>.</p>
<p>Do you load the data from file? Why don’t you load them using standard image loading functions?</p>

---

## Post #5 by @sthirumal (2019-11-27 19:25 UTC)

<p>This works, thank you Andras!</p>

---

## Post #6 by @lassoan (2019-11-27 20:12 UTC)

<p>Do you load the data from file? Why can’t you load them using standard image loading functions?</p>

---

## Post #7 by @lassoan (2021-10-15 14:48 UTC)

<p>A post was split to a new topic: <a href="/t/combine-3-scalar-volumes-into-a-vector/20172">Combine 3 scalar volumes into a vector</a></p>

---

## Post #8 by @PauRo (2025-09-02 14:32 UTC)

<p>Hi,</p>
<p>Unfortunately the link leads to a dead end and I’m insterested in a similar procedure.</p>
<p>My actual goal is to combine 3 scalar volumes Vx, Vy, and Vz into a vector volume to then compute a new scalar volume corresponding to the magnitude of the vector volume, does that make sense from the 3D slicer point of view?</p>
<p>Thanks in advance,</p>
<p>Pau</p>

---

## Post #9 by @lassoan (2025-09-02 15:46 UTC)

<p>The script repository has moved to readthedocs. Here is the direct link to the code snippet: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---
