# Obtain the HU values for given 3D points with x,y,z coordinates

**Topic ID**: 19478
**Date**: 2021-09-02
**URL**: https://discourse.slicer.org/t/obtain-the-hu-values-for-given-3d-points-with-x-y-z-coordinates/19478

---

## Post #1 by @M.Odaba (2021-09-02 06:13 UTC)

<p>Hi,<br>
I’ve been trying to find a way to obtain the HU values for specific x,y,z coordinates. I explain what I’m trying to do.<br>
Let say I have a CT scan of a bone and I have generated rays in 3D space. Once these rays intersect with bone, each can generate different HU profile. So, I do have set of 3D points (x,y,z coordinates) on each ray within the bone and I need to obtain the HU value for each point in order to get the HU profile on the ray. I’m thinking of a code which can get the 3D points (x,y,z coordinates) as inputs and find the HU values. I understand that these point may not be exactly matched with voxel nodes. So, the HU value should be obtained from interpolations/extrapolations I think. Any suggestions, examples, or pre-existing codes?<br>
Thanks a lot.</p>

---

## Post #2 by @lassoan (2021-09-02 06:19 UTC)

<p>You can get an HU profile along a straight line in 3D using “Line profile” module (in Sandbox extension).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/717cf030f636744f7affc568af60b54b4b3d3169.jpeg" data-download-href="/uploads/short-url/gbXDfIn6QeVDJSgGddmA1yOTG9H.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/717cf030f636744f7affc568af60b54b4b3d3169_2_690x418.jpeg" alt="image" data-base62-sha1="gbXDfIn6QeVDJSgGddmA1yOTG9H" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/717cf030f636744f7affc568af60b54b4b3d3169_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/717cf030f636744f7affc568af60b54b4b3d3169_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/717cf030f636744f7affc568af60b54b4b3d3169_2_1380x836.jpeg 2x" data-dominant-color="E3E3DF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1165 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @M.Odaba (2021-09-08 10:19 UTC)

<p>I went through the Python code of the Line Profile, it only accepts the location of markup points manually created on the views to create a line. I need to create the line out of know coordinates in 3D space. Do you know how I can use my own points (using x,y,z coordinates) instead of manually selecting the markup points? Thanks.</p>

---
