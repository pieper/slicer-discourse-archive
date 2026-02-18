# Segmentation restricted to ROI

**Topic ID**: 4524
**Date**: 2018-10-25
**URL**: https://discourse.slicer.org/t/segmentation-restricted-to-roi/4524

---

## Post #1 by @mag (2018-10-25 00:17 UTC)

<p>Hello,</p>
<p>this is probably straightforward but after reading through many posts I haven’t been able to figure out how to do it.</p>
<p>I am segmenting portions of some vessels on CT angiographies and I want to use “grow from seeds”. I am interested only in specific parts of the vessels (e.g. let’s say a small clot, even if it’s not what I’m doing), so to prevent the tool from growing the seed in the whole vessel I’d like to be able to place a ROI around the part I’m interested in and make the segment grow only within the ROI boundaries. I can’t figure out how to do this.</p>
<p>I know I could crop the volume, but I don’t want to do that because 1) I have multiple vascular segments to mark throughout the brain 2) I’m looking at tiny parts and without the surrounding I easily lose track of where I am.</p>
<p>Thanks for any help,</p>
<p>Marta</p>

---

## Post #2 by @lassoan (2018-10-25 03:59 UTC)

<p>Grow from seeds operates on a region around seed segments (if you have extra segments in the segmentation then you can hide them and they will be ignored), so to limit the segmented region, make sure you only paint seeds inside the region of interest.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62fbf13260f12939dfe3b092cecf5fe4cb011922.jpeg" data-download-href="/uploads/short-url/e7EzH5ftmYb1Xgk9nKghEaXePo6.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62fbf13260f12939dfe3b092cecf5fe4cb011922_2_554x500.jpeg" alt="image" data-base62-sha1="e7EzH5ftmYb1Xgk9nKghEaXePo6" width="554" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62fbf13260f12939dfe3b092cecf5fe4cb011922_2_554x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62fbf13260f12939dfe3b092cecf5fe4cb011922.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62fbf13260f12939dfe3b092cecf5fe4cb011922.jpeg 2x" data-dominant-color="2F342E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">629×567 36.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you need a more exact stopping location then you can paint the vessel segment and the background segment right next to it at the boundary of the region.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7680acbb40c751cc2fee00bd1e3defd0e9e8e46f.jpeg" data-download-href="/uploads/short-url/gUk1Bo4619rmJAFKs18MT6lGalN.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7680acbb40c751cc2fee00bd1e3defd0e9e8e46f_2_552x500.jpeg" alt="image" data-base62-sha1="gUk1Bo4619rmJAFKs18MT6lGalN" width="552" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7680acbb40c751cc2fee00bd1e3defd0e9e8e46f_2_552x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7680acbb40c751cc2fee00bd1e3defd0e9e8e46f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7680acbb40c751cc2fee00bd1e3defd0e9e8e46f.jpeg 2x" data-dominant-color="343C33"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">636×576 38.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For localized vessel segmentation, you may also try using “Fast marching” and “Flood filling” effects. They are both available in SegmentEditorExtraEffects extension.</p>

---
