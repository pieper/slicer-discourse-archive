---
topic_id: 44184
title: "Removing Below Threshold Data From Segment"
date: 2025-08-24
url: https://discourse.slicer.org/t/44184
---

# Removing below threshold data from segment

**Topic ID**: 44184
**Date**: 2025-08-24
**URL**: https://discourse.slicer.org/t/removing-below-threshold-data-from-segment/44184

---

## Post #1 by @Learn34 (2025-08-24 00:39 UTC)

<p>Big picture: I want to convert the CT scan data from a SPECT of my spine into a finite element model to validate use of a novel implant in a repair thereof.<br>
Little picture: In attempting to follow <a href="https://www.youtube.com/watch?v=ToIkOpDVfpw&amp;t=2s" rel="noopener nofollow ugc">this workflow</a> for converting the CT data to an stl, I cannot figure out how to clear out the red point cloud I’m left with after thresholding the cropped segment:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46d6bc9d6ef3035715cb102d101bc2ad450c1cdc.jpeg" data-download-href="/uploads/short-url/a6FuEiBmS12fwjBDS0ftZtZrbLS.jpeg?dl=1" title="Capture.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46d6bc9d6ef3035715cb102d101bc2ad450c1cdc_2_690x396.jpeg" alt="Capture.PNG" data-base62-sha1="a6FuEiBmS12fwjBDS0ftZtZrbLS" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46d6bc9d6ef3035715cb102d101bc2ad450c1cdc_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46d6bc9d6ef3035715cb102d101bc2ad450c1cdc_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46d6bc9d6ef3035715cb102d101bc2ad450c1cdc_2_1380x792.jpeg 2x" data-dominant-color="464244"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture.PNG</span><span class="informations">1920×1104 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The documentation for the volume rendering module provides instructions for how to remove arbitrary regions, but not how to removing everything under threshold.</p>
<p>Help?</p>

---

## Post #2 by @pieper (2025-08-24 19:47 UTC)

<p>After you threshold in the SegmentEditor, you can enable the Show 3D to see a surface rendering of the segmentation.  You can turn off the volume rendering in the VolumeRendering module to see the surface better.  If you want to see a volume rendering that takes into account the segmentation, try the <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254">ColorizeVolume</a> module.</p>
<p>If you are planning to make a finite element model, you may want to look at the <a href="https://github.com/lassoan/SlicerSegmentMesher">SegmentMesher</a> extension, although meshing tools outside of Slicer probably give better results for single-material meshes.</p>

---

## Post #3 by @Learn34 (2025-08-24 22:51 UTC)

<p>Yep, that did it. Now I get to figure out the best way to fill back in all the bone the thresholding took out and erase the other bits the thresholding didn’t nix.</p>
<p>Thanks!</p>

---

## Post #4 by @pieper (2025-08-25 14:23 UTC)

<p>Glad you are making progress.  You may also want to try the <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">WrapSolidify</a> module.</p>

---
