# Put a fan-shaped mask to an image displayed in a slice view

**Topic ID**: 1644
**Date**: 2017-12-12
**URL**: https://discourse.slicer.org/t/put-a-fan-shaped-mask-to-an-image-displayed-in-a-slice-view/1644

---

## Post #1 by @urbancsaba (2017-12-12 11:30 UTC)

<p>Hi Folks,</p>
<p>I have a CT volume displayed axially in a slice view. On this volume I perform different kind of algorithms (this is not the point now) to produce ultrasound-like images.</p>
<p>My question is, how can I apply a mask to convert (or to shape) the slices into a fan-shaped slice, like the (convex) ultrasound images look like?</p>
<p>Thanks,<br>
Csaba</p>

---

## Post #2 by @lassoan (2017-12-12 14:06 UTC)

<p>The easiest is probably to create a mask image and use it to mask the processed CT:</p>
<ul>
<li>Create a mask image: it can be a single-slice volume that is non-zero inside the fan and zero outside</li>
<li>In slice view controller: select mask image as background, and the CT as foreground imagecontroller</li>
<li>In Volumes module: apply thresholding to the mask volume to hide voxels that has zero value - this not only hides mask volume contents but also the foreground</li>
<li>To move around this slice: apply a transform to the mask image, and use mask image as Driver in Volume Reslice Driver module (available in SlicerIGT extension)</li>
</ul>

---

## Post #3 by @jcfr (2017-12-12 17:09 UTC)

<p>Cc: <a class="mention" href="/u/dzenanz">@dzenanz</a> <a class="mention" href="/u/thewtex">@thewtex</a></p>

---

## Post #4 by @thewtex (2017-12-12 17:40 UTC)

<p>It is possible to create the mask by inputting a uniform image to the <code>SlicerITKUltrasound</code> extension module for a <a href="https://kitwaremedical.github.io/SlicerITKUltrasoundDoc/Modules/ScanConversion/CurvilinearArray.html" rel="nofollow noopener">curvilinear array</a> or a <a href="https://kitwaremedical.github.io/SlicerITKUltrasoundDoc/Modules/ScanConversion/PhasedArray3D.html" rel="nofollow noopener">3D phased array</a>.</p>

---
