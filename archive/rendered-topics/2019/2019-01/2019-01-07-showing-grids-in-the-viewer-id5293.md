# Showing grids in the viewer

**Topic ID**: 5293
**Date**: 2019-01-07
**URL**: https://discourse.slicer.org/t/showing-grids-in-the-viewer/5293

---

## Post #1 by @feng (2019-01-07 10:49 UTC)

<p>Is it possible to show grids in the viewer like this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3340b546de5f985c0cdcd643c0e534a7faf4212.png" data-download-href="/uploads/short-url/nhLkAaqB6VD3TA43WHv7LutNGHU.png?dl=1" title="Image result for MRI image with grids" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3340b546de5f985c0cdcd643c0e534a7faf4212.png" alt="Image result for MRI image with grids" data-base62-sha1="nhLkAaqB6VD3TA43WHv7LutNGHU" width="690" height="445" data-dominant-color="464E4E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image result for MRI image with grids</span><span class="informations">724×467 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2019-01-07 13:42 UTC)

<p>Yes, one way to do that is to make an identity transform and turn on display.  Go to transforms module, create a linear transform, then turn on ‘visible in slice views’.  I changed the lookup table to make it white instead of black.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e5f915012dd275ab7855d73cfa63e90dddc3327.jpeg" data-download-href="/uploads/short-url/6CeIpBLbHK5806GQYDkf4STrq1F.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e5f915012dd275ab7855d73cfa63e90dddc3327_2_690x356.jpeg" alt="image" data-base62-sha1="6CeIpBLbHK5806GQYDkf4STrq1F" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e5f915012dd275ab7855d73cfa63e90dddc3327_2_690x356.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e5f915012dd275ab7855d73cfa63e90dddc3327_2_1035x534.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e5f915012dd275ab7855d73cfa63e90dddc3327_2_1380x712.jpeg 2x" data-dominant-color="AFAEAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1844×954 367 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @nabid (2020-12-02 01:59 UTC)

<p>Is it possible to show grids in the 3D viewer for regions: Red, Yellow, Green at the same time? Please see the attached image. Or can this be done using some other module?<br>
Thanks.<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/192f60ad5b1168f7b31bd5bdcef229cbcaaed3f6.png" alt="Untitled" data-base62-sha1="3ANrsuYwuBb0URHVyzNJie4Q0FE" width="347" height="366"></p>

---

## Post #4 by @lassoan (2020-12-02 02:10 UTC)

<p>There are lots of options for displaying various grids in 2D and 3D. Over the past few decades we also developed a number of other techniques to convey spatial relationships, distances, etc. between objects. Can you tell a bit about what you would like to achieve?</p>

---

## Post #5 by @nabid (2020-12-02 02:15 UTC)

<p>Thanks for your reply.<br>
I like to display the segmented volume in a 3D XYZ coordinate system (grid). Please let me know how to do it. Using the transform module, it shows a box of grid and the segmented object is not nicely visible. Please see the image in the previous post.</p>

---

## Post #6 by @lassoan (2020-12-02 02:38 UTC)

<p>Can you tell what is your end goal? Why would you like to show grid planes?</p>

---

## Post #7 by @nabid (2020-12-02 02:41 UTC)

<p>The volume of the segmented object will change over time. I want to show the 3D segmented objects in two windows side by side. 3D grid planes help to understand that they are 3D objects.</p>

---
