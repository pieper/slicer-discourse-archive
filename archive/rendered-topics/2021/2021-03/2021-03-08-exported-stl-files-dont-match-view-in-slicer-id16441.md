# Exported STL files dont match view in Slicer

**Topic ID**: 16441
**Date**: 2021-03-08
**URL**: https://discourse.slicer.org/t/exported-stl-files-dont-match-view-in-slicer/16441

---

## Post #1 by @benv (2021-03-08 23:19 UTC)

<p>I’m trying to export a segmentation to an STL mesh. I’m able to export it and read it in successfully, but the mesh I get out doesn’t seem to match up to what I see in Slicer. In the attached image, you can see point 6 and 7 are well within the yellow segmentation (right), but in the exported STL file, 7 ends up outside the mesh (left). Is there something I can do to export the mesh with higher fidelity?</p>
<p>As an alternative, I was considering exporting 2D slices of the segmentations. Is there a way to do this?</p>
<p>I’m using slicer 4.10.2 on a MBP, and Matlab 2020a.</p>
<p>Thanks!<br>
-Ben</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e9f2e2c55130a943232041752f9f50bd50e8fd8.png" data-download-href="/uploads/short-url/klGQh6NqaUJyBFb86k5zo9CaVLy.png?dl=1" title="Screen Shot 2021-03-08 at 10.47.16 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e9f2e2c55130a943232041752f9f50bd50e8fd8_2_690x273.png" alt="Screen Shot 2021-03-08 at 10.47.16 AM" data-base62-sha1="klGQh6NqaUJyBFb86k5zo9CaVLy" width="690" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e9f2e2c55130a943232041752f9f50bd50e8fd8_2_690x273.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e9f2e2c55130a943232041752f9f50bd50e8fd8_2_1035x409.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e9f2e2c55130a943232041752f9f50bd50e8fd8_2_1380x546.png 2x" data-dominant-color="838484"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-08 at 10.47.16 AM</span><span class="informations">1979×783 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-03-08 23:24 UTC)

<p>Slicer now reads all files in LPS coordinate system. Before Slicer-4.11, it expected STL files to be in RAS coordinate system by default. See more information about how to avoid RAS/LPS mismatch in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default">migration guide</a>.</p>
<p>If there is no LPS/RAS issue but slight position and/or orientation differences then most likely that other software does not properly take into account image origin, spacing, or axis directions of the input volume.</p>

---
