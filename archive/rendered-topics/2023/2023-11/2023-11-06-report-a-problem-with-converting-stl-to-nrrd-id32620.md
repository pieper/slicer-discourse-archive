# Report a problem with converting stl to nrrd

**Topic ID**: 32620
**Date**: 2023-11-06
**URL**: https://discourse.slicer.org/t/report-a-problem-with-converting-stl-to-nrrd/32620

---

## Post #1 by @Chuan (2023-11-06 09:03 UTC)

<p>Hi,</p>
<p>I would like to report a problem with converting stl file to nrrd.file.<br>
The red figure is my stl file of a skeleton model. I would like to convert it to nrrd file, and my process is right click my stl model, and choose ‘convert model to segmentation node’, and resave as nrrd file instead of seg.nrrd file.</p>
<p>And the problem occurs, there are several extra bars in my skeleton model (See the yellow figure).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6274da738614367c0893278106cfc1e60bd8fd7.png" data-download-href="/uploads/short-url/wQ21yTb3CUp73rwW45CqrxuyGQD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6274da738614367c0893278106cfc1e60bd8fd7_2_348x500.png" alt="image" data-base62-sha1="wQ21yTb3CUp73rwW45CqrxuyGQD" width="348" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6274da738614367c0893278106cfc1e60bd8fd7_2_348x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6274da738614367c0893278106cfc1e60bd8fd7_2_522x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6274da738614367c0893278106cfc1e60bd8fd7_2_696x1000.png 2x" data-dominant-color="998FBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">975×1397 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b61d930c41e08aec99c4ce90869714fac75953d.png" alt="image" data-base62-sha1="jT20tiR8kDoFxyrEMEH6lyUTWr3" width="513" height="225"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10256023cfc045eeef832d3dd4e2f58084adb3e3.jpeg" data-download-href="/uploads/short-url/2iPIpkgUqjvgCYGfLlnWpMeczU7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10256023cfc045eeef832d3dd4e2f58084adb3e3_2_415x500.jpeg" alt="image" data-base62-sha1="2iPIpkgUqjvgCYGfLlnWpMeczU7" width="415" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10256023cfc045eeef832d3dd4e2f58084adb3e3_2_415x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10256023cfc045eeef832d3dd4e2f58084adb3e3_2_622x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10256023cfc045eeef832d3dd4e2f58084adb3e3.jpeg 2x" data-dominant-color="63636D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">698×840 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To me, it is very strange when I convert my stl model to nrrd, 3D slicer adds some extra voxel on my model. I tried version  5.0.3 and 4.10.2, both of them have the same problem.<br>
I am really confused, and hope someone can tell me how to fix this problem. I can share my stl model if anyone wants to test byself.</p>
<p>Best,<br>
Chuan</p>

---

## Post #2 by @pieper (2023-11-06 15:47 UTC)

<p>It’s very common for STL files to have small artifacts that lead to errors like this when converting to labelmaps.  A few things you might try are changing the resolution of the segmentation, slightly rotating and hardening the models a bit before converting, or using the Surface Toolbox module to clean up the meshes before conversion.</p>

---
