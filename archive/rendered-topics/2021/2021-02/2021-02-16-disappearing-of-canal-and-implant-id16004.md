# Disappearing of Canal and Implant

**Topic ID**: 16004
**Date**: 2021-02-16
**URL**: https://discourse.slicer.org/t/disappearing-of-canal-and-implant/16004

---

## Post #1 by @forfullstack (2021-02-16 01:12 UTC)

<p>I’m struggling on the functions of Canal and Implant.<br>
I know Canal has two display node entities of ModelDisplay and MarkupsFiducialDisplay as well as Implant.<br>
The problem is when I created Canal or Implant and click measurement button or panorama button or implant button twice then there disappears curve of canal and shape of implant in 2D slice views.<br>
Just only fiducial markers are left in the Slice view. 3D view is keeping all the shapes and curves.<br>
I’m wondering is it intended and how can I keep curves of Canal or Implant here.<br>
It seems Slice view keeps only fiducial nodes other than model nodes.<br>
Let me attach screenshots for understanding.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3f4b57145f10a7d0c87e8547a643b20835a5b5e.png" data-download-href="/uploads/short-url/pFXKHIRiyCeSH3zkMzxRBbRdffU.png?dl=1" title="canal1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3f4b57145f10a7d0c87e8547a643b20835a5b5e_2_690x333.png" alt="canal1" data-base62-sha1="pFXKHIRiyCeSH3zkMzxRBbRdffU" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3f4b57145f10a7d0c87e8547a643b20835a5b5e_2_690x333.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3f4b57145f10a7d0c87e8547a643b20835a5b5e_2_1035x499.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3f4b57145f10a7d0c87e8547a643b20835a5b5e.png 2x" data-dominant-color="8C8E92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">canal1</span><span class="informations">1190×575 24.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30caa5e46777a34b9a0ae03c461af53a64319ed9.png" data-download-href="/uploads/short-url/6XD5zMDQkEAcW9hCT9lr0Jrrjwl.png?dl=1" title="canal2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30caa5e46777a34b9a0ae03c461af53a64319ed9_2_690x349.png" alt="canal2" data-base62-sha1="6XD5zMDQkEAcW9hCT9lr0Jrrjwl" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30caa5e46777a34b9a0ae03c461af53a64319ed9_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30caa5e46777a34b9a0ae03c461af53a64319ed9_2_1035x523.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30caa5e46777a34b9a0ae03c461af53a64319ed9.png 2x" data-dominant-color="878B8F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">canal2</span><span class="informations">1204×610 24.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Regards</p>

---

## Post #2 by @lassoan (2021-02-25 19:09 UTC)

<p>Which extension/module is this?<br>
Since Slicer core now natively supports curves (vtkMRMLMarkupsCurveNode), I would recommend to use them instead of generating models from markups fiducials.</p>

---
