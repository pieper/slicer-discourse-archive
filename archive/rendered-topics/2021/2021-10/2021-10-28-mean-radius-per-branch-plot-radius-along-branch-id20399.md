# Mean radius per branch + plot radius along branch

**Topic ID**: 20399
**Date**: 2021-10-28
**URL**: https://discourse.slicer.org/t/mean-radius-per-branch-plot-radius-along-branch/20399

---

## Post #1 by @ames (2021-10-28 07:35 UTC)

<p>Dear all,</p>
<p>I am processing a surface model of the LIMA-LAD bypass in VMTK. I managed to split the domain in separate regions using VMTKBranchExtractor and VMTKBranchClipper, as shown in the figure. For each branch I want to compute its length and its mean radius and I would like to plot the radius along the length of each branch. Using VMTKBranchGeometry I can obtain the length of each branch, but I can’t find how to obtain the radius values for each branch separately.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea7572ce8d6f17f2e37cf39fa96486e5705074c4.png" data-download-href="/uploads/short-url/xs7mkPQY6XSd8sHnEIdXGrJNwm8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7572ce8d6f17f2e37cf39fa96486e5705074c4_2_601x500.png" alt="image" data-base62-sha1="xs7mkPQY6XSd8sHnEIdXGrJNwm8" width="601" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7572ce8d6f17f2e37cf39fa96486e5705074c4_2_601x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea7572ce8d6f17f2e37cf39fa96486e5705074c4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea7572ce8d6f17f2e37cf39fa96486e5705074c4.png 2x" data-dominant-color="F7F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">683×568 48.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can someone help me with either using VMTK functions or working with VTK PolyData in obtaining the radius for each branch? I am developing my workflow in Python</p>
<p>Thanks in advance for any suggestions!</p>

---

## Post #2 by @kayarre (2021-11-04 21:02 UTC)

<p>I have thought about this. The solution I came up with is to divide the volume of the region by the centerline and that would give then average area of the vessel.</p>
<p>steps would be:</p>
<ul>
<li>extract each vessel region</li>
<li>close the surface and compute the volume (straight forward for triangular surface mesh)</li>
<li>extract the vessel region centerline</li>
<li>calculate the length of vessel centerline</li>
<li>divide volume by the centerline length and viola average vessel area.</li>
</ul>
<p>Another thing you could do:<br>
The centerlines already have the radius values so convert the centerlines to a a graph and split the network at the junction locations. then plot each centerline.</p>

---

## Post #3 by @ames (2021-11-10 15:23 UTC)

<p>Thanks Kurt for your suggestions, interesting approach! I managed to read the VTP-files in Python and get the desired output.</p>

---
