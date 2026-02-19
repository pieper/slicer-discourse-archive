---
topic_id: 36857
title: "Inverted Growth Ratio In Boundary Layer Generation"
date: 2024-06-18
url: https://discourse.slicer.org/t/36857
---

# Inverted growth ratio in Boundary Layer generation

**Topic ID**: 36857
**Date**: 2024-06-18
**URL**: https://discourse.slicer.org/t/inverted-growth-ratio-in-boundary-layer-generation/36857

---

## Post #1 by @fil_ita (2024-06-18 07:45 UTC)

<p>Good morning,<br>
I am trying to use VMTK to genera the boundary layer of some TPMS geometries, as it is the only software that seems to have a good BL creation algorithm.</p>
<p>However, I have noticed that along my geometry, there are some regions where the growth ratio is “decreasing” rather than increasing:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4a46f5c236860d2d93207af8e4572dcb291c084.jpeg" data-download-href="/uploads/short-url/wCFa8YgRxMVkUhq4yiSoJaLwPAg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4a46f5c236860d2d93207af8e4572dcb291c084.jpeg" alt="image" data-base62-sha1="wCFa8YgRxMVkUhq4yiSoJaLwPAg" width="690" height="488" data-dominant-color="8C8B97"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">937×664 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75efc68ef61a7cf1cf2627f3339fb3565883bab7.jpeg" data-download-href="/uploads/short-url/gPjA17vOZRQbdzzpszYcOxd7dmT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75efc68ef61a7cf1cf2627f3339fb3565883bab7_2_690x355.jpeg" alt="image" data-base62-sha1="gPjA17vOZRQbdzzpszYcOxd7dmT" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75efc68ef61a7cf1cf2627f3339fb3565883bab7_2_690x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75efc68ef61a7cf1cf2627f3339fb3565883bab7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75efc68ef61a7cf1cf2627f3339fb3565883bab7.jpeg 2x" data-dominant-color="878790"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">946×488 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I was wondering if you would be able to help me in identifying the problem or suggest a workflow to bypass it.<br>
At the moment, I use the following command:</p>
<p>vmtkmeshgenerator -ifile ./cfd_mesh/fluid1.stl -minedgelength 1e-4 -maxedgelength 5e-3 -skipcapping 1 -boundarylayer 1 -thicknessfactor 8e-1 -sublayers 9 -sublayerratio 0.917 -ofile f1_vmtk.vtk -skipremeshing 1</p>
<p>Thank you in advance!</p>

---

## Post #2 by @fil_ita (2024-09-23 21:01 UTC)

<p>Hello,</p>
<p>would anyone be able to help me with this?</p>

---
