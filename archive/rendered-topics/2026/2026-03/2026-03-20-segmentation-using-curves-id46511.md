---
topic_id: 46511
title: "Segmentation Using Curves"
date: 2026-03-20
url: https://discourse.slicer.org/t/46511
---

# Segmentation using curves

**Topic ID**: 46511
**Date**: 2026-03-20
**URL**: https://discourse.slicer.org/t/segmentation-using-curves/46511

---

## Post #1 by @mrrezaie (2026-03-20 13:38 UTC)

<p>Hello all.</p>
<p>I’m trying to do MRI segmentation on a very thin and round structure (knee cartilage). I was wondering if there is any to create a surface on a set of polynomial curves like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eb7f0ee1e8ae45953d8817bab47d66a7f55db5c.jpeg" data-download-href="/uploads/short-url/8WPH6ss2vK25KijBDHDCO7tywag.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eb7f0ee1e8ae45953d8817bab47d66a7f55db5c_2_643x500.jpeg" alt="image" data-base62-sha1="8WPH6ss2vK25KijBDHDCO7tywag" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eb7f0ee1e8ae45953d8817bab47d66a7f55db5c_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eb7f0ee1e8ae45953d8817bab47d66a7f55db5c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eb7f0ee1e8ae45953d8817bab47d66a7f55db5c.jpeg 2x" data-dominant-color="403F3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">792×615 92.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Looking forward to hearing from you.</p>
<p>Mohammadreza</p>

---

## Post #2 by @chir.set (2026-03-20 14:00 UTC)

<p>If you use a <code>closed curve</code> instead of an <code>open curve</code>, the <code>Baffle planner</code> module in the <code>SlicerHeart</code> extension can create a model out of it (not a segmentation).</p>

---

## Post #3 by @mrrezaie (2026-03-20 14:21 UTC)

<p>Thanks a lot for your response. I just tried Baffle planner, it could be definitely helpful in my workflow. One thing about it, I need to create a surface from multiple curves (on every slice). It apparently works with one curve only, and the knee cartilage is a complex geometry:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b7cd6530d9b3b632b7f213ff554d66e8fd85198.jpeg" data-download-href="/uploads/short-url/8ufDg9rO9DLblJupMTmLa4lHdJ6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b7cd6530d9b3b632b7f213ff554d66e8fd85198.jpeg" alt="image" data-base62-sha1="8ufDg9rO9DLblJupMTmLa4lHdJ6" width="474" height="264"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">474×264 17.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2026-03-20 14:27 UTC)

<p>Do you really need the curve representation?  You might only need that if you are exporting to a CAD tool, and that’s a hard problem to do right.</p>
<p>You may be better off making a segmentation (binary labelmap) and reconstructing a surface from that.  You should definitely supersample the segmentation so that the thinnest structures are several voxels thick.  Then you can look at the wrapsolidify extension to get a smooth contour.  Search for similar work people do with thin temporal bones.</p>

---

## Post #5 by @mrrezaie (2026-03-20 14:54 UTC)

<p>Thanks a lot, this is a very thin structure on non-isotropic MRI. I had tried Wrap Solidify, but it was not successful. That’s why I ended up with this idea.</p>

---

## Post #6 by @pieper (2026-03-20 14:57 UTC)

<p>What is your overall goal and plan?  How will you use the surface?  I ask because lofting splines is a non-trivial operation whereas working with segmentations is well studies and you can make it work without developing new tools.</p>

---

## Post #7 by @mrrezaie (2026-03-20 15:09 UTC)

<p>My application is kind of Finite Element Analysis (not exactly; cartilages contact force analyses during physical activities using musculoskeletal modeling: <a href="https://github.com/clnsmith/opensim-jam/blob/master/opensim-jam-release/examples/walking/graphics/walking_contact.gif" class="inline-onebox" rel="noopener nofollow ugc">opensim-jam/opensim-jam-release/examples/walking/graphics/walking_contact.gif at master · clnsmith/opensim-jam · GitHub</a>).</p>
<p>So I need the cartilage surfaces accurate, and smoothed. But what I have already doesn’t allow me to use the common workflows in any medical imaging segmentation software.</p>
<p>Thanks for your help.</p>

---

## Post #8 by @pieper (2026-03-20 15:18 UTC)

<p>Okay, cool, yes, that helps.  I would definitely supersample the segmentation heavily.  Like use the crop volume to get just the cartilage are and the supersample as much as your computer can manage (or get a bigger computer) and then you may be able to paint with threshold and use smoothing to get a faithful surface.  (As an aside, joining curves manually draw slice-by-slice will always lead to bumpy surfaces so some kind of smoothing is needed here).</p>

---

## Post #9 by @mrrezaie (2026-03-20 16:06 UTC)

<p>Thanks again. There were two main issues in this approach: first, thresholding doesn’t work well for these kinds of MRI as this is not the best type for cartilage segmentation; second, the cartilages in children are so thin and narrow, the Brush or Draw tools were a nightmare. Overall, this approach is so boring for 60 patients <img src="https://emoji.discourse-cdn.com/twitter/upside_down_face.png?v=15" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20">. I’ve been thinking about doing sth like this: <a href="https://superhivemarket.com/products/curves-to-mesh" rel="noopener nofollow ugc">https://superhivemarket.com/products/curves-to-mesh</a></p>

---

## Post #10 by @pieper (2026-03-20 16:09 UTC)

<p>Yes, that’s a classic CAD approach.  There’s some support for doing things like that in Slicer extensions (surface markups) but I haven’t used them myself.  Maybe someone else can chime in.  If you are willing / able to do some coding I’m sure it’s doable with vtk or some python packages.</p>

---
