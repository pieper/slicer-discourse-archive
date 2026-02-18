# Smoothing causes offset of portion of copied segment

**Topic ID**: 21340
**Date**: 2022-01-05
**URL**: https://discourse.slicer.org/t/smoothing-causes-offset-of-portion-of-copied-segment/21340

---

## Post #1 by @hherhold (2022-01-05 17:59 UTC)

<p>I have a large segment (whole body) and I want to make a copy of this and delete everything but the head. This all works fine, except when I view the head segment and the body segment in the 3D view with smoothing turned on, the head only segment is offset by a few pixels. This is only in the 3D view and only if smoothing is turned on.</p>
<p>Here is body (orange) and head (blue) together, with smoothing turned off. Blue is a direct copy of orange.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40a781c76dc70c599c396cb255d4649b119f3aba.jpeg" data-download-href="/uploads/short-url/9dXrhIlWvYmXqxYZVBuUCJ7bFWi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40a781c76dc70c599c396cb255d4649b119f3aba_2_589x500.jpeg" alt="image" data-base62-sha1="9dXrhIlWvYmXqxYZVBuUCJ7bFWi" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40a781c76dc70c599c396cb255d4649b119f3aba_2_589x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40a781c76dc70c599c396cb255d4649b119f3aba_2_883x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40a781c76dc70c599c396cb255d4649b119f3aba.jpeg 2x" data-dominant-color="A7B3CC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">958×812 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Now, head and body with smoothing on, set to 0.1:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2206c538d3d994dbbe8411b0c5b53c7457160eb0.jpeg" data-download-href="/uploads/short-url/4R0JQFc4dGV6Z1R3avGP7tRFLdC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2206c538d3d994dbbe8411b0c5b53c7457160eb0_2_664x499.jpeg" alt="image" data-base62-sha1="4R0JQFc4dGV6Z1R3avGP7tRFLdC" width="664" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2206c538d3d994dbbe8411b0c5b53c7457160eb0_2_664x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2206c538d3d994dbbe8411b0c5b53c7457160eb0_2_996x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2206c538d3d994dbbe8411b0c5b53c7457160eb0.jpeg 2x" data-dominant-color="C8C0B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1186×892 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Note the shift to the right of the image of the blue segment when smoothing is turned on.</p>
<p>Any ideas? Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @mikebind (2022-01-07 22:48 UTC)

<p>Are the voxels isotropic?<br>
Ideas for investigation:</p>
<ul>
<li>What happens if you resample segmentation in this region to a higher resolution?</li>
<li>What happens if you draw or paint in thin structures in different orientations? Is the displacement always present and in a consistent direction?  For example you could paint in a sphere, hollow it so it is thin shell, and then smooth that and see what orientations lead to displacements.</li>
</ul>
<p>One idea which comes to mind is that smoothing will tend to shrink convex areas and will tend to expand concave areas, so that could explain some net motion of a structure which is concave on one side and convex on the opposite side.  However, this wouldn’t explain why two identical objects would become displaced from one another due to smoothing.</p>

---

## Post #3 by @pieper (2022-01-08 19:47 UTC)

<p>That looks to me like a bug in the smoothing.  Can you reproduce it on a simpler structure?</p>

---

## Post #4 by @hherhold (2022-01-12 12:27 UTC)

<p>Thanks for the ideas!</p>
<p>Voxels are isotropic. I’ll work on getting an example using a simpler structure.</p>

---

## Post #5 by @hherhold (2022-01-17 18:00 UTC)

<p>I think I have an example that shows the issue in a simpler structure using demo data. There are two segments, a large green one and a smaller red one that is a copy of part of the large green one. When you hide/show the segments, you can see a small shift in position of the smaller red one. It is not to the same degree as the example I showed above, this is possibly due to differences in resolution - MRHead is much lower res than the micro-CT scan from my original image.</p>
<p>Dropbox link to MRB file below.</p>
<p>Any ideas and suggestions would be most welcome! Thanks!!</p>
<p>-Hollister</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/mvcb32vfe8zmqco/AADja_YzPM2ju-QPthZ2l1VNa?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/sh/mvcb32vfe8zmqco/AADja_YzPM2ju-QPthZ2l1VNa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/sh/mvcb32vfe8zmqco/AADja_YzPM2ju-QPthZ2l1VNa?dl=0" target="_blank" rel="noopener nofollow ugc">Slicer-smoothing-issue</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @cpinter (2022-01-17 20:25 UTC)

<p>For issues like this I have always used a little 10x10x10 voxel image with some segmentation. You can find it in the SampleData module, it’s called TinyPatient. The shift will be very obvious if it’s there.</p>

---

## Post #7 by @mikebind (2022-01-18 19:14 UTC)

<p>Is there a component of the smoothing algorithm which takes into account the total size of the object to be smoothed?  If, for example, the bounding box size were used to normalize something, the bounding box size is quite different in both these cases.</p>
<p>If I turn off all smoothing on the segments <a class="mention" href="/u/hherhold">@hherhold</a> generated, the surface renderings look identical (as they should).  At other smoothing factors, there are definite, but small, shifts between the surfaces.  The error may show up as an error in physical dimensions or in voxel dimensions, so it makes sense to play with both of those. I’ll take a look at TinyPatient if I get a chance.</p>

---

## Post #8 by @pieper (2022-01-18 19:32 UTC)

<p>I’ve seen things like this happen in the past when data is resampled but a shift in the origin is not taken into account.  Since, like DICOM, our origin is in the center of a voxel and not the corner, the origin is shifted when we resample the images to a different spacing without changing the physical size of the image bounds.</p>

---

## Post #9 by @lassoan (2022-01-18 23:03 UTC)

<p>As <a class="mention" href="/u/mikebind">@mikebind</a> suspected, the <code>vtkWindowedSincPolyDataFilter</code> normalizes coordinates (rescales the input to a unit cube if <code>NormalizeCoordinates</code> is enabled; which it is), therefore the smoothing result depends on the bounding box size. In general, the difference should be negligible, but it seems that it is possible to see a perceivable shift in real-world applications where the ROI size is very different along the 3 axes.</p>
<p>Disabling coordinates normalization fixes the issue, but I’ll need to check with Will Schroeder (developer of this algorithm) what other issues it may cause if we skip normalization.</p>

---

## Post #10 by @lassoan (2022-01-18 23:36 UTC)

<p>Question posted to the VTK forum:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676" target="_blank" rel="noopener" title="11:34PM - 18 January 2022">VTK – 18 Jan 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/278;"><img src="https://discourse.vtk.org/uploads/default/optimized/2X/0/093f5d3b0df40b4195b4c9cf379fac8869735b30_2_1024x413.jpeg" class="thumbnail" width="690" height="278"></div>

<h3><a href="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676" target="_blank" rel="noopener">Slight offset in vtkWindowedSincPolyDataFilter if normalization is enabled</a></h3>

  <p>When using vtkWindowedSincPolyDataFilter with NormalizeCoordinates enabled then we have found that smoothing result is slightly shifted when the bounding box of the mesh is changed.  Example   Data set:...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @hherhold (2022-01-19 00:46 UTC)

<p>Thank you very much!</p>

---
