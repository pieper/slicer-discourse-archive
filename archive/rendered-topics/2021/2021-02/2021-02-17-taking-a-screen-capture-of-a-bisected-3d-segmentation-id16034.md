# Taking a screen capture of a bisected 3D segmentation

**Topic ID**: 16034
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/taking-a-screen-capture-of-a-bisected-3d-segmentation/16034

---

## Post #1 by @Hannnonk (2021-02-17 16:24 UTC)

<p>Operating system:<br>
Slicer version:13<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Have a 3D segmentation <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea0005fe0699df059085e5e18ce2f29fbac2622b.jpeg" alt="slicer Q1" data-base62-sha1="xo3Mfxe3PGtfDPdqjaCec5wRJ7d" width="551" height="385"></p>
<p>formed from many segments. Would like to “Bisect” it (or put into sections) for an image from the "middle " of the 3D model. The area of the “middle” would vary. Is there an easy way to do this?</p>
<p>Scissors seem to only cut the selected segment…and I dont want to “change” the main file…</p>
<p>thanks<br>
KH</p>

---

## Post #2 by @pieper (2021-02-17 16:54 UTC)

<p>If you want to see the cut-through view you could just use the slice view and turn the slice fill opacity to full, and if the slice isn’t exactly aligned where you want it you can use the reformat module to tilt it to match the section of interest.  Is that not what you are looking for?  Or did you need to see the cut in 3d?</p>

---

## Post #3 by @Hannnonk (2021-02-17 17:27 UTC)

<p>Thanks Steve- no I would like to see the cut in 3D…<br>
thanks<br>
KH</p>

---

## Post #4 by @lassoan (2021-02-17 18:36 UTC)

<p>Plane cut (in 3D) is currently only supported for models, so you need to right-click on the segmentation (in Data module) and export to models, then hide the segmentation.</p>
<p>You can then go to <em>Models</em> module, select all the models you want to clip, and enable <em>Clip selected model</em> in <em>Clipping planes</em> section.</p>
<p>If you want to cap the cut surface then you can use <em>Dynamic Modeler</em> module’s <em>Plane cut</em> tool.</p>

---

## Post #5 by @vet0282 (2021-02-18 18:51 UTC)

<p>Hi Kevin,</p>
<p>Nice segmentation!!</p>
<p>I think that you are looking for ‘Clipping’ of 3D models.<br>
You can make 3D models from your segmentation.  Then, go to ‘model<br>
module’.  There will be ‘Clipping planes’ dropdown in the low part of the<br>
module.<br>
Then, you can simply choose which place you want to clip with and move a<br>
slide bar of the selected slice.</p>
<p>If the CT scan is not straight, you can reslice the images based on the<br>
axis you draw.</p>
<p>Sun</p>

---

## Post #6 by @da5ideber (2024-02-26 18:21 UTC)

<p>Hello, checking in on this -  will clipping ever be supported for segmentations? I am currently trying to segment skulls for a lot of scans and seeing inside the skull in the 3D view would make this much much faster, but I cannot find any tools that allow you to crop the 3D view while still allowing you to edit the segmentation.</p>

---

## Post #7 by @mikebind (2024-02-26 19:47 UTC)

<p>If I need to edit inside of a segment and it’s presence in the 3D view obscures what I want to see, I usually just hide that segment (i.e. close the eye icon for it).  I haven’t run into a use case where I really need to simultaneously see just a portion of another segment in addition to the segment I am editing.  Note that, if desired, you can still prevent a new segment from spilling over into existing segments (even invisible ones) by setting the masking editable area to “Outside all segments”.</p>

---
