---
topic_id: 27460
title: "Unexpected Behaviour With Control Point Coordinates Outside"
date: 2023-01-25
url: https://discourse.slicer.org/t/27460
---

# Unexpected behaviour with control point coordinates outside of Slicer

**Topic ID**: 27460
**Date**: 2023-01-25
**URL**: https://discourse.slicer.org/t/unexpected-behaviour-with-control-point-coordinates-outside-of-slicer/27460

---

## Post #1 by @drobny (2023-01-25 14:53 UTC)

<p>I ran into a problem using a Slicer markup json file outside of Slicer. Either I am missing something or there might be a bug somewhere.</p>
<p>Steps to reproduce:</p>
<ul>
<li>open CTchest sample image</li>
<li>make point annotations and save the control points as a mrk.json file</li>
<li>using nibabel, load the image</li>
<li>nib.aff2axcodes(img.affine) confirms image is in LPS orientation</li>
<li>load the json file and access the coordinates</li>
<li>invert the affine matrix and apply it to the coordinates to compute voxel positions in image</li>
<li>results are not as expected, e.g. values out of image size can appear (also negative values)</li>
<li>invert first two coordinates of control points</li>
<li>convert modified world coordinates to image positions as before</li>
<li>results now correspond to expected values</li>
</ul>
<p>I have seen that the control points are saved with the header information “coordinateSystem”: “LPS” but I do not understand how this influences world coordinates in mm space. I understand that the orientation dictates how image data relate to world coordinates but does a point in mm space depend on the orientation? Shouldn’t I be able to convert these world coordinates into any image by applying the image specific affine matrix?<br>
I wonder if slicer “converts” the LPS coordinate when loading to RAS by flipping the sign on the first two coordinates and vice versa when saving. Otherwise I don’t see how things work out within Slicer but not outside.<br>
Please advice if I have an oversight here or the coordinates are saved as intended.</p>

---

## Post #2 by @lassoan (2023-01-25 20:02 UTC)

<aside class="quote no-group" data-username="drobny" data-post="1" data-topic="27460">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5daacb/48.png" class="avatar"> drobny:</div>
<blockquote>
<p>“LPS” but I do not understand how this influences world coordinates in mm space</p>
</blockquote>
</aside>
<p><code>"coordinateSystem": "LPS"</code> in the markup file means that the coordinates are specified in LPS coordinate system.</p>
<aside class="quote no-group" data-username="drobny" data-post="1" data-topic="27460">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5daacb/48.png" class="avatar"> drobny:</div>
<blockquote>
<p>nib.aff2axcodes(img.affine) confirms image is in LPS orientation</p>
</blockquote>
</aside>
<p>NIFTI always uses RAS as world (physical) coordinate system, regardless of the order or orientation of image axes. By inspecting <code>aff2axcodes</code> output, you may find that order and direction of some image axes happen to coincide with some world coordinate system axes (e.g., direction of image I, J, K axes may be the same as the L, P, S axes of the LPS coordinate system), but that does not change that NIFTI still specifies the image geometry (origin, spacing, axis directions) in the RAS coordinate system.</p>
<aside class="quote no-group" data-username="drobny" data-post="1" data-topic="27460">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5daacb/48.png" class="avatar"> drobny:</div>
<blockquote>
<p>does a point in mm space depend on the orientation?</p>
</blockquote>
</aside>
<p>Yes. Coordinate values of a point depend on the orientation of the coordinate system axes.</p>
<aside class="quote no-group" data-username="drobny" data-post="1" data-topic="27460">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5daacb/48.png" class="avatar"> drobny:</div>
<blockquote>
<p>Shouldn’t I be able to convert these world coordinates into any image by applying the image specific affine matrix?</p>
</blockquote>
</aside>
<p>Yes, conversion between world and voxel coordinates is a simple homogeneous transformation. For example:</p>
<pre><code class="lang-auto">Point_IJK = Transform_RASToIJK * Point_RAS
  = inv(Transform_IJKToRAS) * Point_RAS
  = inv(Transform_IJKToRAS) * Transform_LPSToRAS * Point_LPS
  = inv(Transform_IJKToRAS) * diag(-1,-1,1,1) * Point_LPS
</code></pre>
<aside class="quote no-group" data-username="drobny" data-post="1" data-topic="27460">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/5daacb/48.png" class="avatar"> drobny:</div>
<blockquote>
<p>I wonder if slicer “converts” the LPS coordinate when loading to RAS by flipping the sign on the first two coordinates and vice versa when saving. Otherwise I don’t see how things work out within Slicer but not outside.</p>
</blockquote>
</aside>
<p>Yes, this is exactly what happens. You can see this if you have a look at coordinate values in the Slicer GUI and in the json file. Since practically all medical image computing file formats (DICOM, NRRD, MetaIO, etc.) uses LPS coordinate system we had no other choice in Slicer but save all data in LPS coordinate system. However, Slicer internally still uses RAS coordinate system. We’ll probably switch to LPS coordinate system in the future.</p>

---

## Post #3 by @drobny (2023-01-26 15:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="27460">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>NIFTI always uses RAS as world (physical) coordinate system, regardless of the order or orientation of image axes. By inspecting <code>aff2axcodes</code> output, you may find that order and direction of some image axes happen to coincide with some world coordinate system axes (e.g., direction of image I, J, K axes may be the same as the L, P, S axes of the LPS coordinate system), but that does not change that NIFTI still specifies the image geometry (origin, spacing, axis directions) in the RAS coordinate system.</p>
</blockquote>
</aside>
<p>Thanks a lot for this answer. I see where I got mixed up. It seems to be easiest to just convert everything to RAS while working with NIFTI images. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2023-01-26 16:08 UTC)

<p>NIFTI files are problematic for many reasons (complicated yet limited, ambiguous image orientation definition, etc.) and RAS is only used in few applications (mostly those that were developed before LPS has become the de facto standard coordinate system in medical image computing).</p>
<p>So, in general, my recommendation would be to use LPS coordinate system and not to use NIFTI file format. If you use NIFTI then you can still use LPS coordinate system for all computations (if you use ITK for loading a NIFTI image then it automatically converts it to be in the LPS coordinate system).</p>

---
