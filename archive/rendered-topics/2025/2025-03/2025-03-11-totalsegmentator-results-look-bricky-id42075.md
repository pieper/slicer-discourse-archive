---
topic_id: 42075
title: "Totalsegmentator Results Look Bricky"
date: 2025-03-11
url: https://discourse.slicer.org/t/42075
---

# Totalsegmentator results look bricky

**Topic ID**: 42075
**Date**: 2025-03-11
**URL**: https://discourse.slicer.org/t/totalsegmentator-results-look-bricky/42075

---

## Post #1 by @puck147 (2025-03-11 17:21 UTC)

<p>I would like to use Totalsegmentator to automatically segment the aorta from a CT scan of a baby. However, the results look very bricky. How can I improve the quality and reduce the pixelsize?</p>
<p>Slicer version: 5.8.0</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf5bd157e4dd7b7141aaf6a8bbb7e9d707cb9e50.jpeg" data-download-href="/uploads/short-url/riPUL4GKnImkcijI0bcGO4UTdug.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf5bd157e4dd7b7141aaf6a8bbb7e9d707cb9e50_2_690x492.jpeg" alt="image" data-base62-sha1="riPUL4GKnImkcijI0bcGO4UTdug" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf5bd157e4dd7b7141aaf6a8bbb7e9d707cb9e50_2_690x492.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf5bd157e4dd7b7141aaf6a8bbb7e9d707cb9e50_2_1035x738.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf5bd157e4dd7b7141aaf6a8bbb7e9d707cb9e50_2_1380x984.jpeg 2x" data-dominant-color="504A4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×1027 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-03-11 17:27 UTC)

<p>The segmentation results will be resampled into the source volume’s resolution. If the source volume resolution is anisotropic (e.g., large spacing between coronal slices, as in the screenshot), you can use <code>Crop volume</code> module to resample the source volume to be isotropic before running segmentation.</p>
<p>Also make sure you disable fast mode in TotalSegmentator (that makes the resolution 2x coarser along each axis).</p>
<p>You can tune segmentation surface smoothing settings in the submenu of the “Show 3D” button.</p>
<p>Finally, if you really want to have high-quality rendering then don’t show the segmentation in 3D, just use the segmentation for colorizing volume rendering, by using <code>Colorize volume</code> module in the Sandbox extension. This is how you get renderings like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0422997dbe8017f2d481d332e39a4c35a6c10146.jpeg" data-download-href="/uploads/short-url/AA2qpAZEQM43fP8rj7tw9FrnfM.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0422997dbe8017f2d481d332e39a4c35a6c10146_2_653x500.jpeg" alt="image" data-base62-sha1="AA2qpAZEQM43fP8rj7tw9FrnfM" width="653" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0422997dbe8017f2d481d332e39a4c35a6c10146_2_653x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0422997dbe8017f2d481d332e39a4c35a6c10146_2_979x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0422997dbe8017f2d481d332e39a4c35a6c10146.jpeg 2x" data-dominant-color="8E8983"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1207×923 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
