# Transformation matrix - RAS to LPS

**Topic ID**: 19352
**Date**: 2021-08-25
**URL**: https://discourse.slicer.org/t/transformation-matrix-ras-to-lps/19352

---

## Post #1 by @hmaguilera (2021-08-25 06:48 UTC)

<p>Hi,</p>
<p>As I read in another thread <a href="https://discourse.slicer.org/t/model-files-are-now-saved-in-lps-coordinate-system/10446">link</a> and have been observing when I export the coordinates from slicer to .json the coordinates are saved in LPS instead of RAS.</p>
<p>I wanted to transform some coordinates by using the transformation matrix given in Slicer, however, the transformation matrix is based on RAS. Is there a quick way to solve this? I’ve tried to just change the T(1,4)=T(1,4)<em>-1 and T(2,4)=T(2,4)</em>-1, but as I also have rotation this is not sufficient. My question is, what can I do with the rotation part to get the correct transformation matrix? When I store the transformation it is not converting to LPS as the spatial coordinates.</p>
<p>I am using the transformation matrix because I was not able to store my sequence of points in the transformed location. If there is a quick way to do this, that would also be perfect.</p>
<p>Thanks.<br>
Hans Martin</p>

---

## Post #2 by @muratmaga (2021-08-25 15:18 UTC)

<p>RAS to LPS involves negating values of the first two coordinates (X,Y). However, if you are going to save this, you also need to make sure that you change the coordinate system definition from 0 (RAS) to 1 (LPS) in the JSON header, so that Slicer interprets it correctly.</p>
<aside class="quote no-group" data-username="hmaguilera" data-post="1" data-topic="19352">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>I am using the transformation matrix because I was not able to store my sequence of points in the transformed location. If there is a quick way to do this, that would also be perfect.</p>
</blockquote>
</aside>
<p>Why weren’t you able to save your points in the transformed location? You can either save the whole scene which should preserve all nodes, and hierarchies. Or you can “harden” (i.e., apply) the transform to the fiducial node and save. if you do this all points would be in the new transformed coordinates.</p>

---

## Post #3 by @lassoan (2021-08-26 03:39 UTC)

<aside class="quote no-group" data-username="hmaguilera" data-post="1" data-topic="19352">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>however, the transformation matrix is based on RAS.</p>
</blockquote>
</aside>
<p>Transforms (and all other node types) are saved to files in LPS coordinate system.</p>
<p>When your save transforms to files then there is a switch of direction (modeling/resampling) as well, because ITK transform files store the resampling transform (that is the inverse of the modeling transform). Probably that was what you did not expect. See detailed description <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/transforms.html#transform-files">here</a> and example code to convert between RAS/LPS and modelling/resampling transform <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#convert-between-itk-and-slicer-linear-transforms">here</a>.</p>

---

## Post #4 by @hmaguilera (2021-08-26 06:12 UTC)

<p>Thanks. I was able to save the Closed Curves and Fiducial nodes by “hardening”, but not with a sequence of curves. For context, I have annoted the annulus during the cardiac cycle, and wanted to transform all the annular curves to a new location, not only one.</p>
<p>By saving i mean exporting them to .json. I got problems when I exported the coordinates to .json which then converted the points from RAS to LPS, but I was using the same T-matrix as given in Slicer (i.e in RAS).</p>

---

## Post #5 by @hmaguilera (2021-08-26 06:16 UTC)

<p>Thanks.<br>
Problem for me was that i was not able to save the sequence of points in the transformed location, even with the hardening.<br>
Thanks for the example code, it seems easier than what I ended up doing. Which was:</p>
<p>Import coordinate from .json (LPS)<br>
Convert to RAS<br>
Apply T-matrix from transformation to RAS coordinate<br>
Convert back to LPS.</p>

---
